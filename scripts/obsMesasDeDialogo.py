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

orgao=obs.type
lorgao=u"tipo"
pm__=obs.GuidingMechanism # SKOS
lpm__=u"Mecanismo orientador"
G(pm__,rdf.type,owl.Class)
G(pm__,rdfs.label,L(lpm__,lang="pt"))
G(orgao,rdf.type,owl.ObjectProperty)
G(orgao,rdfs.label,L(lorgao,lang="pt"))
G(orgao,rdfs.range,pm__)
A.add_node(lpm__,style="filled")
A.add_edge(lmesa,lpm__)
e=A.get_edge(lmesa,lpm__)
e.attr["label"]=lorgao
lpm__2=lpm__

orgao=obs.defines
lorgao=u"define"
pm__=obs.ConsensualCompromise # SKOS
lpm__=u"Compromisso consensual"
G(pm__,rdf.type,owl.Class)
G(pm__,rdfs.label,L(lpm__,lang="pt"))
G(orgao,rdf.type,owl.ObjectProperty)
G(orgao,rdfs.label,L(lorgao,lang="pt"))
G(orgao,rdfs.range,pm__)
A.add_node(lpm__,style="filled")
A.add_edge(lmesa,lpm__)
e=A.get_edge(lmesa,lpm__)
e.attr["label"]=lorgao
lpm__3=lpm__
pm__3=pm__

orgao=obs.delivers
lorgao=u"entrega"
G(orgao,rdf.type,owl.ObjectProperty)
G(orgao,rdfs.label,L(lorgao,lang="pt"))
A.add_edge(  lpm__2,lpm__)
e=A.get_edge(lpm__2,lpm__)
e.attr["label"]=lorgao


orgao=obs.permeates
lorgao=u"permeia"
pm__=obs.FederalProgram # SKOS
lpm__=u"Programa federal"
G(pm__,rdf.type,owl.Class)
G(pm__,rdfs.label,L(lpm__,lang="pt"))
G(orgao,rdf.type,owl.ObjectProperty)
G(orgao,rdfs.label,L(lorgao,lang="pt"))
A.add_node(lpm__,style="filled")
A.add_edge(lpm__3,lpm__)
e=A.get_edge(lpm__3,lpm__)
e.attr["label"]=lorgao
lpm__4=lpm__

pm__=obs.PublicPolicy # SKOS
lpm__=u"Política pública"
G(pm__,rdf.type,owl.Class)
G(pm__,rdfs.label,L(lpm__,lang="pt"))
A.add_node(lpm__,style="filled")
A.add_edge(lpm__3,lpm__)
e=A.get_edge(lpm__3,lpm__)
e.attr["label"]=lorgao
lpm__5=lpm__

pm_=obs.NormativeAct # SKOS
lpm_=u"Ato normativo"
G(pm_,rdf.type,owl.Class)
G(pm_,rdfs.label,L(lpm_,lang="pt"))
G(pm__3,rdfs.subClassOf,pm_)
A.add_node(lpm_,style="filled")
A.add_edge(lpm__3,lpm_)
e=A.get_edge(lpm__3,lpm_)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2


orgao=obs.directs
lorgao=u"orienta"
pm__=obs.PublicAgency # SKOS
lpm__=u"Órgão público"
G(pm__,rdf.type,owl.Class)
G(pm__,rdfs.label,L(lpm__,lang="pt"))
G(orgao,rdf.type,owl.ObjectProperty)
G(orgao,rdfs.label,L(lorgao,lang="pt"))
G(orgao,rdfs.range,pm__)
A.add_node(lpm__,style="filled")

A.add_edge(lpm_,lpm__)
e=A.get_edge(lpm_,lpm__)
e.attr["label"]=lorgao

A.add_edge(  lpm__4,lpm__)
e=A.get_edge(lpm__4,lpm__)
e.attr["label"]=lorgao


A.add_edge(  lpm__5,lpm__)
e=A.get_edge(lpm__5,lpm__)
e.attr["label"]=lorgao



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

