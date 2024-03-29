# %%import IPython

from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

# %%

# 1st Color
color1_rgb = sRGBColor(128,3,174)

# 2nd Color
color2_rgb = sRGBColor(97,23,156)

# Convert from RGB to Lab Color Space
color1_lab = convert_color(color1_rgb, LabColor)

# Convert from RGB to Lab Color Space
color2_lab = convert_color(color2_rgb, LabColor)

# Find the color difference
delta_e = delta_e_cie2000(color1_lab, color2_lab)

print ("The difference between the 2 color = ", delta_e)