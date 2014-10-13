from OD import *
#doc = ODSReader("films.ods")
doc = ODSReader("../fontes/base_dados_conselhos_nacionais_normas_ipea_2013.ods")
table = doc.getSheet("Estrutura")
firstRow = table[0]
firstCellOfFirstRow = firstRow[0]
# 3 grupos de colunas:
# 0-19 -> G1 - informações gerais
# 20-27 -> G2 - quantizações básicas
# 28-34 -> G3 - gestão do conselho


