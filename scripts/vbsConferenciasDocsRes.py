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

conf=vbs.Conference
G(conf,rdf.type,skos.Concept)
G(conf,skos.prefLabel,L(u"Conferência",lang="pt"))
G(conf,skos.altLabel,L(u"Conferência nacional",lang="pt"))
G(conf,skos.altLabel,L(u"Conferência de políticas públicas",lang="pt"))
G(conf,skos.definition,L(u"Processo periódico de promoção do diálogo entre governo e sociedade, realizado em etapas, tipicamente convocadas pelo Executivo",lang="pt")) # Melhorar TTM
G(conf,skos.definition,L(u"Instância colegiada temática permanente, instituída por ato normativo, de diálogo entre a sociedade civil e o governo para promover a participação no processo decisório e na gestão de políticas públicas",lang="pt")) # Melhorar TTM

sp=vbs.PoliticalSocialization# SKOS
lsp=u"Socialização política"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))

pm=vbs.ParticipantQualification # SKOS
lpm=u"Capacitação de participante"
G(pm,rdf.type,skos.Concept)
G(pm,skos.prefLabel,L(lpm,lang="pt"))
G(pm,skos.broader,sp)

pm=vbs.ExternalSocietyQualification # SKOS
lpm=u"Capacitação de sociedade externa"
G(pm,rdf.type,skos.Concept)
G(pm,skos.prefLabel,L(lpm,lang="pt"))
G(pm,skos.broader,sp)

pm=vbs.ParticipativeCulture# SKOS
lpm=u"Cultura participativa"
G(pm,rdf.type,skos.Concept)
G(pm,skos.prefLabel,L(lpm,lang="pt"))

pm=vbs.NationalPlan # SKOS
lpm=u"Plano nacional"
G(pm,rdf.type,skos.Concept)
G(pm,skos.prefLabel,L(lpm,lang="pt"))

pm=vbs.Motion # SKOS
lpm=u"Moção"
G(pm,rdf.type,skos.Concept)
G(pm,skos.prefLabel,L(lpm,lang="pt"))

pm=vbs.Letter # SKOS
lpm=u"Carta"
G(pm,rdf.type,skos.Concept)
G(pm,skos.prefLabel,L(lpm,lang="pt"))

pm=vbs.Resolution # SKOS
lpm=u"Resolução"
G(pm,rdf.type,skos.Concept)
G(pm,skos.prefLabel,L(lpm,lang="pt"))

pm=vbs.FinalReport # SKOS
lpm=u"Relatório final"


pm=vbs.ProposalsNotebook # SKOS
lpm=u"Caderno de propostas"
G(pm,rdf.type,skos.Concept)
G(pm,skos.prefLabel,L(lpm,lang="pt"))
pm=vbs.Regiment # SKOS
lpm=u"Regimento"
G(pm,rdf.type,skos.Concept)
G(pm,skos.prefLabel,L(lpm,lang="pt"))
pm=vbs.Manual # SKOS
lpm=u"Manual"
G(pm,rdf.type,skos.Concept)
G(pm,skos.prefLabel,L(lpm,lang="pt"))
pm=vbs.Regulation # SKOS
lpm=u"Regulamento"
G(pm,rdf.type,skos.Concept)
G(pm,skos.prefLabel,L(lpm,lang="pt"))
thfoo=vbs.ConferenceStep
lthfoo=u"Etapa de conferência"
G(thfoo,rdf.type,skos.Concept)
G(thfoo,skos.prefLabel,L(lthfoo,lang="pt"))
pm=vbs.NormativeAct# SKOS
lpm=u"Ato normativo"
G(pm,rdf.type,skos.Concept)
G(pm,skos.prefLabel,L(lpm,lang="pt"))
pm=vbs.MonitoringReport # SKOS
lpm=u"Relatório de monitoramento"
G(pm,rdf.type,skos.Concept)
G(pm,skos.prefLabel,L(lpm,lang="pt"))
pm=vbs.DialogueTextualBase# SKOS
lpm=u"Texto base para diálogo"
G(pm,rdf.type,skos.Concept)
G(pm,skos.prefLabel,L(lpm,lang="pt"))
pm=vbs.InvitationLetter # SKOS
lpm=u"Carta convite"
G(pm,rdf.type,skos.Concept)
G(pm,skos.prefLabel,L(lpm,lang="pt"))

#########

f=open("../rdf/vbsConferenciaDocsRes.rdf","wb")
f.write(g.serialize())
f.close()
f=open("../rdf/vbsConferenciaDocsRes.ttl","wb")
f.write(g.serialize(format="turtle"))
f.close()
