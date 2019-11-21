"""
Library for data pre-processing.
"""

import random
import os
import numpy as np
from sklearn.preprocessing import *
import matplotlib.pyplot as plt


class DataPreparator(object):
    """
    This class prepare data for the SSEnsamble, divides
    """

    def __init__(self, unlabeled_path, labeled_path):
        self.unlabeled_path = unlabeled_path
        self.labeled_path = labeled_path

    def createSperimentationData(self, K=5, val_split=0.33,arff=True):
        # creating validation and test files (for clus purpose)
        KFoldBalancer(self.labeled_path, K, arff)
        for i in range(K):
            validationSplitBalanced(f'5_fold/train{i}.arff', val_split, arff)
        print('file created.')

        # extracting in memory files #
        X, y = extractXy(self.labeled_path)
        self.indexer = NominalIndexer(X)
        self.indexer.fit([1, 5, 12])

        # extract unlabeled data from file
        try:
            un_X, un_y = extractXy(self.unlabeled_path)
            un_y = [-1.0 for _ in un_y]
        except:
            un_X = []
            un_y = []
        self.un_X = un_X.copy()
        self.un_y = un_y.copy()


        train_Xs = []
        val_Xs = []
        test_Xs = []
        train_ys = []
        val_ys = []
        test_ys = []
        for i in range(K):
            # train data
            X, y = extractXy(f'{K}_fold/train{i}.arff')
            train_Xs.append(self.indexer.nominalToNumeric(X=X+un_X).copy())
            train_ys.append((y+un_y).copy())

            # test data
            X, y = extractXy(f'{K}_fold/test{i}.arff')
            test_Xs.append(self.indexer.nominalToNumeric(X=X).copy())
            test_ys.append(y.copy())


            # validation data
            X, y = extractXy(f'{K}_fold/validation_train{i}.arff')
            val_Xs.append(self.indexer.nominalToNumeric(X=X).copy())
            val_ys.append(y.copy())

        return train_Xs, val_Xs, test_Xs, train_ys, val_ys, test_ys


class Normalizer(object):

    """
    Abstract Normalizer for data
    """

    def __init__(self, X):
        """
        Initialize data with list X of samples

        :param X: list of samples
        """
        self.X = list(X).copy()

    def trasform(self, indexes, method=normalize, **kwargs):
        """
        Transform data from the index specified by parameter indexes.
        You can specify in input the transformer method and the associate paramethers.

        :param indexes: indexes of columns to transform
        :param method: method used for transofrmation by default normalize from scikit-learn
        :param kwargs: eventual arguments of the parameter method
        :return:
        """
        ar = np.arange(len(self.X[0]))
        ind = [x for x in ar if x not in indexes]
        X1 = np.array(self.X.copy())
        try:
            X2 = method(X1[:, indexes], **kwargs)
            result = np.concatenate((X1[:, ind], X2), axis=1)
            self.X = list(result)
        except:
            print('failed normalization by indexes.')
        return self.X


class NominalIndexer(object):
    """
    This Class can be used to keep track of the conversions of the Nominal attributes.
    """

    def __init__(self, X):
        """
        Initialize the internal state of the sample list to X.

        :param X: list of samples.
        """
        self.X = list(X).copy()

    def fit(self, indexes):
        """
        This fits the object to the dataset.

        :param indexes: attribute indexes list to be indexed.
        :return: None
        """
        self.indexes = indexes
        self.attributes = dict()
        for i in list(indexes):
            values = set()
            for v in self.X:
                values.add(v[i])
            self.attributes.setdefault(i, list(values))

    def nominalToNumeric(self, indexes=None, X=None):
        """
        Converts nominal attributes into numeric attributes.

        :param indexes: indexes of the attribute to convert
        :return: the list of samples converted.
        """
        if X is None:
            X = self.X

        if indexes is None:
            for x in X:
                for i in self.indexes:
                    try:
                        x[i] = float(self.attributes.get(i).index(x[i])) + 1
                    except:
                        pass
        else:
            for x in X:
                for i in indexes:
                    try:
                        x[i] = float(self.attributes.get(i).index(x[i])) + 1
                    except:
                        pass

        return X.copy()

    def numericToNominal(self, indexes=None, X=None):
        """
        Converts numeric attributes into nominal attributes.

        :param X: set to parse
        :param indexes: indexes of the attribute to convert
        :return: the list of samples converted.
        """
        if X is None:
            X = self.X

        output = self.X
        if indexes is None:
            for x in output:
                for i in self.indexes:
                    try:
                        x[i] = self.attributes[i][int(x[i] - 1)]
                    except:
                        pass
        else:
            for x in output:
                for i in indexes:
                    try:
                        x[i] = self.attributes[i][int(x[i] - 1)]
                    except:
                        pass

        return output.copy()


def extractXy(path, sep=',', st="'", missing_values='?', arff=True):
    """
    Extract X and y vectors respectively the features' vector and labels' vector.

    :param path: The path of the file to split
    :param sep: the features' separator
    :param st: the string delimiter
    :param missing_values: if there are the missing value symbol
    :param arff: if the input file is an arff file.
    :return: X and y vectors
    """

    with open(path) as file:
        lines = file.readlines()
    X = []
    y = []
    if arff:
        start = lines.index('@data\n') + 1
    else:
        start = 0
    for i in range(start, len(lines)):
        parsed = lines[i].replace('\n', "").split(sep)
        for j in range(len(parsed)):
            if (not (st in parsed[j])) and not (missing_values in parsed[j]):
                parsed[j] = float(parsed[j])
            else:
                parsed[j] = parsed[j].replace(st, "")
        X.append(parsed[:-1])
        y.append(parsed[-1])
    return X, y


def KFoldBalancer(path, K=5, arff=True):
    """
    This function split a given file into K train and test folds
    in order to perform a K-fold cross validation.
    The two classes are labeled with 1 and 0 values.

    :param path: the path of the file to split.
    :param K: number of split.
    :param arff: Specifies if the input file is an arff file or not.
    :return: None
    """

    # extract data from file if exists
    with open(path, 'r') as reader:
        lines = reader.readlines()
    if arff:
        start = lines.index('@data\n')
    else:
        start = 0
    intestation = lines[:start + 1].copy()
    data_lines = lines[start + 1:].copy()

    # creating results folder
    if not os.path.exists(f"{K}_fold"):
        os.makedirs(f"{K}_fold")

    # splitting lines with 0 and 1 values
    one_lines = [line for line in data_lines if line.endswith('1\n')]
    zero_lines = [line for line in data_lines if line.endswith('0\n')]
    ONE_STEP = round(len(one_lines) / K)
    ZERO_STEP = round(len(zero_lines) / K)
    for i in range(K):
        one_train = []
        one_test = []
        for j in range(len(one_lines)):
            if i * ONE_STEP <= j < (i + 1) * ONE_STEP:
                one_test.append(one_lines[j])
            else:
                one_train.append(one_lines[j])
        zero_train = []
        zero_test = []
        for j in range(len(zero_lines)):
            if i * ZERO_STEP <= j < (i + 1) * ZERO_STEP:
                zero_test.append(zero_lines[j])
            else:
                zero_train.append(zero_lines[j])
        test_lines = zero_test + one_test
        random.shuffle(test_lines)
        with open(f'{K}_fold/test{i}.arff', 'w') as file:
            file.writelines(intestation)
            file.writelines(test_lines)
        train_lines = zero_train + one_train
        random.shuffle(train_lines)
        with open(f'{K}_fold/train{i}.arff', 'w') as file:
            file.writelines(intestation)
            file.writelines(train_lines)


def validationSplitBalanced(path, split=0.33, arff=True):
    """
    This function split a given file into train and test files
    in order to perform a cross validation.
    The two classes are labeled with 1 and 0 values.

    :param path: the path of the input file
    :param split: a float value in (0.0,1.0) that specifies the percentage of the set to use as validation set
    :param arff: If it is an arff file
    :return: None
    """

    # extract data from file if exists
    with open(path, 'r') as reader:
        lines = reader.readlines()
    if arff:
        start = lines.index('@data\n')
    else:
        start = 0
    intestation = lines[:start + 1].copy()
    data_lines = lines[start + 1:].copy()

    # extracting folder path
    dirname = os.path.split(os.path.abspath(path))

    one_lines = [line for line in data_lines if line.endswith('1\n')]
    zero_lines = [line for line in data_lines if line.endswith('0\n')]

    ONE_STEP = round(len(one_lines) * split)
    ZERO_STEP = round(len(zero_lines) * split)

    one_train = []
    one_test = []
    for j in range(len(one_lines)):
        if ONE_STEP >= j:
            one_test.append(one_lines[j])
        else:
            one_train.append(one_lines[j])
    zero_train = []
    zero_test = []
    for j in range(len(zero_lines)):
        if ZERO_STEP >= j:
            zero_test.append(zero_lines[j])
        else:
            zero_train.append(zero_lines[j])
    test_lines = zero_test + one_test
    random.shuffle(test_lines)
    with open(f'{dirname[0]}/validation_{dirname[1][:dirname[1].index(".")]}.arff', 'w') as file:
        file.writelines(intestation)
        file.writelines(test_lines)
    train_lines = zero_train + one_train
    random.shuffle(train_lines)
    with open(f'{dirname[0]}/{dirname[1]}', 'w') as file:
        file.writelines(intestation)
        file.writelines(train_lines)


def boxplot(lists, labels=None, fontsize=15):
    """
    Function that plots different lists of accuracy.

    :param fontsize: fontsize, by default 15.
    :param lists: list of lists of accuracy.
    :param labels: labels associated to various lists.
    :return: None
    """

    if labels is None:
        labels = [str(x) for x in range(len(lists))]

    plt.errorbar(
        x=[x + 1 for x in range(len(lists))],
        y=[np.mean(x) * 100 for x in lists],
        yerr=[np.std(x) * 100 for x in lists],
        marker=".",
        mew=5,
        linewidth=0,
        elinewidth=2)
    plt.ylim([0, 100])
    plt.ylabel("Accuracy in %", fontsize=fontsize)
    plt.xticks([x + 1 for x in range(len(lists))], labels, fontsize=fontsize)
    plt.yticks(fontsize=fontsize)
    plt.show()


if __name__ == '__main__':
    prep = DataPreparator('resources/unlabeled.arff', 'resources/labeled.arff')
    #train_Xs, val_Xs, test_Xs, train_ys, val_ys, test_ys = prep.createSperimentationData()
    print(train_Xs[0][-2])
    print(val_Xs[0][-2])
    print(test_Xs[0][-2])
    print(train_ys[0][-2])
    print(val_ys[0][-2])
    print(test_ys[0][-2])



