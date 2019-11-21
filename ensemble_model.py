from optimization import *
import conf_models


class SemiSupervisedEnsambleClassifier(object):

    def __init__(self,labeledPath, unlabeledPath, K=5, val_split=0.33,arff=True):
        self.dataPreparator = DataPreparator(labeledPath, unlabeledPath)
        self.K = K
        train_Xs, val_Xs, test_Xs, train_ys, val_ys, test_ys = self.dataPreparator.createSperimentationData(K=K, val_split=val_split,arff=arff)
        self.train_Xs = train_Xs.copy()
        self.val_Xs = val_Xs.copy()
        self.train_ys = train_ys.copy()
        self.val_ys = val_ys.copy()
        self.test_Xs = test_Xs.copy()
        self.test_ys = test_ys.copy()
        self.ensembleManager = EnsembleManager(train_Xs, val_Xs, train_ys, val_ys, self.dataPreparator.indexer)

    def fit(self):
        ensemble = self.ensembleManager
        ensemble.find_best_conf()
        ensemble_train_Xs = []
        self.ensemble_train_ys = self.val_ys.copy()
        ensemble_test_Xs = []
        self.ensemble_test_ys = self.test_ys.copy()
        for i in range(self.K):
            ensemble.learn_classifiers(i)
            ensemble_train_Xs.append(ensemble.get_results(self.val_Xs[i]))
            ensemble_test_Xs.append(ensemble.get_results(self.test_Xs[i]))
        self.ensemble_train_Xs = ensemble_train_Xs.copy()
        self.ensemble_test_Xs = ensemble_test_Xs.copy()
        opt = MetaOptimizer(self.ensemble_train_Xs.copy(),self.ensemble_test_Xs.copy(),
                            self.ensemble_train_ys.copy(),self.ensemble_test_ys.copy())
        opt.fit()

    def predict(self):
        pass

    def save_model(self):
        pass


class EnsembleManager(object):
    def __init__(self, train_Xs, val_Xs, train_ys, val_ys, indexer):
        self.train_Xs = train_Xs.copy()
        self.val_Xs = val_Xs.copy()
        self.train_ys = train_ys.copy()
        self.val_ys = val_ys.copy()
        self.knn = KnnOptimizer(train_Xs, val_Xs, train_ys, val_ys)
        self.pom = PomOptimizer(train_Xs, val_Xs, train_ys, val_ys)
        self.susi = SusiOptimizer(train_Xs, val_Xs, train_ys, val_ys)
        self.clus = ClusSSLOptimizer(train_Xs, val_Xs, train_ys, val_ys, indexer)

    def find_best_conf(self):
        self.knn_conf = self.knn.fit(verbose=False)
        self.pom_conf = self.pom.fit(verbose=False)
        self.susi_conf = self.susi.fit(verbose=False)
        self.clus_conf = self.clus.fit()

    def learn_classifiers(self, i):
        self.knn_model = self.knn.learn(i, self.knn_conf)
        self.pom_model = self.pom.learn(i, self.pom_conf)
        self.susi_model = self.susi.learn(i, self.susi_conf)
        self.clus.learn(i, self.clus_conf)

    def get_results(self, X):
        meta_X = []
        meta_X.append(self.knn_model.predict(X))
        meta_X.append(self.pom_model.predict(X))
        meta_X.append(self.susi_model.predict(X))
        meta_X.append(self.clus.predict(X))
        meta_X = np.array(meta_X).T.tolist()

        return meta_X


if __name__ == '__main__':
    ssEnsamble = SemiSupervisedEnsambleClassifier('resources/unlabeled.arff', 'resources/labeled.arff')
    ssEnsamble.fit()



