#%%
import xarray as xr

filedir = r"C:\Users\Patrick\OneDrive - UNSW\Desktop\1_CTDev\CTDev_PPHR1_10_1_25mm_dH_r1\tomo_R_LoRes.nc"

#%%
rootgrp = xr.open_dataset(filedir)
ds = rootgrp['tomo'][:].data

#%%
from ORSModel import createChannelFromNumpyArray

labels_channel = createChannelFromNumpyArray(ds)
labels_channel.setTitle(rootgrp.dataset_id)
labels_channel.setXSpacing(rootgrp.voxel_size_xyz[0]/1000)
labels_channel.setYSpacing(rootgrp.voxel_size_xyz[1]/1000)
labels_channel.setZSpacing(rootgrp.voxel_size_xyz[2]/1000)
# Set voxel size

labels_channel.publish()

# %%
rootgrp.close()