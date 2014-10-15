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

#conf=vbs.ConferenceStep
#G(conf,rdf.type,skos.Concept)
#G(conf,skos.prefLabel,L(u"Etapa de conferência",lang="pt"))
#G(conf,skos.altLabel,L(u"Conferência nacional",lang="pt"))
#G(conf,skos.altLabel,L(u"Conferência virtual",lang="pt"))
#G(conf,skos.altLabel,L(u"Conferência livre",lang="pt"))
#G(conf,skos.altLabel,L(u"Conferência estadual",lang="pt"))
#G(conf,skos.altLabel,L(u"Conferência",lang="pt"))
#G(conf,skos.definition,L(u"Processo periódico de promoção do diálogo entre governo e sociedade, realizado em etapas, tipicamente convocadas pelo Executivo",lang="pt")) # Melhorar TTM


conf=vbs.Conference
G(conf,rdf.type,skos.Concept)
G(conf,skos.prefLabel,L(u"Conferência",lang="pt"))
G(conf,skos.altLabel,L(u"Conferência nacional",lang="pt"))
G(conf,skos.altLabel,L(u"Conferência de políticas públicas",lang="pt"))
G(conf,skos.definition,L(u"Processo periódico de promoção do diálogo entre governo e sociedade, realizado em etapas, tipicamente convocadas pelo Executivo",lang="pt")) # Melhorar TTM
G(conf,skos.definition,L(u"Instância colegiada temática permanente, instituída por ato normativo, de diálogo entre a sociedade civil e o governo para promover a participação no processo decisório e na gestão de políticas públicas",lang="pt")) # Melhorar TTM

pm=vbs.ParticipationMechanism
G(pm,rdf.type,skos.Concept)
G(pm,skos.prefLabel,L("Mecanismo ou instância de participação social",lang="pt"))
G(pm,skos.altLabel,L("Mecanismo de participação social",lang="pt"))
G(pm,skos.altLabel,L("Instância de participação social",lang="pt"))
G(conf,skos.broader,pm)

re=vbs.Resolution
lre=u"Resolução" #SKOS
G(re,rdf.type,skos.Concept)
G(re,skos.prefLabel,L(lre,lang="pt"))
G(re,skos.altLabel,L(u"Deliberação",lang="pt"))
G(re,skos.altLabel,L(u"Tese",lang="pt"))
G(re,skos.altLabel,L(u"Decisão",lang="pt"))
G(re,skos.altLabel,L(u"Proposta",lang="pt"))
G(re,skos.altLabel,L(u"Diretriz",lang="pt"))
#G(re,skos.definition,L(u"",lang="pt")) # Melhorar TTM

f=open("../rdf/vbsConferencia.rdf","wb")
f.write(g.serialize())
f.close()
f=open("../rdf/vbsConferencia.ttl","wb")
f.write(g.serialize(format="turtle"))
f.close()
