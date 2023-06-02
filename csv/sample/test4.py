from __future__ import print_function, unicode_literals
import  jinja2
import csv

imput_file = csv.DictReader(open("bgp_variables.csv"))

for row in imput_file:
    print(row)
