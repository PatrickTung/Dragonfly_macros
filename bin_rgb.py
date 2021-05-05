#%%
from ORSModel import Channel,orsObj
import numpy as np
from matplotlib import pyplot as plt

# %%
xrf_channel = orsObj('2DD11443C547404A9C115E7BAFEDB166CxvChannel')

#%%

xrf_array = xrf_channel.getNDArray()
xrf_array = xrf_array.swapaxes(0,2)
xrf_array = xrf_array.squeeze()
# xrf_array = xrf_array.reshape(xrf_array.shape[0]*xrf_array.shape[1])
print(xrf_array.shape)

#%%
hist = np.histogram(xrf_array,bins=5)
print(hist)

#%%
bins = np.linspace(0,255,6)
inds = np.digitize(xrf_array,bins)