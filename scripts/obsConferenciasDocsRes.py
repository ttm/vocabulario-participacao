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
lpm=u"Regulação"
G(pm,rdf.type,owl.Class)
G(pm,rdfs.label,L(lpm,lang="pt"))
G(pm,rdfs.subClassOf,th)
A.add_node(lpm,style="filled")
A.add_edge(lpm,lth)
e=A.get_edge(lpm,lth)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

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


