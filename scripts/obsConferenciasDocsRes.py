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
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(conf,rdfs.subClassOf,pm)
A.add_node(lpm,style="filled")
A.add_edge(lconf,lpm)
e=A.get_edge(lconf,lpm)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

ta=obs.produces
lta=u"produz" # SKOS
th=obs.Result
lth=u"Resultado"
G(ta,rdf.type,owl.ObjectProperty)
G(ta,rdfs.label,L(lta,lang="pt"))
G(ta,rdfs.range,th)
G(th,rdf.type,owl.Class)
G(th,rdfs.label,L(lth,lang="pt"))
A.add_node(lth,style="filled")
A.add_edge(lconf,lth)
e=A.get_edge(lconf,lth)
e.attr["label"]=lta

pm=obs.Effect # SKOS
lpm=u"Efeito"
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(pm,rdfs.subClassOf,th)
A.add_node(lpm,style="filled")
A.add_edge(lpm,lth)
e=A.get_edge(lpm,lth)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2
pm_=pm
lpm_=lpm

pm=obs.PublicPolicyReshaping # SKOS
lpm=u"Remodelagem de política pública"
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(pm,rdfs.subClassOf,pm_)
A.add_node(lpm,style="filled")
A.add_edge(lpm,lpm_)
e=A.get_edge(lpm,lpm_)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

pm=obs.Evaluation # SKOS
lpm=u"Avaliação"
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(pm,rdfs.subClassOf,pm_)
A.add_node(lpm,style="filled")
A.add_edge(lpm,lpm_)
e=A.get_edge(lpm,lpm_)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

pm=obs.Articulation # SKOS
lpm=u"Articulação"
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(pm,rdfs.subClassOf,pm_)
A.add_node(lpm,style="filled")
A.add_edge(lpm,lpm_)
e=A.get_edge(lpm,lpm_)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

pm=obs.PoliticalSocialization# SKOS
lpm=u"Socialização política"
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(pm,rdfs.subClassOf,pm_)
A.add_node(lpm,style="filled")
A.add_edge(lpm,lpm_)
e=A.get_edge(lpm,lpm_)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2
pm__=pm
lpm__=lpm

pm=obs.ParticipantQualification # SKOS
lpm=u"Capacitação de participante"
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(pm,rdfs.subClassOf,pm__)
A.add_node(lpm,style="filled")
A.add_edge(lpm,lpm__)
e=A.get_edge(lpm,lpm__)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

pm=obs.ExternalSocietyQualification # SKOS
lpm=u"Capacitação de sociedade externa"
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(pm,rdfs.subClassOf,pm__)
A.add_node(lpm,style="filled")
A.add_edge(lpm,lpm__)
e=A.get_edge(lpm,lpm__)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

pm=obs.ProposalFormulation # SKOS
lpm=u"Formulação de proposta"
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(pm,rdfs.subClassOf,pm_)
A.add_node(lpm,style="filled")
A.add_edge(lpm,lpm_)
e=A.get_edge(lpm,lpm_)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

pm=obs.PublicAgencyIntegration # SKOS
lpm=u"Integração de órgãos públicos"
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(pm,rdfs.subClassOf,pm_)
A.add_node(lpm,style="filled")
A.add_edge(lpm,lpm_)
e=A.get_edge(lpm,lpm_)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

pm=obs.ParticipatoryCultureStrengthening# SKOS
lpm=u"Fortalecimento da cultura participativa"
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(pm,rdfs.subClassOf,pm_)
A.add_node(lpm,style="filled")
A.add_edge(lpm,lpm_)
e=A.get_edge(lpm,lpm_)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

pm=obs.NationalPlanMaturing # SKOS
lpm=u"Amadurecimento do plano nacional"
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(pm,rdfs.subClassOf,pm_)
A.add_node(lpm,style="filled")
A.add_edge(lpm,lpm_)
e=A.get_edge(lpm,lpm_)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

pm=obs.DocumentaryResult# SKOS
lpm=u"Resultado documental"
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(pm,rdfs.subClassOf,th)
A.add_node(lpm,style="filled")
A.add_edge(lpm,lth)
e=A.get_edge(lpm,lth)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2
pm_=pm
lpm_=lpm

pm=obs.Motion # SKOS
lpm=u"Moção"
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(pm,rdfs.subClassOf,pm_)
A.add_node(lpm,style="filled")
A.add_edge(lpm,lpm_)
e=A.get_edge(lpm,lpm_)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

pm=obs.Letter # SKOS
lpm=u"Carta"
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(pm,rdfs.subClassOf,pm_)
A.add_node(lpm,style="filled")
A.add_edge(lpm,lpm_)
e=A.get_edge(lpm,lpm_)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

pm=obs.Resolution # SKOS
lpm=u"Resolução"
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(pm,rdfs.subClassOf,pm_)
A.add_node(lpm,style="filled")
A.add_edge(lpm,lpm_)
e=A.get_edge(lpm,lpm_)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

pm=obs.NationalPlan# SKOS
lpm=u"Plano nacional"
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(pm,rdfs.subClassOf,pm_)
A.add_node(lpm,style="filled")
A.add_edge(lpm,lpm_)
e=A.get_edge(lpm,lpm_)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

pm=obs.FinalReport # SKOS
lpm=u"Relatório final"
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(pm,rdfs.subClassOf,pm_)
A.add_node(lpm,style="filled")
A.add_edge(lpm,lpm_)
e=A.get_edge(lpm,lpm_)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

ta=obs.composes
lta=u"compõe" # SKOS
th=obs.GeneralDescription
lth=u"Descrição geral"
G(ta,rdf.type,owl.ObjectProperty)
G(ta,rdfs.label,L(lta,lang="pt"))
G(th,rdf.type,owl.Class)
G(th,rdfs.label,L(lth,lang="pt"))
A.add_node(lth,style="filled")
A.add_edge(lth,lpm)
e=A.get_edge(lth,lpm)
e.attr["label"]=lta

lth=u"Carta"
A.add_edge(lth,lpm)
e=A.get_edge(lth,lpm)
e.attr["label"]=lta

lth=u"Resolução"
A.add_edge(lth,lpm)
e=A.get_edge(lth,lpm)
e.attr["label"]=lta

lth=u"Moção"
A.add_edge(lth,lpm)
e=A.get_edge(lth,lpm)
e.attr["label"]=lta





pm=obs.ProposalsNotebook # SKOS
lpm=u"Caderno de propostas"
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(pm,rdfs.subClassOf,pm_)
A.add_node(lpm,style="filled")
A.add_edge(lpm,lpm_)
e=A.get_edge(lpm,lpm_)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

ta=obs.has
lta=u"possui" # SKOS
th=obs.Document
lth=u"Documento"
G(ta,rdf.type,owl.ObjectProperty)
G(ta,rdfs.label,L(lta,lang="pt"))
G(ta,rdfs.range,th)
G(th,rdf.type,owl.Class)
G(th,rdfs.label,L(lth,lang="pt"))
A.add_node(lth,style="filled")
A.add_edge(lconf,lth)
e=A.get_edge(lconf,lth)
e.attr["label"]=lta

pm=obs.DocumentaryResult# SKOS
lpm=u"Resultado documental"

G(pm,rdfs.subClassOf,th)
A.add_edge(lpm,lth)
e=A.get_edge(lpm,lth)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2


pm=obs.Regiment # SKOS
lpm=u"Regimento"
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(pm,rdfs.subClassOf,th)
A.add_node(lpm,style="filled")
A.add_edge(lpm,lth)
e=A.get_edge(lpm,lth)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

pm=obs.Video # SKOS
lpm=u"Video"
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(pm,rdfs.subClassOf,th)
A.add_node(lpm,style="filled")
A.add_edge(lpm,lth)
e=A.get_edge(lpm,lth)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

pm=obs.Manual # SKOS
lpm=u"Manual"
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(pm,rdfs.subClassOf,th)
A.add_node(lpm,style="filled")
A.add_edge(lpm,lth)
e=A.get_edge(lpm,lth)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

pm=obs.Regulation # SKOS
lpm=u"Regulamento"
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(pm,rdfs.subClassOf,th)
A.add_node(lpm,style="filled")
A.add_edge(lpm,lth)
e=A.get_edge(lpm,lth)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

tafoo=obs.step
ltafoo=u"etapa" # SKOS
thfoo=obs.ConferenceStep
lthfoo=u"Etapa de conferência"
G(tafoo,rdf.type,owl.ObjectProperty)
G(tafoo,rdfs.label,L(ltafoo,lang="pt"))
G(thfoo,rdf.type,owl.Class)
G(thfoo,rdfs.label,L(lthfoo,lang="pt"))
G(tafoo,rdfs.range,thfoo)
A.add_node(lthfoo,style="filled")
A.add_edge(lpm,lthfoo)
e=A.get_edge(lpm,lthfoo)
e.attr["label"]=ltafoo



pm=obs.NormativeAct# SKOS
lpm=u"Ato normativo"
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(pm,rdfs.subClassOf,th)
A.add_node(lpm,style="filled")
A.add_edge(lpm,lth)
e=A.get_edge(lpm,lth)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

pm=obs.MonitoringReport # SKOS
lpm=u"Relatório de monitoramento"
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(pm,rdfs.subClassOf,th)
A.add_node(lpm,style="filled")
A.add_edge(lpm,lth)
e=A.get_edge(lpm,lth)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2


ta=obs.triggersElaboration
lta=u"provoca elaboração" # SKOS
G(ta,rdf.type,owl.ObjectProperty)
G(ta,rdfs.label,L(lta,lang="pt"))

lpm_=u"Ato normativo"


pm=obs.DialogueTextualBase# SKOS
lpm=u"Texto base para diálogo"
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(pm,rdfs.subClassOf,th)
A.add_node(lpm,style="filled")
A.add_edge(lpm,lth)
e=A.get_edge(lpm,lth)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

A.add_edge(lpm_,lpm)
e=A.get_edge(lpm_,lpm)
e.attr["label"]=lta

pm=obs.InvitationLetter # SKOS
lpm=u"Carta convite"
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(pm,rdfs.subClassOf,th)
A.add_node(lpm,style="filled")
A.add_edge(lpm,lth)
e=A.get_edge(lpm,lth)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2
A.add_edge(lpm_,lpm)
e=A.get_edge(lpm_,lpm)
e.attr["label"]=lta

ta=obs.sets
lta=u"estabelece" # SKOS
th=obs.Theme
lth=u"Tema"
G(ta,rdf.type,owl.ObjectProperty)
G(ta,rdfs.label,L(lta,lang="pt"))
G(ta,rdfs.range,th)
G(th,rdf.type,owl.Class)
G(th,rdfs.label,L(lth,lang="pt"))
A.add_node(lth,style="filled")
A.add_edge(lpm_,lth)
e=A.get_edge(lpm_,lth)
e.attr["label"]=lta

nm=obs.name
lnm=u"nome"
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



#nm=obs.thematicAxes
#lnm=u"eixos temáticos"
#G(nm,rdf.type,owl.DatatypeProperty)
#G(nm,rdfs.label,L(lnm,lang="pt"))
#G(nm,rdfs.range,xsd.string)
#A.add_node(COUNT,style="filled")
#nd=A.get_node(COUNT)
#nd.attr["label"]="xsd:string"
#nd.attr['color']="#A2F3D1"
#A.add_edge(lth,COUNT)
#e=A.get_edge(lth,COUNT); COUNT+=1
#e.attr["label"]=lnm

ta=obs.feeds
lta=u"alimenta" # SKOS
G(ta,rdf.type,owl.ObjectProperty)
G(ta,rdfs.label,L(lta,lang="pt"))
G(ta,rdfs.range,obs.Conference)

lpm=u"Relatório de monitoramento"
lpm_=u"Conferência"
A.add_edge(lpm,lpm_)
e=A.get_edge(lpm,lpm_)
e.attr["label"]=lta

nome=("../figs/obsConferenciaDocsRes.png")
A.draw(nome,prog="dot") # draw to png using circo
nome=("../figs/obsConferenciaDocsRes2.png")
A.draw(nome,prog="circo") # draw to png using circo
nome=("../figs/obsConferenciaDocsRes3.png")
A.draw(nome,prog="fdp") # draw to png using circo
A.write("../rdf/obsConferenciaDocsRes.dot")

f=open("../rdf/obsConferenciaDocsRes.owl","wb")
f.write(g.serialize())
f.close()
f=open("../rdf/obsConferenciaDocsRes.ttl","wb")
f.write(g.serialize(format="turtle"))
f.close()

