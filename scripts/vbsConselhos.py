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

g = r.Graph()
g.namespace_manager.bind("vbs", "http://purl.org/socialparticipation/vbs/")    
g.namespace_manager.bind("rdf", r.namespace.RDF)    
g.namespace_manager.bind("rdfs", r.namespace.RDFS)    
g.namespace_manager.bind("xsd", r.namespace.XSD)    
g.namespace_manager.bind("skos", r.namespace.SKOS)    

cons=vbs.Council
G(cons,rdf.type,skos.Concept)
G(cons,skos.prefLabel,L(u"Conselho",lang="pt"))
G(cons,skos.altLabel,L(u"Conselho de políticas públicas",lang="pt"))
G(cons,skos.altLabel,L(u"Conselho nacional de políticas públicas",lang="pt"))
G(cons,skos.definition,L(u"Espaços públicos vinculados a órgãos do Poder Executivo, tendo por finalidade permitir a participação da sociedade na definição de prioridades para a agenda política, bem como na formulação, no acompanhamento e no controle das políticas públicas (IPEA 2013)",lang="pt"))

pm=vbs.ParticipationMechanism
G(pm,rdf.type,skos.Concept)
G(pm,skos.prefLabel,L("Mecanismo ou instância de participação social",lang="pt"))
G(pm,skos.altLabel,L("Mecanismo de participação social",lang="pt"))
G(pm,skos.altLabel,L("Instância de participação social",lang="pt"))
G(cons,skos.broader,pm)

mn=obs.Ministry
lmn=u"Ministério" # entra no SKOS
G(mn,rdf.type,skos.Concept)
G(mn,skos.prefLabel,L(lmn,lang="pt"))

sc=obs.Secretariat
lsc=u"Secretaria" # entra no SKOS
G(sc,rdf.type,skos.Concept)
G(sc,skos.prefLabel,L(lsc,lang="pt"))




f=open("../rdf/vbsConselho.rdf","wb")
f.write(g.serialize())
f.close()
