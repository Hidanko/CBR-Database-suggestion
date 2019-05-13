class Banco:
    nome = ""

    licenca = ""
    data_lancamento = ""
    data_ultima_atualizacao = ""
    suporte_windows = False
    suporte_linux = False
    suporte_mac = False
    acid = ""
    tamanho_maximo_banco = ""
    tamanho_maximo_tabela = ""
    tamanho_maximo_linha = ""
    tamanho_maximo_blob = ""
    hash = ""
    regex = ""
    queries_em_paralelo = ""
    cursor = ""
    proteção_força_bruta = ""
    auditoria = ""

    def __init__(self, nome, licenca, data_lancamento, data_ultima_atualizacao, suporte_windows, suporte_linux,
                 suporte_mac, acid, max_banco, max_tabela, max_linha, max_blob, hash, regex, paraleto, cursor,
                 protecao_forca_bruta, auditoria):
        self.nome = nome
        self.licenca = licenca
        self.data_lancamento = data_lancamento
        self.data_ultima_atualizacao = data_ultima_atualizacao
        self.suporte_windows = suporte_windows
        self.suporte_linux = suporte_linux
        self.suporte_mac = suporte_mac
        self.acid = acid
        self.tamanho_maximo_banco = max_banco
        self.tamanho_maximo_tabela = max_tabela
        self.tamanho_maximo_linha = max_linha
        self.tamanho_maximo_blob = max_blob
        self.hash = hash
        self.regex = regex
        self.queries_em_paralelo = paraleto
        self.cursor = cursor
        self.proteção_força_bruta = protecao_forca_bruta
        self.auditoria = auditoria
