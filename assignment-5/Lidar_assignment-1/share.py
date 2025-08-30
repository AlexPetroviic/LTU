#Start
'''
point cloud data is stored as a 2D matrix
each row has 3 values i.e. the x, y, z value for a point

Project has to be submitted to github in the private folder assigned to you
Readme file should have the numerical values as described in each task
Create a folder to store the images as described in the tasks.

Try to create commits and version for each task.

'''
#%%
from itertools import count
import matplotlib
import numpy as np
from scipy.spatial import KDTree
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#%% utility functions X1 Y2 Z3
def show_cloud(points_plt):
    ax = plt.axes(projection='3d')
    ax.scatter(points_plt[:,0], points_plt[:,1], points_plt[:,2], s=0.01)
    plt.show()

def show_scatter(x,y):
    plt.scatter(x, y)
    plt.show()

def get_ground_level(pcd):
    hist = np.histogram(pcd[:,2], bins=100) #returns 2 arrays, each bin with 100 points
    count = hist[0] #array1 #each bin with 100 points
    bin_edges = hist[1] #array2 #bin with edges/points
    max_value = max(count) #find max value
    biggest_bin_index = count.tolist().index(max_value) #find the bin index that has the highest point
    ground_level = (bin_edges[biggest_bin_index] + bin_edges[biggest_bin_index+1]) / 2 #find the middle ground level

    
    return ground_level
#%% read file containing point cloud data
pcd1 = np.load("dataset1.npy")
print("pcd1 shape: ", pcd1.shape)

pcd2 = np.load("dataset2.npy")
print("pcd2 shape: ", pcd2.shape)

#%% show downsampled data in external window
%matplotlib qt
show_cloud(pcd1)
show_cloud(pcd2)

#show_cloud(pcd1[::2]) # keep every 2nd point
#show_cloud(pcd2[::2]) # keep every 2nd point

#%% remove ground plane

'''
Task 1 (3)
find the best value for the ground level
One way to do it is useing a histogram 
np.histogram

update the function get_ground_level() with your changes

For both the datasets
Report the ground level in the readme file in your github project
Add the histogram plots to your project readme
'''
#%%
g1 = get_ground_level(pcd1)
print(g1)
pcd1_above_ground = pcd1[pcd1[:,2] > g1]
 #%%
g2 = get_ground_level(pcd2)
print(g2)
pcd2_above_ground = pcd2[pcd2[:,2] > g2]

#%%
show_cloud(pcd1_above_ground[::2]) 
#%%
show_cloud(pcd2_above_ground[::2])
#%%
print("Above pcd1 groundlevel :",pcd1_above_ground.shape)
print("Above pcd2 groundlevel :",pcd2_above_ground.shape)

#%% side view
show_cloud(pcd1_above_ground[::2])
show_cloud(pcd2_above_ground[::2])


# %%
unoptimal_eps = 10
# find the elbow
clustering = DBSCAN(eps = unoptimal_eps, min_samples=5).fit(pcd1_above_ground)

#%%
clusters = len(set(clustering.labels_)) - (1 if -1 in clustering.labels_ else 0)
colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, clusters)]

# %%
# Plotting resulting clusters
plt.figure(figsize=(10,10))
plt.scatter(pcd1_above_ground[:,0], pcd1_above_ground[:,1],
            c=clustering.labels_,
            cmap=matplotlib.colors.ListedColormap(colors),
            s=2)


plt.title('DBSCAN: %d clusters' % clusters,fontsize=20)
plt.xlabel('x axis',fontsize=14)
plt.ylabel('y axis',fontsize=14)
plt.show()