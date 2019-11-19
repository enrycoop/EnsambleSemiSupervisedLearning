import susi
from utilities import *
from data_preparation import *

K = 5

un_X, un_y = extractXy("resources/unlabeled.arff")
un_y = [-1.0 for i in un_y]

# storing various accuracies
acc_ones = []
acc_zeros = []
accs = []

for i in range(K):

    # extract data from arff files
    train_X, train_y = extractXy(f"{K}_fold/train{i}.arff")
    test_X, test_y = extractXy(f"{K}_fold/test{i}.arff")

    # changing unlabeled symbol from '?' to '-1'
    train_X = train_X + un_X
    train_y = train_y + un_y

    # indexing Nominal data into numeric format for the algorithm (float)
    test_indexer = NominalIndexer(test_X)
    test_indexer.fit([1, 5, 12])
    test_X = test_indexer.nominalToNumeric()

    train_indexer = NominalIndexer(train_X)
    train_indexer.fit([1, 5, 12])
    train_X = train_indexer.nominalToNumeric()

    # learning phase

    model = susi.SOMClassifier(
        n_rows=10,
        n_columns=len(train_X[0]),
        train_mode_unsupervised="online",
        train_mode_supervised="online",
        n_iter_unsupervised=5000,
        n_iter_supervised=5000,
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
    print(f'{i} - fold')
    print(f'one: {len(ones)}/{one} -- {division(len(ones),one) }')
    print(f'zero: {len(zeros)}/{zero} -- {division(len(zeros),zero) }')
    print(f'accuracy: {len(nc)}/{len(y_pred)} -- {division(len(nc),len(y_pred))}\n\n')

    acc_ones.append(division(len(ones), one))
    acc_zeros.append(division(len(zeros), zero))
    accs.append(division(len(nc), len(y_pred)))

print('-----------------------------------RESUME------------------------------------')
print(f'total one: {avg(acc_ones)}')
print(f'total zero: {avg(acc_zeros)}')
print(f'total accuracy: {avg(accs)}')

boxplot([acc_ones,acc_zeros,accs], ["ONES", "ZEROS", "ACCURACY"])