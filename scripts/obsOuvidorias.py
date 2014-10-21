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

ouv=obs.OmbudsmanAgency # SKOS
louv =u"Ouvidoria"
A.add_node(louv,style="filled")
nd=A.get_node(louv)
nd.attr['color']="#A29999"

G(ouv,rdf.type,owl.Class)
G(ouv,rdfs.label,L(louv,lang="pt"))
G(ouv,rdfs.comment,L(u"Ouvidoria federal",lang="pt"))

ativa=obs.ativa
lativa=u"ativa"
G(ativa,rdf.type,owl.DatatypeProperty)
G(ativa,rdfs.label,L(lativa,lang="pt"))
G(ativa,rdfs.comment,L(u"ouvidoria é ativa?",lang="pt"))
G(ativa,rdfs.range,xsd.boolean)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:boolean"
nd.attr['color']="#A2F3D1"
A.add_edge(louv,COUNT)
e=A.get_edge(louv,COUNT); COUNT+=1
e.attr["label"]=lativa

responsavel=obs.accountable
lresponsavel=u"responsável" # SKOS
Ouvidor=obs.Ombudsman
lOuvidor=u"Ouvidor"
G(responsavel,rdf.type,owl.ObjectProperty)
G(responsavel,rdfs.label,L(lresponsavel,lang="pt"))
G(Ouvidor,rdf.type,owl.Class)
G(Ouvidor,rdfs.label,L(lOuvidor,lang="pt"))
G(responsavel,rdfs.range,Ouvidor)
A.add_node(lOuvidor,style="filled")
A.add_edge(louv,lOuvidor)
e=A.get_edge(louv,lOuvidor)
e.attr["label"]=lresponsavel

nome=obs.name
lnome=u"nome"
G(nome,rdf.type,owl.DatatypeProperty)
G(nome,rdfs.label,L(lnome,lang="pt"))
G(nome,rdfs.range,xsd.string)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:string"
nd.attr['color']="#A2F3D1"
A.add_edge(lOuvidor,COUNT)
e=A.get_edge(lOuvidor,COUNT); COUNT+=1
e.attr["label"]=lnome

local=obs.location
llocal=u"localização"
G(local,rdf.type,owl.DatatypeProperty)
G(local,rdfs.label,L(llocal,lang="pt"))
G(local,rdfs.comment,L(u"órgão e localização do ouvidor dentro do órgão em que trabalha",lang="pt"))
G(local,rdfs.range,xsd.string)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:string"
nd.attr['color']="#A2F3D1"
A.add_edge(lOuvidor,COUNT)
e=A.get_edge(lOuvidor,COUNT); COUNT+=1
e.attr["label"]=llocal

orgao=obs.agency
lorgao=u"órgão" # SKOS
OrgaoPub=obs.PublicAgency
lOrgaoPub=u"Órgão público"
G(orgao,rdf.type,owl.ObjectProperty)
G(orgao,rdfs.label,L(lorgao,lang="pt"))
G(OrgaoPub,rdf.type,owl.Class)
G(OrgaoPub,rdfs.label,L(lOrgaoPub,lang="pt"))
G(orgao,rdfs.range,OrgaoPub)
A.add_node(lOrgaoPub,style="filled")
A.add_edge(louv,lOrgaoPub)
e=A.get_edge(louv,lOrgaoPub)
e.attr["label"]=lorgao

sp=obs.PublicAdministrationAgency
lsp=u"Órgão da administração pública" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,OrgaoPub)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lOrgaoPub)
e=A.get_edge(lsp,lOrgaoPub)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2
lsp_=lsp

sp=obs.Hospital
lsp=u"Hospital" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,OrgaoPub)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lOrgaoPub)
e=A.get_edge(lsp,lOrgaoPub)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.Ministry
lsp=u"Ministério" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,obs.PublicAdministrationAgency)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp  ,lsp_)
e=A.get_edge(lsp,lsp_)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2




sp=obs.University
lsp=u"Universidade" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,OrgaoPub)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lOrgaoPub)
e=A.get_edge(lsp,lOrgaoPub)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2




sp=obs.IndirectPublicAdministrationAgency
lsp=u"Órgão da administração pública indireta" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,OrgaoPub)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lOrgaoPub)
e=A.get_edge(lsp,lOrgaoPub)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2
lsp__=lsp
sp__=sp

sp=obs.Foundation
lsp=u"Fundação" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,sp__)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp  ,lsp__)
e=A.get_edge(lsp,lsp__)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2




nome=("../figs/obsOuvidoria.png")
A.draw(nome,prog="dot") # draw to png using circo
nome=("../figs/obsOuvidoria2.png")
A.draw(nome,prog="circo") # draw to png using circo
nome=("../figs/obsOuvidoria3.png")
A.draw(nome,prog="fdp") # draw to png using circo
A.write("../rdf/obsOuvidoria.dot")

f=open("../rdf/obsOuvidoria.owl","wb")
f.write(g.serialize())
f.close()
f=open("../rdf/obsOuvidoria.ttl","wb")
f.write(g.serialize(format="turtle"))
f.close()

