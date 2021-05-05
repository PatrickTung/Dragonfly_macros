# %%
from ORSModel import Channel,orsObj
import numpy as np

# %%
red_channel = orsObj('9DB0BBDD9C0E4661B71C15ABC91C9050CxvChannel')
green_channel = orsObj('C691EEA1AC0A4470994971A2408A8665CxvChannel')
blue_channel = orsObj('72E031C786C849B9AF953AB9EAFF0376CxvChannel')

bins = np.linspace(0,255,4)

clusters = 8

# spacing =

# channel = Channel()
# #set it sizes, since we use the default voxel size, the channel is for now 100 meter cube
# channel.setXYZTSize(100,100,100,1)
# channel.setXSpacing(0.01)
# channel.setYSpacing(0.01)
# channel.setZSpacing(0.01)
# #now the channel is 1 meter cube
# #initilize it for float32 data
# channel.initializeDataForFLOAT()
# #publish it so that it is visible in the Object properties list
# channel.publish()

# %%

# array = channel.getNDArray()
# #modify it data
# array[::2,::2,::2] = 1
# #tell the channel that it data was modified (this can trigger event)
# channel.setDataDirty()

#%% crop
#%%
red_array = red_channel.getNDArray()
red_array = red_array.swapaxes(0,2)
red_array = red_array.squeeze()
red_array = red_array.reshape(red_array.shape[0]*red_array.shape[1])
red_inds = np.digitize(red_array,bins)

print(red_array.shape)

#%%
blue_array = blue_channel.getNDArray()
blue_array = blue_array.swapaxes(0,2)
blue_array = blue_array.squeeze()
blue_arrayXDim = blue_array.shape[0]
blue_arrayYDim = blue_array.shape[1]
blue_array = blue_array.reshape(blue_arrayXDim*blue_arrayYDim)
blue_inds = np.digitize(blue_array,bins)

print(blue_array.shape)

#%%
green_array = green_channel.getNDArray()
green_array = green_array.swapaxes(0,2)
green_array = green_array.squeeze()
green_arrayXDim = green_array.shape[0]
green_arrayYDim = green_array.shape[1]
green_array = green_array.reshape(green_arrayXDim*green_arrayYDim)
green_inds = np.digitize(green_array,bins)

# coordinates from dragonfly to python are [(x-1 * yDim) + (y-1)]
print(green_array[((156-1)*green_arrayYDim + (168-1))])

print(green_array.shape)


#%%
# Plot the 3D scatter plot
# from matplotlib import pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# fig = plt.figure()
# ax = Axes3D(fig)

# # ax.scatter(red_array, green_array, blue_array, c = 'b', marker='.')
# ax.scatter(red_inds, green_inds, blue_inds, c = 'b', marker='.')
# plt.show()

#%%
# Concatenate the arrays
# rgb_array = np.zeros((red_array.shape[0],3))
# rgb_array[:,0] = red_array
# rgb_array[:,1] = green_array
# rgb_array[:,2] = blue_array
# print(rgb_array.shape)

rgb_array = np.zeros((red_array.shape[0],3))
rgb_array[:,0] = red_inds
rgb_array[:,1] = green_inds
rgb_array[:,2] = blue_inds
print(rgb_array.shape)

#%%
# from sklearn.cluster import KMeans

# md=[]
# for i in range(1,21):
#   kmeans=KMeans(n_clusters=i)
#   kmeans.fit(rgb_array)
#   o=kmeans.inertia_
#   md.append(o)
# print(md)

#%%
from sklearn.cluster import KMeans

kmeans=KMeans(n_clusters=clusters)
s=kmeans.fit(rgb_array)

#%%
# Extract labels into array
labels=kmeans.labels_
print(labels)
print(labels.shape)

labels = labels.reshape((red_array.shape[0],red_array.shape[1]), order='C')
labels = np.flip(labels, axis=1)
print(labels.shape)
# labels=list(labels)

#%%
# Determine centroids of clusters
# centroid=kmeans.cluster_centers_
# print(centroid)

#%%
# Convert Numpy array to Channel
from ORSModel import createChannelFromNumpyArray
labels_channel = createChannelFromNumpyArray(labels)
labels_channel.setTitle('Labels')
labels_channel.publish()

