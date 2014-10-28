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
G(pm,skos.prefLabel,L("Mecanismo de participação social",lang="pt"))
pm_=pm

pm=vbs.ParticipationInstance
G(pm,rdf.type,skos.Concept)
G(pm,skos.prefLabel,L("Instância de participação social",lang="pt"))
G(conf,skos.broader,pm)
G(pm,skos.related,pm_)

##################

cons=vbs.Council
G(cons,rdf.type,skos.Concept)
G(cons,skos.prefLabel,L(u"Conselho",lang="pt"))
G(cons,skos.altLabel,L(u"Conselho de políticas públicas",lang="pt"))
G(cons,skos.altLabel,L(u"Conselho nacional de políticas públicas",lang="pt"))
G(cons,skos.definition,L(u"Espaços públicos vinculados a órgãos do Poder Executivo, tendo por finalidade permitir a participação da sociedade na definição de prioridades para a agenda política, bem como na formulação, no acompanhamento e no controle das políticas públicas (IPEA 2013)",lang="pt"))
G(cons,skos.broader,pm)

sp=vbs.Ombusdmen
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(u"Ouvidoria",lang="pt"))
G(sp,skos.broader,pm)

sp=vbs.Commission
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(u"Comissão",lang="pt"))
G(sp,skos.broader,pm)

sp=vbs.DialogueTable
lsp=u"Mesa de diálogo" # SKOS TTM
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.broader,pm_)

sp=vbs.InterCouncilForum
lsp=u"Fórum interconselhos" # SKOS TTM
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.broader,pm_)

sp=vbs.PublicAudience
lsp=u"Audiência pública" # SKOS TTM
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.broader,pm_)

sp=vbs.PublicConsultation
lsp=u"Consulta pública" # SKOS TTM
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.broader,pm_)

sp=vbs.VirtualParticipationEnvironment
lsp=u"Ambiente virtual de participação social" # SKOS TTM
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.broader,pm_)

########

sp=vbs.ConferenceEdition
lsp=u"Edição de conferência"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.broader,vbs.Conference)

sp=vbs.Participant
lsp=u"Participante"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))


sp=vbs.PublicAgency
lsp=u"Órgão público"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(vbs.Council,skos.broader,sp)

mn=vbs.Ministry
lmn=u"Ministério" # entra no SKOS
G(mn,rdf.type,skos.Concept)
G(mn,skos.prefLabel,L(lmn,lang="pt"))
G(mn,skos.broader,sp)

sc=vbs.Secretariat
lsc=u"Secretaria" # entra no SKOS
G(sc,rdf.type,skos.Concept)
G(sc,skos.prefLabel,L(lsc,lang="pt"))
G(sc,skos.broader,mn)
sc_=sc

sc=vbs.MinisterialSecretariat
lsc=u"Secretaria com status de ministério" # entra no SKOS
G(sc,rdf.type,skos.Concept)
G(sc,skos.prefLabel,L(lsc,lang="pt"))
G(sc,skos.broader,sc_)


sp_=sp
sp=vbs.ChamberOfDeputies
lsp=u"Câmara dos deputados" # entra no SKOS
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.broader,sp_)

sp=vbs.NonGovernmentalForum
lsp=u"Fórum não governamental" # entra no SKOS
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.broader,sp_)

sp=vbs.Forum
lsp=u"Fórum" # entra no SKOS
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.broader,sp_)

sp=vbs.ConferenceConvocation
lsp=u"Convocação de conferência" # entra no SKOS
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.broader,vbs.Conference)

ac=vbs.Act
lac=u"Ato normativo" # SKOS Ato Institucional
G(ac,rdf.type,skos.Concept)
G(ac,skos.prefLabel,L(lac,lang="pt"))

de=vbs.PresidentialDecree
lde=u"Decreto presidencial" # SKOS
G(de,rdf.type,skos.Concept)
G(de,skos.prefLabel,L(lde,lang="pt"))
G(de,skos.broader,ac)

oe=vbs.MinisterialOrdinance
loe=u"Portaria ministerial" # SKOS
G(oe,rdf.type,skos.Concept)
G(oe,skos.prefLabel,L(loe,lang="pt"))
G(oe,skos.scopeNote,L(u"Portaria emitida por um ou mais ministérios",lang="pt"))
G(oe,skos.broader,ac)

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
G(re,skos.broader,vbs.Act)

###############
ta=vbs.PolicyArea
lta=u"Área de política" # SKOS
G(ta,rdf.type,skos.Concept)
G(ta,skos.prefLabel,L(lta,lang="pt"))
G(ta,skos.altLabel,L(u"Área política",lang="pt"))
G(ta,skos.altLabel,L(u"Área temática",lang="pt"))

sp=vbs.SocialPolicies
lsp=u"Políticas sociais" # SKOS TTM
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.scopeNote,L(u"assistência social, cultura, saúde, segurança alimentar e nutricional",lang="pt"))
G(sp,skos.broader,ta)

sp=vbs.EconomicDevelopment ###
lsp=u"Desenvolvimento econômico" # SKOS
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.scopeNote,L(u"arranjos produtivos locais, assistência técnica e extensão rural, desenvolvimento regional e desenvolvimento rural sustentável e solidário",lang="pt"))
G(sp,skos.broader,ta)

sp=vbs.GuaranteeOfRights ###
lsp=u"Garantia de direitos" # SKOS
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.scopeNote,L(u"criança e adolescente, educação, juventude, LGBT, mulheres e pessoa idosa",lang="pt"))
G(sp,skos.broader,ta)

sp=vbs.Infrastructure ###
lsp=u"Infraestrutura" # SKOS
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.scopeNote,L(u"cidades",lang="pt"))
G(sp,skos.broader,ta)

sp=vbs.NaturalResources ###
lsp=u"Recursos naturais" # SKOS
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.scopeNote,L(u"Recursos naturais",lang="pt"))
G(sp,skos.broader,ta)

#####################

sp=vbs.Theme ###
lsp=u"Tema" # SKOS
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))

sp=vbs.thematicAxes
lsp=u"eixos temáticos"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.broader,sp)

sp=vbs.ConferenceStep
lsp=u"Etapa de conferência"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
sn=u"Uma etapa é um evento participativo e também é chamada de conferência, enquanto 'a' conferência é o processo todo"
G(sp,skos.scopeNote,L(sn,lang="pt"))
G(sp,skos.broader,vbs.Conference)

sp=vbs.Municipality
lsp=u"Município"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))

sp=vbs.Woman
lsp=u"Mulher"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))


sp=vbs.Proposal
lsp=u"Proposta"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
sp_=sp

sp=vbs.ApprovedProposal
lsp=u"Proposta aprovada"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.broader,sp_)

sp=vbs.Delegate
lsp=u"Delegado"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))

sp=vbs.priorization
lsp=u"priorização"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))

sp=vbs.formulation
lsp=u"formulação"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
##########

sp=vbs.StateConference
lsp=u"Conferência estadual"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
sn=u"Uma etapa é um evento participativo, também chamado de conferência, enquanto a conferência em si é o processo todo"
G(sp,skos.scopeNote,L(sn,lang="pt"))
G(sp,skos.broader,vbs.ConferenceStep)

th=vbs.RegionalConference
lth=u"Conferência regional"
G(th,rdf.type,skos.Concept)
G(th,skos.prefLabel,L(lth,lang="pt"))
G(th,skos.scopeNote,L(sn,lang="pt"))
G(th,skos.broader,vbs.ConferenceStep)


sp=vbs.IntercityConferente
lsp=u"Conferência intermunicipal"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.scopeNote,L(sn,lang="pt"))
G(sp,skos.broader,vbs.ConferenceStep)


sp=vbs.MunicipalConference
lsp=u"Conferência municipal"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.scopeNote,L(sn,lang="pt"))
G(sp,skos.broader,vbs.ConferenceStep)


sp=vbs.VirtualConference
lsp=u"Conferência virtual"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.scopeNote,L(sn,lang="pt"))
G(sp,skos.broader,vbs.ConferenceStep)


sp=vbs.FreeConference
lsp=u"Conferência livre"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.scopeNote,L(sn,lang="pt"))
G(sp,skos.broader,vbs.ConferenceStep)

sp=vbs.ExtraordinaryConference
lsp=u"Conferência extraordinária"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.scopeNote,L(sn,lang="pt"))
G(sp,skos.broader,vbs.ConferenceStep)
##########

sp=vbs.ConferenceManagementBody
lsp=u"Corpo gestor de conferência"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
sp_=sp

#############
sp=vbs.ConferenceNationalOrganization
lsp=u"Organização nacional de conferência"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.related,sp_)
G(sp,skos.related,vbs.Council)
sp_=sp


bb=[(vbs.Committee,u"Comitê"),(vbs.Commission,u"Comissão"),(vbs.Coordination,u"Coordenação"),(vbs.Presidency,u"Presidência"),(vbs.Subcommittee,u"Subcomitê"),(vbs.Counsel,u"Assessoria"),(vbs.Coordinator,u"Coordenador"),(vbs.Secretary,u"Secretário"),(vbs.Rapporteur,u"Relator")]

for b in bb:
    sp=b[0]
    lsp=b[1]
    G(sp,rdf.type,skos.Concept)
    G(sp,skos.prefLabel,L(lsp,lang="pt"))
    G(sp,skos.broader,sp_)


#######
sp=vbs.Position
lsp=u"Vaga" # SKOS TTM
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.scopeLabel,L(u"vaga em algum grupo, como na comissão de organização nacional de conferências.",lang="pt"))

sp=vbs.GroupQualifier
lsp=u"qualificador de grupo" # SKOS TTM
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
sp_=sp

pp=[(vbs.deputy,u"adjunto"),(vbs.working,u"de trabalho"),(vbs.general,u"geral"),(vbs.special,u"especial"),(vbs.executive,u"executivo"),(vbs.editorial,u"editorial")]
for pr in pp:
    sp=pr[0]
    lsp=pr[1]
    G(sp,rdf.type,skos.Concept)
    G(sp,skos.prefLabel,L(lsp,lang="pt"))
    G(sp,skos.broader,sp_)

sp=vbs.ConferenceMethodology
lsp=u"Metodologia de conferência"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.broader,vbs.Conference)

sp=vbs.ParticipativeMoment
lsp=u"Momento participativo"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))

sp=vbs.WorkGroup # SKOS
lsp=u"Grupo de trabalho"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.broader,vbs.ParticipativeMoment)

pm=vbs.Lecture # SKOS
lpm=u"Palestra"
G(pm,rdf.type,skos.Concept)
G(pm,skos.prefLabel,L(lpm,lang="pt"))
G(pm,skos.broader,vbs.ParticipativeMoment)

pm=vbs.Workshop # SKOS
lpm=u"Oficina"
G(pm,rdf.type,skos.Concept)
G(pm,skos.prefLabel,L(lpm,lang="pt"))
G(pm,skos.broader,vbs.ParticipativeMoment)

pm=vbs.Plenary # SKOS
lpm=u"Plenária"
G(pm,rdf.type,skos.Concept)
G(pm,skos.prefLabel,L(lpm,lang="pt"))
G(pm,skos.broader,vbs.ParticipativeMoment)

pm=vbs.ThematicPlenary # SKOS
lpm=u"Plenária temática"
G(pm,rdf.type,skos.Concept)
G(pm,skos.prefLabel,L(lpm,lang="pt"))
G(pm,skos.broader,vbs.ParticipativeMoment)
##########


sp=vbs.regiment
lsp=u"regimento"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))

sp=vbs.Government
lsp=u"Governo"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))

sp=vbs.Quota
lsp=u"Cota"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.related,vbs.Position)

sp=vbs.etnicGroup
lsp=u"grupo étnico"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.related,vbs.Position)
G(sp,skos.related,vbs.Quota)




#########

f=open("../rdf/vbsConferencia.rdf","wb")
f.write(g.serialize())
f.close()
f=open("../rdf/vbsConferencia.ttl","wb")
f.write(g.serialize(format="turtle"))
f.close()
