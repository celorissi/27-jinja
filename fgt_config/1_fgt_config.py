#!/usr/bin/env python
from __future__ import print_function, unicode_literals
import  jinja2

#CONFIGURACAO DAS VARIAVEIS


config_vars = {
    "hostname": 'FW_LOJA_CB_2442', # FW_LOJA_CB_1511
    "endereco_ip_wan1": "138.59.148.98 255.255.255.252", # 186.201.14.146 255.255.255.248
    "alias_wan1": 'OUTSIDE_WCS', # "OUTSIDE_WCS"
    "wan1_gateway": '138.59.148.97', # 186.201.14.145
    "endereco_ip_wan2": '',# 189.155.2.32 255.255.255.252
    "alias_wan2": '', #"OUTSIDE_VIVO"
    "wan2_gateway": '', #189.155.2.31
    "LAN_CB": '10.150.160.0 255.255.252.0', # 10.111.88.100 255.255.252.0
    "LAN_Wifi_Corp": '10.212.215.64 255.255.255.224', # 10.212.150.128 255.255.255.128
    "LAN_Wifi_DEVCOR": '10.237.128.128 255.255.255.128',# 10.216.2.128 255.255.255.128
    "LAN_Wifi_Mgmt": '10.215.36.192 255.255.255.248 ',# 10.215.15.128 255.255.255.128
    "VPN1_EQX_ip_tunnel": '10.253.15.140 255.255.255.255',# 10.253.3.10 255.255.255.255
    "VPN1_EQX_interface_saida": 'wan1', # wan1
    "VPN1_EQX_local_id": 'LJ_CB_2442_01',#  "LJ_CB_1511_01"
    "VPN1_EQX_psksecret": 'senhaforte', # senha identifca do user no sdwan
    "VPN2_EQX_ip_tunnel": '10.253.31.140 255.255.255.255',# 10.253.19.10 255.255.255.255
    "VPN2_EQX_interface_saida": 'wan2', # wan2
    "VPN2_EQX_local_id": 'LJ_CB_2442_02',#  "LJ_CB_1511_02"
    "VPN2_EQX_psksecret": 'senhaforte', # senha identifca do user no sdwan
    "dhcp_vlan_212_gateway": '10.212.215.65', # 10.212.150.129
    "dhcp_vlan_212_mascara": '255.255.255.224', # 255.255.255.128
    "dhcp_vlan_212_start": '10.212.215.66', # 10.212.150.130
    "dhcp_vlan_212_end": '10.212.215.94', # 10.212.150.254
    "dhcp_vlan_215_gateway": '10.215.36.193', # 10.215.15.128
    "dhcp_vlan_215_mascara": '255.255.255.248',# 255.255.255.128
    "dhcp_vlan_215_start": '10.215.36.194', # 10.215.15.130
    "dhcp_vlan_215_end": '10.215.36.198', # 10.215.15.254
    "dhcp_vlan_216_gateway": '10.237.128.129', # 10.216.2.129
    "dhcp_vlan_216_mascara": '255.255.255.128',# 255.255.255.128
    "dhcp_vlan_216_start": '10.237.128.130',# 10.216.2.130
    "dhcp_vlan_216_end": '10.237.128.254', # 10.216.2.254
    "dhcp_vlan_22_gateway": '10.150.160.100',# 10.111.88.100
    "dhcp_vlan_22_mascara": '255.255.252.0',#255.255.252.0
    "dhcp_vlan_22_start_22": '10.150.160.22',# 10.111.88.22
    "dhcp_vlan_22_end_99": '10.150.160.99',# 10.111.88.99
    "dhcp_vlan_22_start_105": '10.150.160.105', # 10.111.88.105
    "dhcp_vlan_22_end_254": '10.150.163.254', # 10.111.91.254 (Termina com o iltimo range do /22)
}

#ABRINDO O ARQUIVO JINJA TEMPLATE
template_file = 'fgt_config.j2'
with open(template_file) as f:
    config_template = f.read()

#CONCATENACAO DO ARQUIVO TEMPLATE JINJA COM O PYTHON
template = jinja2.Template(config_template)
print(template.render(config_vars))

#SALVANDO CONTEUDO EM UM ARQUIVO NOVO
arquivo_novo = (template.render(config_vars))

#SALVAR O CONTEUDO DO ARQUIVO NOVO EM UM ARQUIVO .CFG
arquivo = 'FW_LOJA_CB_2442_NEW.conf'
with open(arquivo, 'w') as file:
    # Write the content to the file
    file.write(arquivo_novo)