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

G(conf,rdf.type,owl.Class)
G(conf,rdfs.label,L(lconf,lang="pt"))
G(conf,rdfs.comment,L(u"Conferências são processos nacionais de promoção do diálogo entre governo e sociedade",lang="pt"))

pm=obs.ParticipationMechanism # SKOS
lpm=u"Mecanismo ou instância de participação social"
A.add_node(lpm,style="filled")

G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(conf,rdfs.subClassOf,pm)
A.add_edge(lconf,lpm)
e=A.get_edge(lconf,lpm)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

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
th=obs.publicAgency
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
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,th)
A.add_node(lsp,style="filled") ###
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

sp=obs.Commission
lsp=u"Comissão" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,th)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lth)
e=A.get_edge(lsp,lth)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.Forum
lsp=u"Fórum" # entra no SKOS
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
lca=u"Convocação"
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










#####
nome=("../figs/obsConferencia.png")
A.draw(nome,prog="dot") # draw to png using circo
nome=("../figs/obsConferencia2.png")
A.draw(nome,prog="circo") # draw to png using circo
nome=("../figs/obsConferencia3.png")
A.draw(nome,prog="fdp") # draw to png using circo

f=open("../rdf/obsConferencia.owl","wb")
f.write(g.serialize())
f.close()
f=open("../rdf/obsConferencia.ttl","wb")
f.write(g.serialize(format="turtle"))
f.close()
