#-*- coding: utf-8 -*-
import rdflib as r, pygraphviz as gv, sys
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



ouv=vbs.OmbudsmanAgency # SKOS
louv =u"Ouvidoria"
G(ouv,rdf.type,skos.Concept)
G(ouv,skos.prefLabel,L(louv,lang="pt"))
G(ouv,skos.altLabel,L(u"Ouvidoria federal",lang="pt"))
G(ouv,skos.altLabel,L(u"Ouvidoria pública",lang="pt"))
G(ouv,skos.altLabel,L(u"Ouvidoria pública federal",lang="pt"))
G(ouv,skos.definition,L(u"instância de controle e participação social responsável pelo tratamento das reclamações, solicitações, denúncias, sugestões e elogios relativos às políticas e aos serviços públicos, prestados sob qualquer forma ou regime, com vistas ao aprimoramento da gestão pública",lang="pt"))
ouv_=ouv


ouv=vbs.ActiveOmbudsmanAgency # SKOS
louv =u"Ouvidoria ativa"
G(ouv,rdf.type,skos.Concept)
G(ouv,skos.prefLabel,L(louv,lang="pt"))
G(ouv,skos.broader,ouv_)
ouv__=ouv


ouv=vbs.PassiveOmbudsmanAgency # SKOS
louv =u"Ouvidoria passiva"
G(ouv,rdf.type,skos.Concept)
G(ouv,skos.prefLabel,L(louv,lang="pt"))
G(ouv,skos.broader,ouv_)
G(ouv,skos.related,ouv__)

ouv=vbs.Ombudsman
louv=u"Ouvidor"
G(ouv,rdf.type,skos.Concept)
G(ouv,skos.prefLabel,L(louv,lang="pt"))
G(ouv,skos.related,ouv_)

ouv=vbs.PublicAgency
louv=u"Órgão público" # SKOS
G(ouv,rdf.type,skos.Concept)
G(ouv,skos.prefLabel,L(louv,lang="pt"))
ouv_=ouv


sp=vbs.PublicAdministrationAgency
lsp=u"Órgão da administração pública" # entra no SKOS
G(ouv,rdf.type,skos.Concept)
G(ouv,skos.prefLabel,L(louv,lang="pt"))
G(ouv,skos.broader,ouv_)


sp=vbs.IndirectPublicAdministrationAgency
lsp=u"Órgão da administração pública indireta" # entra no SKOS
G(ouv,rdf.type,skos.Concept)
G(ouv,skos.prefLabel,L(louv,lang="pt"))
G(ouv,skos.broader,ouv_)


ouv=vbs.OmbudsmanNationalSystem
lou=u"Sistema Federal de Ouvidorias"
G(ouv,rdf.type,skos.Concept)
G(ouv,skos.prefLabel,L(louv,lang="pt"))
G(vbs.OmbudsmanAgency,skos.broader,ouv)


ouv=vbs.SAC
louv=u"SAC (Sistema de Atendimento ao Cidadão)" # entra no SKOS
G(ouv,rdf.type,skos.Concept)
G(ouv,skos.prefLabel,L(louv,lang="pt"))
G(vbs.OmbudsmanAgency,skos.broader,ouv)

ouv=vbs.OGU
louv=u"OGU (Ouvidoria Geral da União)"
G(ouv,rdf.type,skos.Concept)
G(ouv,skos.prefLabel,L(louv,lang="pt"))
G(vbs.OmbudsmanAgency,skos.broader,ouv)


ouv=vbs.Control
louv=u"Controle"
G(ouv,rdf.type,skos.Concept)
G(ouv,skos.prefLabel,L(louv,lang="pt"))
ouv_=ouv

ouv=vbs.InternalControl
louv=u"Controle interno" # entra no SKOS
G(ouv,rdf.type,skos.Concept)
G(ouv,skos.prefLabel,L(louv,lang="pt"))
G(ouv,skos.broader,ouv_)

ouv=vbs.ExternalControl
louv=u"Controle externo" # entra no SKOS
G(ouv,rdf.type,skos.Concept)
G(ouv,skos.prefLabel,L(louv,lang="pt"))
G(ouv,skos.broader,ouv_)


ouv=vbs.ParticipationInstanceOrMechanism # SKOS
louv=u"Instância ou mecanismo de participação social"
G(ouv,rdf.type,skos.Concept)
G(ouv,skos.prefLabel,L(louv,lang="pt"))
G(vbs.OmbudsmanAgency,skos.broader,ouv)



ouv=vbs.LAI# SKOS
louv=u"LAI (Lei de Acesso à Informação)" # SKOS
G(ouv,rdf.type,skos.Concept)
G(ouv,skos.prefLabel,L(louv,lang="pt"))


ouv=vbs.Manifestation # SKOS
louv=u"Manifestação" # SKOS
G(ouv,rdf.type,skos.Concept)
G(ouv,skos.prefLabel,L(louv,lang="pt"))

sp=vbs.Request
lsp=u"Solicitação" # entra no SKOS
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.broader,ouv)

sp=vbs.Complaint
lsp=u"Reclamação" # entra no SKOS
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.broader,ouv)

sp=vbs.Compliment
lsp=u"Elogio" # entra no SKOS
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.broader,ouv)

sp=vbs.Suggestion
lsp=u"Sugestão" # entra no SKOS
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.broader,ouv)

sp=vbs.Denunciation
lsp=u"Denúncia" # entra no SKOS
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.broader,ouv)

sp=vbs.IdentityReservation
lsp=u"Reserva de identidade"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))

sp=vbs.AnonymousManifestation
lsp=u"Manifestação anônima" # SKOS
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))



f=open("../rdf/vbsOuvidoria.rdf","wb")
f.write(g.serialize())
f.close()

f=open("../rdf/vbsOuvidoria.ttl","wb")
f.write(g.serialize(format="turtle"))
f.close()


sys.exit()
pm=vbs.ParticipationMechanism
G(pm,rdf.type,skos.Concept)
G(pm,skos.prefLabel,L("Mecanismo de participação social",lang="pt"))
pm_=pm

pm=vbs.ParticipationInstance
G(pm,rdf.type,skos.Concept)
G(pm,skos.prefLabel,L(u"Instância de participação social",lang="pt"))
G(pm,skos.altLabel,L(u"Instância participativa",lang="pt"))
G(pm,skos.altLabel,L(u"Espaço participativo",lang="pt"))
G(pm,skos.altLabel,L(u"Espaço de participação social",lang="pt"))
G(pm,skos.altLabel,L(u"Instituição participativa",lang="pt"))
G(cons,skos.broader,pm)
G(pm,skos.related,pm_)


mn=vbs.Ministry
lmn=u"Ministério" # entra no SKOS
G(mn,rdf.type,skos.Concept)
G(mn,skos.prefLabel,L(lmn,lang="pt"))

sc=vbs.Secretariat
lsc=u"Secretaria" # entra no SKOS
G(sc,rdf.type,skos.Concept)
G(sc,skos.prefLabel,L(lsc,lang="pt"))
G(sc,skos.broader,mn)

####
ac=vbs.Act
lac=u"Ato normativo" # SKOS Ato Institucional
G(ac,rdf.type,skos.Concept)
G(ac,skos.prefLabel,L(lac,lang="pt"))

####
la=vbs.Law
lla=u"Lei" # SKOS
G(la,rdf.type,skos.Concept)
G(la,skos.prefLabel,L(lla,lang="pt"))
G(la,skos.broader,ac)

oe=vbs.Ordinance
loe=u"Portaria" # SKOS
G(oe,rdf.type,skos.Concept)
G(oe,skos.prefLabel,L(loe,lang="pt"))
G(oe,skos.broader,ac)

d
