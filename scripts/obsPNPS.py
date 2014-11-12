#-*- coding: utf-8 -*-
import rdflib as r, pygraphviz as gv
def G(g,S,P,O):
    g.add((S,P,O))
L=r.Literal
COUNT=1

obs = r.Namespace("http://purl.org/socialparticipation/obs/")
rdf = r.namespace.RDF
rdfs = r.namespace.RDFS
owl = r.namespace.OWL
xsd = r.namespace.XSD

ags={"geral":(r.Graph(),gv.AGraph(directed=True,strict=False)),
     "preliminar":(r.Graph(),gv.AGraph(directed=True,strict=False)),
     "conselho":(r.Graph(),gv.AGraph(directed=True,strict=False)),
     "conferencia":(r.Graph(),gv.AGraph(directed=True,strict=False)),
     "comissao":(r.Graph(),gv.AGraph(directed=True,strict=False)),
     "ouvidoria":(r.Graph(),gv.AGraph(directed=True,strict=False)),
     "mesa":(r.Graph(),gv.AGraph(directed=True,strict=False)),
     "audiencia":(r.Graph(),gv.AGraph(directed=True,strict=False)),
     "consulta":(r.Graph(),gv.AGraph(directed=True,strict=False)),
     "ambientev":(r.Graph(),gv.AGraph(directed=True,strict=False)),
     "mesam":(r.Graph(),gv.AGraph(directed=True,strict=False))}

agsL=ags.keys()
for l in agsL:
    g=ags[l][0]
    A=ags[l][1]
    A.graph_attr["label"]="Decreto 8.243 (PNPS) - %s"%(l,)
    g.namespace_manager.bind("obs", "http://purl.org/socialparticipation/obs/")    
    g.namespace_manager.bind("rdf", r.namespace.RDF)    
    g.namespace_manager.bind("rdfs", r.namespace.RDFS)    
    g.namespace_manager.bind("xsd", r.namespace.XSD)    
    g.namespace_manager.bind("owl", r.namespace.OWL)    

def C(ag=[ags["geral"]],uri="foo",label="bar",superclass=None,comment=None,color=None):
    for gg in ag:
        g,A=gg
        G(g,uri,rdf.type,owl.Class)
        G(g,uri,rdfs.label,L(label,lang="pt"))
        A.add_node(label,style="filled")
        nd=A.get_node(label)
        if superclass:
            G(g,uri,rdfs.subClassOf,superclass)
            lsuperclass=[i for i in g.objects(superclass,rdfs.label)][0]
            A.add_edge(  label, lsuperclass)
            e=A.get_edge(label, lsuperclass)
            e.attr["arrowhead"]="empty"
            e.attr["arrowsize"]=2
        if comment:
            G(g,uri,rdfs.comment,L(comment,lang="pt"))
        if color:
            nd.attr['color']=color

C([ags["geral"],ags["preliminar"]],obs.Decree8243,u"Decreto 8.243",color="#A29999")
C([ags["geral"],ags["preliminar"]],obs.Theme,u"Tema")
C([ags["geral"],ags["preliminar"]],obs.PNPS,u"Política Nacional de Participação Social (PNPS)")
C([ags["geral"],ags["preliminar"]],obs.SNPS,u"Sistema Nacional de Participação Social (SNPS)")
C([ags["geral"],ags["preliminar"]],obs.ParticipationInstanceOrMechanism,u"Instância ou mecanismo de participação social")
C([ags["geral"],ags["preliminar"]],obs.ParticipationMechanism,u"Mecanismo de participação social",obs.ParticipationInstanceOrMechanism) # SKOS
C([ags["geral"],ags["preliminar"]],obs.ParticipationInstance,u"Instância de participação social",obs.ParticipationInstanceOrMechanism) # SKOS
C([ags["geral"],ags["preliminar"]],obs.Directive,u"Diretriz")
C([ags["geral"],ags["preliminar"]],obs.Objective,u"Objetivo")
C([ags["geral"],ags["preliminar"]],obs.PublicManagement,u"Gestão pública")
C([ags["geral"],ags["preliminar"]],obs.PublicPolicy,u"Política pública")
C([ags["geral"],ags["preliminar"]],obs.GovernmentProgram,u"Programa governamental")
C([ags["geral"]],obs.PublicService,u"Serviço público")
C([ags["geral"],ags["preliminar"]],obs.Formulation,u"Formulação")
C([ags["geral"],ags["preliminar"]],obs.Execution,u"Execução")
C([ags["geral"],ags["preliminar"]],obs.Monitoring,u"Monitoramento",False,u"usado também como sinônimo de acompanhamento")
C([ags["geral"],ags["preliminar"]],obs.Evaluation,u"Avaliação")
C([ags["geral"],ags["preliminar"]],obs.Improvement,u"Aprimoramento")
C([ags["geral"]],obs.Improvement,u"Debate")
C([ags["geral"]],obs.Improvement,u"Negociação")
C([ags["geral"],ags["preliminar"]],obs.CivilSociety,u"Sociedade civil")
C([ags["geral"],ags["preliminar"]],obs.Collective,u"Coletivo",obs.CivilSociety)
C([ags["geral"],ags["preliminar"]],obs.Citizen,u"Cidadão",obs.CivilSociety)
C([ags["geral"],ags["preliminar"]],obs.InstitutedSocialMovement,u"Movimento social instituído",obs.CivilSociety)
C([ags["geral"],ags["preliminar"]],obs.NotOrganizedSocialMovement,u"Movimento social não organizado",obs.CivilSociety)
C([ags["geral"],ags["preliminar"]],obs.Network,u"Rede",obs.CivilSociety)
C([ags["geral"],ags["preliminar"]],obs.SocialOrganization,u"Organização social",obs.CivilSociety)
C([ags["geral"],ags["preliminar"]],obs.NormativeAct,u"Ato normativo")
C([ags["geral"],ags["preliminar"]],obs.Dialogue,u"Diálogo")
C([ags["geral"],ags["preliminar"]],obs.SocialParticipation,u"Participação social")
C([ags["geral"]],obs.SocialControl,u"Controle social")
C([ags["geral"],ags["preliminar"]],obs.DecisionMakingProcess,u"Processo decisório")
C([ags["geral"],ags["preliminar"]],obs.PolicyManagement,u"Gestão de política")
C([ags["geral"],ags["preliminar"]],obs.Commission,u"Comissão",obs.ParticipationInstance,color="#F29999")
C([ags["geral"],ags["preliminar"]],obs.Council,u"Conselho",obs.ParticipationInstance,color="#F29999")
C([ags["geral"],ags["preliminar"]],obs.Government,u"Governo")
C([ags["geral"],ags["preliminar"]],obs.Conference,u"Conferência",obs.ParticipationInstance,color="#F29999")
C([ags["geral"],ags["preliminar"]],obs.OmbudsmanAgency,u"Ouvidoria",obs.ParticipationInstance,color="#F29999")
C([ags["geral"],ags["preliminar"]],obs.DialogueTable, u"Mesa de diálogo",obs.ParticipationMechanism,color="#F29999")
C([ags["geral"],ags["preliminar"]],obs.InterCouncilForum,u"Fórum interconselhos",obs.ParticipationMechanism,color="#F29999")
C([ags["geral"],ags["preliminar"]],obs.PublicAudience,u"Audiência pública",obs.ParticipationMechanism,color="#F29999")

C([ags["geral"],ags["preliminar"]],obs.PublicConsultation,u"Consulta pública",obs.ParticipationMechanism,color="#F29999")
C([ags["geral"],ags["preliminar"]],obs.SocialParticipationVirtualEnvironment,u"Ambiente virtual de participação social",obs.ParticipationMechanism,color="#F29999")

C([ags["geral"]],obs.ManagementBody,u"Corpo gestor")
C([ags["geral"]],obs.DirectlyInvolvedBody,u"Corpo diretamente envolvido",obs.ManagementBody)
C([ags["geral"]],obs.Participant,u"Participante")
C([ags["geral"]],obs.InterestedPerson,u"Pessoa interessada",obs.Participant)
C([ags["geral"]],obs.CouncilRepresentant,u"Representante de conselho",obs.Participant)
C([ags["geral"]],obs.CommissionRepresentant,u"Representante de comissão",obs.Participant)
C([ags["geral"]],obs.GovernmentRepresentant,u"Representante do governo",obs.Participant)
C([ags["geral"]],obs.CivilSocietyRepresentant,u"Representante da sociedade civil",obs.Participant)
C([ags["geral"]],obs.ConferenceStep,u"Etapa de conferência")
C([ags["geral"]],obs.StateConference,u"Conferência estadual",obs.ConferenceStep)
C([ags["geral"]],obs.RegionalConference,u"Conferência regional",obs.ConferenceStep)
C([ags["geral"]],obs.DistrictConference,u"Conferência distrital",obs.ConferenceStep)
C([ags["geral"]],obs.MunicipalConference,u"Conferência municipal",obs.ConferenceStep)
C([ags["geral"]],obs.IndividualCitizenCommunication,u"Comunicação individual de cidadãos")
C([ags["geral"]],obs.Complaint,u"Reclamação",obs.IndividualCitizenCommunication)
C([ags["geral"]],obs.Request,u"Solicitação",obs.IndividualCitizenCommunication)
C([ags["geral"]],obs.Compliment,u"Elogio",obs.IndividualCitizenCommunication)
C([ags["geral"]],obs.Suggestion,u"Sugestão",obs.IndividualCitizenCommunication)
C([ags["geral"]],obs.Denunciation,u"Denúncia",obs.IndividualCitizenCommunication)
C([ags["geral"]],obs.SocialConflict,u"Conflito social")
C([ags["geral"]],obs.Recommendation,u"Recomendação")
C([ags["geral"]],obs.Intersectoriality,u"Intersetorialidade")
C([ags["geral"]],obs.Transversality,u"Transversalidade")
C([ags["geral"]],obs.Presential,u"Presencial")
C([ags["geral"]],obs.Consultative,u"Consultiva")
C([ags["geral"]],obs.GovernmentDecisionSubsidizing,u"Subsídio para decisão governamental")
C([ags["geral"]],obs.WrittenContribution,u"Contribuição escrita")
C([ags["geral"]],obs.ConvocationAct,u"Ato de convocação",obs.NormativeAct)
C([ags["geral"]],obs.Topic,u"Assunto",comment=u"assunto é mais específico que tema")
C([ags["geral"]],obs.ICT,u"TIC",comment=u"Tecnologias de Informação e Comunicação")
C([ags["geral"]],obs.Internet,u"Internet",obs.ICT)
C([ags["geral"]],obs.FederalPublicAdministration,u"Administração pública federal")
def P(ag=[ags["geral"]],uri="foo",label="bar"):
    for gg in ag:
        g=gg[0]
        G(g,uri,rdf.type,owl.ObjectProperty)
        G(g,uri,rdfs.label,L(label,lang="pt"))
P([ags["geral"]],obs.considers,u"considera")
P([ags["geral"]],obs.establishes,u"institui")
P([ags["geral"]],obs.articulates,u"articula")
P([ags["geral"]],obs.strengthens,u"fortalece")
P([ags["geral"]],obs.orientation,u"orientação")
P([ags["geral"]],obs.reflects,u"reflete")
P([ags["geral"]],obs.activity,u"atividade")
P([ags["geral"]],obs.promotes,u"promove")
P([ags["geral"]],obs.purpose,u"propósito")
P([ags["geral"]],obs.thematic,u"temática")
P([ags["geral"]],obs.nature,u"natureza")
P([ags["geral"]],obs.part,u"parte")
P([ags["geral"]],obs.about,u"sobre")
P([ags["geral"]],obs.composition,u"composição")
P([ags["geral"]],obs.member,u"membro")
P([ags["geral"]],obs.step,u"etapa")
P([ags["geral"]],obs.proposes,u"propõe")
P([ags["geral"]],obs.responsability,u"responsabilidade")
P([ags["geral"]],obs.bond,u"vínculo")
P([ags["geral"]],obs.handles,u"trata")
P([ags["geral"]],obs.prevents,u"previne")
P([ags["geral"]],obs.solves,u"soluciona")
P([ags["geral"]],obs.mediates,u"media")
P([ags["geral"]],obs.scope,u"escopo")
P([ags["geral"]],obs.formulates,u"formula")
P([ags["geral"]],obs.oralManifestation,u"manifestação oral")
P([ags["geral"]],obs.receives,u"recebe")
P([ags["geral"]],obs.form,u"forma")
P([ags["geral"]],obs.source,u"fonte")
P([ags["geral"]],obs.uses,u"utiliza")
P([ags["geral"]],obs.emphasis,u"ênfase")
def D(ag=[ags["geral"]],uri="foo",label="bar",dtype="baz"):
    for gg in ag:
        g=gg[0]
        G(g,uri,rdf.type,owl.DatatypeProperty)
        G(g,uri,rdfs.label,L(label,lang="pt"))
        G(g,uri,rdfs.range,dtype)
D([ags["geral"]],obs.continuity,u"continuidade",xsd.boolean)
D([ags["geral"]],obs.specificObject,u"objetivo específico",xsd.string)
D([ags["geral"]],obs.operationPeriod,u"período de funcionamento",xsd.duration)
D([ags["geral"]],obs.startDate,u"início",xsd.dateTime)
D([ags["geral"]],obs.periodicity,u"periodicidade",xsd.gYear)
D([ags["geral"]],obs.publicInterest,u"interesse público",xsd.boolean)
D([ags["geral"]],obs.Deadline,u"prazo",xsd.dateTime)
D([ags["geral"]],obs.description,u"descrição",xsd.string)
def L(ag=[ags["geral"]],olabel="foo",llabel="bar",dlabel="baz"):
    # origin, link, destination
    for gg in ag:
        A=gg[1]
        A.add_edge(  olabel,dlabel)
        e=A.get_edge(olabel,dlabel)
        e.attr["label"]=llabel
def LD(ag=[ags["geral"]],olabel="foo",llabel="bar",dlabel="baz"):
    global COUNT
    for gg in ag:
        A=gg[1]
        A.add_node(COUNT,style="filled")
        nd=A.get_node(COUNT)
        nd.attr["label"]=dlabel
        nd.attr['color']="#A2F3D1"
        A.add_edge(  olabel,COUNT)
        e=A.get_edge(olabel,COUNT); COUNT+=1
        e.attr["label"]=llabel

L([ags["geral"],ags["preliminar"]],u"Decreto 8.243",u"institui",u"Política Nacional de Participação Social (PNPS)")
L([ags["geral"],ags["preliminar"]],u"Decreto 8.243",u"institui",u"Sistema Nacional de Participação Social (SNPS)")
L([ags["geral"],ags["preliminar"]],u"Política Nacional de Participação Social (PNPS)",u"fortalece",u"Instância ou mecanismo de participação social")
L([ags["geral"],ags["preliminar"]],u"Política Nacional de Participação Social (PNPS)",u"articula",u"Instância ou mecanismo de participação social")
L([ags["geral"],ags["preliminar"]],u"Sistema Nacional de Participação Social (SNPS)",u"fortalece",u"Instância ou mecanismo de participação social")
L([ags["geral"],ags["preliminar"]],u"Sistema Nacional de Participação Social (SNPS)",u"articula",u"Instância ou mecanismo de participação social")
L([ags["geral"],ags["preliminar"]],u"Decreto 8.243",u"orientação",u"Diretriz")
L([ags["geral"],ags["preliminar"]],u"Decreto 8.243",u"orientação",u"Objetivo")


L([ags["geral"],ags["preliminar"]],u"Política pública",u"atividade",u"Formulação")
L([ags["geral"],ags["preliminar"]],u"Política pública",u"atividade",u"Execução")
L([ags["geral"],ags["preliminar"]],u"Política pública",u"atividade",u"Monitoramento")
L([ags["geral"],ags["preliminar"]],u"Política pública",u"atividade",u"Avaliação")
L([ags["geral"],ags["preliminar"]],u"Programa governamental",u"atividade",u"Formulação")
L([ags["geral"],ags["preliminar"]],u"Programa governamental",u"atividade",u"Execução")
L([ags["geral"],ags["preliminar"]],u"Programa governamental",u"atividade",u"Monitoramento")
L([ags["geral"],ags["preliminar"]],u"Programa governamental",u"atividade",u"Avaliação")
L
L([ags["geral"],ags["preliminar"]],u"Formulação"   ,u"reflete",u"Objetivo")
L([ags["geral"],ags["preliminar"]],u"Execução"     ,u"reflete",u"Objetivo")
L([ags["geral"],ags["preliminar"]],u"Monitoramento",u"reflete",u"Objetivo")
L([ags["geral"],ags["preliminar"]],u"Avaliação"    ,u"reflete",u"Objetivo")
L([ags["geral"],ags["preliminar"]],u"Formulação"   ,u"reflete",u"Diretriz")
L([ags["geral"],ags["preliminar"]],u"Execução"     ,u"reflete",u"Diretriz")
L([ags["geral"],ags["preliminar"]],u"Monitoramento",u"reflete",u"Diretriz")
L([ags["geral"],ags["preliminar"]],u"Avaliação"    ,u"reflete",u"Diretriz")
L
L([ags["geral"],ags["preliminar"]],u"Gestão pública",u"atividade",u"Aprimoramento")
L([ags["geral"],ags["preliminar"]],u"Aprimoramento"    ,u"reflete",u"Diretriz")
L([ags["geral"],ags["preliminar"]],u"Aprimoramento"    ,u"reflete",u"Objetivo")

L([ags["geral"],ags["preliminar"]],u"Decreto 8.243",u"considera",u"Sociedade civil")
L([ags["geral"],ags["preliminar"]],u"Decreto 8.243",u"considera",u"Conselho")
L([ags["geral"],ags["preliminar"]],u"Decreto 8.243",u"considera",u"Comissão")

L([ags["geral"],ags["preliminar"]],u"Ato normativo",u"institui",u"Conselho")
L([ags["geral"],ags["preliminar"]],u"Ato normativo",u"institui",u"Comissão")

L([ags["geral"],ags["preliminar"]],u"Conselho",u"promove",u"Participação social")
L([ags["geral"],ags["preliminar"]],u"Participação social",u"para",u"Processo decisório")
L([ags["geral"],ags["preliminar"]],u"Participação social",u"para",u"Gestão de política")
L([ags["geral"],ags["preliminar"]],u"Conselho",u"temática",u"Tema")
LD([ags["geral"],ags["preliminar"]],u"Conselho",u"continuidade",u"True")
L([ags["geral"],ags["preliminar"]],u"Conselho",u"natureza",u"Diálogo")
L( [ags["geral"],ags["preliminar"]],u"Diálogo",u"parte",u"Sociedade civil")
L( [ags["geral"],ags["preliminar"]],u"Diálogo",u"parte",u"Governo")
LD([ags["geral"],ags["preliminar"]],u"Diálogo",u"objetivo específico",u"xsd:string")

L( [ags["geral"],ags["preliminar"]],u"Comissão",u"natureza",u"Diálogo")
LD([ags["geral"],ags["preliminar"]],u"Comissão",u"período de funcionamento",u"xsd:duration")
LD([ags["geral"],ags["preliminar"]],u"Comissão",u"início",u"xsd:dateTime")

# Conferências
L( [ags["geral"]],u"Decreto 8.243",u"considera",u"Conferência")
LD([ags["geral"]],u"Conferência",u"periodicidade",u"xsd:gYear")
L([ags["geral"]],u"Conferência",u"natureza",u"Formulação")
L([ags["geral"]],u"Conferência",u"natureza",u"Avaliação")
L([ags["geral"]],u"Formulação",u"sobre",u"Tema")
L([ags["geral"]],u"Avaliação" ,u"sobre",u"Tema")
LD([ags["geral"]],u"Tema",u"interesse público",u"xsd:boolean") # na conferência essa boleana é verdadeira
L([ags["geral"]],u"Conferência",u"composição",u"Corpo gestor")
L([ags["geral"]],u"Corpo gestor",u"member",u"Representante do governo")
L([ags["geral"]],u"Corpo gestor",u"member",u"Representante da sociedade civil")
L([ags["geral"]],u"Conferência",u"etapa",u"Etapa de conferência")
L([ags["geral"]],u"Etapa de conferência",u"propõe",u"Diretriz")

# Ouvidorias
L([ags["geral"]],u"Decreto 8.243",u"considera",u"Ouvidoria")
L([ags["geral"]],u"Ouvidoria",u"natureza",u"Participação social")
L([ags["geral"]],u"Ouvidoria",u"natureza",u"Controle social")
L([ags["geral"]],u"Ouvidoria",u"trata",u"Comunicação individual de cidadãos")
L([ags["geral"]],u"Comunicação individual de cidadãos",u"propósito",u"Aprimoramento")
L([ags["geral"]],u"Comunicação individual de cidadãos",u"vínculo",  u"Política pública")
L([ags["geral"]],u"Comunicação individual de cidadãos",u"vínculo",  u"Serviço público")

# Mesa de diálogo
L([ags["geral"]],u"Decreto 8.243",u"considera",u"Mesa de diálogo")
L([ags["geral"]],u"Mesa de diálogo",u"natureza",u"Negociação")
L([ags["geral"]],u"Mesa de diálogo",u"natureza",u"Debate")
L([ags["geral"]],u"Mesa de diálogo",u"composição",u"Corpo diretamente envolvido")
L([ags["geral"]],u"Mesa de diálogo",u"previne",u"Conflito social")
L([ags["geral"]],u"Mesa de diálogo",u"media",u"Conflito social")
L([ags["geral"]],u"Mesa de diálogo",u"soluciona",u"Conflito social")

# criar as classes e propriedades automaticamente
# aceitar vários subjects, properties e objects

# Mesa de diálogo
L([ags["geral"]],u"Decreto 8.243",u"considera",u"Fórum interconselhos")
L([ags["geral"]],u"Fórum interconselhos",u"natureza",u"Debate")
L([ags["geral"]],u"Fórum interconselhos",u"membro",u"Representante de conselho")
L([ags["geral"]],u"Fórum interconselhos",u"membro",u"Representante de comissão")
L([ags["geral"]],u"Fórum interconselhos",u"propósito",u"Monitoramento")
L([ags["geral"]],u"Monitoramento",u"escopo",u"Política pública")
L([ags["geral"]],u"Monitoramento",u"escopo",u"Programa governamental")
L([ags["geral"]],u"Fórum interconselhos",u"formula",u"Recomendação")
L([ags["geral"]],u"Recomendação",u"propósito",u"Aprimoramento")
L([ags["geral"]],u"Aprimoramento",u"escopo",u"Intersetorialidade")
L([ags["geral"]],u"Aprimoramento",u"escopo",u"Transversalidade")

# Audiência pública
L([ags["geral"]],u"Decreto 8.243",u"considera",u"Audiência pública")
L([ags["geral"]],u"Audiência pública",u"natureza",u"Presencial")
L([ags["geral"]],u"Audiência pública",u"natureza",u"Consultiva")
L([ags["geral"]],u"Audiência pública",u"manifestação oral",u"Participante")
L([ags["geral"]],u"Audiência pública",u"propósito",u"Subsídio para decisão governamental")

# Consulta pública
L([ags["geral"]],u"Decreto 8.243",u"considera",u"Consulta pública")
L([ags["geral"]],u"Consulta pública",u"natureza",u"Consultiva")
LD([ags["geral"]],u"Consulta pública",u"prazo",u"xsd:dateTime")
L([ags["geral"]],u"Consulta pública",u"recebe",u"Contribuição escrita")
L([ags["geral"]],u"Contribuição escrita",u"forma",u"Ato de convocação")
L([ags["geral"]],u"Contribuição escrita",u"fonte",u"Sociedade civil")
L([ags["geral"]],u"Consulta pública",u"membro",u"Pessoa interessada")
L([ags["geral"]],u"Consulta pública",u"sobre",u"Assunto")
LD([ags["geral"]],u"Assunto",u"descrição",u"xsd:string")

# Ambiete virtual
L([ags["geral"]],u"Decreto 8.243",u"considera",u"Ambiente virtual de participação social")
L([ags["geral"]],u"Ambiente virtual de participação social",u"utiliza",u"TIC")
L([ags["geral"]],u"Ambiente virtual de participação social",u"ênfase",u"Internet")
L([ags["geral"]],u"Ambiente virtual de participação social",u"promove",u"Diálogo")
L([ags["geral"]],u"Diálogo",u"parte",u"Sociedade civil")
L([ags["geral"]],u"Diálogo",u"parte",u"Administração pública federal")


A=ags["geral"][1]
nome=("../figs/obsPNPS.png")
A.draw(nome,prog="dot") # draw to png using circo
nome=("../figs/obsPNPS2.png")
A.draw(nome,prog="circo") # draw to png using circo
nome=("../figs/obsPNPS3.png")
A.draw(nome,prog="fdp") # draw to png using circo
g=ags["geral"][0]
f=open("../rdf/obsPNPS.owl","wb")
f.write(g.serialize())
f.close()
f=open("../rdf/obsPNPS.ttl","wb")
f.write(g.serialize(format="turtle"))
f.close()




A=ags["preliminar"][1]
g=ags["preliminar"][0]
nome_="preliminar"
nome=("../figs/obsPNPS_%s.png"%(nome_,))
A.draw(nome,prog="dot") # draw to png using circo
nome=("../figs/obsPNPS_%s2.png"%(nome_,))
A.draw(nome,prog="circo") # draw to png using circo
nome=("../figs/obsPNPS_%s3.png"%(nome_,))
A.draw(nome,prog="fdp") # draw to png using circo
f=open("../rdf/obsPNPS_%s.owl"%(nome_,),"wb")
f.write(g.serialize())
f.close()
f=open("../rdf/obsPNPS_%s.ttl"%(nome_,),"wb")
f.write(g.serialize(format="turtle"))
f.close()


