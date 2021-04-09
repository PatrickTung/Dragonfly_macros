# %%

from ORSModel import Channel,orsObj
# %%
channel = orsObj('891DD8F288DA43F5B4E0BDF3888C411CCxvChannel')
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
array = channel.getNDArray()

array = array.swapaxes(0,2)
array = array.squeeze()
arrayXDim = array.shape[0]
arrayYDim = array.shape[1]
array = array.reshape(arrayXDim*arrayYDim)
# coordinates from dragonfly to python are [(x-1 * yDim) + (y-1)]


print(array[(268*arrayYDim + 156)])

print(array.shape)

#%%
from matplotlib import pyplot as plt

# NEXT STEP: VISUALIZE IF THERE ARE CLUSTERS WITH THE RED ARRAY
