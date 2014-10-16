#-*- coding: utf-8 -*-
import rdflib as r, pygraphviz as gv
def G(S,P,O):
    g.add((S,P,O))
L=r.Literal

vbs = r.Namespace("http://purl.org/socialparticipation/vbs/")
rdf = r.namespace.RDF
rdfs = r.namespace.RDFS
skos = r.namespace.SKOS
xsd = r.namespace.XSD

store="../rdf/vbsConferencia.rdf"
g = r.Graph()
g.load(store)
#g.namespace_manager.bind("vbs", "http://purl.org/socialparticipation/vbs/")    
#g.namespace_manager.bind("rdf", r.namespace.RDF)    
#g.namespace_manager.bind("rdfs", r.namespace.RDFS)    
#g.namespace_manager.bind("xsd", r.namespace.XSD)    
#g.namespace_manager.bind("skos", r.namespace.SKOS)    

#conf=vbs.ConferenceStep
#G(conf,rdf.type,skos.Concept)
#

PREFIX="""PREFIX skos: <http://www.w3.org/2004/02/skos/core#>"""

q="SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l . }"
res=g.query(PREFIX+q)
conceitos=[rr for rr in res]
