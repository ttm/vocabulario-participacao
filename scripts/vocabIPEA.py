#-*- coding: utf-8 -*-
from openpyxl import load_workbook
import unicodedata
import rdflib as r, sys

def sa(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')
def G(S,P,O):
    g.add((S,P,O))
L=r.Literal

vbs = r.Namespace("http://purl.org/socialparticipation/vbs/")
rdf = r.namespace.RDF
rdfs = r.namespace.RDFS
skos = r.namespace.SKOS
xsd = r.namespace.XSD

g = r.Graph()
g.namespace_manager.bind("vbs", "http://purl.org/socialparticipation/vbs/")    
g.namespace_manager.bind("rdf", r.namespace.RDF)    
g.namespace_manager.bind("rdfs", r.namespace.RDFS)    
g.namespace_manager.bind("xsd", r.namespace.XSD)    
g.namespace_manager.bind("skos", r.namespace.SKOS)    

wb2 = load_workbook('../fontes/vocabIPEA.xlsx')
ws=wb2.get_sheet_by_name("Plan1")
count=0
for row in ws.rows:
    count+=1
    ss=row[0].value
    print ss,ss.strip(),ss.replace(" ","")
    if "Codefat" in ss:
        slug="Codefat"
    elif "PNRS" in ss:
        slug="PNRS"
    elif "SIM" in ss:
        slug="SIM"
    else:
        slug=sa(ss.title().replace(" ","").replace("-",""))
    uri=eval("vbs.ipea"+slug)
    G(uri,rdf.type,skos.Concept)
    G(uri,skos.prefLabel,L(ss,lang="pt"))

f=open("../rdf/vbsIPEA.rdf","wb")
f.write(g.serialize())
f.close()

f=open("../rdf/vbsIPEA.ttl","wb")
f.write(g.serialize(format="turtle"))
f.close()


