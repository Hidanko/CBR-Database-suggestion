from Peso import Pesos as Peso
from dateutil.relativedelta import relativedelta

data_lancamento = 1
data_ultima_atualizacao = 1
suporte_windows = 1
suporte_linux = 1
suporte_mac = 1
acid = 1
tamanho_maximo_banco = 1
tamanho_maximo_tabela = 1
tamanho_maximo_linha = 1
tamanho_maximo_blob = 1
hash = 1
regex = 1
queries_em_paralelo = 1
cursor = 1
proteção_força_bruta = 1
auditoria = 1

# 1 licenca paga / 0 open source
get_peso_licenca(valor, recebido):
if valor != recebido:
    return valor * Peso.licenca
return 0

get_peso_data_lancamento(valor, recebido):
diferenca = relativedelta(valor, recebido).years
diferenca = diferenca if (diferenca > 0) else -diferenca
