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

conf=obs.Conference # SKOS
lconf=u"Conferência"
A.add_node(lconf,style="filled")

G(conf,rdf.type,owl.Class)
G(conf,rdfs.label,L(lconf,lang="pt"))
G(conf,rdfs.comment,L(u"Conferências são processos nacionais de promoção do diálogo entre governo e sociedade",lang="pt"))

pm=obs.ParticipationMechanism # SKOS
lpm=u"Mecanismo ou instância de participação social"
A.add_node(lpm,style="filled")

G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(conf,rdfs.subClassOf,pm)
A.add_edge(lconf,lpm)
e=A.get_edge(lconf,lpm)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

#####
nome=("../figs/obsConferencia.png")
A.draw(nome,prog="dot") # draw to png using circo
nome=("../figs/obsConferencia2.png")
A.draw(nome,prog="circo") # draw to png using circo
nome=("../figs/obsConferencia3.png")
A.draw(nome,prog="fdp") # draw to png using circo

f=open("../rdf/obsConferencia.owl","wb")
f.write(g.serialize())
f.close()
f=open("../rdf/obsConferencia.ttl","wb")
f.write(g.serialize(format="turtle"))
f.close()
