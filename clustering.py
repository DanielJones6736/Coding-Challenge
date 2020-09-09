import csv
import sklearn.cluster
import matplotlib.pyplot as plt
import random


# read ClusterPlot.csv to a list
with open('ClusterPlot.csv') as data_file:
    csv_temp = csv.reader(data_file, delimiter=',')
    next(csv_temp)  # skip 1st row of names

    data_pts = []
    for row in csv_temp:
        data_pts.append(row)

# convert strings to float and format array
data_pts = [[float(c) for c in r] for r in data_pts]
# get rid of 1st column
for i in data_pts:
    del i[0]


# place one colored point onto graph
def plot_pt(point, hue):
    x = [point[0]]
    y = [point[1]]

    plt.scatter(x, y, color=hue)


# generate random rgb value
def gen_color():
    r = random.random()
    g = random.random()
    b = random.random()
    random_color = (r, g, b)

    while random_color <= (0.06, 0.06, 0.06):    # prevent a cluster from looking like black
        r = random.random()
        g = random.random()
        b = random.random()
        random_color = (r, g, b)

    return random_color


# clustering algorithm DBSCAN
epsilon = 0.2    # name from sklearn website
min_pts = 5
fit_clusters = sklearn.cluster.DBSCAN(eps=epsilon, min_samples=min_pts).fit(data_pts)
cluster_list = fit_clusters.labels_

# output cluster number
print("There are " + str(len(set(cluster_list))-1) + " clusters.")  # subtract 1 because outliers count as 1 cluster

# plot clusters
cluster_color_dict = { -1: (0, 0, 0) }    # outlier has a color of black
# iterate over every point and plot corresponding color
for i in range(0, len(data_pts)):
    if cluster_list[i] not in cluster_color_dict:   # if color for cluster has not already been made, add rand color to dictionary
        cluster_color_dict[cluster_list[i]] = gen_color()

    plot_pt(data_pts[i], cluster_color_dict[cluster_list[i]])

# display colored scatterplot
plt.show()

