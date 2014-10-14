#-*- coding: utf-8 -*-
import rdflib as r, pygraphviz as gv
def G(S,P,O):
    g.add((S,P,O))
L=r.Literal

obs = r.Namespace("http://purl.org/socialparticipation/obs/")
rdf = r.namespace.RDF
rdfs = r.namespace.RDFS
owl = r.namespace.OWL

g = r.Graph()
g.namespace_manager.bind("obs", "http://purl.org/socialparticipation/obs/")    
g.namespace_manager.bind("rdf", r.namespace.RDF)    
g.namespace_manager.bind("rdfs", r.namespace.RDFS)    
g.namespace_manager.bind("xsd", r.namespace.XSD)    
g.namespace_manager.bind("owl", r.namespace.OWL)    

cons=obs.Council
G(cons,rdf.type,owl.Class)
G(cons,rdfs.label,L(u"Conselho",lang="pt"))
G(cons,rdfs.comment,L(u"Conselho de políticas públicas",lang="pt"))


f=open("../rdf/obsConselho.owl","wb")
f.write(g.serialize())
f.close()
