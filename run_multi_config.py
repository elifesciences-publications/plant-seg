import glob
import yaml

paths = [## './config_resunet_ds2x_bce_gcr.yaml',
         './config_unet_ds2x_bce_gcr_aff.yaml']
         ## './config_unet_ds2x_dice_gcr_all.yaml',
         ## './config_unet_ds2x_bce_gcr.yaml',
         ## './config_unet_ds2x_bce_gcr_all.yaml',
         ## './config_unet_ds2x_bce_crg.yaml',
         ## './config_unet_ds1x_bce_aff_crg.yaml',
         ## './config_unet_ds2x_bce_gcr_noise.yaml',
         ## './config_unet_ds1x_bce_gcr.yaml',
         ## './config_unet_ds1x_bce_aff_gcr.yaml',
         ## './config_unet_ds2x_dice_gcr.yaml',
         ## './config_unet_ds2x_dice_gcr_aff.yaml']
         ## './config_unet_ds2x_bce_cgr.yaml',
         ## './config_unet_ds1x_bce_cgr.yaml',
         ## './config_unet_ds1x_bce_aff_cgr.yaml']

paths = glob.glob("./examples/segmentation/GASP/config_*.yaml")

import subprocess
for path in paths:
    print(path)
    subprocess.run(["python", "plantseg.py", "--config", path])