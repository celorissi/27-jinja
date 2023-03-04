
#!/usr/bin/env python
## -*- coding: utf-8 -*-
import csv
from jinja2 import Environment, FileSystemLoader
from jinja2 import Template

source_file = "bgp_variables.csv"
bgp_template_file = "nxos_bgp_csv.j2"

with open(bgp_template_file) as f:
	bgp_template = Template(f.read(), keep_trailing_newline=True)

type(bgp_template)

with open(source_file) as f:
	reader = csv.DictReader(f)
	for row in reader:
		bgp_config = bgp_template.render(
			hostname = row["hostname"],
			local_as = row["local_as"],
			peer1_ip = row["peer_1_ip"],
			peer1_as = row["peer_1_as"],
			peer1_ipv6 = row["peer_1_ipv6"],
			advertised_routes = row["advertised_routes"]
			
		)
print(bgp_config)
