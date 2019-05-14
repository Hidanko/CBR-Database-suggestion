from Peso import Pesos as Peso


class Calculos:

    def validacao_generica_boolean(valor, recebido, peso):
        if valor != recebido:
            return valor * Peso.licenca
        return 0

    # tamanho_maximo_banco = 1
    # tamanho_maximo_tabela = 1
    # tamanho_maximo_linha = 1
    # tamanho_maximo_blob = 1

    # 1 licenca paga / 0 open source
    def get_peso_licenca(valor, recebido):
        return validacao_generica_boolean(valor, recebido, Peso.licenca)

    def get_peso_data_lancamento(valor, recebido):
        diferenca = relativedelta(valor, recebido).years
        diferenca = diferenca if (diferenca > 0) else -diferenca
        return diferenca * Peso.data_lancamento

    def get_peso_ultima_atualizacao(valor, recebido):
        diferenca = relativedelta(valor, recebido).months
        diferenca = diferenca if (diferenca > 0) else -diferenca
        return diferenca * Peso.data_ultima_atualizacao

    def get_peso_suporte_windows(valor, recebido):
        return validacao_generica_boolean(valor, recebido, Peso.suporte_windows)

    def get_peso_suporte_linux(valor, recebido):
        return validacao_generica_boolean(valor, recebido, Peso.suporte_linux)

    def get_peso_suporte_mac(valor, recebido):
        return validacao_generica_boolean(valor, recebido, Peso.suporte_mac)

    def get_peso_acid(valor, recebido):
        return validacao_generica_boolean(valor, recebido, Peso.acid)

    def get_peso_hash(valor, recebido):
        return validacao_generica_boolean(valor, recebido, Peso.hash)

    def get_peso_regex(valor, recebido):
        return validacao_generica_boolean(valor, recebido, Peso.regex)

    def get_peso_paralelismo(valor, recebido):
        return validacao_generica_boolean(valor, recebido, Peso.queries_em_paralelo)

    def get_peso_cursor(valor, recebido):
        return validacao_generica_boolean(valor, recebido, Peso.cursor)

    def get_peso_protecao_forca_bruta(valor, recebido):
        return validacao_generica_boolean(valor, recebido, Peso.proteção_força_bruta)

    def get_peso_auditoria(valor, recebido):
        return validacao_generica_boolean(valor, recebido, Peso.auditoria)
