# %%
from ORSModel import Channel,orsObj
import numpy as np
from matplotlib import pyplot as plt

# %%
xrf_channel = orsObj('51C5EF1F95C742E2A12E6A42AF671C68CxvChannel')

#%% crop
#%%
xrf_stack = xrf_channel.getNDArray()
xrf_stack = xrf_stack.swapaxes(0,2)
print(xrf_stack.shape)

#%%
# fig = plt.figure()
# plt.imshow(xrf_stack[:,:,0])
# plt.show()

#%%
#! USER INPUT
thresh = 255
binary = np.zeros_like(xrf_stack)
print(binary.shape)

#%%
for i in range(xrf_stack.shape[2]):
    for j in range(xrf_stack.shape[1]):
        for k in range(xrf_stack.shape[0]):
            if xrf_stack[k,j,i] >= thresh:
                binary[k,j,i] = 1



#%%
labels = np.zeros((xrf_stack.shape[0],xrf_stack.shape[1]),dtype=np.int32)
# power = xrf_stack.shape[2]-1

for j in range(xrf_stack.shape[1]):
    for k in range(xrf_stack.shape[0]):
        label_num = 0
        for i in range(xrf_stack.shape[2]):
            label_num += binary[k,j,i] * (10**i)
            labels[k,j] = int(label_num)

#%%
# print(binary[265,159,:])
# print(labels[265,159])
# print(labels.dtype)

#%%
# Convert Numpy array to Channel
from ORSModel import createChannelFromNumpyArray
labels_channel = createChannelFromNumpyArray(labels)
labels_channel.setTitle('Labels')
labels_channel.publish()