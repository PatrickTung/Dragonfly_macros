# %%
from ORSModel import Channel,orsObj,Progress,MultiROI,ArrayUnsignedLong,Color
import numpy as np
from matplotlib import pyplot as plt

#%%
multi_roi = orsObj('F3EE6FB4E7BA4A08A733B7963349EA2BCxvLabeledMultiROI')
preview = orsObj('3F9C5390478C4A5B99BA5F47A2DE39EACxvLabeledMultiROI')

#%%
# multi_roi_array = multi_roi.getAsArray(tIndex=1,)
# multi_roi_array = np.zeros((1,644,644))
# multi_roi_array = multi_roi.getNDArray()

# multi_roi_array = ArrayUnsignedLong()
# multi_roi.getAsArray(tIndex=0,pOutputArray=multi_roi_array)

# Convert both the multi ROI and preview ROI to numpy arrays
multi_roi_channel = Channel()
multi_roi_progress = Progress()
multi_roi.getAsChannel(inOutStructuredGrid=multi_roi_channel,IProgress=multi_roi_progress)
multi_roi_array = multi_roi_channel.getNDArray()

preview_channel = Channel()
preview_progress = Progress()
preview.getAsChannel(inOutStructuredGrid=preview_channel,IProgress=preview_progress)
preview_array = preview_channel.getNDArray()

#%%
# Get the numpy indices where preview ROI is in relation to the multi ROI
x_slice_ind = int (((preview.getOrigin()[0] - multi_roi.getOrigin()[0]) / multi_roi.getXSpacing())) 
y_slice_ind = int (((preview.getOrigin()[1] - multi_roi.getOrigin()[1]) / multi_roi.getYSpacing()))
z_slice_ind = int (((preview.getOrigin()[2] - multi_roi.getOrigin()[2]) / multi_roi.getZSpacing()))

#%%
# Replace values in target multi ROI with the preview ROI
multi_roi_array[z_slice_ind:z_slice_ind+preview_array.shape[0],y_slice_ind:y_slice_ind+preview_array.shape[1],x_slice_ind:x_slice_ind+preview_array.shape[2]] = preview_array[:]

#%%
# blah = plt.imshow(multi_roi_array[:,:,z_slice_ind+1])
# plt.show()

#%%
# Output numpy array as multi ROI
from ORSModel import createChannelFromNumpyArray
newChannel = createChannelFromNumpyArray(multi_roi_array)
newMROI = MultiROI()
newChannel.getAsMultiROI(inOutStructuredGrid=newMROI,IProgress=multi_roi_progress)
newMROI.setOrigin(multi_roi.getOrigin())
newMROI.setXSpacing(multi_roi.getXSpacing())
newMROI.setYSpacing(multi_roi.getYSpacing())
newMROI.setZSpacing(multi_roi.getZSpacing())
for i in range(multi_roi.getLabelCount()):
    newMROI.setLabelColor(i+1,multi_roi.getLabelColor(i+1))
    newMROI.setLabelName(i+1,multi_roi.getLabelName(i+1))
newMROI.publish()

#%%
# multi_roi_array.setDataDirty()