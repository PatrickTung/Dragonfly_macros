# %%
from ORSModel import Channel,orsObj
import numpy as np
from PIL import Image

# %%
#! User Input
# voxel size (microns)
voxel_size = 0.902757

# %%

channel = Channel()
#set it sizes, since we use the default voxel size, the channel is for now 100 meter cube
#! User Input
channel.setXYZTSize(664,664,502,1)
channel.setXSpacing(voxel_size/1000000)
channel.setYSpacing(voxel_size/1000000)
channel.setZSpacing(voxel_size/1000000)

#initilize it for 8-bit data
channel.initializeDataForUINT()

array = channel.getNDArray()

# %%
# from ORSModel import ROI, orsColor
# mask_roi = ROI()
# mask_roi.setInitialColor(orsColor(209,80,230,127))
# mask_roi.copyShapeFromStructuredGrid(channel)

# channel.getAsROIWithinRangeInArea(1, 1, 0, 0, 0, channel.getXSize()*0.5, channel.getYSize()*0.5, channel.getZSize()*0.5, None, roi)

# %%
#! User Input
slice_numbers =[27,83,103,139,159,181,208,223,253,261,281,303,314,330,345,363,365,409,446]
counter = 1
for i in slice_numbers:
    #! User Input
    # file_prefix = r"C:\Users\Patrick\OneDrive - UNSW\CTDev_FuelCell_DL_demo\QM_segment_images\block00000000.view"
    # file_suffix = r".labels.tif"
    # file_dir = file_prefix + str(i).rjust(3,'0') + file_suffix
    # file_prefix = "C:\\Users\\Patrick\\OneDrive - UNSW\\CTDev_FuelCell_DL_demo\\fuel_cell_2D\\fuel_cell_2D\\label_convert\\"
    file_prefix = "C:\\Users\\Patrick\\Downloads\\label_new_convert_PT\\"

    # file_suffix = r".labels.tif"
    file_suffix = r".png"
    # file_dir = file_prefix + f'{i:03}' + file_suffix
    file_dir = file_prefix + str(counter) + file_suffix
    # if counter != 6:
    print(file_dir)
    im = Image.open(file_dir)
    imarray = np.array(im)
    array[i-1,:,:] = imarray[:]
    # print(array.shape)
    # print(imarray.shape)
    counter += 1

#TODO make a mask ROI automatically


# %%
#publish it so that it is visible in the Object properties list
# channel.publish()
# mask_roi.publish()

# %%

# array = channel.getNDArray()
# #modify it data
# array[::2,::2,::2] = 1
# #tell the channel that it data was modified (this can trigger event)
# channel.setDataDirty()

from ORSModel import createChannelFromNumpyArray
labels_channel = createChannelFromNumpyArray(array)
labels_channel.setXSpacing(voxel_size/1000000)
labels_channel.setYSpacing(voxel_size/1000000)
labels_channel.setZSpacing(voxel_size/1000000)
labels_channel.setTitle('Labels')
labels_channel.publish()


# mask_roi.publish()
