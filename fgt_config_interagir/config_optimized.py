#!/usr/bin/env python
from __future__ import print_function, unicode_literals
import  jinja2
import os
import glob

os.path.abspath('*')

#diretorios
diretorio_template = "/data/rissi/jinja/fgt_config_interagir/templates/"
diretorio_destino = "/data/rissi/jinja/fgt_config_interagir/arquivos_configuracao/"

#VARIAVEIS
arquivocfg = 'FW_LOJA_CB_TESTE.conf'
hostname = 'FW_LOJA_CB_1511'#input("Digite o Hostname da loja Ex: FW_LOJA_CB_1511: " )
endereço_ip_wan1 = '186.201.14.146 255.255.255.248' #186.201.14.146 255.255.255.248
wan1_gateway = '186.201.14.145' 
alias_wan1 = 'OUTSIDE_WCS' #OUTSIDE_WCS
endereço_ip_wan2 = '200.100.110.2 255.255.255.252'
alias_wan2 = 'OUTSIDE_VIVO' #OUTSIDE_VIVO
wan2_gateway = '200.100.110.1' 
LAN_CB = '10.111.88.100 255.255.252.0' # 10.111.88.100 255.255.252.0
gateway_vlan22 = '10.110.88.100' #input("Digite o ip do gateway vlan 22: Exe 10.110.88.100 " )
LAN_Wifi_Corp = '10.212.150.128 255.255.255.128' # 10.212.150.128 255.255.255.128
LAN_Wifi_DEVCOR = '10.216.2.128 255.255.255.128' # 10.216.2.128 255.255.255.128
LAN_Wifi_Mgmt = '10.215.15.128 255.255.255.128' # 10.215.15.128 255.255.255.128
VPN1_EQX_ip_tunnel = '10.253.3.10 255.255.255.255'# 10.253.3.10 255.255.255.255
VPN1_EQX_interface_saida =  'wan1' # wan1
VPN1_EQX_local_id = 'LJ_CB_1511_01'  #LJ_CB_1511_01
VPN1_EQX_psksecret = 'senhaforte' # senha identifca do user no sdwan
VPN2_EQX_ip_tunnel =  '10.253.19.10 255.255.255.255' # 10.253.19.10 255.255.255.255
VPN2_EQX_interface_saida = 'wan2' # wan2
VPN2_EQX_local_id = 'LJ_CB_1511_02' #  LJ_CB_1511_02
VPN2_EQX_psksecret =  'senhaforte'  # senha identifca do user no sdwan
dhcp_vlan_212_gateway =  '10.212.150.129'  # 10.212.150.129
dhcp_vlan_212_mascara =  '255.255.255.128' # 255.255.255.128
dhcp_vlan_212_start =  '10.212.150.130'  # 10.212.150.130
dhcp_vlan_212_end = '10.212.150.254'  # 10.212.150.254
dhcp_vlan_215_gateway = '10.215.15.128'  # 10.215.15.128
dhcp_vlan_215_mascara =  '255.255.255.128'# 255.255.255.128
dhcp_vlan_215_start =  '10.215.15.130'  # 10.215.15.130
dhcp_vlan_215_end =  '10.215.15.254'  # 10.215.15.254
dhcp_vlan_216_gateway =  '10.216.2.129'  # 10.216.2.129
dhcp_vlan_216_mascara =  '255.255.255.128' # 255.255.255.128
dhcp_vlan_216_start =  '10.216.2.130' # 10.216.2.130
dhcp_vlan_216_end = '10.216.2.254'  # 10.216.2.254
dhcp_vlan_22_gateway =  '10.111.88.100' # 10.111.88.100
dhcp_vlan_22_mascara = '255.255.252.0' #255.255.252.0
dhcp_vlan_22_start_22 = '10.111.88.22'# 10.111.88.22
dhcp_vlan_22_end_99 =  '10.111.88.99' # 10.111.88.99
dhcp_vlan_22_start_105 = '10.111.88.105'  # 10.111.88.105
dhcp_vlan_22_end_254 = '10.111.91.254'  # 10.111.91.254 (Termina com o iltimo range do /22)
impressora_inicial = '10.111.88.120' # 10.111.88.120
impressora_final =  '10.111.88.194' # 10.111.88.194
bgp_router_id = '10.111.93.254' #10.111.93.254

#Dicionarios
config_vars_1 = {
    "hostname": hostname, # FW_LOJA_CB_1511
}

config_vars_2 = {}
config_vars_3 = {}

config_vars_4 = {
    "endereço_ip_wan1": endereço_ip_wan1,
    "alias_wan1": alias_wan1,
    "endereço_ip_wan2": endereço_ip_wan2 ,
    "alias_wan2": alias_wan2,
    "LAN_CB": LAN_CB, 
    "LAN_Wifi_Corp": LAN_Wifi_Corp, 
    "LAN_Wifi_DEVCOR": LAN_Wifi_DEVCOR,
    "LAN_Wifi_Mgmt": LAN_Wifi_Mgmt,
}
config_vars_5 = {}
config_vars_6 = {
    "gateway_vlan22": gateway_vlan22,
}
config_vars_7 = {}
config_vars_8 = {
    "gateway_vlan22": gateway_vlan22,
}
config_vars_9 = {}
config_vars_10 = {
    "gateway_vlan22": gateway_vlan22, 
}
config_vars_11 = {
    "dhcp_vlan_212_gateway": dhcp_vlan_212_gateway,
    "dhcp_vlan_212_mascara": dhcp_vlan_212_mascara, 
    "dhcp_vlan_212_start": dhcp_vlan_212_start,
    "dhcp_vlan_212_end": dhcp_vlan_212_end, 
    "dhcp_vlan_215_gateway": dhcp_vlan_215_gateway,
    "dhcp_vlan_215_mascara": dhcp_vlan_215_mascara,
    "dhcp_vlan_215_start": dhcp_vlan_215_start,
    "dhcp_vlan_215_end": dhcp_vlan_215_end, 
    "dhcp_vlan_216_gateway": dhcp_vlan_216_gateway, 
    "dhcp_vlan_216_mascara": dhcp_vlan_216_mascara,
    "dhcp_vlan_216_start": dhcp_vlan_216_start,
    "dhcp_vlan_216_end": dhcp_vlan_216_end, 
    "dhcp_vlan_22_gateway": dhcp_vlan_22_gateway,
    "dhcp_vlan_22_mascara": dhcp_vlan_22_mascara,
    "dhcp_vlan_22_start_22": dhcp_vlan_22_start_22,
    "dhcp_vlan_22_end_99": dhcp_vlan_22_end_99,
    "dhcp_vlan_22_start_105": dhcp_vlan_22_start_105,
    "dhcp_vlan_22_end_254": dhcp_vlan_22_end_254,
}
config_vars_12 = {}
config_vars_13 = {
    "impressora_inicial": impressora_inicial,
    "impressora_final": impressora_final,
    "LAN_CB": LAN_CB, 
    "LAN_Wifi_Corp": LAN_Wifi_Corp, 
    "LAN_Wifi_DEVCOR": LAN_Wifi_DEVCOR,
    "LAN_Wifi_Mgmt": LAN_Wifi_Mgmt,
}
config_vars_14 = {}
config_vars_15 = {}
config_vars_16 = {}
config_vars_17 = {}
config_vars_18 = {}
config_vars_19 = {}
config_vars_20 = {}
config_vars_21 = {}
config_vars_22 = {}
config_vars_23 = {
    "gateway_vlan22": gateway_vlan22,
}
config_vars_24 = {}
config_vars_25 = {}
config_vars_26 = {
    "VPN1_EQX_ip_tunnel": VPN1_EQX_ip_tunnel,
    "VPN1_EQX_interface_saida": VPN1_EQX_interface_saida, 
    "VPN1_EQX_local_id": VPN1_EQX_local_id,
    "VPN1_EQX_psksecret": VPN1_EQX_psksecret, 
    "VPN2_EQX_ip_tunnel": VPN2_EQX_ip_tunnel,
    "VPN2_EQX_interface_saida": VPN2_EQX_interface_saida,
    "VPN2_EQX_local_id": VPN2_EQX_local_id,
    "VPN2_EQX_psksecret": VPN2_EQX_psksecret,
}
config_vars_27 = {}
config_vars_28 = {}
config_vars_29 = {}
config_vars_30 = {
    "gateway_vlan22": gateway_vlan22,
    "wan1_gateway": wan1_gateway,
    "wan2_gateway": wan2_gateway,
    "alias_wan1": alias_wan1,
    "alias_wan2": alias_wan2,
    
}
config_vars_31 = {}
config_vars_32 = {}
config_vars_33 = {}
config_vars_34 = {}
config_vars_35 = {
    "bgp_router_id":bgp_router_id,
    "LAN_CB": LAN_CB, 
    "LAN_Wifi_Corp": LAN_Wifi_Corp, 
    "LAN_Wifi_DEVCOR": LAN_Wifi_DEVCOR,
    "LAN_Wifi_Mgmt": LAN_Wifi_Mgmt,
    
}

#LISTANDO DIRETORIOS

dir_path = '/data/rissi/jinja/fgt_config_interagir/templates/'



lista_de_arquivos = os.listdir(dir_path)


sorted_files = sorted(lista_de_arquivos)
#print(sorted_files)

for path in sorted_files:
    #print(path)

    template_file_1 = diretorio_template + path
    with open(template_file_1) as f:
        config_template = f.read()
        #print(config_template)
        #print(path.name)
    
        template1 = jinja2.Template(config_template)
        #print(template1.render(config_vars_1))
        
        nome_arquivo = arquivocfg
        arquivo_novo = (template1.render(config_vars_1)) + '\n'
        
        with open(diretorio_destino + nome_arquivo, 'a') as file:
        # Write the content to the file
            file.write(arquivo_novo)
   

        

