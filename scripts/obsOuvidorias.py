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

nome=obs.telephone
lnome=u"telefone"
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

A.add_edge(u"Ouvidor",lOrgaoPub)
e=A.get_edge(u"Ouvidor",lOrgaoPub)
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


sj=obs.shouldJoin
lsj=u"integrará" # SKOS
Ou=obs.OmbudsmanNationalSystem
lOu=u"Sistema Federal de Ouvidorias"
G(sj,rdf.type,owl.ObjectProperty)
G(sj,rdfs.label,L(lsj,lang="pt"))
G(Ou,rdf.type,owl.Class)
G(Ou,rdfs.label,L(lOu,lang="pt"))
G(sj,rdfs.range,Ou)
A.add_node(lOu,style="filled")
A.add_edge(louv,lOu)
e=A.get_edge(louv,lOu)
e.attr["label"]=lsj

sp=obs.SAC
lsp=u"SAC (Sistema de Atendimento ao Cidadão)" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(ouv,rdfs.subClassOf,sp)
A.add_node(lsp,style="filled") ###
A.add_edge(louv,lsp)
e=A.get_edge(louv,lsp)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sj=obs.articulates
lsj=u"articula" # SKOS
Ou=obs.OGU
lOu=u"OGU (Ouvidoria Geral da União)"
G(sj,rdf.type,owl.ObjectProperty)
G(sj,rdfs.label,L(lsj,lang="pt"))
G(Ou,rdf.type,owl.Class)
G(Ou,rdfs.label,L(lOu,lang="pt"))
G(sj,rdfs.range,ouv)
A.add_node(lOu,style="filled")
A.add_edge(lOu,louv)
e=A.get_edge(lOu,louv)
e.attr["label"]=lsj


sj=obs.delivers
lsj=u"entrega" # SKOS
Ou=obs.Report
lOu=u"Relatório"
G(sj,rdf.type,owl.ObjectProperty)
G(sj,rdfs.label,L(lsj,lang="pt"))
G(Ou,rdf.type,owl.Class)
G(Ou,rdfs.label,L(lOu,lang="pt"))
G(sj,rdfs.range,ouv)
A.add_node(lOu,style="filled")
A.add_edge(louv,lOu)
e=A.get_edge(louv,lOu)
e.attr["label"]=lsj
lOu_=lOu


nm=obs.periodicity
lnm=u"peridodicidade"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.range,xsd.integer)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:integer"
nd.attr['color']="#A2F3D1"
A.add_edge(  lOu,COUNT)
e=A.get_edge(lOu,COUNT); COUNT+=1
e.attr["label"]=lnm


sj=obs.guides
lsj=u"orienta" # SKOS
Ou=obs.Control
lOu=u"Controle"
G(sj,rdf.type,owl.ObjectProperty)
G(sj,rdfs.label,L(lsj,lang="pt"))
G(Ou,rdf.type,owl.Class)
G(Ou,rdfs.label,L(lOu,lang="pt"))
G(sj,rdfs.range,ouv)
A.add_node(lOu,style="filled")
A.add_edge(lOu_,lOu)
e=A.get_edge(lOu_,lOu)
e.attr["label"]=lsj

sp=obs.InternalControl
lsp=u"Controle interno" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,Ou)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lOu)
e=A.get_edge(lsp,lOu)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2


sp=obs.ExternalControl
lsp=u"Controle externo" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,Ou)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lOu)
e=A.get_edge(lsp,lOu)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sj=obs.dialogues
lsj=u"dialoga" # SKOS
pm__=obs.ParticipationInstanceOrMechanism # SKOS
lpm__=u"Instância ou mecanismo de participação social"
G(sj,rdf.type,owl.ObjectProperty)
G(sj,rdfs.label,L(lsj,lang="pt"))
G(sj,rdfs.range,pm__)
G(pm__,rdf.type,owl.Class)
G(pm__,rdfs.label,L(lpm__,lang="pt"))
A.add_node(lpm__,style="filled")
A.add_edge(louv,lpm__)
e=A.get_edge(louv,lpm__)
e.attr["label"]=lsj

sj=obs.incorporates
lsj=u"incorpora" # SKOS
pm__=obs.LAI# SKOS
lpm__=u"LAI (Lei de Acesso à Informação)" # SKOS
G(sj,rdf.type,owl.ObjectProperty)
G(sj,rdfs.label,L(lsj,lang="pt"))
G(sj,rdfs.range,pm__)
G(pm__,rdf.type,owl.Class)
G(pm__,rdfs.label,L(lpm__,lang="pt"))
A.add_node(lpm__,style="filled")
A.add_edge(louv,lpm__)
e=A.get_edge(louv,lpm__)
e.attr["label"]=lsj


sj=obs.receives
lsj=u"recebe" # SKOS
pm__=obs.Manifestation # SKOS
lpm__=u"Manifestação" # SKOS
G(sj,rdf.type,owl.ObjectProperty)
G(sj,rdfs.label,L(lsj,lang="pt"))
G(sj,rdfs.range,pm__)
G(pm__,rdf.type,owl.Class)
G(pm__,rdfs.label,L(lpm__,lang="pt"))
A.add_node(lpm__,style="filled")
A.add_edge(louv,lpm__)
e=A.get_edge(louv,lpm__)
e.attr["label"]=lsj

sp=obs.Request
lsp=u"Solicitação" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,pm__)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lpm__)
e=A.get_edge(lsp,lpm__)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.Complaint
lsp=u"Reclamação" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,pm__)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lpm__)
e=A.get_edge(lsp,lpm__)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.Compliment
lsp=u"Elogio" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,pm__)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lpm__)
e=A.get_edge(lsp,lpm__)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.Suggestion
lsp=u"Sugestão" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,pm__)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lpm__)
e=A.get_edge(lsp,lpm__)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.Denunciation
lsp=u"Denúncia" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,pm__)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lpm__)
e=A.get_edge(lsp,lpm__)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

nm=obs.identityReservation
lnm=u"reserva de identidade"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.range,xsd.boolean)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:boolean"
nd.attr['color']="#A2F3D1"
A.add_edge(  lpm__,COUNT)
e=A.get_edge(lpm__,COUNT); COUNT+=1
e.attr["label"]=lnm

nm=obs.anonymous
lnm=u"anônima"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.range,xsd.boolean)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:boolean"
nd.attr['color']="#A2F3D1"
A.add_edge(  lpm__,COUNT)
e=A.get_edge(lpm__,COUNT); COUNT+=1
e.attr["label"]=lnm

# 
sj=obs.qualifies
lsj=u"qualifica" # SKOS
Ou=obs.FormationActivity
lOu=u"Atividade de formação"
G(sj,rdf.type,owl.ObjectProperty)
G(sj,rdfs.label,L(lsj,lang="pt"))
G(Ou,rdf.type,owl.Class)
G(Ou,rdfs.label,L(lOu,lang="pt"))
G(sj,rdfs.domain,Ou)
A.add_node(lOu,style="filled")
A.add_edge(lOu,louv)
e=A.get_edge(lOu,louv)
e.attr["label"]=lsj

sp=obs.Lecture
lsp=u"Palestra" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,Ou)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp  ,lOu)
e=A.get_edge(lsp,lOu)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.Course
lsp=u"Curso" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,Ou)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp  ,lOu)
e=A.get_edge(lsp,lOu)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.Seminar
lsp=u"Seminário" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,Ou)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp  ,lOu)
e=A.get_edge(lsp,lOu)
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

