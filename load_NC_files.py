# %%
from netCDF4 import Dataset

rootgrp = Dataset(r"C:\Users\Patrick\Music\tomo_R_LoRes.nc", "r")

ds = rootgrp['tomo'][:]
print("Voxel size is ",rootgrp.voxel_size_xyz[0]*1000, " microns")
# print(rootgrp.total_grid_size_xyz)

rootgrp.close()

# %%
from ORSModel import createChannelFromNumpyArray
labels_channel = createChannelFromNumpyArray(ds)
labels_channel.setTitle('Labels')
# Set voxel size

labels_channel.publish()