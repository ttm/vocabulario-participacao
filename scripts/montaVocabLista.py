#!python3
#-*- coding: utf-8 -*-
import xml.etree.ElementTree as ET, os

# leitura dos termos dos arquivos na pasta ../fontes/
termos=[]
arquivos=os.listdir("../fontes/")
arquivos=[ar for ar in arquivos if ar.endswith("txt")]
for arquivo in arquivos:
    path="../fontes/"+arquivo
    tfile=open(path,"rb")
    termos_=tfile.readlines()
    termos+=termos_
root = ET.Element('node')
root.set("id","vocab_part")
root.set("label",u"Vocabulário Controlado para Biblioteca de Participação Social")
foo= ET.SubElement(root, "isComposedBy")
conta_id=1
for palavra in termos:
    termo = ET.SubElement(foo, "node")
    termo.set("id",str(conta_id))
    conta_id+=1
    # Para deixar em caixa alta somente as palavras mais
    # significativas, conforme modelo recebido
    palavra_=" ".join(w.capitalize() if w not in ["de","e","da","do","na","no"] else w for w in palavra[:-1].split())
    termo.set("label",palavra_.decode("utf-8"))
tree = ET.ElementTree(root)
tree.write('vp-lista.xml', xml_declaration=True, encoding='utf-8')
# para deixar bem formatado:
# ! xmllint --format - 
