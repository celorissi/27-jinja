
#!/usr/bin/env python
from __future__ import print_function, unicode_literals
import  jinja2
import pandas as pd

csv_file = pd.read_csv("bgp_variables.csv", sep=",")
with open(csv_file) as f:
	read_csv = csv.splitlines()
	print(read_csv)
#	for bgp_vars in read_csv:
#        advertised_routes = bgp_vars['advertised_routes']
#        advertised_routes = advertised_routes.split()
#	    bgp_vars['advertised_routes'] = advertised_routes 
#
#
#	    with open(template_file) as f:
#		    bgp_template = f.read()
#
#	    template = jinja2.Template(bgp_template)
#	    print()
#	    print('-' * 80)
#	    print(template.render(bgp_vars))
#	    print('-' * 80)
#	    print()