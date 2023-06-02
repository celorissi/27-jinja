#!/usr/bin/env python
from __future__ import print_function, unicode_literals
import  jinja2

#CONFIGURACAO DAS VARIAVEIS
diretorio_template = "/data/rissi/jinja/fgt_config_interagir/templates/"
diretorio_destino = "/data/rissi/jinja/fgt_config_interagir/arquivos_configuracao/"
hostname = 'FW_TESTE.conf' #input("Digite o Hostname da loja EX: FW_LOJA_CB_1511 :" )

##############################################
config_vars = {
    "hostname": hostname, # FW_LOJA_CB_1511
}

#ABRINDO O ARQUIVO JINJA TEMPLATE
template_file = diretorio_template +'1_fgt_config_global.j2'
with open(template_file) as f:
    config_template = f.read()

#CONCATENACAO DO ARQUIVO TEMPLATE JINJA COM O PYTHON
template = jinja2.Template(config_template)
print(template.render(config_vars))

#SALVANDO CONTEUDO EM UM ARQUIVO NOVO
arquivo_novo = (template.render(config_vars))

#SALVAR O CONTEUDO DO ARQUIVO NOVO EM UM ARQUIVO .CFG
arquivo = diretorio_destino + 'FW_TESTE.cfg'
with open(arquivo, 'w') as file:
    # Write the content to the file
    file.write(arquivo_novo)