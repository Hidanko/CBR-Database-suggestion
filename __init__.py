import datetime

from Banco import Banco
from Calculos import Calculos

nome = "Referencia buscada"
licenca = ""
data_lancamento = datetime.strptime('2012-02-10', '%Y-%m-%d')
data_ultima_atualizacao = datetime.strptime('2012-02-10', '%Y-%m-%d')
suporte_windows = False
suporte_linux = False
suporte_mac = False
acid = False
hash = False
regex = False
queries_em_paralelo = False
cursor = False
proteção_força_bruta = False
auditoria = False

menor_valor = 9999999
menor_banco = Banco
arquivo = open("bancos.txt")
bancos = list()

max_lancamento = 0
min_lancamento = 99999
max_atualizacao = 0
min_atualizacao = 99999

for linha in arquivo:
    print(linha)
    attr = linha.split(";")
    b = Banco(attr[0], attr[1], attr[2], attr[3], attr[4], attr[5], attr[6], attr[7], attr[8], attr[9], attr[10],
              attr[11],
              attr[12], attr[13], attr[14], attr[15], attr[16], attr[17])

for b in bancos:
    bancos.append(b)
    soma = 0
    soma += Calculos.get_peso_licenca(licenca, b.licenca)
    soma += Calculos.get_peso_data_lancamento(data_lancamento, b.data_lancamento)
    soma += Calculos.get_peso_ultima_atualizacao(data_ultima_atualizacao, b.data_ultima_atualizacao)
    soma += Calculos.get_peso_suporte_linux(linux, b.suporte_linux)
    soma += Calculos.get_peso_suporte_mac(suporte_mac, b.suporte_mac)
    soma += Calculos.get_peso_acid(acid, b.acid)
    soma += Calculos.get_peso_hash(hash, b.hash)
    soma += Calculos.get_peso_regex(regex, b.regex)
    soma += Calculos.get_peso_paralelismo(queries_em_paralelo, b.queries_em_paralelo)
    soma += Calculos.get_peso_cursor(cursor, b.cursor)
    soma += Calculos.get_peso_protecao_forca_bruta(proteção_força_bruta, b.proteção_força_bruta)
    soma += Calculos.get_peso_auditoria(auditoria, b.auditoria)

    if soma < menor_valor:
        menor_valor = soma
        menor_banco = bancos

print("Resposta =" + b.nome)
print("Diferenca de " + menor_valor)
