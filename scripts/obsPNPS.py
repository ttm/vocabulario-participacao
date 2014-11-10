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

def C(uri,label,superclass=None,comment=None,color=None):
    G(uri,rdf.type,owl.Class)
    G(uri,rdfs.label,L(label,lang="pt"))
    A.add_node(label,style="filled")
    nd=A.get_node(label)
    if superclass:
        G(uri,rdfs.subClassOf,superclass)
        lsuperclass=[i for i in g.objects(superclass,rdfs.label)][0]
        A.add_edge(  label, lsuperclass)
        e=A.get_edge(label, lsuperclass)
        e.attr["arrowhead"]="empty"
        e.attr["arrowsize"]=2
    if comment:
        G(uri,rdfs.comment,L(comment,lang="pt"))
    if color:
        nd.attr['color']="#F29999"
    return nd
nd=C(obs.Decree8243,u"Decreto 8.243")
nd.attr['color']="#A29999"
C(obs.Theme,u"Tema")
C(obs.PNPS,u"Política Nacional de Participação Social (PNPS)")
C(obs.SNPS,u"Sistema Nacional de Participação Social (SNPS)")
C(obs.ParticipationInstanceOrMechanism,u"Instância ou mecanismo de participação social")
C(obs.ParticipationMechanism,u"Mecanismo de participação social",obs.ParticipationInstanceOrMechanism) # SKOS
C(obs.ParticipationInstance,u"Instância de participação social",obs.ParticipationInstanceOrMechanism) # SKOS
C(obs.Directive,u"Diretriz")
C(obs.Objective,u"Objetivo")
C(obs.PublicManagement,u"Gestão pública")
C(obs.PublicPolicy,u"Política pública")
C(obs.GovernmentProgram,u"Programa governamental")
C(obs.PublicService,u"Serviço público")
C(obs.Formulation,u"Formulação")
C(obs.Execution,u"Execução")
C(obs.Monitoring,u"Monitoramento",False,u"usado também como sinônimo de acompanhamento")
C(obs.Evaluation,u"Avaliação")
C(obs.Improvement,u"Aprimoramento")
C(obs.Improvement,u"Debate")
C(obs.Improvement,u"Negociação")
C(obs.CivilSociety,u"Sociedade civil")
C(obs.Collective,u"Coletivo",obs.CivilSociety)
C(obs.Citizen,u"Cidadão",obs.CivilSociety)
C(obs.InstitutedSocialMovement,u"Movimento social instituído",obs.CivilSociety)
C(obs.NotOrganizedSocialMovement,u"Movimento social não organizado",obs.CivilSociety)
C(obs.Network,u"Rede",obs.CivilSociety)
C(obs.SocialOrganization,u"Organização social",obs.CivilSociety)
C(obs.NormativeAct,u"Ato normativo")
C(obs.Dialogue,u"Diálogo")
C(obs.SocialParticipation,u"Participação social")
C(obs.SocialControl,u"Controle social")
C(obs.DecisionMakingProcess,u"Processo decisório")
C(obs.PolicyManagement,u"Gestão de política")
nd=C(obs.Commission,u"Comissão",obs.ParticipationInstance)
nd.attr['color']="#F29999"
nd=C(obs.Council,u"Conselho",obs.ParticipationInstance)
nd.attr['color']="#F29999"
C(obs.Government,u"Governo")
nd=C(obs.Conference,u"Conferência",obs.ParticipationInstance)
nd.attr['color']="#F29999"
nd=C(obs.OmbudsmanAgency,u"Ouvidoria",obs.ParticipationInstance)
nd.attr['color']="#F29999"

nd=C(obs.DialogueTable, u"Mesa de diálogo",obs.ParticipationMechanism)
nd.attr['color']="#F29999"

nd=C(obs.InterCouncilForum,u"Fórum interconselhos",obs.ParticipationMechanism)
nd.attr['color']="#F29999"

nd=C(obs.PublicAudience,u"Audiência pública",obs.ParticipationMechanism)
nd.attr['color']="#F29999"

nd=C(obs.PublicConsultation,u"Consulta pública",obs.ParticipationMechanism,color="#F29999")

C(obs.ManagementBody,u"Corpo gestor")
C(obs.DirectlyInvolvedBody,u"Corpo diretamente envolvido",obs.ManagementBody)
C(obs.Participant,u"Participante")
C(obs.InterestedPerson,u"Pessoa interessada",obs.Participant)
C(obs.CouncilRepresentant,u"Representante de conselho",obs.Participant)
C(obs.CommissionRepresentant,u"Representante de comissão",obs.Participant)
C(obs.GovernmentRepresentant,u"Representante do governo",obs.Participant)
C(obs.CivilSocietyRepresentant,u"Representante da sociedade civil",obs.Participant)
C(obs.ConferenceStep,u"Etapa de conferência")
C(obs.StateConference,u"Conferência estadual",obs.ConferenceStep)
C(obs.RegionalConference,u"Conferência regional",obs.ConferenceStep)
C(obs.DistrictConference,u"Conferência distrital",obs.ConferenceStep)
C(obs.MunicipalConference,u"Conferência municipal",obs.ConferenceStep)
C(obs.IndividualCitizenCommunication,u"Comunicação individual de cidadãos")
C(obs.Complaint,u"Reclamação",obs.IndividualCitizenCommunication)
C(obs.Request,u"Solicitação",obs.IndividualCitizenCommunication)
C(obs.Compliment,u"Elogio",obs.IndividualCitizenCommunication)
C(obs.Suggestion,u"Sugestão",obs.IndividualCitizenCommunication)
C(obs.Denunciation,u"Denúncia",obs.IndividualCitizenCommunication)
C(obs.SocialConflict,u"Conflito social")
C(obs.Recommendation,u"Recomendação")
C(obs.Intersectoriality,u"Intersetorialidade")
C(obs.Transversality,u"Transversalidade")
C(obs.Presential,u"Presencial")
C(obs.Consultative,u"Consultiva")
C(obs.GovernmentDecisionSubsidizing,u"Subsídio para decisão governamental")
C(obs.WrittenContribution,u"Contribuição escrita")
C(obs.ConvocationAct,u"Ato de convocação",obs.NormativeAct)
C(obs.Topic,u"Assunto",comment=u"assunto é mais específico que tema")
def P(uri,label):
    G(uri,rdf.type,owl.ObjectProperty)
    G(uri,rdfs.label,L(label,lang="pt"))
P(obs.considers,u"considera")
P(obs.establishes,u"institui")
P(obs.articulates,u"articula")
P(obs.strengthens,u"fortalece")
P(obs.orientation,u"orientação")
P(obs.reflects,u"reflete")
P(obs.activity,u"atividade")
P(obs.promotes,u"promove")
P(obs.purpose,u"propósito")
P(obs.thematic,u"temática")
P(obs.nature,u"natureza")
P(obs.part,u"parte")
P(obs.about,u"sobre")
P(obs.composition,u"composição")
P(obs.member,u"membro")
P(obs.step,u"etapa")
P(obs.proposes,u"propõe")
P(obs.responsability,u"responsabilidade")
P(obs.bond,u"vínculo")
P(obs.handles,u"trata")
P(obs.prevents,u"previne")
P(obs.solves,u"soluciona")
P(obs.mediates,u"media")
P(obs.scope,u"escopo")
P(obs.formulates,u"formula")
P(obs.oralManifestation,u"manifestação oral")
P(obs.receives,u"recebe")
P(obs.form,u"forma")
P(obs.source,u"fonte")
def D(uri,label,dtype):
    G(uri,rdf.type,owl.DatatypeProperty)
    G(uri,rdfs.label,L(label,lang="pt"))
    G(uri,rdfs.range,dtype)
D(obs.continuity,u"continuidade",xsd.boolean)
D(obs.specificObject,u"objetivo específico",xsd.string)
D(obs.operationPeriod,u"período de funcionamento",xsd.duration)
D(obs.startDate,u"início",xsd.dateTime)
D(obs.periodicity,u"periodicidade",xsd.gYear)
D(obs.publicInterest,u"interesse público",xsd.boolean)
D(obs.Deadline,u"prazo",xsd.dateTime)
D(obs.description,u"descrição",xsd.string)
def L(olabel,llabel,dlabel):
    # origin, link, destination
    A.add_edge(  olabel,dlabel)
    e=A.get_edge(olabel,dlabel)
    e.attr["label"]=llabel
def LD(olabel,llabel,dlabel):
    global COUNT
    A.add_node(COUNT,style="filled")
    nd=A.get_node(COUNT)
    nd.attr["label"]=dlabel
    nd.attr['color']="#A2F3D1"
    A.add_edge(  olabel,COUNT)
    e=A.get_edge(olabel,COUNT); COUNT+=1
    e.attr["label"]=llabel

L(u"Decreto 8.243",u"institui",u"Política Nacional de Participação Social (PNPS)")
L(u"Decreto 8.243",u"institui",u"Sistema Nacional de Participação Social (SNPS)")
L(u"Política Nacional de Participação Social (PNPS)",u"fortalece",u"Instância ou mecanismo de participação social")
L(u"Política Nacional de Participação Social (PNPS)",u"articula",u"Instância ou mecanismo de participação social")
L(u"Sistema Nacional de Participação Social (SNPS)",u"fortalece",u"Instância ou mecanismo de participação social")
L(u"Sistema Nacional de Participação Social (SNPS)",u"articula",u"Instância ou mecanismo de participação social")
L(u"Decreto 8.243",u"orientação",u"Diretriz")
L(u"Decreto 8.243",u"orientação",u"Objetivo")


L(u"Política pública",u"atividade",u"Formulação")
L(u"Política pública",u"atividade",u"Execução")
L(u"Política pública",u"atividade",u"Monitoramento")
L(u"Política pública",u"atividade",u"Avaliação")
L(u"Programa governamental",u"atividade",u"Formulação")
L(u"Programa governamental",u"atividade",u"Execução")
L(u"Programa governamental",u"atividade",u"Monitoramento")
L(u"Programa governamental",u"atividade",u"Avaliação")
L
L(u"Formulação"   ,u"reflete",u"Objetivo")
L(u"Execução"     ,u"reflete",u"Objetivo")
L(u"Monitoramento",u"reflete",u"Objetivo")
L(u"Avaliação"    ,u"reflete",u"Objetivo")
L(u"Formulação"   ,u"reflete",u"Diretriz")
L(u"Execução"     ,u"reflete",u"Diretriz")
L(u"Monitoramento",u"reflete",u"Diretriz")
L(u"Avaliação"    ,u"reflete",u"Diretriz")
L
L(u"Gestão pública",u"atividade",u"Aprimoramento")
L(u"Aprimoramento"    ,u"reflete",u"Diretriz")
L(u"Aprimoramento"    ,u"reflete",u"Objetivo")

L(u"Decreto 8.243",u"considera",u"Sociedade civil")
L(u"Decreto 8.243",u"considera",u"Conselho")
L(u"Decreto 8.243",u"considera",u"Comissão")

L(u"Ato normativo",u"institui",u"Conselho")
L(u"Ato normativo",u"institui",u"Comissão")

L(u"Conselho",u"promove",u"Participação social")
L(u"Participação social",u"para",u"Processo decisório")
L(u"Participação social",u"para",u"Gestão de política")
L(u"Conselho",u"temática",u"Tema")
LD(u"Conselho",u"continuidade",u"True")
L(u"Conselho",u"natureza",u"Diálogo")
L(u"Diálogo",u"parte",u"Sociedade civil")
L(u"Diálogo",u"parte",u"Governo")
LD(u"Diálogo",u"objetivo específico",u"xsd:string")

L(u"Comissão",u"natureza",u"Diálogo")
LD(u"Comissão",u"período de funcionamento",u"xsd:duration")
LD(u"Comissão",u"início",u"xsd:dateTime")

# Conferências
L(u"Decreto 8.243",u"considera",u"Conferência")
LD(u"Conferência",u"periodicidade",u"xsd:gYear")
L(u"Conferência",u"natureza",u"Formulação")
L(u"Conferência",u"natureza",u"Avaliação")
L(u"Formulação",u"sobre",u"Tema")
L(u"Avaliação" ,u"sobre",u"Tema")
LD(u"Tema",u"interesse público",u"xsd:boolean") # na conferência essa boleana é verdadeira
L(u"Conferência",u"composição",u"Corpo gestor")
L(u"Corpo gestor",u"member",u"Representante do governo")
L(u"Corpo gestor",u"member",u"Representante da sociedade civil")
L(u"Conferência",u"etapa",u"Etapa de conferência")
L(u"Etapa de conferência",u"propõe",u"Diretriz")

# Ouvidorias
L(u"Decreto 8.243",u"considera",u"Ouvidoria")
L(u"Ouvidoria",u"natureza",u"Participação social")
L(u"Ouvidoria",u"natureza",u"Controle social")
L(u"Ouvidoria",u"trata",u"Comunicação individual de cidadãos")
L(u"Comunicação individual de cidadãos",u"propósito",u"Aprimoramento")
L(u"Comunicação individual de cidadãos",u"vínculo",  u"Política pública")
L(u"Comunicação individual de cidadãos",u"vínculo",  u"Serviço público")

# Mesa de diálogo
L(u"Decreto 8.243",u"considera",u"Mesa de diálogo")
L(u"Mesa de diálogo",u"natureza",u"Negociação")
L(u"Mesa de diálogo",u"natureza",u"Debate")
L(u"Mesa de diálogo",u"composição",u"Corpo diretamente envolvido")
L(u"Mesa de diálogo",u"previne",u"Conflito social")
L(u"Mesa de diálogo",u"media",u"Conflito social")
L(u"Mesa de diálogo",u"soluciona",u"Conflito social")

# criar as classes e propriedades automaticamente
# aceitar vários subjects, properties e objects

# Mesa de diálogo
L(u"Decreto 8.243",u"considera",u"Fórum interconselhos")
L(u"Fórum interconselhos",u"natureza",u"Debate")
L(u"Fórum interconselhos",u"membro",u"Representante de conselho")
L(u"Fórum interconselhos",u"membro",u"Representante de comissão")
L(u"Fórum interconselhos",u"propósito",u"Monitoramento")
L(u"Monitoramento",u"escopo",u"Política pública")
L(u"Monitoramento",u"escopo",u"Programa governamental")
L(u"Fórum interconselhos",u"formula",u"Recomendação")
L(u"Recomendação",u"propósito",u"Aprimoramento")
L(u"Aprimoramento",u"escopo",u"Intersetorialidade")
L(u"Aprimoramento",u"escopo",u"Transversalidade")

# Audiência pública
L(u"Decreto 8.243",u"considera",u"Audiência pública")
L(u"Audiência pública",u"natureza",u"Presencial")
L(u"Audiência pública",u"natureza",u"Consultiva")
L(u"Audiência pública",u"manifestação oral",u"Participante")
L(u"Audiência pública",u"propósito",u"Subsídio para decisão governamental")

# Consulta pública
L(u"Decreto 8.243",u"considera",u"Consulta pública")
L(u"Consulta pública",u"natureza",u"Consultiva")
LD(u"Consulta pública",u"prazo",u"xsd:dateTime")
L(u"Consulta pública",u"recebe",u"Contribuição escrita")
L(u"Contribuição escrita",u"forma",u"Ato de convocação")
L(u"Contribuição escrita",u"fonte",u"Sociedade civil")
L(u"Consulta pública",u"membro",u"Pessoa interessada")
L(u"Consulta pública",u"sobre",u"Assunto")
LD(u"Assunto",u"descrição",u"xsd:string")


nome=("../figs/obsPNPS.png")
A.draw(nome,prog="dot") # draw to png using circo
nome=("../figs/obsPNPS2.png")
A.draw(nome,prog="circo") # draw to png using circo
nome=("../figs/obsPNPS3.png")
A.draw(nome,prog="fdp") # draw to png using circo
f=open("../rdf/obsPNPS.owl","wb")
f.write(g.serialize())
f.close()
f=open("../rdf/obsPNPS.ttl","wb")
f.write(g.serialize(format="turtle"))
f.close()
