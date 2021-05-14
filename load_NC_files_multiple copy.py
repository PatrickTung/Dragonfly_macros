
# %%
from netCDF4 import Dataset
import numpy as np

start_file_num = 0
end_file_num = 37
example_dir = r"C:\Users\Patrick\OneDrive - UNSW\Desktop\1_CTDev\CT_Dev_PT_Lead_single_crystal_1.5mm_C_r1\tomo_R_nc\block00000000.nc"


# %%

file_prefix = example_dir.split('block')[0] + 'block'
file_suffix = r".nc"

# %%
# get the dimension of the data sets
file_dir = file_prefix + str(start_file_num).rjust(8,'0') + file_suffix
rootgrp = Dataset(file_dir, "r")
xdim = rootgrp.dimensions['tomo_xdim'].size
ydim = rootgrp.dimensions['tomo_ydim'].size
zdim_first = rootgrp.dimensions['tomo_zdim'].size

file_dir = file_prefix + str(end_file_num).rjust(8,'0') + file_suffix
rootgrp = Dataset(file_dir, "r")
zdim_last = rootgrp.dimensions['tomo_zdim'].size

# make the array to hold the data
ds = np.zeros(( (end_file_num-start_file_num)*zdim_first + zdim_last, ydim, xdim))

for i in range( start_file_num, end_file_num+1 ):
    
    # print("Loading image stack: ",i)
    # file_dir = file_prefix + str(i).rjust(8,'0') + file_suffix
    # rootgrp = Dataset(file_dir, "r")
    # if i != start_file_num:
    #     ds1 = rootgrp['tomo'][:].data.astype('ushort')
    #     ds[
    #     ds = np.vstack((ds,ds1))
    # else:
    #     ds = rootgrp['tomo'][:].data.astype('ushort')

# print("Voxel size is ",rootgrp.voxel_size_xyz[0]*1000, " microns")
# print(rootgrp.total_grid_size_xyz)

# %%

from ORSModel import createChannelFromNumpyArray

labels_channel = createChannelFromNumpyArray(ds)
labels_channel.setTitle(rootgrp.data_description)
labels_channel.setXSpacing(rootgrp.voxel_size_xyz[0]/1000)
labels_channel.setYSpacing(rootgrp.voxel_size_xyz[1]/1000)
labels_channel.setZSpacing(rootgrp.voxel_size_xyz[2]/1000)
labels_channel.publish()

rootgrp.close()