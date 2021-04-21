# %%
from netCDF4 import Dataset
# import netCDF4 as nc

rootgrp = Dataset(r"C:\Users\Patrick\Music\tomo_R_LoRes.nc", "r")
print(rootgrp.data_model)
print(rootgrp.variables)
print(rootgrp.variables['tomo'].shape[0])
print(rootgrp.dimensions['tomo_xdim'].size)
# rootgrp.close()

# ds = nc.Dataset(r"C:\Users\Patrick\Music\tomo_R_LoRes.nc", "r")
# ds.t

# %%
# import xarray as xr

# %%
# ds_disk = xr.open_dataset(r"C:\Users\Patrick\Desktop\tomo_R_LoRes.nc")