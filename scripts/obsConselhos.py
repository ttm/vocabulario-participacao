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

cons=obs.Council # SKOS
lcons=u"Conselho"
A.add_node(lcons,style="filled")

G(cons,rdf.type,owl.Class)
G(cons,rdfs.label,L(lcons,lang="pt"))
G(cons,rdfs.comment,L(u"Conselho de políticas públicas",lang="pt"))

pm=obs.ParticipationMechanism # SKOS
lpm=u"Mecanismo ou instância de participação social"
A.add_node(lpm,style="filled")

G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(cons,rdfs.subClassOf,pm)
A.add_edge(lcons,lpm)
e=A.get_edge(lcons,lpm)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

ab=obs.acronym
lab=u"sigla"
G(ab,rdf.type,owl.DatatypeProperty)
G(ab,rdfs.label,L(lab,lang="pt"))
G(ab,rdfs.range,xsd.string)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:string"
nd.attr['color']="#A2F3D1"
A.add_edge(lcons,COUNT)
e=A.get_edge(lcons,COUNT); COUNT+=1
e.attr["label"]=lab

nm=obs.name
lnm=u"nome"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.range,xsd.string)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:string"
nd.attr['color']="#A2F3D1"
A.add_edge(lcons,COUNT)
e=A.get_edge(lcons,COUNT); COUNT+=1
e.attr["label"]=lnm

la=obs.linkedAgency
lla=u"órgão vinculado"
mn=obs.Ministry
lmn=u"Ministério" # entra no SKOS
sc=obs.Secretariat
lsc=u"Secretaria" # entra no SKOS

G(mn,rdf.type,owl.Class)
G(mn,rdfs.label,L(lmn,lang="pt"))
G(sc,rdf.type,owl.Class)
G(sc,rdfs.label,L(lsc,lang="pt"))

G(la,rdf.type,owl.ObjectProperty)
G(la,rdfs.label,L(lla,lang="pt"))
B=r.BNode()
G(B, owl.unionOf, mn)
G(B, owl.unionOf, sc)
G(la,rdfs.range,B)
A.add_node(lmn,style="filled")
nd=A.get_node(lmn)
#nd.attr["label"]=u"%s<br />%s"%(lmn,lsc)
nd.attr["label"]=(u"<%s<br />%s>")%(lmn,lsc)
A.add_edge(lcons,lmn)
e=A.get_edge(lcons,lmn)
e.attr["label"]=lla

yc=obs.yearCreated
lyc=u"Ano de criação"
G(yc,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lyc,lang="pt"))
G(nm,rdfs.range,xsd.gYear)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:gYear"
nd.attr['color']="#A2F3D1"
A.add_edge(lcons,COUNT)
e=A.get_edge(lcons,COUNT); COUNT+=1
e.attr["label"]=lyc

########### PPP
ca=obs.creationAct
lca=u"ato de criação"
ac=obs.Act
lac=u"Ato normativo" # SKOS Ato Institucional

pu=obs.datePublished
lpu=u"data de publicação"
nr=obs.numericReference
lnr=u"referêcia numérica"

la=obs.Law
lla=u"Lei" # SKOS
oe=obs.Ordinance
loe=u"Portaria" # SKOS
de=obs.Decree
lde=u"Decreto" # SKOS
bl=obs.Bylaws
lbl=u"Regimento interno" #SKOS
re=obs.Resolution
lre=u"Resolução" #SKOS

G(ca,rdf.type,owl.ObjectProperty)
G(ca,rdfs.label,L(lca,lang="pt"))
G(ca,rdfs.range,ac)
G(la,rdfs.subClassOf,ac)
G(oe,rdfs.subClassOf,ac)
G(de,rdfs.subClassOf,ac)
G(bl,rdfs.subClassOf,ac)
G(re,rdfs.subClassOf,ac)

G(ac,rdf.type,owl.Class)
G(ac,rdfs.label,L(lac,lang="pt"))
G(la,rdf.type,owl.Class)
G(la,rdfs.label,L(lla,lang="pt"))
G(oe,rdf.type,owl.Class)
G(oe,rdfs.label,L(loe,lang="pt"))
G(de,rdf.type,owl.Class)
G(de,rdfs.label,L(lde,lang="pt"))
G(bl,rdf.type,owl.Class)
G(bl,rdfs.label,L(lbl,lang="pt"))
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
A.add_edge(lcons,lac)
e=A.get_edge(lcons,lac)
e.attr["label"]=lca
A.add_node(lla,style="filled") ###
A.add_edge(lla,lac)
e=A.get_edge(lla,lac)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2
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
A.add_node(lbl,style="filled") ###
A.add_edge(lbl,lac)
e=A.get_edge(lbl,lac)
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

###########
re=obs.reformulation
lre=u"reformulação" # SKOS
G(re,rdf.type,owl.ObjectProperty)
G(re,rdfs.label,L(lre,lang="pt"))
G(re,rdfs.range,ac)
A.add_edge(lcons,lac)
e=A.get_edge(lcons,lac)
e.attr["label"]=lre
###########
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
A.add_edge(lcons,lth)
e=A.get_edge(lcons,lth)
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

##########

ti=obs.type
lti=u"tipo"
de=obs.DeliberativeInstance
lde=u"Instância deliberativa" # SKOS
co=obs.AdvisoryInstance
lco=u"Instância consultiva" # SKOS
G(de,rdf.type,owl.Class)
G(de,rdfs.label,L(lde,lang="pt"))
G(co,rdf.type,owl.Class)
G(co,rdfs.label,L(lco,lang="pt"))

G(ti,rdf.type,owl.ObjectProperty)
G(ti,rdfs.label,L(lti,lang="pt"))
B=r.BNode()
G(B, owl.unionOf,de)
G(B, owl.unionOf,co)
G(ca,rdfs.range,B)
G(ca,rdfs.domain,obs.ParticipationMechanism)
A.add_node(lde,style="filled")
nd=A.get_node(lde)
nd.attr["label"]=(u"<%s<br />%s>")%(lde,lco)
A.add_edge(lcons,lde)
e=A.get_edge(lcons,lde)
e.attr["label"]=lti

#####

mi=obs.meetingsInterval
lmi=u"meses entre reuniões"
G(mi,rdf.type,owl.DatatypeProperty)
G(mi,rdfs.label,L(lmi,lang="pt"))
G(mi,rdfs.range,xsd.integer)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:integer"
nd.attr['color']="#A2F3D1"
A.add_edge(lcons,COUNT)
e=A.get_edge(lcons,COUNT); COUNT+=1
e.attr["label"]=lmi

#####

es=obs.executiveSecretariat
les=u"possui secretaria executiva"
G(es,rdf.type,owl.DatatypeProperty)
G(es,rdfs.label,L(les,lang="pt"))
G(es,rdfs.range,xsd.boolean)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:boolean"
nd.attr['color']="#A2F3D1"
A.add_edge(lcons,COUNT)
e=A.get_edge(lcons,COUNT); COUNT+=1
e.attr["label"]=les


es=obs.commission
les=u"trabalha com comissões"
G(es,rdf.type,owl.DatatypeProperty)
G(es,rdfs.label,L(les,lang="pt"))
G(es,rdfs.range,xsd.boolean)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:boolean"
nd.attr['color']="#A2F3D1"
A.add_edge(lcons,COUNT)
e=A.get_edge(lcons,COUNT); COUNT+=1
e.attr["label"]=les

es=obs.conference
les=u"realizou conferencias" # SKOS
G(es,rdf.type,owl.DatatypeProperty)
G(es,rdfs.label,L(les,lang="pt"))
G(es,rdfs.range,xsd.boolean)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:boolean"
nd.attr['color']="#A2F3D1"
A.add_edge(lcons,COUNT)
e=A.get_edge(lcons,COUNT); COUNT+=1
e.attr["label"]=les

es=obs.conferencesCount
les=u"quantas conferencias"
G(es,rdf.type,owl.DatatypeProperty)
G(es,rdfs.label,L(les,lang="pt"))
G(es,rdfs.range,xsd.integer)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:integer"
nd.attr['color']="#A2F3D1"
A.add_edge(lcons,COUNT)
e=A.get_edge(lcons,COUNT); COUNT+=1
e.attr["label"]=les

###########
es=obs.linkedPolicy
les=u"política vinculada"
pu=obs.PublicPolicy
lpu=u"Política pública" # SKOS

G(es,rdf.type,owl.ObjectProperty)
G(es,rdfs.label,L(les,lang="pt"))
G(es,rdfs.range,pu)
G(pu,rdf.type,owl.Class)
G(pu,rdfs.label,L(lpu,lang="pt"))

sy=obs.NationalSystem
lsy=u"Sistema nacional" # SKOS
G(sy,rdf.type,owl.Class)
G(sy,rdfs.label,L(lsy,lang="pt"))
G(sy,rdfs.subClassOf,pu)
pl=obs.NationalPlan
lpl=u"Política ou plano nacional" # SKOS
G(pl,rdf.type,owl.Class)
G(pl,rdfs.label,L(lpl,lang="pt"))
G(pl,rdfs.subClassOf,pu)
st=obs.Statute
lst=u"Estatuto" # SKOS
G(st,rdf.type,owl.Class)
G(st,rdfs.label,L(lst,lang="pt"))
G(st,rdfs.subClassOf,pu)

# desenhar certinho
A.add_node(lpu,style="filled")
A.add_edge(lcons,lpu)
e=A.get_edge(lcons,lpu)
e.attr["label"]=les

A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:string"
nd.attr['color']="#A2F3D1"
A.add_edge(lpu,COUNT)
e=A.get_edge(lpu,COUNT); COUNT+=1
e.attr["label"]=u"nome"

A.add_node(lsy,style="filled") ###
A.add_edge(lsy,lpu)
e=A.get_edge(lsy,lpu)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2
A.add_node(lpl,style="filled") ###
A.add_edge(lpl,lpu)
e=A.get_edge(lpl,lpu)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2
A.add_node(lst,style="filled") ###
A.add_edge(lst,lpu)
e=A.get_edge(lst,lpu)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

##########
# composicao dos conselhos

co=obs.composition
lco=u"composição"
bo=obs.Body
lbo=u"Corpo"
G(co,rdf.type,owl.ObjectProperty)
G(co,rdfs.label,L(lco,lang="pt"))
G(co,rdfs.range,bo)
G(bo,rdf.type,owl.Class)
G(bo,rdfs.label,L(lbo,lang="pt"))
A.add_node(lbo,style="filled")
A.add_edge(lcons,lbo)
e=A.get_edge(lcons,lbo)
e.attr["label"]=lco

#>>>>

mc=obs.membersCount
lmc=u"quantidade de membros"
G(mc,rdf.type,owl.DatatypeProperty)
G(mc,rdfs.label,L(lmc,lang="pt"))
G(mc,rdfs.range,xsd.integer)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:integer"
nd.attr['color']="#A2F3D1"
A.add_edge(lbo,COUNT)
e=A.get_edge(lbo,COUNT); COUNT+=1
e.attr["label"]=lmc


mc=obs.governmentFraction
lmc=u"fração do governo"
G(mc,rdf.type,owl.DatatypeProperty)
G(mc,rdfs.label,L(lmc,lang="pt"))
G(mc,rdfs.range,xsd.double)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:double"
nd.attr['color']="#A2F3D1"
A.add_edge(lbo,COUNT)
e=A.get_edge(lbo,COUNT); COUNT+=1
e.attr["label"]=lmc

mc=obs.parity
lmc=u"paridade"
G(mc,rdf.type,owl.DatatypeProperty)
G(mc,rdfs.label,L(lmc,lang="pt"))
G(mc,rdfs.range,xsd.boolean)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:boolean"
nd.attr['color']="#A2F3D1"
A.add_edge(lbo,COUNT)
e=A.get_edge(lbo,COUNT); COUNT+=1
e.attr["label"]=lmc

mc=obs.limitedMandate
lmc=u"limite de mandato"
G(mc,rdf.type,owl.DatatypeProperty)
G(mc,rdfs.label,L(lmc,lang="pt"))
G(mc,rdfs.range,xsd.boolean)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:boolean"
nd.attr['color']="#A2F3D1"
A.add_edge(lbo,COUNT)
e=A.get_edge(lbo,COUNT); COUNT+=1
e.attr["label"]=lmc

mc=obs.civilSocietySelectionMethod
lmc=u"método de escolha de membros da sociedade civil"
G(mc,rdf.type,owl.DatatypeProperty)
G(mc,rdfs.label,L(lmc,lang="pt"))
G(mc,rdfs.range,xsd.string)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:string"
nd.attr['color']="#A2F3D1"
A.add_edge(lbo,COUNT)
e=A.get_edge(lbo,COUNT); COUNT+=1
e.attr["label"]=lmc


mc=obs.presidencySelectionMethod
lmc=u"método de escolha da presidência" # SKO
G(mc,rdf.type,owl.DatatypeProperty)
G(mc,rdfs.label,L(lmc,lang="pt"))
G(mc,rdfs.range,xsd.string)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:string"
nd.attr['color']="#A2F3D1"
A.add_edge(lbo,COUNT)
e=A.get_edge(lbo,COUNT); COUNT+=1
e.attr["label"]=lmc

mc=obs.internalGovernanceBody
lmc=u"órgão interno de governança"
gb=obs.GovernanceBody
lgb=u"Órgão de governança"
G(mc,rdf.type,owl.ObjectProperty)
G(mc,rdfs.label,L(lmc,lang="pt"))
G(mc,rdfs.range,gb)
G(gb,rdf.type,owl.Class)
G(gb,rdfs.label,L(lgb,lang="pt"))

A.add_node(lgb,style="filled")
A.add_edge(lbo,lgb)
e=A.get_edge(lbo,lgb)
e.attr["label"]=lmc

# name, metodo

mc=obs.governanceBodySelectionMethod
lmc=u"método de seleção de membros do órgão de governança"
G(mc,rdf.type,owl.DatatypeProperty)
G(mc,rdfs.label,L(lmc,lang="pt"))
G(mc,rdfs.range,xsd.string)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:string"
nd.attr['color']="#A2F3D1"
A.add_edge(lgb,COUNT)
e=A.get_edge(lgb,COUNT); COUNT+=1
e.attr["label"]=lmc

A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:string"
nd.attr['color']="#A2F3D1"
A.add_edge(lgb,COUNT)
e=A.get_edge(lgb,COUNT); COUNT+=1
e.attr["label"]="nome"

#####

mc=obs.agendaPreparation
lmc=u"encarregado pela pauta"
G(mc,rdf.type,owl.DatatypeProperty)
G(mc,rdfs.label,L(lmc,lang="pt"))
G(mc,rdfs.range,xsd.string)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:string"
nd.attr['color']="#A2F3D1"
A.add_edge(lcons,COUNT)
e=A.get_edge(lcons,COUNT); COUNT+=1
e.attr["label"]=lmc

mc=obs.presidentialQualityVote
lmc=u"voto de qualidade do presidente"
G(mc,rdf.type,owl.DatatypeProperty)
G(mc,rdfs.label,L(lmc,lang="pt"))
G(mc,rdfs.range,xsd.boolean)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:boolean"
nd.attr['color']="#A2F3D1"
A.add_edge(lcons,COUNT)
e=A.get_edge(lcons,COUNT); COUNT+=1
e.attr["label"]=lmc

mc=obs.adReferendumDecisions
lmc=u"decisões ad referendum"
G(mc,rdf.type,owl.DatatypeProperty)
G(mc,rdfs.label,L(lmc,lang="pt"))
G(mc,rdfs.range,xsd.boolean)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:boolean"
nd.attr['color']="#A2F3D1"
A.add_edge(lcons,COUNT)
e=A.get_edge(lcons,COUNT); COUNT+=1
e.attr["label"]=lmc




nome=("../figs/obsConselho.png")
A.draw(nome,prog="dot") # draw to png using circo
nome=("../figs/obsConselho2.png")
A.draw(nome,prog="circo") # draw to png using circo
nome=("../figs/obsConselho3.png")
A.draw(nome,prog="fdp") # draw to png using circo
f=open("../rdf/obsConselho.owl","wb")
f.write(g.serialize())
f.close()
