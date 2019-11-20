import os
import susi
import subprocess
from pomegranate import *
from data_preparation import *
from pomegranate.distributions import *
from sklearn.semi_supervised import label_propagation
from optimization import *


class MetaClassifierDataPreparator(object):
    def __init__(self, labeledPath, unlabeledPath):
        prep = DataPreparator(labeledPath,unlabeledPath)
        train_Xs, val_Xs, test_Xs, train_ys, val_ys, test_ys = prep.createSperimentationData()
        self.train_Xs = train_Xs.copy()
        self.val_Xs = val_Xs.copy()
        self.test_Xs = test_Xs.copy()
        self.train_ys = train_ys.copy()
        self.val_ys = val_ys.copy()
        self.test_ys = test_ys.copy()
        self.knn = KnnOptimizer(train_Xs, val_Xs, train_ys, val_ys)
        self.pom = PomOptimizer(train_Xs, val_Xs, train_ys, val_ys)
        self.susi = SusiOptimizer(train_Xs, val_Xs, train_ys, val_ys)
        self.clus = ClusSSLOptimizer(train_Xs, val_Xs, train_ys, val_ys, prep.indexer)

    def find_best_conf(self):
        self.knn_conf = self.knn.fit()
        self.pom_conf = self.pom.fit()
        self.susi_conf = self.susi.fit()
        self.clus_conf = self.clus.fit()

    def learn_classifiers(self, i):
        self.knn_model = self.knn.learn(i,self.knn_conf)
        self.pom_model = self.pom.learn(i,self.pom_conf)
        self.susi_model = self.susi.learn(i,self.susi_conf)
        self.clus.learn(i,self.clus_conf)

    def get_dataset(self,):
        pass



class SSEnsamble(object):
    def __init__(self):
        pass

    def fit(self):
        pass

    def predict(self):
        pass

    def save_model(self):
        pass


