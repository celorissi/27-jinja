import glob

# search all files inside a specific folder
# *.* means file name with any extension
dir_path = r'/data/rissi/jinja/fgt_config_interagir/templates/'
res = glob.glob(dir_path)
print(res)