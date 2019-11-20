import os
import susi
import subprocess
from pomegranate import *
from data_preparation import *
from pomegranate.distributions import *
from sklearn.semi_supervised import label_propagation
from optimization import *
import conf_models


class SSEnsamble(object):
    def __init__(self):
        pass

    def fit(self):
        pass

    def predict(self):
        pass

    def save_model(self):
        pass


class EnsambleManager(object):
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
        #self.susi_conf = self.susi.fit(verbose=False)
        self.clus_conf = self.clus.fit()

    def learn_classifiers(self, i):
        self.knn_model = self.knn.learn(i, self.knn_conf)
        self.pom_model = self.pom.learn(i, self.pom_conf)
        #self.susi_model = self.susi.learn(i, self.susi_conf)
        self.clus.learn(i, self.clus_conf)

    def get_results(self, X):
        meta_X = []
        meta_X.append(self.knn_model.predict(X))
        meta_X.append(self.pom_model.predict(X))
        #meta_X.append(self.susi_model.predict(X))
        meta_X.append(self.clus.predict(X))
        meta_X = list(np.array(meta_X).T)
        return meta_X


if __name__ == '__main__':
    prep = DataPreparator('resources/unlabeled.arff', 'resources/labeled.arff')
    train_Xs, val_Xs, test_Xs, train_ys, val_ys, test_ys = prep.createSperimentationData()
    ensemble = EnsambleManager(train_Xs, val_Xs, train_ys, val_ys, prep.indexer)
    ensemble.find_best_conf()
    ensemble.learn_classifiers(0)
    X = ensemble.get_results(val_Xs[0])
    print(X)
    test_X = ensemble.get_results(test_Xs[0])
    print(test_X)


