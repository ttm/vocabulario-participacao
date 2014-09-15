#!python3
#-*- coding: utf-8 -*-
import xml.etree.ElementTree as ET, os

# leitura dos termos dos arquivos na pasta ../fontes/
arquivos=os.listdir("../fontes/")
arquivos=[ar for ar in arquivos if ar.endswith("txt")]

root = ET.Element('node')
root.set("id","vocab_part")
root.set("label",u"Vocabulário Controlado para Biblioteca de Participação Social")
foo= ET.SubElement(root, "isComposedBy")
conta_id=1
labels={'vocabIPEA.txt':u'Vocabulário repassado pelo IPEA',
 'vocabOPS.txt':u'Vocabulário observado na OPS',
 'vocabFreqParticipa.txt':u'Vocabulário com anta incidência no Participa.br',
 'vocabOPA.txt':u'Vocabulário observado na OPA',
 'vocabPNPS.txt':u'Vocabulário observado no Decreto nº 8243/14 (PNPS)'}
for arquivo in arquivos:
    path="../fontes/"+arquivo
    tfile=open(path,"rb")
    termos_=tfile.readlines()
    fonte= ET.SubElement(foo, "node")
    fonte.set("label",labels[arquivo])
    foo2= ET.SubElement(fonte, "isComposedBy")
    for palavra in termos_:
        termo = ET.SubElement(foo2, "node")
        termo.set("id",str(conta_id))
        conta_id+=1
        termo.set("label",palavra[:-1].decode("utf-8"))
tree = ET.ElementTree(root)
tree.write('vp-fonte.xml', xml_declaration=True, encoding='utf-8')
# para deixar bem formatado:
# ! xmllint --format - 
