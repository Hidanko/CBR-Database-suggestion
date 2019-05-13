from Banco import Banco




arquivo = open("bancos.txt")
bancos = list()
for linha in arquivo:
    print(linha)
    attr = linha.split(";")
    b = Banco(attr[0],attr[1],attr[2],attr[3],attr[4],attr[5],attr[6],attr[7],attr[8],attr[9],attr[10],attr[11],
              attr[12],attr[13],attr[14],attr[15],attr[16],attr[17])
    bancos.append(b)

