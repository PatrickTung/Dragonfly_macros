# %%
from ORSModel import Channel,orsObj
# %%
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from PIL import Image

# %%
# im = Image.open(r"C:\Users\Patrick\OneDrive - UNSW\Patrick sample 10-1 basalt\Patrick sample10-1 grey scale\sample 10-1 greyscale side close to mark1\Relevant elements\10-1 close to mark 1 Al.tif")

# %%
img_Al = mpimg.imread(r"C:\Users\Patrick\OneDrive - UNSW\Patrick sample 10-1 basalt\Patrick sample10-1 grey scale\sample 10-1 greyscale side close to mark1\Relevant elements\10-1 close to mark 1 Al.tif")
img_Ca = mpimg.imread(r"C:\Users\Patrick\OneDrive - UNSW\Patrick sample 10-1 basalt\Patrick sample10-1 grey scale\sample 10-1 greyscale side close to mark1\Relevant elements\10-1 close to mark 1 Ca.tif")
img_Fe = mpimg.imread(r"C:\Users\Patrick\OneDrive - UNSW\Patrick sample 10-1 basalt\Patrick sample10-1 grey scale\sample 10-1 greyscale side close to mark1\Relevant elements\10-1 close to mark 1 Fe.tif")
img_K = mpimg.imread(r"C:\Users\Patrick\OneDrive - UNSW\Patrick sample 10-1 basalt\Patrick sample10-1 grey scale\sample 10-1 greyscale side close to mark1\Relevant elements\10-1 close to mark 1 K.tif")
img_Mg = mpimg.imread(r"C:\Users\Patrick\OneDrive - UNSW\Patrick sample 10-1 basalt\Patrick sample10-1 grey scale\sample 10-1 greyscale side close to mark1\Relevant elements\10-1 close to mark 1 Mg.tif")
img_Mn = mpimg.imread(r"C:\Users\Patrick\OneDrive - UNSW\Patrick sample 10-1 basalt\Patrick sample10-1 grey scale\sample 10-1 greyscale side close to mark1\Relevant elements\10-1 close to mark 1 Mn.tif")
img_Si = mpimg.imread(r"C:\Users\Patrick\OneDrive - UNSW\Patrick sample 10-1 basalt\Patrick sample10-1 grey scale\sample 10-1 greyscale side close to mark1\Relevant elements\10-1 close to mark 1 Si.tif")

# %%
# Could possibly use manual bins
bins = np.linspace(0,255,4)
img_inds_Al = np.digitize(img_Al,bins,right=False)
img_inds_Ca = np.digitize(img_Ca,bins,right=False)
img_inds_Fe = np.digitize(img_Fe,bins,right=False)
img_inds_K  = np.digitize(img_K ,bins,right=False)
img_inds_Mg = np.digitize(img_Mg,bins,right=False)
img_inds_Mn = np.digitize(img_Mn,bins,right=False)
img_inds_Si = np.digitize(img_Si,bins,right=False)

# %%
# img_rgb_Al = np.full_like(img_Al,bins[bins.shape[0]-1])
img_rgb_Al = np.zeros_like(img_Al)
img_rgb_Ca = np.zeros_like(img_Ca)
img_rgb_Fe = np.zeros_like(img_Fe)
img_rgb_K  = np.zeros_like(img_K )
img_rgb_Mg = np.zeros_like(img_Mg)
img_rgb_Mn = np.zeros_like(img_Mn)
img_rgb_Si = np.zeros_like(img_Si)

# %%
# img_inds_Al[img_inds_Al == bins.shape[0]] = bins.shape[0]-1
# for i in range(img_Al.shape[0]):
#     for j in range(img_Al.shape[1]):
#         for k in range(img_Al.shape[2]):
#             if img_inds_Al[i,j,0] == k+1: 
#                 img_rgb_Al[i,j,k] = bins[k+1]

img_inds_Fe[img_inds_Fe == bins.shape[0]] = bins.shape[0]-1
for i in range(img_Fe.shape[0]):
    for j in range(img_Fe.shape[1]):
        for k in range(img_Fe.shape[2]):
            if img_inds_Fe[i,j,0] == k+1:
                img_rgb_Fe[i,j,k] = bins[k+1]

# $$
# Save as RGB
img_rgb_Fe = np.flip(img_rgb_Fe,2)
im_rgb_Fe = Image.fromarray(img_rgb_Fe,"RGB")
im_rgb_Fe.save("Fe_RGB.png")


# %%
# Swap axes for Dragonfly compatibility




# %%
# for i in range(1,4):
#     # img_rgb_Al[:,:,i-1] = img_inds_Al[:,:,i-1] == i
#     img_rgb_Al[img_inds_Al[:,:,i-1] == i] = bins[i-1]
#     img_rgb_Ca[img_inds_Ca[:,:,i-1] == i] = bins[i-1]
#     img_rgb_Fe[img_inds_Fe[:,:,i-1] == i] = bins[i-1]
#     img_rgb_K [img_inds_K [:,:,i-1] == i] = bins[i-1]
#     img_rgb_Mg[img_inds_Mg[:,:,i-1] == i] = bins[i-1]
#     img_rgb_Mn[img_inds_Mn[:,:,i-1] == i] = bins[i-1]
#     img_rgb_Si[img_inds_Si[:,:,i-1] == i] = bins[i-1]

# %%
# img_total = img_inds_Al + img_inds_Ca + img_inds_Fe + img_inds_K + img_inds_Mg + img_inds_Mn + img_inds_Si
# img_total = img_rgb_Al + img_rgb_Ca + img_rgb_Fe + img_rgb_K + img_rgb_Mg + img_rgb_Mn + img_rgb_Si

# img_total = img_total.astype(np.int32)


#%%
# Convert Numpy array to Channel
from ORSModel import createChannelFromNumpyArray
labels_channel = createChannelFromNumpyArray(img_rgb_Fe)
labels_channel.setTitle('Labels')
labels_channel.publish()

