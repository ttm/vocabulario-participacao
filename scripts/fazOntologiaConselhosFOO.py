#!/usr/bin/python
#-*- coding: utf-8 -*-
import cPickle as pickle, time, string
from SPARQLWrapper import SPARQLWrapper, JSON
import rdflib as r, pygraphviz as gv
import pylab as pl

U=r.URIRef
g=r.Graph() # para a ontologia
def G(S,P,O):
    g.add((S,P,O))
dct=r.namespace.DCTERMS
owl = r.namespace.OWL
rdf = r.namespace.RDF
rdfs = r.namespace.RDFS
obs = r.Namespace("http://purl.org/socialparticipation/obs/")
xsd = r.namespace.XSD

ouri=obs.obs+".owl"
g.add((ouri,rdf.type,owl.Ontology)) 
g.add((ouri,dct.title,r.Literal("Ontologia da Biblioteca Semantica de participação social")))
g.add((ouri,owl.versionInfo,r.Literal("0.001a")))
g.add((ouri,dct.description,r.Literal("Ontologia para uso pela biblioteca digital (e semântica) de participação social")))

g2=r.Graph()
g2.load("../rdf/conselhos.rdf")

q="SELECT DISTINCT ?o WHERE {?s rdf:type ?o}"
q2="SELECT DISTINCT ?p WHERE {?s ?p ?o}"
q3="SELECT DISTINCT ?p (datatype(?o) as ?do) WHERE { ?s ?p ?o . }"
rr=g2.query(q2)
rr=[rrr for rrr in rr]
rr2=g2.query(q3)
rr2=[rrr for rrr in rr2]

# O que teremos aqui na ontologia?
# apenas a classe conselho
cons=[foo for foo in g2.query(q)][0][0]
G(cons,rdf.type,owl.Class)
# e várias propriedades
# e os tipos ao final delas
prop_objs=[foo for foo in g2.query(q3)]
A=gv.AGraph(directed=True)
label=cons.split("/")[-1]
A.add_node(label,style="filled")
i=0
for po in prop_objs:
    prop,obj=po
    if "22-rdf-syntax-ns" not in prop:
        labelp=prop.split("/")[-1]
        labelo=obj.split("/")[-1]
        print labelp, labelo
        A.add_node(i,style="filled")
        nd=A.get_node(i)
        nd.attr["label"]=labelo
        A.add_edge(label,i)
        e=A.get_edge(label,i)
        e.attr["label"]=labelp
        G(prop,rdf.type,owl.DatatypeProperty)
        G(prop,rdfs.range,obj)
        G(prop,rdfs.domain,cons)
        i+=1

nome=("../figs/Conselho0.png")
A.draw(nome,prog="dot") # draw to png using circo
print("Wrote %s"%(nome,))

# enriquecer com cada documento e plotar a figura
# fabbri_tab_consolidada.docx
# campo 1: contemplado com obs:name e obs:abbreviation
# Endereço: não está na tabela do ipea
# Telefone: \\
# email:    \\
# URL:     \\
# Orgão vinculado: obs:linkedAgency
# area politica: obs:thematicArea, Infraestrutura e recursos naturais aparecem sempre juntos
# tipo: obs.disposition
# composição do conselho: obs.membersCount, obs.governmentMembersCount, obs.civilSocietyMembersCount, obs.governmentRepresentativesProportion, obs.civilSocietyRepresentativesProportion
# forma de escolha: obs.internalGovernanceBodyMemberCriterion, obs.civilSocietySelectionMethod
# competencia: \\
# estrutura: obs.executiveSecretary, obs.commission, falta especificar todos os outros itens \\
# legislação: obs.creationAct, obs.reformulationAct, obs.regulationAct
# secretario executivo: \\
# conselheiros: \\
# gestão do conselho: \\
# presidente da gestão: \\
# vice: \\
# documentação da gestão: \\
# Atos normaticos: \\

# posso enriquecer a ontologia com os elementos faltantes
# e entregar ela assim.
