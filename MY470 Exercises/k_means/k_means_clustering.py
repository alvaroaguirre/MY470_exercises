## Alvaro Aguirre

'''This code was made for an exercise of the class Computer Programming at LSE.
 K-means clustering is a simple unsupervised ML method for cluster analysis.
 The objective is to partition a set of points into k clusters, such that each
 point is assigned to the nearest cluster. The algorithm iterates through:
 1. Assign each data point to the cluster with the nearest centroid.
 2. Update the centroids of the clusters given the nw assignment.
 The algorithm converges when the assignments no longer change.

 In this simplified version we will run the algorithm a fixed number of times, 
 and we will initialize only once, using a naive method of randomly choosing k 
 points from the data to use as initial cluster centroids
 Dataset to use: "Wholesale customers data.csv" from http://archive.ics.uci.edu/ml/index.php'''


# Part 1 - Define a function for Euclidean distance

import math
import csv
import random

def get_distance(x1, x2):
	'''Assumes x1 and x2 to be n-dimensional vectors 
	of ints or floats that represent the coordinates of a point'''
	dist = 0
	for i in range(len(x1)):
		dist += (x1[i] - x2[i])**2
	return math.sqrt(dist)

# Part 2 - Function to estimate the centroid of a collection of points

def get_centroid(lst):
	'''Assumes input is a list that contains a set of n-dimensional 
	points. Returns list with the coordinates of the virtual center point'''
	centroid = [sum(ele[i] for ele in lst)/len(lst) for i in range(len(lst[0]))]
	return centroid

# Part 3 - Function to read data
 
def get_data():
 	'''Opens CSV file and returns data in a list, with each element
 	as integer (ignores headers and first two ID cols). Dimension is 440x6.'''
 	with open('Wholesale customers data.csv', newline= '') as f:
 		data = list(csv.reader(f))[1:]
 		for ele in data:
 			del ele[:2]
 			for i in range(len(ele)):
 				ele[i] = int(ele[i])
 		return data

data = get_data()

# Part 4 - Function to implement k-means algorithm
# Write a function that clusters a collection ofpoints into k clusters
# Should take a list of n-dim points and K as arguments 
# Should return a clustering (list of k clusters with points), centroids
# Instead of looking for convergence, run 100 iterations

def kmeans(points, k):
	'''Simple K-means clustering algorithm. 
	Randomly chooss k of the n-dimensional points as centroids.
	Iterates 100 times'''
	
	# Initial centroids
	init = random.sample(points, k)

	# List of k-lists to contain assigned points to each cluster
	clusters = [[] for i in init]

	# Centroids
	centroids = [i for i in init]

	# First manual run
	# Assing each point to the cluster with closes centroid
	for x in points:
		distance_centroids = [get_distance(x, centroids[i]) for i in range(len(centroids))]
		clusters[distance_centroids.index(min(distance_centroids))].append(x)

	# Update the centroids
	for i in range(len(clusters)):
		centroids[i] = get_centroid(clusters[i])

	# Empty the clusters list for new iteration
	clusters = [[] for i in init]

	# Repetition 100 times. Each new repetition refines the clustering

	iteration = 0
	for i in range(100):
		for x in points:
			distance_centroids = [get_distance(x, centroids[i]) for i in range(len(centroids))]
			clusters[distance_centroids.index(min(distance_centroids))].append(x)
		for i in range(len(clusters)):
			centroids[i] = get_centroid(clusters[i])
		iteration += 1
		if iteration < 100:
			clusters = [[] for i in init]

	return clusters, centroids

# Testing the algorithm with the data. Using K=3

k_means = list(kmeans(data, 3))

# Number of customers assigned to each cluster

print("Cluster Onee has", len(k_means[0][0]),"customers assigned.")
print("Cluster Two has", len(k_means[0][1]),"customers assigned.")
print("Cluster Three has", len(k_means[0][2]),"customers assigned.")

# Centroids

print("Centroid of Cluster One:", ['%.2f' % elem for elem in k_means[1][0]])
print("Centroid of Cluster Two:", ['%.2f' % elem for elem in k_means[1][1]])
print("Centroid of Cluster Three:", ['%.2f' % elem for elem in k_means[1][2]])

