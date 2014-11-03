#-*- coding: utf-8 -*-
import rdflib as r, pygraphviz as gv
def G(S,P,O):
    g.add((S,P,O))
L=r.Literal
COUNT=1
A=gv.AGraph(directed=True,strict=False)

obs = r.Namespace("http://purl.org/socialparticipation/obs/")
rdf = r.namespace.RDF
rdfs = r.namespace.RDFS
owl = r.namespace.OWL
xsd = r.namespace.XSD

g = r.Graph()
g.namespace_manager.bind("obs", "http://purl.org/socialparticipation/obs/")    
g.namespace_manager.bind("rdf", r.namespace.RDF)    
g.namespace_manager.bind("rdfs", r.namespace.RDFS)    
g.namespace_manager.bind("xsd", r.namespace.XSD)    
g.namespace_manager.bind("owl", r.namespace.OWL)    

# Mecanismos
sp=obs.DialogueTable
lsp=u"Mesa de diálogo" # SKOS TTM
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,obs.ParticipationMechanism)
A.add_node(lsp,style="filled") ###
nd=A.get_node(lsp)
nd.attr['color']="#A29999"
lmesa=lsp


nome=obs.periodicity
lnome=u"periodicidade"
G(nome,rdf.type,owl.DatatypeProperty)
G(nome,rdfs.label,L(lnome,lang="pt"))
#G(nome,rdfs.range,xsd.gMonth)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:gMonth"
nd.attr['color']="#A2F3D1"
A.add_edge(lmesa,COUNT)
e=A.get_edge(lmesa,COUNT); COUNT+=1
e.attr["label"]=lnome

orgao=obs.iterate
lorgao=u"itera"
pm__=obs.ParticipationInstanceOrMechanism # SKOS
lpm__=u"Instância ou mecanismo de participação social"
A.add_node(lpm__,style="filled")
G(pm__,rdf.type,owl.Class)
G(pm__,rdfs.label,L(lpm__,lang="pt"))
G(orgao,rdf.type,owl.ObjectProperty)
G(orgao,rdfs.label,L(lorgao,lang="pt"))
G(orgao,rdfs.range,pm__)
A.add_node(lpm__,style="filled")
A.add_edge(lmesa,lpm__)
e=A.get_edge(lmesa,lpm__)
e.attr["label"]=lorgao

pm_=obs.ParticipationMechanism # SKOS
lpm_=u"Mecanismo de participação social"
A.add_node(lpm_,style="filled")
G(pm_,rdf.type,owl.Class)
G(pm_,rdfs.label,L(lpm_,lang="pt"))

G(pm_,rdfs.subClassOf,pm__)
A.add_edge(lpm_,lpm__)
e=A.get_edge(lpm_,lpm__)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

A.add_edge(lmesa,lpm_)
e=A.get_edge(lmesa,lpm_)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2


nome=("../figs/obsMesaDeDialogo.png")
A.draw(nome,prog="dot") # draw to png using circo
nome=("../figs/obsMesaDeDialogo2.png")
A.draw(nome,prog="circo") # draw to png using circo
nome=("../figs/obsMesaDeDialogo3.png")
A.draw(nome,prog="fdp") # draw to png using circo
A.write("../rdf/obsMesaDeDialogo.dot")

f=open("../rdf/obsMesaDeDialogo.owl","wb")
f.write(g.serialize())
f.close()
f=open("../rdf/obsMesaDeDialogo.ttl","wb")
f.write(g.serialize(format="turtle"))
f.close()

