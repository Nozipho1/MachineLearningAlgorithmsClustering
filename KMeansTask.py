import csv
import matplotlib.pyplot as plt
import numpy as np
from random import sample

# Define a function that computes the distance between two data points
def euclidean_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Define a function that reads data in from the csv files
def read_csv(path):
    csv_content = csv.reader(open(path, "r"))
    next(csv_content)
    country_names_list = []
    data_point_list = []

    for record in csv_content:
        country_names_list.append(record[0])
        data_point_list.append([float(record[1]), float(record[2])])

    return country_names_list, data_point_list

# Define a function that returns the x and y data
def x_and_y(data):
    return [data_point[0] for data_point in data], [data_point[1] for data_point in data]

# Define a function that determines the mean of the cluster
def calculate_mean(cluster):
    x_data, y_data = x_and_y(cluster)
    return [sum(x_data) / len(cluster), sum(y_data) / len(cluster)]

# conditional body to start the program
if __name__ == "__main__":

    # Ask user for values
    filename = input("Name Of CSV File: ")
    k = int(input("How many clusters would you like to generate: "))
    iteration_end = int(input("How many iterations would you like: "))

    # Initialise variables Variables
    country_names, data = read_csv(filename)
    iteration_index = 0
    clusters = []
    colors = ["red", "green", "black", "yellow", "blue"]
    centroids = sample(data, k)

    # while loop to loop within the number of iterations the user inputted (the k value)
    while iteration_index != iteration_end:

        clusters = [[] for i in range(k)]

        # for loop looping over data to create index points
        for data_point_index, data_point in enumerate(data):
            # print(f"{data_point_index}) {data_point}, center points = {centroids}, iteration = {iteration_index}")
            data_point_centroid_distance = [euclidean_distance(data_point, centroid) for centroid in centroids]
            clusters[data_point_centroid_distance.index(min(data_point_centroid_distance))].append(data_point)

        centroids = [calculate_mean(clusters[i]) for i in range(k)]

        iteration_index += 1

    plt.xlabel("Birthrate")
    plt.ylabel("Life Expectancy")

    # for loop to plot the points
    for i in range(k):
        x, y = x_and_y(clusters[i])
        plt.scatter(x, y, c=colors[i], label="#")
        plt.scatter(centroids[i][0], centroids[i][1], c="Yellow", label="#")

        print(f"Mean of cluster {i} | Color: {colors[i]} has a mean of {centroids[i]}")


    plt.show()