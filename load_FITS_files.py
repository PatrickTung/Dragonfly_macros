# %%
import numpy as np

# %%
#! USER INPUT
file_dir = r"E:\Exp_MCP_Feb2020\07_FeSample\2\Corrected\FeSample_002_00000.fits"
file_dir = r"C:\Users\Patrick\OneDrive - UNSW\Desktop\FeSample_002_00000.fits"
folder_dir_prefix = r"E:\Exp_MCP_Feb2020\07_FeSample\2\Corrected\FeSample_002_"
folder_dir_prefix = r"C:\Users\Patrick\Downloads\Corrected\Corrected\NiTi_A_Stress1_000_"

start_file_num = 0
end_file_num = 1957

# %%
from astropy.io import fits

for i in range (start_file_num, end_file_num):
    file_dir = folder_dir_prefix + str(i).rjust(5,'0') +'.fits'
    hdulist = fits.open(file_dir)
    
    if i != start_file_num:
        ds1 = hdulist[0].data.astype('ushort')
        ds[i-start_file_num,:,:] = ds1
    else:
        ds0 = hdulist[0].data.astype('ushort')
        ds = np.zeros((end_file_num-start_file_num,ds0.shape[0],ds0.shape[1]),dtype='ushort')
        ds[0,:,:] = ds0
    
    hdulist.close()
    # print("File loaded:",i)
# with fits.open(fits_image_filename) as hdul:
# print("Voxel size is ",rootgrp.voxel_size_xyz[0]*1000, " microns")
# print(rootgrp.total_grid_size_xyz)


    # %%
from ORSModel import createChannelFromNumpyArray

labels_channel = createChannelFromNumpyArray(ds)
# labels_channel.setTitle(rootgrp.data_description)
# labels_channel.setXSpacing(rootgrp.voxel_size_xyz[0]/1000)
# labels_channel.setYSpacing(rootgrp.voxel_size_xyz[1]/1000)
# labels_channel.setZSpacing(rootgrp.voxel_size_xyz[2]/1000)
# Set voxel size

labels_channel.publish()
