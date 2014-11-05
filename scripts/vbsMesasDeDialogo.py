#-*- coding: utf-8 -*-
import rdflib as r, pygraphviz as gv, sys
def G(S,P,O):
    if type(O)==type(u"astring"):
        O=L(O,lang="pt")
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


mesa=vbs.DialogueTable
lmesa=u"Mesa de diálogo" # SKOS TTM
G(mesa,rdf.type,skos.Concept)
G(mesa,skos.prefLabel,L(lmesa,lang="pt"))
G(mesa,skos.altLabel,L(u"Mesa de diálogo federal ",lang="pt"))
G(mesa,skos.definition,L(u"mecanismo de debate e de negociação com a participação dos setores da sociedade civil e do governo diretamente envolvidos no intuito de prevenir, mediar e solucionar conflitos sociais (PNPS)",lang="pt"))


foo=vbs.Periodicity
lfoo=u"Periodicidade"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.SocialParticipationIteration
lfoo=u"Iteração com instância ou mecanismo de participação social"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))


foo=vbs.ParticipationInstanceOrMechanism # SKOS
lfoo=u"Instância ou mecanismo de participação social"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

pm=vbs.ParticipationMechanism
G(pm,rdf.type,skos.Concept)
G(pm,skos.prefLabel,L("Mecanismo de participação social",lang="pt"))
G(pm,skos.altLabel,L("Instância de participação social",lang="pt"))
G(pm,skos.broader,foo)
G(mesa,skos.broader,pm)
pm_=pm

pm=vbs.ParticipationInstance
G(pm,rdf.type,skos.Concept)
G(pm,skos.prefLabel,L("Instância de participação social",lang="pt"))
G(pm,skos.altLabel,L("Mecanismo de participação social",lang="pt"))
G(pm,skos.broader,foo)
G(pm,skos.related,pm_)


pm__=vbs.GuidingMechanism # SKOS
lpm__=u"Mecanismo orientador"
G(pm__,rdf.type,skos.Concept)
G(pm__,skos.prefLabel,L(lpm__,lang="pt"))

pm__=vbs.ConsensualCompromise # SKOS
lpm__=u"Compromisso consensual"
G(pm__,rdf.type,skos.Concept)
G(pm__,skos.prefLabel,L(lpm__,lang="pt"))


pm__=vbs.FederalProgram # SKOS
lpm__=u"Programa federal"
G(pm__,rdf.type,skos.Concept)
G(pm__,skos.prefLabel,L(lpm__,lang="pt"))


pm__=vbs.PublicPolicy # SKOS
lpm__=u"Política pública"
G(pm__,rdf.type,skos.Concept)
G(pm__,skos.prefLabel,L(lpm__,lang="pt"))

pm_=vbs.NormativeAct # SKOS
lpm_=u"Ato normativo"
G(pm__,rdf.type,skos.Concept)
G(pm__,skos.prefLabel,L(lpm__,lang="pt"))

pm__=vbs.PublicAgency # SKOS
lpm__=u"Órgão público"
G(pm__,rdf.type,skos.Concept)
G(pm__,skos.prefLabel,L(lpm__,lang="pt"))

pm__=vbs.SGPR # SKOS
lpm__=u"SGPR"
G(pm__,rdf.type,skos.Concept)
G(pm__,skos.prefLabel,L(lpm__,lang="pt"))
G(pm__,skos.altLabel,L(u"Secretaria-Geral da Presidência da República",lang="pt"))
G(pm__,skos.altLabel,L(u"Secretaria-Geral da Presidência da República (SGPR)",lang="pt"))
G(pm__,skos.altLabel,L(u"Secretaria-Geral da Presidência da República - SGPR",lang="pt"))

orgao=vbs.convene
lorgao=u"convocar"
G(orgao,rdf.type,skos.Concept)
G(orgao,skos.prefLabel,L(lorgao,lang="pt"))

orgao=vbs.coordinate
lorgao=u"coordenar"
G(orgao,rdf.type,skos.Concept)
G(orgao,skos.prefLabel,L(lorgao,lang="pt"))

orgao=vbs.divulge
lorgao=u"divulgar"
G(orgao,rdf.type,skos.Concept)
G(orgao,skos.prefLabel,L(lorgao,lang="pt"))


bo=vbs.ManagementBody
lbo=u"Corpo gestor"
G(bo,rdf.type,skos.Concept)
G(bo,skos.prefLabel,L(lbo,lang="pt"))

co=vbs.composition
lco=u"composição"
G(co,rdf.type,skos.Concept)
G(co,skos.prefLabel,L(lco,lang="pt"))


sp=vbs.WorkGroup
lsp=u"Grupo de trabalho" # SKOS TTM
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))

orgao=vbs.member
lorgao=u"membro"
G(orgao,rdf.type,skos.Concept)
G(orgao,skos.prefLabel,L(lorgao,lang="pt"))
pm__=vbs.Participant # SKOS
lpm__=u"Participante"
G(pm__,rdf.type,skos.Concept)
G(pm__,skos.prefLabel,L(lpm__,lang="pt"))

sp=vbs.ReferenceDocument
lsp=u"Documento de referência" # SKOS TTM
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))

pm__=vbs.Letter # SKOS
lpm__=u"Carta"
G(pm__,rdf.type,skos.Concept)
G(pm__,skos.prefLabel,L(lpm__,lang="pt"))

pm__=vbs.Petition # SKOS
lpm__=u"Requerimento"
G(pm__,rdf.type,skos.Concept)
G(pm__,skos.prefLabel,L(lpm__,lang="pt"))

pm__=vbs.AuditReport # SKOS
lpm__=u"Relatório de auditoria"
G(pm__,rdf.type,skos.Concept)
G(pm__,skos.prefLabel,L(lpm__,lang="pt"))

pm__=vbs.Regiment # SKOS
lpm__=u"Regimento"
G(pm__,rdf.type,skos.Concept)
G(pm__,skos.prefLabel,L(lpm__,lang="pt"))

pm__=vbs.NormativeOrdinance # SKOS
lpm__=u"Portaria normativa"
G(pm__,rdf.type,skos.Concept)
G(pm__,skos.prefLabel,L(lpm__,lang="pt"))

pm__=vbs.NormativeAct # SKOS
lpm__=u"Ato normativo"
G(pm__,rdf.type,skos.Concept)
G(pm__,skos.prefLabel,L(lpm__,lang="pt"))

pm__=vbs.CreationOrdinance# SKOS
lpm__=u"Portaria de criação"
G(pm__,rdf.type,skos.Concept)
G(pm__,skos.prefLabel,L(lpm__,lang="pt"))

pm__=vbs.CouncilMinute # SKOS
lpm__=u"Ata de conselho"
G(pm__,rdf.type,skos.Concept)
G(pm__,skos.prefLabel,L(lpm__,lang="pt"))

pm__=vbs.SocialMovementOffice# SKOS
lpm__=u"Ofício de movimento social"
G(pm__,rdf.type,skos.Concept)
G(pm__,skos.prefLabel,lpm__)

orgao=vbs.reason
lorgao=u"motivo"
G(pm__,rdf.type,skos.Concept)
G(pm__,skos.prefLabel,lpm__)

pm__=vbs.Demand # SKOS
lpm__=u"Demanda"
G(pm__,rdf.type,skos.Concept)
G(pm__,skos.prefLabel,lpm__)

pm__=vbs.Complaint # SKOS
lpm__=u"Denúncia"
G(pm__,rdf.type,skos.Concept)
G(pm__,skos.prefLabel,lpm__)

nome=vbs.problem
lnome=u"problema"
G(nome,rdf.type,skos.Concept)
G(nome,skos.prefLabel,lnome)

orgao=vbs.creation
lorgao=u"criação"
G(orgao,rdf.type,skos.Concept)
G(orgao,skos.prefLabel,lorgao)

sp=vbs.ExecutiveOffice
lsp=u"Secretaria executiva" # SKOS TTM
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,lsp)

sp=vbs.Coordinate
lsp=u"Coordenação" # SKOS TTM
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,lsp)

orgao=vbs.organization
lorgao=u"organização"
G(orgao,rdf.type,skos.Concept)
G(orgao,skos.prefLabel,lorgao)


f=open("../rdf/vbsMesaDeDialogo.rdf","wb")
f.write(g.serialize())
f.close()

f=open("../rdf/vbsMesaDeDialogo.ttl","wb")
f.write(g.serialize(format="turtle"))
f.close()


