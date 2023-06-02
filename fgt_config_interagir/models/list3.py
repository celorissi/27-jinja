import os

# get all files inside a specific folder
dir_path = r'/data/rissi/jinja/fgt_config_interagir/templates/'
for path in os.scandir(dir_path):
    if path.is_file():
        print(path.name)