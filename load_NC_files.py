# %%
# USER INPUT
file_dir = r"C:\Users\Patrick\OneDrive - UNSW\Desktop\1_CTDev\CTDev_Lakshmi_Civil\CIVIL_Steve_sample2by1_43mm_bot_SF_BeamC\tomo_RMG_LoRes.nc"

# %%
from netCDF4 import Dataset
rootgrp = Dataset(file_dir, "r")

ds = rootgrp['tomo'][:]
# print("Voxel size is ",rootgrp.voxel_size_xyz[0]*1000, " microns")
# print(rootgrp.total_grid_size_xyz)


# %%
from ORSModel import createChannelFromNumpyArray
labels_channel = createChannelFromNumpyArray(ds)
labels_channel.setTitle(rootgrp.dataset_id)
labels_channel.setXSpacing(rootgrp.voxel_size_xyz[0]/1000)
labels_channel.setYSpacing(rootgrp.voxel_size_xyz[1]/1000)
labels_channel.setZSpacing(rootgrp.voxel_size_xyz[2]/1000)
# Set voxel size

labels_channel.publish()

rootgrp.close()