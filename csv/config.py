
#!/usr/bin/env python
from __future__ import print_function, unicode_literals
import  jinja2
import pandas as pd


with open('bgp_variables.csv') as f:
    csv_file = csv.DictReader(f)
for bgp_vars in csv_file:
    advertised_routes = bgp_vars['advertised_routes']
    advertised_routes = advertised_routes.split()
    bgp_vars['advertised_routes'] = advertised_routes
    
template_file = 'nxos_bgp_csv.j2'
with open(template_file) as f:
    bgp_template = f.read()
template = jinja2.Template(bgp_template)
print()
print('-' * 80)
print(template.render(bgp_vars))
print('-' * 80)
print()