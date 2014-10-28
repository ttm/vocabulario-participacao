#!python3
#-*- coding: utf-8 -*-
import xml.etree.ElementTree as ET, os
import rdflib as r
def G(S,P,O):
    g.add((S,P,O))
L=r.Literal

vbs = r.Namespace("http://purl.org/socialparticipation/vbs/")
rdf = r.namespace.RDF
rdfs = r.namespace.RDFS
skos = r.namespace.SKOS
xsd = r.namespace.XSD

store="../rdf/vbsConferencia.rdf"
store2="../rdf/vbsConselho.rdf"
store3="../rdf/vbsOuvidoria.rdf"
g = r.Graph()
g.load(store)
g.load(store2)
g.load(store3)

PREFIX="""PREFIX skos: <http://www.w3.org/2004/02/skos/core#>"""

q="SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l . }"
res=g.query(PREFIX+q)
conceitos=[rr[0] for rr in res]
conceitos=sorted(conceitos,key=lambda s: s.replace(u"á",u"a").replace(u"Á",u"a").replace(u"Ó",u"o").replace(u"ó",u"o").encode("utf8").lower())

#f=open("../rdf/vbsConferenciaPalavras.txt", "wb")
#sys.stdout = f
for cc in conceitos:
    print (u"%s"%(cc,)).encode("utf8")

#f.close()
#
#
#
## leitura dos termos dos arquivos na pasta ../fontes/
#termos=[]
#arquivos=os.listdir("../fontes/")
#arquivos=[ar for ar in arquivos if ar.endswith("txt")]
#for arquivo in arquivos:
#    path="../fontes/"+arquivo
#    tfile=open(path,"rb")
#    termos_=tfile.readlines()
#    termos+=termos_
root = ET.Element('node')
root.set("id","vocab_part")
root.set("label",u"Vocabulário Controlado para Biblioteca de Participação Social")
foo= ET.SubElement(root, "isComposedBy")
conta_id=1
#for palavra in termos:
for palavra in conceitos:
    termo = ET.SubElement(foo, "node")
    termo.set("id",str(conta_id))
    conta_id+=1
    # Para deixar em caixa alta somente as palavras mais
    # significativas, conforme modelo recebido
    palavra_=" ".join(w.capitalize() if w not in ["com",u"não","ad","dos","ou","de","e","da","do","na","no","ao",u"à"] else w for w in palavra.split()).replace("Sac","SAC").replace("(sistema","(Sistema").replace("Lai","LAI").replace("(lei","(Lei").replace("Ogu","OGU").replace("(ouvidoria","(Ouvidoria")
    #termo.set("label",palavra_.decode("utf-8"))
    #termo.set("label",palavra_.encode("utf-8"))
    termo.set("label",palavra_)
tree = ET.ElementTree(root)
tree.write('../vocabulario/dspace.xml', xml_declaration=True, encoding='utf-8')
#tree.write('../vocabulario/dspace.xml', xml_declaration=True)
# para deixar bem formatado:
# ! xmllint --format - 
