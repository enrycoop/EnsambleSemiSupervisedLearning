import susi
import subprocess
from utilities import *
from pomegranate import *
from data_preparation import *
from pomegranate.distributions import *
from sklearn.semi_supervised import label_propagation
import conf_models


class Optimizer(object):
    def __init__(self, train_Xs, val_Xs, train_ys, val_ys):
        super().__init__()
        self.train_Xs = train_Xs.copy()
        self.val_Xs = val_Xs.copy()
        self.train_ys = train_ys.copy()
        self.val_ys = val_ys.copy()
        self.K = len(self.train_ys)


class KnnOptimizer(Optimizer):
    """
    Classe che specializza Optimizer, serve a ottimizzare KNN di SKLearn
    """
    def __init__(self, train_Xs, val_Xs, train_ys, val_ys):
        super().__init__(train_Xs, val_Xs, train_ys, val_ys)

    def learn(self, i, conf):
        train_X = self.val_Xs[i].copy()
        train_y = self.val_ys[i].copy()
        return label_propagation.LabelSpreading(kernel='knn', n_neighbors=conf[0], alpha=conf[1]).fit(train_X,train_y)

    def learnFromSamples(self,X, y, conf):
        return label_propagation.LabelSpreading(kernel='knn', n_neighbors=conf[0], alpha=conf[1]).fit(X,y)

    def fit(self, min_k=1, max_k=9, verbose=True):
        acc_ones = []
        acc_zeros = []
        accs = []
        if verbose:
            print('-----------------------------------START KNN OPTIMIZATION------------------------------------')
        best = dict()
        for (n, a) in [(x, a) for x in range(min_k, max_k + 1, 2) for a in [0.1, 0.01, 0.001, 0.0001]]:
            metric = []
            for i in range(self.K):
                train_X = self.train_Xs[i].copy()
                train_y = self.train_ys[i].copy()

                test_X = self.val_Xs[i].copy()
                test_y = self.val_ys[i].copy()

                model = label_propagation.LabelSpreading(kernel='knn', n_neighbors=n, alpha=a)
                model.fit(train_X, train_y)
                y_pred = model.predict(test_X)

                # evaluating by accuracy #
                # counting respectively True Positives, True Negatives and Correct count values
                ones = [(x, y) for (x, y) in zip(y_pred, test_y) if x == y and y == 1.0]
                zeros = [(x, y) for (x, y) in zip(y_pred, test_y) if x == y and y == 0.0]
                nc = [(x, y) for (x, y) in zip(y_pred, test_y) if x == y]

                one = test_y.count(1.0)
                zero = test_y.count(0.0)

                # accuracy calculation
                if verbose:
                    print(f'{i} - fold')

                acc_ones.append(division(len(ones), one))
                acc_zeros.append(division(len(zeros), zero))
                accs.append(division(len(nc), len(y_pred)))
                metric.append(avg([division(len(ones), one), division(len(zeros), zero)]))
            best.setdefault(avg(metric), (n, a))
            if verbose:
                print(f'----------------------{n}----------------------------')
                print(f'total one: {avg(acc_ones)}')
                print(f'total zero: {avg(acc_zeros)}')
                print(f'total accuracy: {geo_avg(accs)}')
        conf = best.get(np.array(list(best.keys())).max())
        if verbose:
            print('-----------------------------------RESUME KNN OPTIMIZATION------------------------------------')
            print(f"best n: {conf[0]} - best alpha: {conf[1]}")

        return conf


class PomOptimizer(Optimizer):
    """
    Classe che specializza Optimizer e serve a ottimizzare Pomegranade
    """
    def __init__(self, train_Xs, val_Xs, train_ys, val_ys):
        super().__init__(train_Xs, val_Xs, train_ys, val_ys)

    def fit(self, verbose=True):
        acc_ones = []
        acc_zeros = []
        accs = []
        if verbose:
            print('-----------------------------------START POM OPTIMIZATION------------------------------------')
        best = dict()
        distributions = [ExponentialDistribution, UniformDistribution, PoissonDistribution]
        for distr in distributions:
            metric = []
            for i in range(self.K):
                train_X = self.train_Xs[i].copy()
                train_y = self.train_ys[i].copy()

                test_X = self.val_Xs[i].copy()
                test_y = self.val_ys[i].copy()

                model = NaiveBayes.from_samples(distr, train_X, train_y, verbose=False)
                y_pred = model.predict(test_X)

                # evaluating by accuracy #
                # counting respectively True Positives, True Negatives and Correct count values
                ones = [(x, y) for (x, y) in zip(y_pred, test_y) if x == y and y == 1.0]
                zeros = [(x, y) for (x, y) in zip(y_pred, test_y) if x == y and y == 0.0]
                nc = [(x, y) for (x, y) in zip(y_pred, test_y) if x == y]

                one = test_y.count(1.0)
                zero = test_y.count(0.0)

                # accuracy calculation
                if verbose:
                    print(f'{i} - fold')

                acc_ones.append(division(len(ones), one))
                acc_zeros.append(division(len(zeros), zero))
                accs.append(division(len(nc), len(y_pred)))
                metric.append(avg([division(len(ones), one), division(len(zeros), zero)]))
            best.setdefault(avg(metric), distr)
            if verbose:
                print(f'----------------------{distr}----------------------------')
                print(f'total one: {avg(acc_ones)}')
                print(f'total zero: {avg(acc_zeros)}')
                print(f'total accuracy: {geo_avg(accs)}')
        conf = best.get(np.array(list(best.keys())).max())
        if verbose:
            print('-----------------------------------RESUME KNN OPTIMIZATION------------------------------------')
            print(f"best n: {conf}")

        # building final model
        return conf

    def learn(self,i,conf):
        train_X = self.val_Xs[i].copy()
        train_y = self.val_ys[i].copy()
        return NaiveBayes.from_samples(conf, train_X, train_y, verbose=False)


class SusiOptimizer(Optimizer):
    """
    Classe che specializza Optimizer, ha lo scopo di ottimizzare l'algoritmo SUSI
    """
    def __init__(self, train_Xs, val_Xs, train_ys, val_ys):
        super().__init__(train_Xs, val_Xs, train_ys, val_ys)

    def fit(self, min_rows=1, max_rows=20, min_iter_unsup=100, max_iter_unsup=500, min_iter_sup=100, max_iter_sup=500,
            verbose=True):
        acc_ones = []
        acc_zeros = []
        accs = []
        if verbose:
            print('-----------------------------------START SUSI OPTIMIZATION------------------------------------')
        best = dict()
        for (rows, iter_un, iter_su) in [(x, a, b) for x in range(min_rows, max_rows + 1, 5)
                                         for a in range(min_iter_unsup, max_iter_unsup + 1, 100)
                                         for b in range(min_iter_sup, max_iter_sup + 1, 100)]:

            metric = []
            for i in range(self.K):
                train_X = self.train_Xs[i].copy()
                train_y = self.train_ys[i].copy()

                test_X = self.val_Xs[i].copy()
                test_y = self.val_ys[i].copy()

                model = susi.SOMClassifier(
                    n_rows=rows,
                    n_columns=len(train_X[0]),
                    train_mode_unsupervised="online",
                    train_mode_supervised="online",
                    n_iter_unsupervised=iter_un,
                    n_iter_supervised=iter_su,
                    missing_label_placeholder=-1,
                    random_state=123)
                model.fit(train_X, train_y)
                y_pred = model.predict(test_X)

                # evaluating by accuracy #
                # counting respectively True Positives, True Negatives and Correct count values
                ones = [(x, y) for (x, y) in zip(y_pred, test_y) if x == y and y == 1.0]
                zeros = [(x, y) for (x, y) in zip(y_pred, test_y) if x == y and y == 0.0]
                nc = [(x, y) for (x, y) in zip(y_pred, test_y) if x == y]

                one = test_y.count(1.0)
                zero = test_y.count(0.0)

                # accuracy calculation
                if verbose:
                    print(f'{i} - fold')

                acc_ones.append(division(len(ones), one))
                acc_zeros.append(division(len(zeros), zero))
                accs.append(division(len(nc), len(y_pred)))
                metric.append(avg([division(len(ones), one), division(len(zeros), zero)]))
            best.setdefault(avg(metric), (rows, iter_un, iter_su))
            if verbose:
                print(f'----------------------{rows},{iter_un},{iter_su}----------------------------')
                print(f'total one: {avg(acc_ones)}')
                print(f'total zero: {avg(acc_zeros)}')
                print(f'total accuracy: {geo_avg(accs)}')
        conf = best.get(np.array(list(best.keys())).max())
        if verbose:
            print('-----------------------------------RESUME SUSI OPTIMIZATION------------------------------------')
            print(f"best rows: {conf[0]} - best uns_it: {conf[1]} - best su_it: {conf[2]}")

        return conf

    def learn(self,i,conf):
        train_X = self.val_Xs[i].copy()
        train_y = self.val_ys[i].copy()
        return susi.SOMClassifier(
                    n_rows=conf[0],
                    n_columns=len(train_X[0]),
                    train_mode_unsupervised="online",
                    train_mode_supervised="online",
                    n_iter_unsupervised=conf[1],
                    n_iter_supervised=conf[2],
                    missing_label_placeholder=-1,
                    random_state=123).fit(train_X,train_y)


class ClusSSLOptimizer(Optimizer):
    """
    Classe che specializza Optimizer, ha lo scopo di ottimizzare l'algoritmo CLUS
    """
    def __init__(self, train_Xs, val_Xs, train_ys, val_ys, indexer):
        self.indexer = indexer
        super().__init__(train_Xs, val_Xs, train_ys, val_ys)

    def fix(self):
        with open('external_libraries/conf_trees.py','r') as file:
            lines = file.readlines()
        with open('conf_trees.py','w') as file:
            for line in lines:
                file.write(str(line).replace("''", "'"))
        with open('external_libraries/conf_models.py','r') as file:
            lines = file.readlines()
        with open('conf_models.py','w') as file:
                file.writelines(lines)
        os.remove('external_libraries/conf_trees.py')
        os.remove('external_libraries/conf_models.py')

        print('fixato')

    def read_number(self):
        with open('conf_models.py', 'r') as file:
            lines = file.readlines()
        for line in lines:
            if 'ensemble' in line:
                return int(line.split('_')[1].split('(')[0])

    def fit(self, heuristics=('GainRatio', 'Gain', 'VarianceReduction'), min_iter_unsup=5, max_iter_unsup=50,
            min_iter_sup=10, max_iter_sup=50, verbose=True):
        acc_ones = []
        acc_zeros = []
        accs = []
        if verbose:
            print('-----------------------------------START SUSI OPTIMIZATION------------------------------------')
        best = dict()
        for (heuristic, iter_un, iter_su) in [(x, a, b) for x in heuristics
                                              for a in range(min_iter_unsup, max_iter_unsup + 1,
                                                             round((max_iter_unsup - min_iter_unsup) / 3))
                                              for b in range(min_iter_sup, max_iter_sup + 1,
                                                             round((max_iter_unsup - min_iter_unsup) / 3))]:
            metric = []
            for i in range(self.K):
                test_X = self.val_Xs[i].copy()
                test_y = self.val_ys[i].copy()

                self.prepare_conf(i, heuristic, iter_un, iter_su)
                subprocess.run(['java', '-jar', 'external_libraries/clusSSL.jar', '-ssl', '-forest',
                                'external_libraries/conf.s'])
                self.fix()

                one_accuracy,zero_accuracy, final_accuracy, metric_value = self.test(test_X,test_y,self.read_number())

                # accuracy calculation
                if verbose:
                    print(f'{i} - fold')

                acc_ones.append(one_accuracy)
                acc_zeros.append(zero_accuracy)
                accs.append(final_accuracy)
                metric.append(metric_value)
            best.setdefault(avg(metric), (heuristic, iter_un, iter_su))
            if verbose:
                print(f'----------------------{heuristic},{iter_un},{iter_su}----------------------------')
                print(f'total one: {avg(acc_ones)}')
                print(f'total zero: {avg(acc_zeros)}')
                print(f'total accuracy: {geo_avg(accs)}')
        conf = best.get(np.array(list(best.keys())).max())
        if verbose:
            print('-----------------------------------RESUME SUSI OPTIMIZATION------------------------------------')
            print(f"best rows: {conf[0]} - best uns_it: {conf[1]} - best su_it: {conf[2]}")
        # building final model
        print('########################################################################################################')
        print('building final model for CLUS...')
        return conf

    def learn(self,i, heuristic, unsup, sup):
        self.prepare_conf(i,heuristic,unsup,sup,train=False)
        subprocess.run(['java', '-jar', 'external_libraries/clusSSL.jar', '-ssl', '-forest',
                        'external_libraries/conf.s'])
        self.fix()

        self.tree = eval("conf_models.ensemble_{}".format(sup))

    def predict(self,X):
        return [float(self.tree(x)[0]) for x in X]

    def test(self, test_X, test_y, length):
        X = self.indexer.numericToNominal(test_X.copy())
        tree = eval("conf_models.ensemble_{}".format(length))

        y_pred = [float(tree(x)[0]) for x in X]
        # evaluating by accuracy #
        # counting respectively True Positives, True Negatives and Correct count values
        ones = [(x, y) for (x, y) in zip(y_pred, test_y) if x == y and y == 1.0]
        zeros = [(x, y) for (x, y) in zip(y_pred, test_y) if x == y and y == 0.0]
        nc = [(x, y) for (x, y) in zip(y_pred, test_y) if x == y]

        one = test_y.count(1.0)
        zero = test_y.count(0.0)
        return division(len(ones), one),division(len(zeros), zero),division(len(nc), len(y_pred)),avg([division(len(ones), one), division(len(zeros), zero)])

    def prepare_conf(self, i, heuristic, unsup, sup, train=True):
        # changing train and test file into dataset
        if train:
            with open('external_libraries/conf.s', 'r') as file:
                first = file.readlines()
            first[first.index('[Data]\n') + 1] = f"File = {self.K}_fold/train{i}.arff\n"
            first[first.index('[Data]\n') + 2] = f"TestSet = {self.K}_fold/test{i}.arff\n"
            first[first.index('[Tree]\n') + 1] = f"Heuristic = {heuristic}\n"
            first[first.index('[Ensemble]\n') + 1] = f"Iterations = {sup}\n"
            first[first.index('[SemiSupervised]\n') + 1] = f"Iterations = {unsup}\n"

            with open('external_libraries/conf.s', 'w') as file:
                file.writelines(first)
        else:
            with open('external_libraries/conf.s', 'r') as file:
                first = file.readlines()
            first[first.index('[Data]\n') + 1] = f"File = {self.K}_fold/validation_train{i}.arff\n"
            first[first.index('[Data]\n') + 2] = f"TestSet = {self.K}_fold/validation_test{i}.arff\n"
            first[first.index('[Tree]\n') + 1] = f"Heuristic = {heuristic}\n"
            first[first.index('[Ensemble]\n') + 1] = f"Iterations = {sup}\n"
            first[first.index('[SemiSupervised]\n') + 1] = f"Iterations = {unsup}\n"

            with open('external_libraries/conf.s', 'w') as file:
                file.writelines(first)


class MetaOptimizer(Optimizer):
    def __init__(self, train_Xs, val_Xs, train_ys, val_ys):
        super().__init__(train_Xs, val_Xs, train_ys, val_ys)

    def learn(self):
        pass

    def fit(self):
        pass


class MetaClassifierDataPreparator(Optimizer):
    def __init__(self, train_Xs, val_Xs, train_ys, val_ys, test_Xs, test_ys):
        super().__init__(train_Xs, val_Xs, train_ys, val_ys)
        self.test_Xs = test_Xs.copy()
        self.test_ys = test_ys.copy()

    def fit(self):
        pass

    def getDataset(self):
        pass

if __name__ == '__main__':
    prep = DataPreparator('resources/unlabeled.arff', 'resources/labeled.arff')
    train_Xs, val_Xs, test_Xs, train_ys, val_ys, test_ys = prep.createSperimentationData()
    opt = ClusSSLOptimizer(train_Xs, val_Xs, train_ys, val_ys, prep.indexer)
    conf = opt.fit()
    opt.learn(0,conf[0],conf[1],conf[2])
    print(opt.predict(test_Xs[0]))
