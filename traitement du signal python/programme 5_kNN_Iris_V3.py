#https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/
#https://www.python-course.eu/k_nearest_neighbor_classifier.php

#The data set consists of 50 samples from each of three species of Iris
# 1.Iris setosa,
# 2.Iris virginica and
# 3.Iris versicolor.
# Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres.


# k-nearest neighbors on the Iris Flowers Dataset
from random import seed
from random import randrange
from csv import reader
from math import sqrt
import os
 
# Load a CSV file
def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset
 
# Convert string column to float
def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())
        
 
# Convert string column to integer
def str_column_to_int(dataset, column):
	class_values = [row[column] for row in dataset]
##	print(class_values)
	unique = set(class_values)
##	print unique
	lookup = dict()
	for i, value in enumerate(unique):
		lookup[value] = i
##	print(lookup)	
	for row in dataset:
		row[column] = lookup[row[column]]
	return lookup
 
 
# Split a dataset into k folds 
def cross_validation_split(dataset, n_folds):
	dataset_split = list()
	dataset_copy = list(dataset)
	fold_size = int(len(dataset) / n_folds)
	for _ in range(n_folds):
		fold = list()
		while len(fold) < fold_size:
			index = randrange(len(dataset_copy))
			fold.append(dataset_copy.pop(index)) 
		dataset_split.append(fold)
	return dataset_split

# Calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
	distance = 0.0
	for i in range(len(row1)-1):
		distance += (row1[i] - row2[i])**2
	return sqrt(distance)

# Calculate accuracy percentage
def accuracy_metric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
	return correct / float(len(actual)) * 100.0
 
# Evaluate an algorithm using a cross validation split
def evaluate_algorithm(dataset, folds, n_folds, num_neighbors):
	
	scores = list()
	for fold in folds:
		train_set = list(folds)
##		print train_set
		train_set.remove(fold)
##		print train_set
		train_set = sum(train_set, [])
##		print train_set
		test_set = list()
		for row in fold:
			row_copy = list(row)
			test_set.append(row_copy)
			row_copy[-1] = None                
##		print(fold); print(test_set)
		predicted = k_nearest_neighbors(train_set, test_set, num_neighbors)
		actual = [row[-1] for row in fold]
		accuracy = accuracy_metric(actual, predicted)
		scores.append(accuracy)
	return scores
 

 
# Locate the most similar neighbors
def get_neighbors(train, row, num_neighbors):
	distances = list()
	for train_row in train:
		dist = euclidean_distance(row, train_row)
		distances.append((train_row, dist))
	print(distances)
	distances.sort(key=lambda tup: tup[1])
	print(distances)
	neighbors = list()
	for i in range(num_neighbors):
		neighbors.append(distances[i][0])
	return neighbors
 

 
# kNN Algorithm
def k_nearest_neighbors(train, test, num_neighbors):
	predictions = list()
	for row in test:
		neighbors = get_neighbors(train, row, num_neighbors)
##		print(neighbors)
		output_values = [row[-1] for row in neighbors]
##		print(output_values)
		output = max(set(output_values), key=output_values.count)
##		print(output)
		predictions.append(output)
##		os.system("pause")
	return(predictions)

 
# Test the kNN on the Iris Flowers dataset
seed(1)
filename = 'iris.csv'
dataset = load_csv(filename)
##print(dataset)

for i in range(len(dataset[0])-1):
	str_column_to_float(dataset, i)
##print(dataset)

# convert class column to integers
str_column_to_int(dataset, len(dataset[0])-1)
##print(dataset)

# Divide dataset into n_folds to use n_folds_cross_validation
n_folds = 2
num_neighbors = 5
folds = cross_validation_split(dataset, n_folds)
##print(folds)

# evaluate algorithm 
scores = evaluate_algorithm(dataset, folds, n_folds, num_neighbors)
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))

