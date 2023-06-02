#!/usr/bin/env python
from __future__ import print_function, unicode_literals
import  jinja2

#diretorios
diretorio_template = "/data/rissi/jinja/fgt_config_interagir/templates/"
diretorio_destino = "/data/rissi/jinja/fgt_config_interagir/arquivos_configuracao/"

#VARIAVEIS
arquivocfg = 'FW_LOJA_CB_1511.conf' #input("Digite o nome do arquivo.cfg: Ex: FW_LOJA_CB_1511.cfg : " )
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

#ABRINDO O ARQUIVO JINJA TEMPLATE
template_file_1 = diretorio_template + '01_fgt_config_global.j2'
with open(template_file_1) as f:
    config_template = f.read()
#print(config_template)

template_file_2 = diretorio_template + '02_fgt_acc_profile.j2'
with open(template_file_2) as f:
    config_template_2 = f.read()

template_file_3 = diretorio_template +'03_fgt_virtual_switch.j2'
with open(template_file_3) as f:
    config_template_3 = f.read()

template_file_4 = diretorio_template + '04_fgt_interfaces.j2'
with open(template_file_4) as f:
    config_template_4 = f.read()
    
template_file_5 = diretorio_template + '05_fgt_sys_admin.j2'
with open(template_file_5) as f:
    config_template_5 = f.read()

template_file_6 = diretorio_template + '06_fgt_dns.j2'
with open(template_file_6) as f:
    config_template_6 = f.read()
    
template_file_7 = diretorio_template + '07_fgt_snmp.j2'
with open(template_file_7) as f:
    config_template_7 = f.read()

template_file_8 = diretorio_template + '08_fgt_fortimanager.j2'
with open(template_file_8) as f:
    config_template_8 = f.read()
    
template_file_9 = diretorio_template + '09_fgt_ips.j2'
with open(template_file_9) as f:
    config_template_9 = f.read()

template_file_10 = diretorio_template + '10_fgt_fortianayzer.j2'
with open(template_file_10) as f:
    config_template_10 = f.read()
    
template_file_11 = diretorio_template + '11_fgt_dhcp.j2'
with open(template_file_11) as f:
    config_template_11 = f.read()
    
template_file_12 = diretorio_template + '12_fgt_zone.j2'
with open(template_file_12) as f:
    config_template_12 = f.read()

template_file_13 = diretorio_template + '13_fgt_address.j2'
with open(template_file_13) as f:
    config_template_13 = f.read()

template_file_14 = diretorio_template + '14_fgt_address_group.j2'
with open(template_file_14) as f:
    config_template_14 = f.read()
    
template_file_15 = diretorio_template + '15_fgt_service_custon.j2'
with open(template_file_15) as f:
    config_template_15 = f.read()

template_file_16 = diretorio_template + '16_fgt_service_group.j2'
with open(template_file_16) as f:
    config_template_16 = f.read()

template_file_17 = diretorio_template + '17_fgt_webfilter_ftgd-local-rating.j2'
with open(template_file_17) as f:
    config_template_17 = f.read()  

template_file_18 = diretorio_template + '18_fgt_ips.j2'
with open(template_file_18) as f:
    config_template_18 = f.read()  

template_file_19 = diretorio_template + '19_fgt_traffic_shapper.j2'
with open(template_file_19) as f:
    config_template_19 = f.read()     

template_file_20 = diretorio_template + '20_fgt_app_control.j2'
with open(template_file_20) as f:
    config_template_20 = f.read()   

template_file_21 = diretorio_template + '21_fgt_dlp.j2'
with open(template_file_21) as f:
    config_template_21 = f.read()   
    
template_file_22 = diretorio_template + '22_fgt_webfilter_urlfilter.j2'
with open(template_file_22) as f:
    config_template_22 = f.read()  

template_file_23 = diretorio_template + '23_fgt_tacacs.j2'
with open(template_file_23) as f:
    config_template_23 = f.read()  

template_file_24 = diretorio_template + '24_fgt_ldap.j2'
with open(template_file_24) as f:
    config_template_24 = f.read()  

template_file_25 = diretorio_template + '25_fgt_user_group.j2'
with open(template_file_25) as f:
    config_template_25 = f.read() 
    
template_file_26 = diretorio_template + '26_fgt_vpn.j2'
with open(template_file_26) as f:
    config_template_26 = f.read() 

template_file_27 = diretorio_template + '27_fgt_av.j2'
with open(template_file_27) as f:
    config_template_27 = f.read() 

template_file_28 = diretorio_template + '28_fgt_webfilter.j2'
with open(template_file_28) as f:
    config_template_28 = f.read() 

template_file_29 = diretorio_template + '29_fgt_webfilter_local_rating.j2'
with open(template_file_29) as f:
    config_template_29 = f.read() 
    
template_file_30 = diretorio_template + '30_fgt_sdwan.j2'
with open(template_file_30) as f:
    config_template_30 = f.read() 
    
template_file_31 = diretorio_template + '31_fgt_ssl.j2'
with open(template_file_31) as f:
    config_template_31 = f.read() 
    
template_file_32 = diretorio_template + '32_fgt_policy.j2'
with open(template_file_32) as f:
    config_template_32 = f.read() 
    
template_file_33 = diretorio_template + '33_fgt_local_policy.j2'
with open(template_file_33) as f:
    config_template_33 = f.read() 

template_file_34 = diretorio_template + '34_fgt_static_route.j2'
with open(template_file_34) as f:
    config_template_34 = f.read() 
    
template_file_35 = diretorio_template + '35_fgt_bgp.j2'
with open(template_file_35) as f:
    config_template_35 = f.read() 
    
#CONCATENACAO DO ARQUIVO TEMPLATE JINJA COM O PYTHON
template1 = jinja2.Template(config_template)
template2 = jinja2.Template(config_template_2)
template3 = jinja2.Template(config_template_3)
template4 = jinja2.Template(config_template_4)
template5 = jinja2.Template(config_template_5)
template6 = jinja2.Template(config_template_6)
template7 = jinja2.Template(config_template_7)
template8 = jinja2.Template(config_template_8)
template9 = jinja2.Template(config_template_9)
template10 = jinja2.Template(config_template_10)
template11 = jinja2.Template(config_template_11)
template12 = jinja2.Template(config_template_12)
template13 = jinja2.Template(config_template_13)
template14 = jinja2.Template(config_template_14)
template15 = jinja2.Template(config_template_15)
template16 = jinja2.Template(config_template_16)
template17 = jinja2.Template(config_template_17)
template18 = jinja2.Template(config_template_18)
template19 = jinja2.Template(config_template_19)
template20 = jinja2.Template(config_template_20)
template21 = jinja2.Template(config_template_21)
template22 = jinja2.Template(config_template_22)
template23 = jinja2.Template(config_template_23)
template24 = jinja2.Template(config_template_24)
template25 = jinja2.Template(config_template_25)
template26 = jinja2.Template(config_template_26)
template27 = jinja2.Template(config_template_27)
template28 = jinja2.Template(config_template_28)
template29 = jinja2.Template(config_template_29)
template30 = jinja2.Template(config_template_30)
template31 = jinja2.Template(config_template_31)
template32 = jinja2.Template(config_template_32)
template33 = jinja2.Template(config_template_33)
template34 = jinja2.Template(config_template_34)
template35 = jinja2.Template(config_template_35)
#print(template2.render(config_vars_2))


#SALVAR O CONTEUDO DO ARQUIVO NOVO EM UM ARQUIVO.CFG
nome_arquivo = arquivocfg
arquivo_novo = (template1.render(config_vars_1)) + '\n' + (template2.render(config_vars_2)) + '\n' + (template3.render(config_vars_3)) + '\n' + (template4.render(config_vars_4)) + '\n' + (template5.render(config_vars_5)) + '\n' + (template6.render(config_vars_6)) + '\n' + (template7.render(config_vars_7)) + '\n' + (template8.render(config_vars_8)) + '\n' + (template9.render(config_vars_9)) + '\n' + (template10.render(config_vars_10)) + '\n' + (template11.render(config_vars_11)) + '\n' + (template12.render(config_vars_12)) + '\n' + (template13.render(config_vars_13)) + '\n' + (template14.render(config_vars_14)) + '\n' + (template15.render(config_vars_15)) + '\n' + (template16.render(config_vars_16)) + '\n' + (template17.render(config_vars_17)) + '\n' + (template18.render(config_vars_18)) + '\n' + (template19.render(config_vars_19)) + '\n' + (template20.render(config_vars_20)) + '\n' + (template21.render(config_vars_21)) + '\n' + (template22.render(config_vars_22)) + '\n' + (template23.render(config_vars_23)) + '\n' + (template24.render(config_vars_24)) + '\n' + (template25.render(config_vars_25)) + '\n' + (template26.render(config_vars_26)) + '\n' + (template27.render(config_vars_27)) + '\n' + (template28.render(config_vars_28)) + '\n' + (template29.render(config_vars_29)) + '\n' + (template30.render(config_vars_30)) + '\n' + (template31.render(config_vars_31)) + '\n' + (template32.render(config_vars_32)) + '\n' + (template33.render(config_vars_33)) + '\n' + (template34.render(config_vars_34)) + '\n' + (template35.render(config_vars_35))


with open(diretorio_destino + nome_arquivo, 'w') as file:
    # Write the content to the file
    file.write(arquivo_novo)
    
#VISUALIZAR O CONTEUDO DO ARQUIVO .CONF
print(arquivo_novo)
