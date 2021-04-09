# %%

from ORSModel import Channel,orsObj
# %%
channel = orsObj('358E6EBB0D0F407ABEBEDA0FDF68CB72CxvChannel')
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

#%%
array = channel.getNDArray()
print(array.shape)