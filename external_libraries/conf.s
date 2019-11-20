[General]
RandomSeed = 1
Verbose = 0

[Data]
File = 5_fold/train0.arff
TestSet = 5_fold/test0.arff

[Attributes]
Target = 14
Descriptive = 1-13
Clustering = 14
Weights = Normalize

[Tree]
Heuristic = GainRatio

[Ensemble]
Iterations = 10
EnsembleMethod = RForest

[SemiSupervised]
Iterations = 5
ConfidenceMeasure = RandomGaussian
UnlabeledData = resources/unlabeled.arff
SemiSupervisedMethod = PCT
UnlabeledCriteria = KMostConfident
ConfidenceThreshold = 0.9

Normalization = Standardization

[Output]
TrainErrors = Yes
TestErrors = Yes
WriteErrorFile = Yes
OutputPythonModel = Yes

