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
G(cons,skos.altLabel,L(u"Conselho gestor",lang="pt"))
G(cons,skos.definition,L(u"Espaços públicos vinculados a órgãos do Poder Executivo, tendo por finalidade permitir a participação da sociedade na definição de prioridades para a agenda política, bem como na formulação, no acompanhamento e no controle das políticas públicas (IPEA 2013)",lang="pt"))
G(cons,skos.scopeNote,L(u"Espaço participativo com a finalidade de incidir nas políticas públicas de determinado tema, nos quais é prevista certa permanência no tempo, composto por representantes do poder público e da sociedade civil, esta podendo ser dividida em diferentes segmentos.",lang="pt"))
G(cons,skos.scopeNote,L(u"espaço contínuo de participação social",lang="pt"))

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

de=vbs.Decree
lde=u"Decreto" # SKOS
G(de,rdf.type,skos.Concept)
G(de,skos.prefLabel,L(lde,lang="pt"))
G(de,skos.broader,ac)

bl=vbs.Bylaws
lbl=u"Regimento interno" #SKOS
G(bl,rdf.type,skos.Concept)
G(bl,skos.prefLabel,L(lbl,lang="pt"))
G(bl,skos.altLabel,L(u"Estatuto",lang="pt"))
G(bl,skos.broader,ac)

re=vbs.Resolution
lre=u"Resolução" #SKOS
G(re,rdf.type,skos.Concept)
G(re,skos.prefLabel,L(lre,lang="pt"))
G(re,skos.altLabel,L(u"Deliberação",lang="pt"))
G(re,skos.altLabel,L(u"Tese",lang="pt"))
G(re,skos.altLabel,L(u"Diretriz",lang="pt"))
G(re,skos.altLabel,L(u"Decisão",lang="pt"))
G(re,skos.altLabel,L(u"Proposta",lang="pt"))

G(re,skos.broader,ac)

###
re=vbs.reformulation # menor pq eh propriedade na obs
lre=u"Reformulação" #SKOS
G(re,rdf.type,skos.Concept)
G(re,skos.prefLabel,L(lre,lang="pt"))

### TTM
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


######
sp=vbs.DeliberativeInstance
lsp=u"Instância deliberativa" # SKOS
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.broader,vbs.ParticipationInstance)

sp=vbs.AdvisoryInstance
lsp=u"Instância consultiva" # SKOS
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.broader,vbs.ParticipationInstance)
######
sp=vbs.DeliberativeMechanism
lsp=u"Mecanismo deliberativo" # SKOS
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.broader,vbs.ParticipationMechanism)

sp=vbs.AdvisoryMechanism
lsp=u"Mecanismo consultivo" # SKOS
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.broader,vbs.ParticipationMechanism)


####
sp=vbs.ExecutiveSecretariat
lsp=u"Secretaria executiva"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))

conf=vbs.Conference
G(conf,rdf.type,skos.Concept)
G(conf,skos.prefLabel,L(u"Conferência",lang="pt"))
G(conf,skos.altLabel,L(u"Conferência nacional",lang="pt"))
G(conf,skos.altLabel,L(u"Conferência de políticas públicas",lang="pt"))
G(conf,skos.definition,L(u"Processo periódico de promoção do diálogo entre governo e sociedade, realizado em etapas, tipicamente convocadas pelo Executivo",lang="pt")) # Melhorar TTM
G(conf,skos.definition,L(u"Instância colegiada de temática permanente, instituída por ato normativo, de diálogo entre a sociedade civil e o governo para promover a participação no processo decisório e na gestão de políticas públicas",lang="pt")) # Melhorar TTM
G(conf,skos.broader,vbs.ParticipationInstance)


####

pu=vbs.PublicPolicy
lpu=u"Política pública" # SKOS
G(pu,rdf.type,skos.Concept)
G(pu,skos.prefLabel,L(lpu,lang="pt"))

sp=vbs.NationalSystem
lsp=u"Sistema nacional"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.broader,pu)

sp=vbs.NationalPlan
lsp=u"Política ou plano nacional"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.broader,pu)

sp=vbs.Statute
lsp=u"Estatuto"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.definition,L(u"Conjunto de normas do ordenamento jurídico brasileiro usualmente instituído por lei.",lang="pt"))
G(sp,skos.scopeNote,L(u"Estatuto que instaura política pública",lang="pt"))
G(sp,skos.scopeNote,L(u"Não é estatuto sinônimo de regimento interno",lang="pt"))
G(sp,skos.broader,pu)

####
sp=vbs.parity
lsp=u"paridade"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.scopeNote,L(u"paridade é um conceito local, podendo por exemplo, ser considerada proporção igual de membros do governo e da sociedade ou alguma equivalência semelhante se desconsiderado algum grupo especial",lang="pt"))

mc=vbs.ParticipantSelectionMethod
lmc=u"Método de seleção de participantes"
G(mc,rdf.type,skos.Concept)
G(mc,skos.prefLabel,L(lmc,lang="pt"))

mc=vbs.agenda
lmc=u"pauta"
G(mc,rdf.type,skos.Concept)
G(mc,skos.prefLabel,L(lmc,lang="pt"))

mc=vbs.QualityVote
lmc=u"Voto de qualidade"
G(mc,rdf.type,skos.Concept)
G(cons,skos.definition,L(u"voto de desempate de votação",lang="pt"))
G(cons,skos.altLabel,L(u"voto de desempate",lang="pt"))
G(cons,skos.altLabel,L(u"voto de minerva",lang="pt"))
G(mc,skos.prefLabel,L(lmc,lang="pt"))

mc=vbs.AdReferendum
lmc=u"Decisão ad referendum"
G(mc,rdf.type,skos.Concept)
G(cons,skos.definition,L(u"decisão a ser referenciada pelo grupo legitimado posteriormente",lang="pt"))
G(mc,skos.prefLabel,L(lmc,lang="pt"))

mc=vbs.renewal
lmc=u"Recondução de mandato"
G(mc,rdf.type,skos.Concept)
G(mc,skos.prefLabel,L(lmc,lang="pt"))
G(mc,skos.scopeNote,L(u"Quando há 'limite de mandato', há limite para recondução.",lang="pt"))
G(mc,skos.scopeNote,L(u"Este conceito foi trazido do campo dos conselhos, pode ser aplicável em outros contextos.",lang="pt"))



f=open("../rdf/vbsConselho.rdf","wb")
f.write(g.serialize())
f.close()
