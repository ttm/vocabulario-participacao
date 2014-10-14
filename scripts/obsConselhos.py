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

###########
ca=obs.creationAct
lca=u"ato de criação"
ac=obs.Act
lac=u"Ato" # Talvez colocar no SKOS Ato Participativo ou Ato Institucional

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
ta=obs.thematicArea
lta=u"área temática"
th=obs.Theme
lth=u"Tema"
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
lsp=u"Políticas sociais"
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
lsp=u"Desenvolvimento econômico"
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
lsp=u"Garantia de direitos"
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
lsp=u"Infraestrutura"
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
lsp=u"Recursos naturais"
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
lde=u"Instância deliberativa"
co=obs.AdvisoryInstance
lco=u"Instância consultiva"

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





nome=("../figs/obsConselho.png")
A.draw(nome,prog="dot") # draw to png using circo
f=open("../rdf/obsConselho.owl","wb")
f.write(g.serialize())
f.close()
