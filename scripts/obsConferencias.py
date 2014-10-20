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
nd=A.get_node(lconf)
nd.attr['color']="#A29999"

G(conf,rdf.type,owl.Class)
G(conf,rdfs.label,L(lconf,lang="pt"))
G(conf,rdfs.comment,L(u"Conferências são processos nacionais de promoção do diálogo entre governo e sociedade",lang="pt"))

pm=obs.ParticipationInstance # SKOS
lpm=u"Instância de participação social"
A.add_node(lpm,style="filled")

G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(conf,rdfs.subClassOf,pm)
A.add_edge(lconf,lpm)
e=A.get_edge(lconf,lpm)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

####
# define mecanismo de part
pm_=obs.ParticipationMechanism # SKOS
lpm_=u"Mecanismo de participação social"
A.add_node(lpm_,style="filled")
G(pm_,rdf.type,owl.Class)
G(pm_,rdfs.label,L(lpm_,lang="pt"))

pm__=obs.ParticipationInstanceOrMechanism # SKOS
lpm__=u"Instância ou mecanismo de participação social"
A.add_node(lpm__,style="filled")
G(pm__,rdf.type,owl.Class)
G(pm__,rdfs.label,L(lpm__,lang="pt"))

G(pm_,rdfs.subClassOf,pm__)
A.add_edge(lpm_,lpm__)
e=A.get_edge(lpm_,lpm__)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2
G(pm,rdfs.subClassOf,pm__)
A.add_edge(lpm,lpm__)
e=A.get_edge(lpm,lpm__)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

# coloca conselho como subclasse de inst de part soc
sp=obs.Council
lsp=u"Conselho" # SKOS TTM
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,obs.ParticipationInstance)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lpm)
e=A.get_edge(lsp,lpm)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.Ombusdmen
lsp=u"Ouvidoria" # SKOS TTM
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,obs.ParticipationInstance)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lpm)
e=A.get_edge(lsp,lpm)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.Commission
lsp=u"Comissão" # SKOS TTM
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,obs.ParticipationInstance)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lpm)
e=A.get_edge(lsp,lpm)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

# Mecanismos
sp=obs.DialogueTable
lsp=u"Mesa de diálogo" # SKOS TTM
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,obs.ParticipationMechanism)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lpm_)
e=A.get_edge(lsp,lpm_)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.InterCouncilForum
lsp=u"Fórum interconselhos" # SKOS TTM
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,obs.ParticipationMechanism)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lpm_)
e=A.get_edge(lsp,lpm_)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.PublicAudience
lsp=u"Audiência pública" # SKOS TTM
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,obs.ParticipationMechanism)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lpm_)
e=A.get_edge(lsp,lpm_)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.PublicConsultation
lsp=u"Consulta pública" # SKOS TTM
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,obs.ParticipationMechanism)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lpm_)
e=A.get_edge(lsp,lpm_)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.VirtualParticipationEnvironment
lsp=u"Ambente virtual de participação social" # SKOS TTM
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,obs.ParticipationMechanism)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lpm_)
e=A.get_edge(lsp,lpm_)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2









# define demais classes para as instancias e mecanismos de part soc


####
nm=obs.name
lnm=u"nome"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.range,xsd.string)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:string"
nd.attr['color']="#A2F3D1"
A.add_edge(lconf,COUNT)
e=A.get_edge(lconf,COUNT); COUNT+=1
e.attr["label"]=lnm

####

nm=obs.edition
lnm=u"edição"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.range,xsd.integer)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:integer"
nd.attr['color']="#A2F3D1"
A.add_edge(lconf,COUNT)
e=A.get_edge(lconf,COUNT); COUNT+=1
e.attr["label"]=lnm

####

nm=obs.participants
lnm=u"participantes"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.range,xsd.integer)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:integer"
nd.attr['color']="#A2F3D1"
A.add_edge(lconf,COUNT)
e=A.get_edge(lconf,COUNT); COUNT+=1
e.attr["label"]=lnm

####

nm=obs.unidentified
lnm=u"não identificados"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.comment,L(u"participantes não identificados",lang="pt"))
G(nm,rdfs.range,xsd.integer)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:integer"
nd.attr['color']="#A2F3D1"
A.add_edge(lconf,COUNT)
e=A.get_edge(lconf,COUNT); COUNT+=1
e.attr["label"]=lnm


####

nm=obs.year
lnm=u"ano"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.range,xsd.gYear)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:gYear"
nd.attr['color']="#A2F3D1"
A.add_edge(lconf,COUNT)
e=A.get_edge(lconf,COUNT); COUNT+=1
e.attr["label"]=lnm

#########
ta=obs.responsibleAgency
lta=u"órgão responsável"
th=obs.PublicAgency
lth=u"Órgão público"
G(ta,rdf.type,owl.ObjectProperty)
G(ta,rdfs.label,L(lta,lang="pt"))
G(ta,rdfs.range,th)
G(th,rdf.type,owl.Class)
G(th,rdfs.label,L(lth,lang="pt"))
A.add_node(lth,style="filled")
A.add_edge(lconf,lth)
e=A.get_edge(lconf,lth)
e.attr["label"]=lta

sp=obs.Council
lsp=u"Conselho" # SKOS TTM
G(sp,rdfs.subClassOf,th)
A.add_edge(lsp,lth)
e=A.get_edge(lsp,lth)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.Ministry
lsp=u"Ministério" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,th)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lth)
e=A.get_edge(lsp,lth)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2


sp=obs.Secretariat
lsp=u"Secretaria" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.comment,L(u"Secretaria com status ministerial",lang="pt"))
G(sp,rdfs.subClassOf,th)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lth)
e=A.get_edge(lsp,lth)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.ChamberOfDeputies
lsp=u"Câmara dos deputados" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,th)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lth)
e=A.get_edge(lsp,lth)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.NonGovernmentalForum
lsp=u"Fórum não governamental" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,th)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lth)
e=A.get_edge(lsp,lth)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

#### TTM
ca=obs.convocation
lca=u"convocação"
ac=obs.Act
lac=u"Ato normativo" # SKOS Ato Institucional

pu=obs.datePublished
lpu=u"data de publicação"
nr=obs.numericReference
lnr=u"referêcia numérica"

#la=obs.Law
#lla=u"Lei" # SKOS
oe=obs.Ordinance
loe=u"Portaria ministerial ou interministerial" # SKOS
de=obs.Decree
lde=u"Decreto presidencial" # SKOS
#bl=obs.Bylaws
#lbl=u"Regimento interno" #SKOS
re=obs.Resolution
lre=u"Resolução de conselho" #SKOS

G(ca,rdf.type,owl.ObjectProperty)
G(ca,rdfs.label,L(lca,lang="pt"))
G(ca,rdfs.range,ac)
G(oe,rdfs.subClassOf,ac)
G(de,rdfs.subClassOf,ac)
G(re,rdfs.subClassOf,ac)

G(ac,rdf.type,owl.Class)
G(ac,rdfs.label,L(lac,lang="pt"))
G(oe,rdf.type,owl.Class)
G(oe,rdfs.label,L(loe,lang="pt"))
G(de,rdf.type,owl.Class)
G(de,rdfs.label,L(lde,lang="pt"))
G(re,rdf.type,owl.Class)
G(re,rdfs.label,L(lre,lang="pt"))

G(pu,rdf.type,owl.DatatypeProperty)
G(pu,rdfs.label,L(lpu,lang="pt"))
G(pu,rdfs.range,xsd.dateTime)
G(nr,rdf.type,owl.DatatypeProperty)
G(nr,rdfs.label,L(lnr,lang="pt"))
G(nr,rdfs.range,xsd.string)

# desenhar isso
A.add_node(lac,style="filled")
A.add_edge(lconf,lac)
e=A.get_edge(lconf,lac)
e.attr["label"]=lca
A.add_node(loe,style="filled") ###
A.add_edge(loe,lac)
e=A.get_edge(loe,lac)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2
A.add_node(lde,style="filled") ###
A.add_edge(lde,lac)
e=A.get_edge(lde,lac)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2
A.add_node(lre,style="filled") ###
A.add_edge(lre,lac)
e=A.get_edge(lre,lac)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:dateTime"
nd.attr['color']="#A2F3D1"
A.add_edge(lac,COUNT)
e=A.get_edge(lac,COUNT); COUNT+=1
e.attr["label"]=lpu

A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:string"
nd.attr['color']="#A2F3D1"
A.add_edge(lac,COUNT)
e=A.get_edge(lac,COUNT); COUNT+=1
e.attr["label"]=lnr

####
#ta=obs.thematicArea
#lta=u"área temática" # SKOS
#th=obs.Theme
#lth=u"Tema"
ta=obs.area
lta=u"área" # SKOS
th=obs.PolicyArea
lth=u"Área de política"
G(ta,rdf.type,owl.ObjectProperty)
G(ta,rdfs.label,L(lta,lang="pt"))
G(ta,rdfs.range,th)
G(th,rdf.type,owl.Class)
G(th,rdfs.label,L(lth,lang="pt"))
A.add_node(lth,style="filled")
A.add_edge(lconf,lth)
e=A.get_edge(lconf,lth)
e.attr["label"]=lta

sp=obs.SocialPolicies
lsp=u"Políticas sociais" # SKOS TTM
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.comment,L(u"assistência social, cultura, saúde, segurança alimentar e nutricional",lang="pt"))
G(sp,rdfs.subClassOf,th)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lth)
e=A.get_edge(lsp,lth)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.EconomicDevelopment ###
lsp=u"Desenvolvimento econômico" # SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.comment,L(u"arranjos produtivos locais, assistência técnica e extensão rural, desenvolvimento regional e desenvolvimento rural sustentável e solidário",lang="pt"))
G(sp,rdfs.subClassOf,th)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lth)
e=A.get_edge(lsp,lth)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.GuaranteeOfRights ###
lsp=u"Garantia de direitos" # SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.comment,L(u"criança e adolescente, educação, juventude, LGBT, mulheres e pessoa idosa",lang="pt"))
G(sp,rdfs.subClassOf,th)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lth)
e=A.get_edge(lsp,lth)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.Infrastructure ###
lsp=u"Infraestrutura" # SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.comment,L(u"cidades",lang="pt"))
G(sp,rdfs.subClassOf,th)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lth)
e=A.get_edge(lsp,lth)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.NaturalResources ###
lsp=u"Recursos naturais" # SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.comment,L(u"meio ambiente",lang="pt"))
G(sp,rdfs.subClassOf,th)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lth)
e=A.get_edge(lsp,lth)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

################
ta=obs.has
lta=u"possui" # SKOS
th=obs.Goals
lth=u"Objetivos"
G(ta,rdf.type,owl.ObjectProperty)
G(ta,rdfs.label,L(lta,lang="pt"))
G(th,rdf.type,owl.Class)
G(th,rdfs.label,L(lth,lang="pt"))
A.add_node(lth,style="filled")
A.add_edge(lconf,lth)
e=A.get_edge(lconf,lth)
e.attr["label"]=lta

nm=obs.schedulingPurpose
lnm=u"agendamento"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.comment,L(u"possui a conferência objetivo de agendamento?",lang="pt"))
G(nm,rdfs.range,xsd.boolean)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:boolean"
nd.attr['color']="#A2F3D1"
A.add_edge(lth,COUNT)
e=A.get_edge(lth,COUNT); COUNT+=1
e.attr["label"]=lnm

nm=obs.evaluationPurpose
lnm=u"avaliação"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.comment,L(u"possui a conferência objetivo de avaliação?",lang="pt"))
G(nm,rdfs.range,xsd.boolean)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:boolean"
nd.attr['color']="#A2F3D1"
A.add_edge(lth,COUNT)
e=A.get_edge(lth,COUNT); COUNT+=1
e.attr["label"]=lnm

nm=obs.participationPurpose
lnm=u"participação"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.comment,L(u"possui a conferência objetivo de participação?",lang="pt"))
G(nm,rdfs.range,xsd.boolean)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:boolean"
nd.attr['color']="#A2F3D1"
A.add_edge(lth,COUNT)
e=A.get_edge(lth,COUNT); COUNT+=1
e.attr["label"]=lnm


nm=obs.propositionPurpose
lnm=u"proposição"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.comment,L(u"possui a conferência objetivo de proposição?",lang="pt"))
G(nm,rdfs.range,xsd.boolean)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:boolean"
nd.attr['color']="#A2F3D1"
A.add_edge(lth,COUNT)
e=A.get_edge(lth,COUNT); COUNT+=1
e.attr["label"]=lnm
####

th=obs.Theme
lth=u"Tema"
G(th,rdf.type,owl.Class)
G(th,rdfs.label,L(lth,lang="pt"))
A.add_node(lth,style="filled")
A.add_edge(lconf,lth)
e=A.get_edge(lconf,lth)
e.attr["label"]=lta

nm=obs.phrase
lnm=u"frase de referência"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.comment,L(u"frase de referência do tema da conferência",lang="pt"))
G(nm,rdfs.range,xsd.string)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:string"
nd.attr['color']="#A2F3D1"
A.add_edge(lth,COUNT)
e=A.get_edge(lth,COUNT); COUNT+=1
e.attr["label"]=lnm

nm=obs.thematicAxes
lnm=u"eixos temáticos"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.range,xsd.string)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:string"
nd.attr['color']="#A2F3D1"
A.add_edge(lth,COUNT)
e=A.get_edge(lth,COUNT); COUNT+=1
e.attr["label"]=lnm
####

ta=obs.step
lta=u"etapa" # SKOS
th=obs.ConferenceStep
lth=u"Etapa de conferência"
G(ta,rdf.type,owl.ObjectProperty)
G(ta,rdfs.label,L(lta,lang="pt"))
G(th,rdf.type,owl.Class)
G(th,rdfs.label,L(lth,lang="pt"))
G(th,rdfs.comment,L(u"Uma etapa é um evento participativo e também é chamada de conferência, enquanto 'a' conferência é o processo todo",lang="pt"))
G(ta,rdfs.range,th)
A.add_node(lth,style="filled")
A.add_edge(lconf,lth)
e=A.get_edge(lconf,lth)
e.attr["label"]=lta
lth_=lth

A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:integer"
nd.attr['color']="#A2F3D1"
A.add_edge(lth,COUNT)
e=A.get_edge(lth,COUNT); COUNT+=1
e.attr["label"]=u"participantes"


nm=obs.municipalities
lnm=u"municípios"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.comment,L(u"número de municípios envolvidos na etapa",lang="pt"))
G(nm,rdfs.range,xsd.integer)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:integer"
nd.attr['color']="#A2F3D1"
A.add_edge(lth,COUNT)
e=A.get_edge(lth,COUNT); COUNT+=1
e.attr["label"]=lnm

nm=obs.women
lnm=u"mulheres"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.comment,L(u"número de mulheres participantes ou reservado para mulheres",lang="pt"))
G(nm,rdfs.range,xsd.integer)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:integer"
nd.attr['color']="#A2F3D1"
A.add_edge(lth,COUNT)
e=A.get_edge(lth,COUNT); COUNT+=1
e.attr["label"]=lnm

nm=obs.proposals
lnm=u"propostas aprovadas"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.comment,L(u"número de propostas aprovadas na etapa",lang="pt"))
G(nm,rdfs.range,xsd.integer)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:integer"
nd.attr['color']="#A2F3D1"
A.add_edge(lth,COUNT)
e=A.get_edge(lth,COUNT); COUNT+=1
e.attr["label"]=lnm

nm=obs.delegateFocus
lnm=u"delegados referência para observação de gênero"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.comment,L(u"Para a contabilização da incidência de gênero dentre os participantes, se somente os delegados foram considerados, o objeto é True",lang="pt"))
G(nm,rdfs.range,xsd.boolen)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:boolean"
nd.attr['color']="#A2F3D1"
A.add_edge(lth,COUNT)
e=A.get_edge(lth,COUNT); COUNT+=1
e.attr["label"]=lnm

th=obs.NationalConference
lth=u"Conferência nacional"
G(th,rdf.type,owl.Class)
G(th,rdfs.label,L(lth,lang="pt"))
G(th,rdfs.comment,L(u"Uma fase é um evento participativo, enquanto a conferência em si é o processo todo",lang="pt"))
A.add_node(lth,style="filled")
A.add_edge(lth,lth_)
e=A.get_edge(lth,lth_)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

nm=obs.proposalsPriorization
lnm=u"priorização de propostas"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.range,xsd.boolean)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:boolean"
nd.attr['color']="#A2F3D1"
A.add_edge(lth,COUNT)
e=A.get_edge(lth,COUNT); COUNT+=1
e.attr["label"]=lnm

nm=obs.proposalsFormulation
lnm=u"formulação de propostas"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.range,xsd.boolean)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:boolean"
nd.attr['color']="#A2F3D1"
A.add_edge(lth,COUNT)
e=A.get_edge(lth,COUNT); COUNT+=1
e.attr["label"]=lnm

th=obs.StateConference
lth=u"Conferência estadual"
G(th,rdf.type,owl.Class)
G(th,rdfs.label,L(lth,lang="pt"))
G(th,rdfs.comment,L(u"Uma fase é um evento participativo, enquanto a conferência em si é o processo todo",lang="pt"))
A.add_node(lth,style="filled")
A.add_edge(lth,lth_)
e=A.get_edge(lth,lth_)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

th=obs.RegionalConference
lth=u"Conferência regional"
G(th,rdf.type,owl.Class)
G(th,rdfs.label,L(lth,lang="pt"))
G(th,rdfs.comment,L(u"Uma fase é um evento participativo, enquanto a conferência em si é o processo todo",lang="pt"))
A.add_node(lth,style="filled")
A.add_edge(lth,lth_)
e=A.get_edge(lth,lth_)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

th=obs.IntercityConferente
lth=u"Conferência intermunicipal"
G(th,rdf.type,owl.Class)
G(th,rdfs.label,L(lth,lang="pt"))
G(th,rdfs.comment,L(u"Uma fase é um evento participativo, enquanto a conferência em si é o processo todo",lang="pt"))
A.add_node(lth,style="filled")
A.add_edge(lth,lth_)
e=A.get_edge(lth,lth_)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

th=obs.MunicipalConference
lth=u"Conferência municipal"
G(th,rdf.type,owl.Class)
G(th,rdfs.label,L(lth,lang="pt"))
G(th,rdfs.comment,L(u"Uma fase é um evento participativo, enquanto a conferência em si é o processo todo",lang="pt"))
A.add_node(lth,style="filled")
A.add_edge(lth,lth_)
e=A.get_edge(lth,lth_)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

th=obs.VirtualConference
lth=u"Conferência virtual"
G(th,rdf.type,owl.Class)
G(th,rdfs.label,L(lth,lang="pt"))
G(th,rdfs.comment,L(u"Uma fase é um evento participativo, enquanto a conferência em si é o processo todo",lang="pt"))
A.add_node(lth,style="filled")
A.add_edge(lth,lth_)
e=A.get_edge(lth,lth_)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

th=obs.FreeConference
lth=u"Conferência livre"
G(th,rdf.type,owl.Class)
G(th,rdfs.label,L(lth,lang="pt"))
G(th,rdfs.comment,L(u"Uma fase é um evento participativo, enquanto a conferência em si é o processo todo",lang="pt"))
A.add_node(lth,style="filled")
A.add_edge(lth,lth_)
e=A.get_edge(lth,lth_)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2


th=obs.ExtraordinaryConference
lth=u"Conferência extraordinária"
G(th,rdf.type,owl.Class)
G(th,rdfs.label,L(lth,lang="pt"))
G(th,rdfs.comment,L(u"Uma etapa é um evento participativo, também chamado de conferência, enquanto a conferência em si é o processo todo",lang="pt"))
A.add_node(lth,style="filled")
A.add_edge(lth,lth_)
e=A.get_edge(lth,lth_)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

###
mm=obs.startDate
lnm=u"início"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.range,xsd.dateTime) # usar "P%sM",datatype=xsd.duration 
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:dateTime"
nd.attr['color']="#A2F3D1"
A.add_edge(lconf,COUNT)
e=A.get_edge(lconf,COUNT); COUNT+=1
e.attr["label"]=lnm

mm=obs.endDate
lnm=u"término"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.range,xsd.dateTime) # usar "P%sM",datatype=xsd.duration 
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:dateTime"
nd.attr['color']="#A2F3D1"
A.add_edge(lconf,COUNT)
e=A.get_edge(lconf,COUNT); COUNT+=1
e.attr["label"]=lnm

###
ta=obs.conselho
lta=u"conselho"
G(ta,rdfs.label,L(lta,lang="pt"))
G(ta,rdfs.range,obs.Council)
A.add_edge(lconf,u"Conselho")
e=A.get_edge(lconf,u"Conselho")
e.attr["label"]=lta
##########

co=obs.composition
lco=u"composição"
bo=obs.ManagementBody
lbo=u"Corpo gestor"
G(co,rdf.type,owl.ObjectProperty)
G(co,rdfs.label,L(lco,lang="pt"))
G(co,rdfs.range,bo)
G(bo,rdf.type,owl.Class)
G(bo,rdfs.label,L(lbo,lang="pt"))
A.add_node(lbo,style="filled")
A.add_edge(lconf,lbo)
e=A.get_edge(lconf,lbo)
e.attr["label"]=lco

co_=obs.commission
lco_=u"commissão"
bo_=obs.NationalOrganizationCommission
lbo_=u"Comissão da organização nacional"
G(co_,rdf.type,owl.ObjectProperty)
G(co_,rdfs.label,L(lco_,lang="pt"))
G(co_,rdfs.range,bo_)
G(bo_,rdf.type,owl.Class)
G(bo_,rdfs.label,L(lbo_,lang="pt"))
A.add_node(lbo_,style="filled")
A.add_edge(lbo,lbo_)
e=A.get_edge(lbo,lbo_)
e.attr["label"]=lco_


co=obs.entity
lco=u"entidade"
bo__=obs.NationalOrganizationCommissionComponent
lbo___=u"Componente da comissão de organização nacional"

G(co,rdf.type,owl.ObjectProperty)
G(co,rdfs.label,L(lco,lang="pt"))
G(co,rdfs.range,bo)
G(bo__,rdf.type,owl.Class)
G(bo__,rdfs.label,L(lbo___,lang="pt"))
A.add_node(lbo___,style="filled")
A.add_edge(lbo_,lbo___)
e=A.get_edge(lbo_,lbo___)
e.attr["label"]=lco


bb=[(obs.Committee,u"Comitê"),(obs.Group,u"Grupo"),(obs.Commission,u"Comissão"),(obs.Coordination,u"Coordenação"),(obs.Presidency,u"Presidência"),(obs.Subcommittee,u"Subcomitê"),(obs.Counsel,u"Assessoria"),(obs.Coordinator,u"Coordenador"),(obs.Secretary,u"Secretário"),(obs.Rapporteur,u"Relator")]
jaTem=[obs.Commission]

for b in bb:
    bo_=b[0]
    lbo__=b[1]
    G(bo_,rdf.type,owl.Class)
    G(bo_,rdfs.label,L(lbo_,lang="pt"))
    A.add_node(lbo__,style="filled")
    A.add_edge(lbo__,lbo___)
    e=A.get_edge(lbo__,lbo___)
    e.attr["arrowhead"]="empty"
    e.attr["arrowsize"]=2


pp=[(obs.deputy,u"adjunta"),(obs.working,u"de trabalho"),(obs.general,u"geral"),(obs.special,u"especial"),(obs.executive,u"executiva"),(obs.editorial,u"editorial")]
for pr in pp:
    nm=pr[0]
    lnm=pr[1]
    #nm=obs.participationPurpose
    #lnm=u"participação"
    G(nm,rdf.type,owl.DatatypeProperty)
    G(nm,rdfs.label,L(lnm,lang="pt"))
    G(nm,rdfs.comment,L(u"A componente é %s"%(lnm,),lang="pt")) 
    G(nm,rdfs.range,xsd.boolean)
    A.add_node(COUNT,style="filled")
    nd=A.get_node(COUNT)
    nd.attr["label"]="xsd:boolean"
    nd.attr['color']="#A2F3D1"
    A.add_edge(lbo___,COUNT)
    e=A.get_edge(lbo___,COUNT); COUNT+=1
    e.attr["label"]=lnm


nm=obs.nonGovernmentalPositions
lnm=u"vagas não governamentais"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.range,xsd.integer)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:integer"
nd.attr['color']="#A2F3D1"
A.add_edge(lbo_,COUNT)
e=A.get_edge(lbo_,COUNT); COUNT+=1
e.attr["label"]=lnm

nm=obs.governmentalPositions
lnm=u"vagas governamentais"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.range,xsd.integer)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:integer"
nd.attr['color']="#A2F3D1"
A.add_edge(lbo_,COUNT)
e=A.get_edge(lbo_,COUNT); COUNT+=1
e.attr["label"]=lnm

nm=obs.councilPositions
lnm=u"vagas para membros do conselho"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.range,xsd.integer)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:integer"
nd.attr['color']="#A2F3D1"
A.add_edge(lbo_,COUNT)
e=A.get_edge(lbo_,COUNT); COUNT+=1
e.attr["label"]=lnm

####
# Colunas AD-AH, fazendo pelo diagrama cacoo
co_=obs.methodology
lco_=u"metodologia"
bo_=obs.ConferenceMethodology
lbo_=u"Metodologia de conferência"
G(co_,rdf.type,owl.ObjectProperty)
G(co_,rdfs.label,L(lco_,lang="pt"))
G(co_,rdfs.range,bo_)
G(bo_,rdf.type,owl.Class)
G(bo_,rdfs.label,L(lbo_,lang="pt"))
A.add_node(lbo_,style="filled")
A.add_edge(lconf,lbo_)
e=A.get_edge(lconf,lbo_)
e.attr["label"]=lco_

lbo__=lbo_

co_=obs.form
lco_=u"forma"
bo_=obs.InteractionDialogueForm
lbo_=u"Forma de interação e diálogo"
G(co_,rdf.type,owl.ObjectProperty)
G(co_,rdfs.label,L(lco_,lang="pt"))
G(co_,rdfs.range,bo_)
G(bo_,rdf.type,owl.Class)
G(bo_,rdfs.label,L(lbo_,lang="pt"))
A.add_node(lbo_,style="filled")
A.add_edge(lbo__,lbo_)
e=A.get_edge(lbo__,lbo_)
e.attr["label"]=lco_

lbo___=lbo_

co_=obs.predicts
lco_=u"prevê"
bo_=obs.ParticipativeMoment
lbo_=u"Momento participativo"
G(co_,rdf.type,owl.ObjectProperty)
G(co_,rdfs.label,L(lco_,lang="pt"))
G(co_,rdfs.range,bo_)
G(bo_,rdf.type,owl.Class)
G(bo_,rdfs.label,L(lbo_,lang="pt"))
A.add_node(lbo_,style="filled")
A.add_edge(lbo__,lbo_)
e=A.get_edge(lbo__,lbo_)
e.attr["label"]=lco_

bo____=bo_
lbo____=lbo_

co_=obs.incorporates
lco_=u"incorpora"
G(co_,rdf.type,owl.ObjectProperty)
G(co_,rdfs.label,L(lco_,lang="pt"))
G(co_,rdfs.range,bo_)
G(bo_,rdf.type,owl.Class)
G(bo_,rdfs.label,L(lbo_,lang="pt"))
A.add_node(lbo_,style="filled")
A.add_edge(lbo___,lbo_)
e=A.get_edge(lbo___,lbo_)
e.attr["label"]=lco_

## Momentos

pm=obs.WorkGroup # SKOS
lpm=u"Grupo de trabalho"
A.add_node(lpm,style="filled")
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(pm,rdfs.subClassOf,bo____)
A.add_edge(lpm,lbo____)
e=A.get_edge(lpm,lbo____)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

pm=obs.Lecture # SKOS
lpm=u"Palestra"
A.add_node(lpm,style="filled")
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(pm,rdfs.subClassOf,bo____)
A.add_edge(lpm,lbo____)
e=A.get_edge(lpm,lbo____)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

pm=obs.Workshop # SKOS
lpm=u"Oficina"
A.add_node(lpm,style="filled")
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(pm,rdfs.subClassOf,bo____)
A.add_edge(lpm,lbo____)
e=A.get_edge(lpm,lbo____)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

pm=obs.Plenary # SKOS
lpm=u"Plenária"
A.add_node(lpm,style="filled")
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(pm,rdfs.subClassOf,bo____)
A.add_edge(lpm,lbo____)
e=A.get_edge(lpm,lbo____)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

pmF=pm
lpmF=lpm

pm=obs.ThematicPlenary # SKOS
lpm=u"Plenária temática"
lpm_=u"Plenária intermediária"
A.add_node(lpm,style="filled")
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(pm,rdfs.label,L(lpm_,lang="pt"))
G(pm,rdfs.subClassOf,pmF)
A.add_edge(lpm,lpmF)
e=A.get_edge(lpm,lpmF)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2


####

lth=u"Etapa de conferência"
ta=obs.proposalsLimit
lta=u"limite de propostas" # SKOS

G(ta,rdf.type,owl.DatatypeProperty)
G(ta,rdfs.label,L(lta,lang="pt"))
G(ta,rdfs.range,xsd.integer)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]=u"xsd:integer"
nd.attr['color']="#A2F3D1"
A.add_edge(lth,COUNT)
e=A.get_edge(lth,COUNT); COUNT+=1
e.attr["label"]=lta

#####
# Colunas AQ e AR contempladas diretamente na classe NationalConference
###
# AS-AU
co=obs.regiment
lco=u"regimento"
bo=obs.Positions
lbo=u"Vagas"
G(co,rdf.type,owl.ObjectProperty)
G(co,rdfs.label,L(lco,lang="pt"))
G(bo,rdf.type,owl.Class)
G(bo,rdfs.label,L(lbo,lang="pt"))
A.add_node(lbo,style="filled")
A.add_edge(u"Corpo gestor",lbo)
e=A.get_edge(u"Corpo gestor",lbo)
e.attr["label"]=lco

nm=obs.delegates
lnm=u"delegados"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.range,xsd.integer)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:integer"
nd.attr['color']="#A2F3D1"
A.add_edge(lbo,COUNT)
e=A.get_edge(lbo,COUNT); COUNT+=1
e.attr["label"]=lnm

nm=obs.governmental
lnm=u"governamentais"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.range,xsd.integer)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:integer"
nd.attr['color']="#A2F3D1"
A.add_edge(lbo,COUNT)
e=A.get_edge(lbo,COUNT); COUNT+=1
e.attr["label"]=lnm

nm=obs.nonGovernmental
lnm=u"não governamentais"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.range,xsd.integer)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:integer"
nd.attr['color']="#A2F3D1"
A.add_edge(lbo,COUNT)
e=A.get_edge(lbo,COUNT); COUNT+=1
e.attr["label"]=lnm

nm=obs.guests
lnm=u"convidados"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.range,xsd.boolean)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:boolean"
nd.attr['color']="#A2F3D1"
A.add_edge(lbo,COUNT)
e=A.get_edge(lbo,COUNT); COUNT+=1
e.attr["label"]=lnm


####

ta=obs.other
lta=u"outro" # SKOS
th=obs.OtherGroup
lth=u"Outro Grupo"
G(ta,rdf.type,owl.ObjectProperty)
G(ta,rdfs.label,L(lta,lang="pt"))
G(th,rdf.type,owl.Class)
G(th,rdfs.label,L(lth,lang="pt"))
G(ta,rdfs.range,th)
A.add_node(lth,style="filled")
A.add_edge(lbo,lth)
e=A.get_edge(lbo,lth)
e.attr["label"]=lta
lth_=lth


nm=obs.quantity
lnm=u"quantidade"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.range,xsd.integer)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:integer"
nd.attr['color']="#A2F3D1"
A.add_edge(lth,COUNT)
e=A.get_edge(lth,COUNT); COUNT+=1
e.attr["label"]=lnm

nm=obs.description
lnm=u"descrição"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.range,xsd.string)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:string"
nd.attr['color']="#A2F3D1"
A.add_edge(lth,COUNT)
e=A.get_edge(lth,COUNT); COUNT+=1
e.attr["label"]=lnm

####
# Cotas

bo=obs.Quotas
lbo=u"Cotas"
G(bo,rdf.type,owl.Class)
G(bo,rdfs.label,L(lbo,lang="pt"))
A.add_node(lbo,style="filled")
A.add_edge(u"Corpo gestor",lbo)
e=A.get_edge(u"Corpo gestor",lbo)
e.attr["label"]=lco

A.add_edge(lbo,lth)
e=A.get_edge(lbo,lth)
e.attr["label"]=lta

lnm=u"mulheres"
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:integer"
nd.attr['color']="#A2F3D1"
A.add_edge(lbo,COUNT)
e=A.get_edge(lbo,COUNT); COUNT+=1
e.attr["label"]=lnm

nm=obs.etnicGroup
lnm=u"grupo étnico"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.range,xsd.integer)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:integer"
nd.attr['color']="#A2F3D1"
A.add_edge(lbo,COUNT)
e=A.get_edge(lbo,COUNT); COUNT+=1
e.attr["label"]=lnm

####






#####
nome=("../figs/obsConferencia.png")
A.draw(nome,prog="dot") # draw to png using circo
nome=("../figs/obsConferencia2.png")
A.draw(nome,prog="circo") # draw to png using circo
nome=("../figs/obsConferencia3.png")
A.draw(nome,prog="fdp") # draw to png using circo
A.write("../rdf/obsConferencia.dot")

f=open("../rdf/obsConferencia.owl","wb")
f.write(g.serialize())
f.close()
f=open("../rdf/obsConferencia.ttl","wb")
f.write(g.serialize(format="turtle"))
f.close()
