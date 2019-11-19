import conf_trees


def aggregate(predictions):
    n = len(predictions)
    m = len(predictions[0])
    counts = [{} for _ in range(m)]
    for i in range(n):
        for j in range(m):
            pred = predictions[i][j]
            if pred not in counts[j]:
                counts[j][pred] = 0
            counts[j][pred] += 1
    return [max(counts[j], key=lambda pred: counts[j][pred]) for j in range(m)]


def ensemble_25(xs):
	base_predictions = [None for _ in range(25)]
	for i in range(len(base_predictions)):
		tree = eval("conf_trees.tree_{}".format(i + 1))
		base_predictions[i] = tree(xs)
	return aggregate(base_predictions)


