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
     "forumInterconselhos":(r.Graph(),gv.AGraph(directed=True,strict=False)),
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
    l_=l
    if l=="mesa":
        l_="mesa de dialogo"
    if l=="forumInterconselhos":
        l_=u"forum interconselhos"
    if l=="ambientev":
        l_=u"ambiente virtual"
    A.graph_attr["label"]=u"Decreto 8.243 (PNPS) - %s"%(l_,)
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

C([ags[i] for i in ("geral","preliminar","conferencia","ouvidoria","mesa","forumInterconselhos","audiencia","consulta","ambientev","conselho","comissao")],obs.Decree8243,u"Decreto 8.243",color="#A29999")
C([ags[i] for i in ("geral","conferencia","conselho","comissao")],obs.Theme,u"Tema")
C([ags[i] for i in ("geral","preliminar")],obs.PNPS,u"Política Nacional de Participação Social (PNPS)")
C([ags["geral"],ags["preliminar"]],obs.SNPS,u"Sistema Nacional de Participação Social (SNPS)")
C([ags[i] for i in ("geral","preliminar","conferencia","ouvidoria","mesa","forumInterconselhos","audiencia","consulta","ambientev","conselho","comissao")],obs.ParticipationInstanceOrMechanism,u"Instância ou mecanismo de participação social")
C([ags[i] for i in ("geral","preliminar","mesa","forumInterconselhos","audiencia","consulta","ambientev")],obs.ParticipationMechanism,u"Mecanismo de participação social",obs.ParticipationInstanceOrMechanism) # SKOS
C([ags[i] for i in ("geral","preliminar","conferencia","ouvidoria","conselho","comissao")],obs.ParticipationInstance,u"Instância de participação social",obs.ParticipationInstanceOrMechanism) # SKOS
C([ags[i] for i in ("geral","preliminar","conferencia")],obs.Directive,u"Diretriz")
C([ags[i] for i in ("geral","preliminar","comissao")],obs.Objective,u"Objetivo")
C([ags["geral"],ags["preliminar"]],obs.PublicManagement,u"Gestão pública")
C([ags[i] for i in ("geral","preliminar","ouvidoria","forumInterconselhos")],obs.PublicPolicy,u"Política pública")
C([ags[i] for i in ("geral","preliminar","forumInterconselhos")],obs.GovernmentProgram,u"Programa governamental")
C([ags[i] for i in ("geral","ouvidoria")],obs.PublicService,u"Serviço público")
C([ags[i] for i in ("geral","preliminar","conferencia","forumInterconselhos")],obs.Formulation,u"Formulação")
C([ags["geral"],ags["preliminar"]],obs.Execution,u"Execução")
C([ags[i] for i in ("geral","preliminar","forumInterconselhos")],obs.Monitoring,u"Monitoramento",False,u"usado também como sinônimo de acompanhamento")
C([ags[i] for i in ("geral","preliminar","conferencia")],obs.Evaluation,u"Avaliação")
C([ags[i] for i in ("geral","preliminar","ouvidoria","forumInterconselhos")],obs.Improvement,u"Aprimoramento")
C([ags[i] for i in ("geral","mesa","forumInterconselhos")],obs.Debate,u"Debate")
C([ags[i] for i in ("geral","mesa")],obs.Negotiation,u"Negociação")
C([ags[i] for i in ("geral","preliminar","consulta","ambientev","conselho")],obs.CivilSociety,u"Sociedade civil")
C([ags["geral"],ags["preliminar"]],obs.Collective,u"Coletivo",obs.CivilSociety)
C([ags["geral"],ags["preliminar"]],obs.Citizen,u"Cidadão",obs.CivilSociety)
C([ags["geral"],ags["preliminar"]],obs.InstitutedSocialMovement,u"Movimento social instituído",obs.CivilSociety)
C([ags["geral"],ags["preliminar"]],obs.NotOrganizedSocialMovement,u"Movimento social não organizado",obs.CivilSociety)
C([ags["geral"],ags["preliminar"]],obs.Network,u"Rede",obs.CivilSociety)
C([ags["geral"],ags["preliminar"]],obs.SocialOrganization,u"Organização social",obs.CivilSociety)
C([ags[i] for i in ("geral","preliminar","consulta","conselho","comissao")],obs.NormativeAct,u"Ato normativo")
C([ags[i] for i in ("geral","ambientev","conselho","comissao")],obs.Dialogue,u"Diálogo")
C([ags[i] for i in ("geral","ouvidoria","conselho")],obs.SocialParticipation,u"Participação social")
C([ags[i] for i in ("geral","ouvidoria")],obs.SocialControl,u"Controle social")
C([ags[i] for i in ("geral","conselho")],obs.DecisionMakingProcess,u"Processo decisório")
C([ags[i] for i in ("geral","conselho")],obs.PolicyManagement,u"Gestão de política")
C([ags[i] for i in ("geral","preliminar","comissao")],obs.Commission,u"Comissão",obs.ParticipationInstance,color="#F29999")
C([ags[i] for i in ("geral","preliminar","conselho")],obs.Council,u"Conselho",obs.ParticipationInstance,color="#F29999")
C([ags[i] for i in ("geral","conselho")],obs.Government,u"Governo")
C([ags[i] for i in ("geral","preliminar","conferencia","conselho")],obs.Conference,u"Conferência",obs.ParticipationInstance,color="#F29999")
C([ags[i] for i in ("geral","preliminar","ouvidoria")],obs.OmbudsmanAgency,u"Ouvidoria",obs.ParticipationInstance,color="#F29999")
C([ags[i] for i in ("geral","preliminar","mesa")],obs.DialogueTable, u"Mesa de diálogo",obs.ParticipationMechanism,color="#F29999")
C([ags[i] for i in ("geral","preliminar","forumInterconselhos")],obs.InterCouncilForum,u"Fórum interconselhos",obs.ParticipationMechanism,color="#F29999")
C([ags[i] for i in ("geral","preliminar","audiencia")],obs.PublicAudience,u"Audiência pública",obs.ParticipationMechanism,color="#F29999")

C([ags[i] for i in ("geral","preliminar","consulta")],obs.PublicConsultation,u"Consulta pública",obs.ParticipationMechanism,color="#F29999")
C([ags[i] for i in ("geral","preliminar","ambientev")],obs.SocialParticipationVirtualEnvironment,u"Ambiente virtual de participação social",obs.ParticipationMechanism,color="#F29999")

C([ags[i] for i in ("geral","conferencia")],obs.ManagementBody,u"Corpo gestor")
C([ags[i] for i in ("geral","conferencia","mesa","forumInterconselhos","audiencia","consulta","conselho")],obs.Participant,u"Participante")
C([ags[i] for i in ("geral","conselho")],obs.UnpaidParticipant,u"Participante não remunerado",obs.Participant)
C([ags[i] for i in ("geral","mesa")],obs.DirectlyInvolvedParticipant,u"Participante diretamente envolvido",obs.Participant)
C([ags[i] for i in ("geral","consulta")],obs.InterestedPerson,u"Pessoa interessada",obs.Participant)
C([ags[i] for i in ("geral","forumInterconselhos")],obs.CouncilRepresentant,u"Representante de conselho",obs.Participant)
C([ags[i] for i in ("geral","forumInterconselhos")],obs.CommissionRepresentant,u"Representante de comissão",obs.Participant)
C([ags[i] for i in ("geral","conferencia")],obs.GovernmentRepresentant,u"Representante do governo",obs.Participant)
C([ags[i] for i in ("geral","conferencia")],obs.CivilSocietyRepresentant,u"Representante da sociedade civil",obs.Participant)
C([ags[i] for i in ("geral","conferencia")],obs.ConferenceStep,u"Etapa de conferência")
C([ags[i] for i in ("geral","conferencia")],obs.StateConference,u"Conferência estadual",obs.ConferenceStep)
C([ags[i] for i in ("geral","conferencia")],obs.RegionalConference,u"Conferência regional",obs.ConferenceStep)
C([ags[i] for i in ("geral","conferencia")],obs.DistrictConference,u"Conferência distrital",obs.ConferenceStep)
C([ags[i] for i in ("geral","conferencia")],obs.MunicipalConference,u"Conferência municipal",obs.ConferenceStep)
C([ags[i] for i in ("geral","ouvidoria")],obs.IndividualCitizenCommunication,u"Comunicação individual de cidadãos")
C([ags["geral"]],obs.Complaint,u"Reclamação",obs.IndividualCitizenCommunication)
C([ags["geral"]],obs.Request,u"Solicitação",obs.IndividualCitizenCommunication)
C([ags["geral"]],obs.Compliment,u"Elogio",obs.IndividualCitizenCommunication)
C([ags["geral"]],obs.Suggestion,u"Sugestão",obs.IndividualCitizenCommunication)
C([ags["geral"]],obs.Denunciation,u"Denúncia",obs.IndividualCitizenCommunication)
C([ags[i] for i in ("geral","mesa")],obs.SocialConflict,u"Conflito social")
C([ags[i] for i in ("geral","forumInterconselhos")],obs.Recommendation,u"Recomendação")
C([ags[i] for i in ("geral","forumInterconselhos")],obs.Intersectoriality,u"Intersetorialidade")
C([ags[i] for i in ("geral","forumInterconselhos")],obs.Transversality,u"Transversalidade")
C([ags[i] for i in ("geral","audiencia")],obs.Presential,u"Presencial")
C([ags[i] for i in ("geral","audiencia","consulta")],obs.Consultative,u"Consultiva")
C([ags[i] for i in ("geral","audiencia")],obs.GovernmentDecisionSubsidizing,u"Subsídio para decisão governamental")
C([ags[i] for i in ("geral","consulta")],obs.WrittenContribution,u"Contribuição escrita")
C([ags[i] for i in ("geral","consulta")],obs.ConvocationAct,u"Ato de convocação",obs.NormativeAct)
C([ags[i] for i in ("geral","consulta")],obs.Topic,u"Assunto",comment=u"assunto é mais específico que tema")
C([ags[i] for i in ("geral","ambientev")],obs.ICT,u"TIC",comment=u"Tecnologias de Informação e Comunicação")
C([ags[i] for i in ("geral","ambientev")],obs.Internet,u"Internet",obs.ICT)
C([ags[i] for i in ("geral","ambientev")],obs.FederalPublicAdministration,u"Administração pública federal")
C([ags[i] for i in ("geral","conselho")],obs.PerformedActivity,u"Atividade desempenhada")
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
P([ags["geral"]],obs.trait,u"traço")
P([ags["geral"]],obs.trait,u"traço")
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
P([ags["geral"]],obs.tracks,u"acompanha")
P([ags["geral"]],obs.integrates,u"integra")
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
D([ags["geral"],ags["conselho"]],obs.nature,u"natureza",xsd.string)
D([ags["geral"],ags["conselho"]],obs.assignment,u"atribuição",xsd.string)
D([ags["geral"],ags["conselho"]],obs.competence,u"competência",xsd.string)
D([ags["geral"],ags["comissao"]],obs.memberChoiceCriteria,u"critério de escolha de membros",xsd.string)
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


L([ags[i] for i in ("geral","preliminar","forumInterconselhos")],u"Política pública",u"atividade",u"Formulação")
L([ags["geral"],ags["preliminar"]],u"Política pública",u"atividade",u"Execução")
L([ags["geral"],ags["preliminar"]],u"Política pública",u"atividade",u"Monitoramento")
L([ags["geral"],ags["preliminar"]],u"Política pública",u"atividade",u"Avaliação")
L([ags[i] for i in ("geral","preliminar","forumInterconselhos")],u"Programa governamental",u"atividade",u"Formulação")
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

L([ags[i] for i in ("geral","preliminar","ambientev")],u"Decreto 8.243",u"considera",u"Sociedade civil")

# Conselho
L([ags["geral"], ags["conselho"]],u"Decreto 8.243",u"considera",u"Conselho")
L([ags["geral"],ags["preliminar"],ags["conselho"]],u"Ato normativo",u"institui",u"Conselho")
L([ags["geral"], ags["conselho"]],u"Conselho",u"promove",u"Participação social")
L([ags["geral"], ags["conselho"]],u"Participação social",u"para",u"Processo decisório")
L([ags["geral"], ags["conselho"]],u"Participação social",u"para",u"Gestão de política")
L([ags["geral"], ags["conselho"]],u"Conselho",u"temática",u"Tema")
LD([ags["geral"],ags["conselho"]],u"Conselho",u"continuidade",u"True")
L([ags["geral"], ags["conselho"]],u"Conselho",u"traço",u"Diálogo")
L( [ags["geral"],ags["conselho"]],u"Diálogo",u"parte",u"Sociedade civil")
L( [ags["geral"],ags["conselho"]],u"Diálogo",u"parte",u"Governo")
LD([ags["geral"],ags["conselho"]],u"Diálogo",u"objetivo específico",u"xsd:string")
LD([ags["geral"],ags["conselho"]],u"Conselho",u"natureza",u"xsd:string")
LD([ags["geral"],ags["conselho"]],u"Conselho",u"atribuição",u"xsd:string")
LD([ags["geral"],ags["conselho"]],u"Conselho",u"competência",u"xsd:string")

L([ags["geral"], ags["conselho"]],u"Conselho",u"acompanha",u"Conferência")
L([ags["geral"], ags["conselho"]],u"Conselho",u"membro",u"Participante não remunerado")
L([ags["geral"], ags["conselho"]],u"Conselho",u"publica",u"Atividade desempenhada")


# Comissão
L([ags["geral"],ags["comissao"]],u"Decreto 8.243",u"considera",u"Comissão")
L([ags["geral"],ags["preliminar"],ags["comissao"]],u"Ato normativo",u"institui",u"Comissão")
L( [ags["geral"],ags["comissao"]],u"Comissão",u"traço",u"Diálogo")
LD([ags["geral"],ags["comissao"]],u"Comissão",u"período de funcionamento",u"xsd:duration")
LD([ags["geral"],ags["comissao"]],u"Comissão",u"início",u"xsd:dateTime")
LD([ags["geral"],ags["comissao"]],u"Comissão",u"prazo",u"xsd:dateTime")
L([ags["geral"], ags["comissao"]],u"Comissão",u"publica",u"Atividade desempenhada")
L([ags["geral"], ags["comissao"]],u"Comissao",u"temática",u"Tema")
L([ags["geral"],ags["comissao"]],u"Comissao" ,u"reflete",u"Objetivo")
L([ags["geral"],ags["comissao"]],u"Comissao" ,u"critério de escolha de membros",u"xsd:string")

# Conferências
L( [ags["geral"],ags["conferencia"]],u"Decreto 8.243",u"considera",u"Conferência")
LD([ags["geral"],ags["conferencia"]],u"Conferência",u"periodicidade",u"xsd:gYear")
L( [ags["geral"],ags["conferencia"]],u"Conferência",u"traço",u"Formulação")
L( [ags["geral"],ags["conferencia"]],u"Conferência",u"traço",u"Avaliação")
L( [ags["geral"],ags["conferencia"]],u"Formulação",u"sobre",u"Tema")
L( [ags["geral"],ags["conferencia"]],u"Avaliação" ,u"sobre",u"Tema")
LD([ags["geral"],ags["conferencia"]],u"Tema",u"interesse público",u"xsd:boolean") # na conferência essa boleana é verdadeira
L( [ags["geral"],ags["conferencia"]],u"Conferência",u"composição",u"Corpo gestor")
L( [ags["geral"],ags["conferencia"]],u"Corpo gestor",u"membro",u"Representante do governo")
L( [ags["geral"],ags["conferencia"]],u"Corpo gestor",u"membro",u"Representante da sociedade civil")
L( [ags["geral"],ags["conferencia"]],u"Conferência",u"integra",u"Etapa de conferência")
L( [ags["geral"],ags["conferencia"]],u"Etapa de conferência",u"propõe",u"Diretriz")
L([ags["geral"], ags["conferencia"]],u"Conferência",u"publica",u"Atividade desempenhada")

#  Ouvidorias
L( [ags["geral"],ags["ouvidoria"]],u"Decreto 8.243",u"considera",u"Ouvidoria")
L( [ags["geral"],ags["ouvidoria"]],u"Ouvidoria",u"traço",u"Participação social")
L( [ags["geral"],ags["ouvidoria"]],u"Ouvidoria",u"traço",u"Controle social")
L( [ags["geral"],ags["ouvidoria"]],u"Ouvidoria",u"trata",u"Comunicação individual de cidadãos")
L( [ags["geral"],ags["ouvidoria"]],u"Comunicação individual de cidadãos",u"propósito",u"Aprimoramento")
L( [ags["geral"],ags["ouvidoria"]],u"Comunicação individual de cidadãos",u"vínculo",  u"Política pública")
L( [ags["geral"],ags["ouvidoria"]],u"Comunicação individual de cidadãos",u"vínculo",  u"Serviço público")

# Mesa de diálogo
L([ags["geral"],ags["mesa"]],u"Decreto 8.243",u"considera",u"Mesa de diálogo")
L([ags["geral"],ags["mesa"]],u"Mesa de diálogo",u"traço",u"Negociação")
L([ags["geral"],ags["mesa"]],u"Mesa de diálogo",u"traço",u"Debate")
L([ags["geral"],ags["mesa"]],u"Mesa de diálogo",u"membro",u"Participante diretamente envolvido")
L([ags["geral"],ags["mesa"]],u"Mesa de diálogo",u"previne",u"Conflito social")
L([ags["geral"],ags["mesa"]],u"Mesa de diálogo",u"media",u"Conflito social")
L([ags["geral"],ags["mesa"]],u"Mesa de diálogo",u"soluciona",u"Conflito social")

# criar as classes e propriedades automaticamente
# aceitar vários subjects, properties e objects

# Fórum interconselhos
L([ags["geral"],ags["forumInterconselhos"]],u"Decreto 8.243",u"considera",u"Fórum interconselhos")
L([ags["geral"],ags["forumInterconselhos"]],u"Fórum interconselhos",u"traço",u"Debate")
L([ags["geral"],ags["forumInterconselhos"]],u"Fórum interconselhos",u"membro",u"Representante de conselho")
L([ags["geral"],ags["forumInterconselhos"]],u"Fórum interconselhos",u"membro",u"Representante de comissão")
L([ags["geral"],ags["forumInterconselhos"]],u"Fórum interconselhos",u"propósito",u"Monitoramento")
L([ags["geral"],ags["forumInterconselhos"]],u"Monitoramento",u"escopo",u"Política pública")
L([ags["geral"],ags["forumInterconselhos"]],u"Monitoramento",u"escopo",u"Programa governamental")
L([ags["geral"],ags["forumInterconselhos"]],u"Fórum interconselhos",u"formula",u"Recomendação")
L([ags["geral"],ags["forumInterconselhos"]],u"Recomendação",u"propósito",u"Aprimoramento")
L([ags["geral"],ags["forumInterconselhos"]],u"Aprimoramento",u"escopo",u"Intersetorialidade")
L([ags["geral"],ags["forumInterconselhos"]],u"Aprimoramento",u"escopo",u"Transversalidade")

# Audiência pública
L([ags["geral"],ags["audiencia"]],u"Decreto 8.243",u"considera",u"Audiência pública")
L([ags["geral"],ags["audiencia"]],u"Audiência pública",u"traço",u"Presencial")
L([ags["geral"],ags["audiencia"]],u"Audiência pública",u"traço",u"Consultiva")
L([ags["geral"],ags["audiencia"]],u"Audiência pública",u"manifestação oral",u"Participante")
L([ags["geral"],ags["audiencia"]],u"Audiência pública",u"propósito",u"Subsídio para decisão governamental")

# Consulta pública
L([ ags["geral"],ags["consulta"]],u"Decreto 8.243",u"considera",u"Consulta pública")
L([ ags["geral"],ags["consulta"]],u"Consulta pública",u"traço",u"Consultiva")
LD([ags["geral"],ags["consulta"]],u"Consulta pública",u"prazo",u"xsd:dateTime")
L([ ags["geral"],ags["consulta"]],u"Consulta pública",u"recebe",u"Contribuição escrita")
L([ ags["geral"],ags["consulta"]],u"Contribuição escrita",u"forma",u"Ato de convocação")
L([ ags["geral"],ags["consulta"]],u"Contribuição escrita",u"fonte",u"Sociedade civil")
L([ ags["geral"],ags["consulta"]],u"Consulta pública",u"membro",u"Pessoa interessada")
L([ ags["geral"],ags["consulta"]],u"Consulta pública",u"sobre",u"Assunto")
LD([ags["geral"],ags["consulta"]],u"Assunto",u"descrição",u"xsd:string")

# Ambiente virtual
L([ags["geral"],ags["ambientev"]],u"Decreto 8.243",u"considera",u"Ambiente virtual de participação social")
L([ags["geral"],ags["ambientev"]],u"Ambiente virtual de participação social",u"utiliza",u"TIC")
L([ags["geral"],ags["ambientev"]],u"Ambiente virtual de participação social",u"ênfase",u"Internet")
L([ags["geral"],ags["ambientev"]],u"Ambiente virtual de participação social",u"promove",u"Diálogo")
L([ags["geral"],ags["ambientev"]],u"Diálogo",u"parte",u"Sociedade civil")
L([ags["geral"],ags["ambientev"]],u"Diálogo",u"parte",u"Administração pública federal")


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


nome_="conferencia"
A=ags[nome_][1]
g=ags[nome_][0]
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

nome_="ouvidoria"
A=ags[nome_][1]
g=ags[nome_][0]
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

nome_="mesa"
A=ags[nome_][1]
g=ags[nome_][0]
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

nome_="forumInterconselhos"
A=ags[nome_][1]
g=ags[nome_][0]
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

nome_="audiencia"
A=ags[nome_][1]
g=ags[nome_][0]
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

nome_="consulta"
A=ags[nome_][1]
g=ags[nome_][0]
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

nome_="ambientev"
A=ags[nome_][1]
g=ags[nome_][0]
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

nome_="conselho"
A=ags[nome_][1]
g=ags[nome_][0]
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

nome_="comissao"
A=ags[nome_][1]
g=ags[nome_][0]
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




