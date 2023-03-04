
#!/usr/bin/env python
from __future__ import print_function, unicode_literals
import  jinja2
import pandas as pd

csv_file = pd.read_csv("bgp_variables.csv", sep=",")

f = open(csv_file)
csv_content = f.read()
f.close()


csv_lines = csv_content.splitlines()
headers = csv_lines[0].split(";")
for i in range(1, len(csv_lines)):
    values = csv_lines[i].split(";")
    parameter_dict = dict()
    for h in range(0, len(headers)):
        parameter_dict[headers[h]] = values[h]
    config_parameters.append(parameter_dict)

for parameter in config_parameters:
    result = template.render(parameter)
    f = open(os.path.join(output_directory, parameter + ".config"), "w")
    f.write(result)
    f.close()

