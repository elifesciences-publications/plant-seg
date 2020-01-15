import glob
import yaml

#paths = glob.glob("./examples/segmentation//config_*bc.yaml")

paths = ["config_resunet_ds2x_dice_gcr.yaml",
         "config_unet_ds2x_bce_bcr.yaml",
         "config_unet_ds2x_dice_gcr_noise.yaml"]

locations = [#"examples/segmentation/GASP/",
            #"examples/segmentation/MtxWS/",
             "examples/segmentation/MultiCut/"]
            #"examples/segmentation/WS/"]
import subprocess
for location in locations:
    for path in paths:
        print(location + path)
        subprocess.run(["python", "plantseg.py", "--config", location + path])