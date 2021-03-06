import numpy as np
from csv import reader
from sklearn.model_selection import train_test_split
import pandas as pd

with open('iris2.csv') as f:
    raw_data = f.read()

####PREPROCESS OF THE DATASET######
def data_preprocess(raw_data):
    # Load a CSV file
    dataset = list()
    #with filename as file:
    csv_reader = reader(raw_data.split('\n'), delimiter=',')
    for row in csv_reader:
        if not row:
            continue
        dataset.append(row)

    pd_data = pd.DataFrame(dataset)

    labels = pd_data.iloc[:,-1].values
    labels = labels[:, np.newaxis]
    #CONVERTING TEXT CLASS LABELS TO NUMBERS
    b, c = np.unique(labels, return_inverse=True)
    labels = c[:, np.newaxis] + 1
    labels = pd.DataFrame(labels)

    pd_data.drop(pd_data.columns[len(pd_data.columns)-1], axis=1, inplace=True)

    result = pd.concat([pd_data, labels], axis=1)
    dataset = result.values
    dataset = np.array(dataset).astype(np.float)


    # Find the min and max values for each column
    stats = [[min(column), max(column)] for column in zip(*dataset)]

    # Rescale dataset columns to the range 0-1 - normalization
    for row in dataset:
        for i in range(len(row)-1):
            row[i] = (row[i] - stats[i][0]) / (stats[i][1] - stats[i][0])
    return dataset

dataset = data_preprocess(raw_data)
numClasses = len(np.unique(dataset[:,-1]))



#def data_preprocess2(filename):
#	# Load a CSV file
#	data = np.loadtxt(filename, delimiter=',', usecols=(0, 1, 2, 3))
#	labels = np.loadtxt(filename, delimiter=",", dtype='S', usecols=(4)).astype(str)
#	rLabels = np.zeros(shape = (0,1))
#	for i in labels[:]:
#            if i == 'setosa':
#                rLabels = np.vstack([rLabels,[1]])
#            if i == 'versicolor':
#                rLabels = np.vstack([rLabels,[2]])
#            if i == 'virginica':
#                rLabels = np.vstack([rLabels,[3]])
#	#dataset = np.array(dataset).astype(np.float)
#	#print (data.shape)
#	#print (rLabels.shape)
#	
#	#print(dataset)
#
#	# Find the min and max values for each column
#	stats = [[min(column), max(column)] for column in zip(*data)]
#
#	# Rescale dataset columns to the range 0-1 - normalization
#	for row in data:
#		for i in range(len(row)):
#			row[i] = (row[i] - stats[i][0]) / (stats[i][1] - stats[i][0])
#
#	dataset = np.concatenate((data, rLabels), axis=1)
#	#print (dataset)
#	return dataset
#
#
#dataset = data_preprocess('iris2.csv')
##print (dataset)
##count the number of classes
#numClasses = len(np.unique(dataset[:,-1]))
#print(numClasses)

#train, test = train_test_split(dataset, test_size=0.2)
