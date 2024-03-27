from email.mime import image
from fileinput import filename
import sys
import numpy as np
from loguru import logger
from pathlib import Path
import scaffan
import scaffan.image as scim
import matplotlib.pyplot as plt

# Decellularized
# filename = "PIG-001_J-17-0569_LM_HE" # memory leaks
# filename = "PIG-003_J-18-0169_HE__l" # raw 1849 - noblanks 1119
# filename = "PIG-002_J-18-0092_HE__-1" # raw 1849 - noblanks 1640
# filename = "PIG-003_J-18-0165_HE__-1-2" # raw 1849 - noblanks 1077
# filename = "PIG-003_J-18-0166_HE__-1-3" # raw 1849 - noblanks 1307
# filename = "PIG-003_J-18-0167_HE__f-1" # raw 1849 - noblanks 1062
# filename = "PIG-003_J-18-0168_HE__-1-4" # raw 1849 - noblanks 1222
# filename = "PIG-003_J-18-0170_HE" # raw 1849 - noblanks 1692
# filename = "PIG-003_J-18-0170_HE_10min__-2" # raw 1849 - noblanks 1592

# Living
foldername = "J18_6"
# filename = "J7_5_a" # raw 1849 - noblanks 85
# filename = "J7_5_b" # 64
# filename = "J7_5_c" # 67
# filename = "J7_5_e" # 174
# filename = "J7_9_a" # 100
# filename = "J7_9_c" # 33
# filename = "J8_5_a" # 136
# filename = "J8_5_b" # 145
# filename = "J8_5_c" # 81
# filename = "J9_9_a" # 193
# filename = "J10_3_a" # 120
# filename = "J10_3_b" # 90
# filename = "J10_3_c" # 91
# filename = "J10_3_d" # 5
# filename = "J11_14_a" # 142
# filename = "J11_14_b" # 187
# filename = "J11_14_c" # 172
# filename = "J11_14_d" # 29
# filename = "J17_10_a" # 40
# filename = "J17_10_c" # 36
# filename = "J18_6_a" # 109
# filename = "J18_6_b" # 81
# filename = "J18_6_c" # 117
filename = "J18_6_d" # 61

# fn = Path(f"data\Scaffan-analysis-jena-zeiss\{filename}.czi").resolve()
fn = Path(f"data\Anicka - reticular fibers\{foldername}\{filename}.czi").resolve()
logger.info(f"Reading file {fn}")
anim = scim.AnnotatedImage(fn)

# pixelsize_mm = [0.005, 0.005] # 200x200
# pixelsize_mm = [0.002, 0.002] # 500x500
pixelsize_mm = [0.001, 0.001] # 1000x1000

# 3000 - 46000 for x
c = 0
for i in range(43):
    for j in range(43):
        
        view = anim.get_view(center=((i+3)*1000,(j+3)*1000), size_mm=[1, 1], pixelsize_mm=pixelsize_mm) # slide through the raw czi image
        img = view.get_region_image(as_gray=False)

        if not np.all(img == 255):
            plt.imsave(f"pngdata/splits_live/{filename}/{filename}_split_{c}.png", img) # save the cropped part as a png
        c += 1

logger.info(f"File {fn} was split successfully.")