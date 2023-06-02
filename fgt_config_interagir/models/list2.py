from os import walk

# folder path
dir_path = r'/data/rissi/jinja/fgt_config_interagir/templates/'

# list to store files name
res = []
for (dir_path, dir_names, file_names) in walk(dir_path):
    res.extend(file_names)
print(res)