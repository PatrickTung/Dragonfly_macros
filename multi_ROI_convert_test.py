# %%
from numpy.core import multiarray
from ORSModel import Channel,orsObj, ROI, MultiROI, Progress
import numpy as np
from matplotlib import pyplot as plt

#%%
multi_roi = orsObj('0C26D381C74346608B568DEDCC6A27A2CxvLabeledMultiROI')

#%%
# multi_roi_array = multi_roi.getAsArray(tIndex=1,)
# multi_roi_array = np.zeros((1,644,644))
# multi_roi_array = multi_roi.getNDArray()

multi_roi_channel = Channel()
multi_roi_progress = Progress()
# multi_roi.getAsChannel(inOutStructuredGrid=multi_roi_channel,IProgress=multi_roi_progress)
multi_roi_array = multi_roi_channel.getNDArray()

# multi_roi_array = multi_roi_array.swapaxes(0,2)
# multi_roi_array = multi_roi_array.squeeze()

print(np.max(multi_roi_array))
print(np.min(multi_roi_array))
print(multi_roi_array.shape)

#%%
# blah = plt.imshow(multi_roi_array)
# plt.show()