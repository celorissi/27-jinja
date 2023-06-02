#!/usr/bin/env python
from __future__ import print_function, unicode_literals
import  jinja2

#CONFIGURACAO DAS VARIAVEIS

arquivocfg = 'FW_LOJA_CB_TESTE.conf' #input("Digite o nome do arquivo.cfg: Ex: FW_LOJA_CB_1511.cfg : " )
hostname = 'FW_LOJA_CB_1511'#input("Digite o Hostname da loja Ex: FW_LOJA_CB_1511: " )
gateway_vlan22 = '10.110.88.100' #input("Digite o ip do gateway vlan 22: Exe 10.110.88.100 " )

##############################################
config_vars_1 = {
    "hostname": hostname, # FW_LOJA_CB_1511
}
config_vars_6 = {
    "gateway_vlan22": gateway_vlan22, # 10.110.88.100
}



#ABRINDO O ARQUIVO JINJA TEMPLATE
template_file_1 = '1_fgt_config_global.j2'
with open(template_file_1) as f:
    config_template = f.read()
#print(config_template)

template_file_6 = '6_fgt_dns.j2'
with open(template_file_6) as f:
    config_template_6 = f.read()
#print(config_template_2)

#CONCATENACAO DO ARQUIVO TEMPLATE JINJA COM O PYTHON
template1 = jinja2.Template(config_template)
#print(template.render(config_vars))

template6 = jinja2.Template(config_template_6)
#print(template2.render(config_vars_2))

#SALVAR O CONTEUDO DO ARQUIVO NOVO EM UM ARQUIVO.CFG
arquivo = arquivocfg
arquivo_novo = (template1.render(config_vars_1)) + '\n' + (template6.render(config_vars_6))

print(arquivo_novo)
with open(arquivo, 'w') as file:
    # Write the content to the file
    file.write(arquivo_novo)
