# %%
import numpy as np
from ORSModel import Channel,orsObj

#%%
def save_channel_to_numpy(obj_id):
    data_channel = obj_id
    data_array = data_channel.getNDArray()
    print(data_array.shape)
    np.save('data',data_array)
    

#%%
#! USER INPUT
save_channel_to_numpy(orsObj('51C5EF1F95C742E2A12E6A42AF671C68CxvChannel'))