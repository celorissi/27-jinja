#!/usr/bin/env python
from __future__ import print_function, unicode_literals
import  jinja2

#CONFIGURACAO DAS VARIAVEIS

hostname = input("Digite o Hostname da loja EX: FW_LOJA_CB_1511 :" )
endereço_ip_wan1 = input("Digite o ip da WAN1 EXE: 186.201.14.146 255.255.255.248 :" )



##############################################
config_vars = {
    "hostname": hostname, # FW_LOJA_CB_1511
    "endereço ip wan1": endereço_ip_wan1, # 186.201.14.146 255.255.255.248
    "alias wan1": 'OUTSIDE_WCS', # "OUTSIDE_WCS"
    "wan1_gateway": '', # 186.201.14.145
    "endereço ip wan2": '',# 189.155.2.32 255.255.255.252
    "alias wan2": '', #"OUTSIDE_VIVO"
    "wan2_gateway": '', #189.155.2.31
    "LAN_CB": '', # 10.111.88.100 255.255.252.0
    "LAN_Wifi_Corp": '', # 10.212.150.128 255.255.255.128
    "LAN_Wifi_DEVCOR": '',# 10.216.2.128 255.255.255.128
    "LAN_Wifi_Mgmt": '',# 10.215.15.128 255.255.255.128
    "VPN1_EQX_ip_tunnel": '',# 10.253.3.10 255.255.255.255
    "VPN1_EQX_interface_saida": '', # wan1
    "VPN1_EQX_local id": '',#  "LJ_CB_1511_01"
    "VPN1_EQX_psksecret": '', # senha identifca do user no sdwan
    "VPN2_EQX_ip_tunnel": '',# 10.253.19.10 255.255.255.255
    "VPN2_EQX_interface_saida": '', # wan2
    "VPN2_EQX_local id": '',#  "LJ_CB_1511_02"
    "VPN2_EQX_psksecret": '', # senha identifca do user no sdwan
    "dhcp_vlan_212_gateway": '', # 10.212.150.129
    "dhcp_vlan_212_mascara": '', # 255.255.255.128
    "dhcp_vlan_212_start": '', # 10.212.150.130
    "dhcp_vlan_212_end": '', # 10.212.150.254
    "dhcp_vlan_215_gateway": '', # 10.215.15.128
    "dhcp_vlan_215_mascara": '',# 255.255.255.128
    "dhcp_vlan_215_start": '', # 10.215.15.130
    "dhcp_vlan_215_end": '', # 10.215.15.254
    "dhcp_vlan_216_gateway": '', # 10.216.2.129
    "dhcp_vlan_216_mascara": '',# 255.255.255.128
    "dhcp_vlan_216_start": '',# 10.216.2.130
    "dhcp_vlan_216_end": '', # 10.216.2.254
    "dhcp_vlan_22_gateway": '',# 10.111.88.100
    "dhcp_vlan_22_mascara": '',#255.255.252.0
    "dhcp_vlan_22_start_22": '',# 10.111.88.22
    "dhcp_vlan_22_end_99": '',# 10.111.88.99
    "dhcp_vlan_22_start_105": '', # 10.111.88.105
    "dhcp_vlan_22_end_254": '', # 10.111.91.254 (Termina com o iltimo range do /22)
    "impressora_inicial": '' , # 10.111.88.120
    "impressora_final": '' , # 10.111.88.194
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
arquivo = 'FW_LOJA_CB_2442_NEW.cfg'
with open(arquivo, 'w') as file:
    # Write the content to the file
    file.write(arquivo_novo)