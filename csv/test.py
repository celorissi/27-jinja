#!/usr/bin/env python
## -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
import  jinja2
import csv

source_file = "bgp_variables.csv"
template_file = 'nxos_bgp_csv.j2'

type(bgp_template)

with open(source_file, "r") as arquivo:
	arquivo = csv.DictReader(arquivo, delimiter=",")
	for bgp_vars in arquivo:
        advertised_routes = bgp_vars['advertised_routes']
        advertised_routes = advertised_routes.split()
		bgp_vars['advertised_routes'] = advertised_routes


	with open(template_file) as f:
	    bgp_template = f.read()

	    template = jinja2.Template(bgp_template)
	    print()
	    print('-' * 80)
	    print(template.render(bgp_vars))
	    print('-' * 80)
	    print()
