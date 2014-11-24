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

consu=obs.PublicConsultation
lconsu=u"Consulta pública" # SKOS TTM
G(consu,rdf.type,owl.Class)
G(consu,rdfs.label,L(lconsu,lang="pt"))
A.add_node(lconsu,style="filled")
nd=A.get_node(lconsu)
nd.attr['color']="#A29999"

ta=obs.has
lta=u"possui" # SKOS
G(ta,rdf.type,owl.ObjectProperty)
G(ta,rdfs.label,L(lta,lang="pt"))

th=obs.Theme
lth=u"Tema"
G(th,rdf.type,owl.Class)
G(th,rdfs.label,L(lth,lang="pt"))
A.add_node(lth,style="filled")
A.add_edge(lconsu,lth)
e=A.get_edge(lconsu,lth)
e.attr["label"]=lta

nm=obs.phrase
lnm=u"frase de referência"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.comment,L(u"frase de referência do tema da consulta",lang="pt"))
G(nm,rdfs.range,xsd.string)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:string"
nd.attr['color']="#A2F3D1"
A.add_edge(lth,COUNT)
e=A.get_edge(lth,COUNT); COUNT+=1
e.attr["label"]=lnm

nm=obs.thematicAxes
lnm=u"eixos temáticos"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.range,xsd.string)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:string"
nd.attr['color']="#A2F3D1"
A.add_edge(lth,COUNT)
e=A.get_edge(lth,COUNT); COUNT+=1
e.attr["label"]=lnm

co_=obs.methodology
lco_=u"metodologia"
bo_=obs.ConferenceMethodology
lbo_=u"Metodologia de consulta"
G(co_,rdf.type,owl.ObjectProperty)
G(co_,rdfs.label,L(lco_,lang="pt"))
G(bo_,rdf.type,owl.Class)
G(bo_,rdfs.label,L(lbo_,lang="pt"))
A.add_node(lbo_,style="filled")
A.add_edge(lconsu,lbo_)
e=A.get_edge(lconsu,lbo_)
e.attr["label"]=lco_
lbo__=lbo_


co_=obs.interface
lco_=u"interface"
bo_=obs.InteractionZone
lbo_=u"Zona de interação"
G(co_,rdf.type,owl.ObjectProperty)
G(co_,rdfs.label,L(lco_,lang="pt"))
G(bo_,rdf.type,owl.Class)
G(bo_,rdfs.label,L(lbo_,lang="pt"))
A.add_node(lbo_,style="filled")
A.add_edge(  lbo__,lbo_)
e=A.get_edge(lbo__,lbo_)
e.attr["label"]=lco_


co_=obs.event
lco_=u"evento"
bo_=obs.ParticipativeMoment
lbo_=u"Momento participativo"
G(co_,rdf.type,owl.ObjectProperty)
G(co_,rdfs.label,L(lco_,lang="pt"))
G(bo_,rdf.type,owl.Class)
G(bo_,rdfs.label,L(lbo_,lang="pt"))
A.add_node(lbo_,style="filled")
A.add_edge(  lbo__,lbo_)
e=A.get_edge(lbo__,lbo_)
e.attr["label"]=lco_


nome=("../figs/obsConsulta.png")
A.draw(nome,prog="dot") # draw to png using circo
nome=("../figs/obsConsulta2.png")
A.draw(nome,prog="circo") # draw to png using circo
nome=("../figs/obsConsulta3.png")
A.draw(nome,prog="fdp") # draw to png using circo
A.write("../dot/obsConsulta.dot")

f=open("../rdf/obsConsulta.owl","wb")
f.write(g.serialize())
f.close()
f=open("../rdf/obsConsulta.ttl","wb")
f.write(g.serialize(format="turtle"))
f.close()

