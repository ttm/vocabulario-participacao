#-*- coding: utf-8 -*-
import rdflib as r, pygraphviz as gv
def G(S,P,O):
    g.add((S,P,O))
L=r.Literal

vbs = r.Namespace("http://purl.org/socialparticipation/vbs/")
rdf = r.namespace.RDF
rdfs = r.namespace.RDFS
skos = r.namespace.SKOS
xsd = r.namespace.XSD

g = r.Graph()
g.namespace_manager.bind("vbs", "http://purl.org/socialparticipation/vbs/")    
g.namespace_manager.bind("rdf", r.namespace.RDF)    
g.namespace_manager.bind("rdfs", r.namespace.RDFS)    
g.namespace_manager.bind("xsd", r.namespace.XSD)    
g.namespace_manager.bind("skos", r.namespace.SKOS)    

pnps=vbs.PNPS
G(pnps,rdf.type,skos.Concept)
G(pnps,skos.prefLabel,L(u"PNPS",lang="pt"))
G(pnps,skos.altLabel,L(u"Política Nacional de Participação Social",lang="pt"))
G(pnps,skos.altLabel,L(u"Política Nacional de Participação Social (PNPS)",lang="pt"))
G(pnps,skos.altLabel,L(u"Política Nacional de Participação Social - PNPS",lang="pt"))

pnps=vbs.DemocraticDialogueInstance
G(pnps,rdf.type,skos.Concept)
G(pnps,skos.prefLabel,L(u"Instância democrática de diálogo",lang="pt"))

foo=vbs.FederalPublicAdministration
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(u"Administração pública federal",lang="pt"))

foo=vbs.CivilSociety
lfoo=u"Sociedade civil"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))
G(foo,skos.definition,L(u"o cidadão, os coletivos, os movimentos sociais institucionalizados ou não institucionalizados, suas redes e suas organizações (PNPS)",lang="pt"))

cons=vbs.Council
G(cons,rdf.type,skos.Concept)
G(cons,skos.prefLabel,L(u"Conselho",lang="pt"))
G(cons,skos.altLabel,L(u"Conselho de políticas públicas",lang="pt"))
G(cons,skos.altLabel,L(u"Conselho nacional de políticas públicas",lang="pt"))
G(cons,skos.altLabel,L(u"Conselho gestor",lang="pt"))
G(cons,skos.definition,L(u"instância colegiada temática permanente, instituída por ato normativo, de diálogo entre a sociedade civil e o governo para promover a participação no processo decisório e na gestão de políticas públicas (PNPS)",lang="pt"))
G(cons,skos.definition,L(u"Espaços públicos vinculados a órgãos do Poder Executivo, tendo por finalidade permitir a participação da sociedade na definição de prioridades para a agenda política, bem como na formulação, no acompanhamento e no controle das políticas públicas (IPEA 2013)",lang="pt"))
G(cons,skos.scopeNote,L(u"Espaço participativo com a finalidade de incidir nas políticas públicas de determinado tema, nos quais é prevista certa permanência no tempo, composto por representantes do poder público e da sociedade civil, esta podendo ser dividida em diferentes segmentos.",lang="pt"))
G(cons,skos.scopeNote,L(u"espaço contínuo de participação social",lang="pt"))

foo=vbs.Commision
lfoo=u"Comissão"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))
G(foo,skos.altLabel,L(u"Comissão de políticas públicas",lang="pt"))
G(foo,skos.definition,L(u"instância colegiada temática, instituída por ato normativo, criada para o diálogo entre a sociedade civil e o governo em torno de objetivo específico, com prazo de funcionamento vinculado ao cumprimento de suas finalidades",lang="pt"))

conf=vbs.Conference
G(conf,rdf.type,skos.Concept)
G(conf,skos.prefLabel,L(u"Conferência",lang="pt"))
G(conf,skos.altLabel,L(u"Conferência nacional",lang="pt"))
G(conf,skos.altLabel,L(u"Conferência de políticas públicas",lang="pt"))
G(conf,skos.definition,L(u"Processo periódico de promoção do diálogo entre governo e sociedade, realizado em etapas, tipicamente convocadas pelo Executivo",lang="pt")) # Melhorar TTM
G(conf,skos.definition,L(u"Instância colegiada temática permanente, instituída por ato normativo, de diálogo entre a sociedade civil e o governo para promover a participação no processo decisório e na gestão de políticas públicas",lang="pt")) # Melhorar TTM
G(conf,skos.definition,L(u"instância periódica de debate, de formulação e de avaliação sobre temas específicos e de interesse público, com a participação de representantes do governo e da sociedade civil, podendo contemplar etapas estaduais, distrital, municipais ou regionais, para propor diretrizes e ações acerca do tema tratado (PNPS)",lang="pt")) # Melhorar TTM

ouv=vbs.OmbudsmanAgency # SKOS
louv =u"Ouvidoria"
G(ouv,rdf.type,skos.Concept)
G(ouv,skos.prefLabel,L(louv,lang="pt"))
G(ouv,skos.altLabel,L(u"Ouvidoria federal",lang="pt"))
G(ouv,skos.altLabel,L(u"Ouvidoria pública",lang="pt"))
G(ouv,skos.altLabel,L(u"Ouvidoria pública federal",lang="pt"))
G(ouv,skos.definition,L(u"instância de controle e participação social responsável pelo tratamento das reclamações, solicitações, denúncias, sugestões e elogios relativos às políticas e aos serviços públicos, prestados sob qualquer forma ou regime, com vistas ao aprimoramento da gestão pública (PNPS)",lang="pt"))

foo=vbs.DialogueTable
lfoo=u"Mesa de diálogo" # SKOS TTM
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))
G(foo,skos.definition,L(u"mecanismo de debate e de negociação com a participação dos setores da sociedade civil e do governo diretamente envolvidos no intuito de prevenir, mediar e solucionar conflitos sociais (PNPS)",lang="pt"))


foo=vbs.InterCouncilForum
lfoo=u"Fórum interconselhos" # SKOS TTM
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))
G(foo,skos.definition,L(u"mecanismo para o diálogo entre representantes dos conselhos e comissões de políticas públicas, no intuito de acompanhar as políticas públicas e os programas governamentais, formulando recomendações para aprimorar sua intersetorialidade e transversalidade (PNPS)",lang="pt"))


foo=vbs.PublicAudience
lfoo=u"Audiência pública" # SKOS TTM
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))
G(foo,skos.definition,L(u"mecanismo participativo de caráter presencial, consultivo, aberto a qualquer interessado, com a possibilidade de manifestação oral dos participantes, cujo objetivo é subsidiar decisões governamentais (PNPS)",lang="pt"))

sp=vbs.PublicConsultation
lsp=u"Consulta pública" # SKOS TTM
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.definition,L(u"mecanismo participativo, a se realizar em prazo definido, de caráter consultivo, aberto a qualquer interessado, que visa a receber contribuições por escrito da sociedade civil sobre determinado assunto, na forma definida no seu ato de convocação (PNPS)",lang="pt"))

sp=vbs.VirtualParticipationEnvironment
lsp=u"Ambiente virtual de participação social" # SKOS TTM
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.definition,L(u"mecanismo de interação social que utiliza tecnologias de informação e de comunicação, em especial a internet, para promover o diálogo entre administração pública federal e sociedade civil (PNPS)",lang="pt"))
G(sp,skos.definition,L(u"mecanismo participativo, a se realizar em prazo definido, de caráter consultivo, aberto a qualquer interessado, que visa a receber contribuições por escrito da sociedade civil sobre determinado assunto, na forma definida no seu ato de convocação (PNPS)",lang="pt"))


foo=vbs.Guideline
lfoo=u"Diretriz"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.CitizenRight
lfoo=u"Direito do cidadão"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.AutonomyExpression
lfoo=u"Expressão de autonomia"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.DirectDemocracy
lfoo=u"Democracia direta"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.ParticipativeDemocracy
lfoo=u"Democracia participativa"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.RepresentativeDemocracy
lfoo=u"Democracia representativa"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.Citizenship
lfoo=u"Cidadania"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.Transparency
lfoo=u"Transparência"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.SocialControl
lfoo=u"Controle social"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.PublicAction
lfoo=u"Ação pública"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.ActiveCitizenship
lfoo=u"Cidadania ativa"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.Autonomy
lfoo=u"Autonomia"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.FreeFunctioning
lfoo=u"Livre funcionamento"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.Independence
lfoo=u"Independência"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.Independence
lfoo=u"Independência"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.CivilSocietyOrganization
lfoo=u"Organização da sociedade civil"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.GovernmentMethod
lfoo=u"Método de governo"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

pm=vbs.ParticipationMechanism
G(pm,rdf.type,skos.Concept)
G(pm,skos.prefLabel,L("Mecanismo de participação social",lang="pt"))
pm_=pm

pm=vbs.ParticipationInstance
G(pm,rdf.type,skos.Concept)
G(pm,skos.prefLabel,L("Instância de participação social",lang="pt"))
G(conf,skos.broader,pm)
G(pm,skos.related,pm_)
pm__=pm

pm=vbs.ParticipationInstanceOrMechanism
G(pm,rdf.type,skos.Concept)
G(pm,skos.prefLabel,L("Instância ou mecanismo de participação social",lang="pt"))
G(pm__,skos.broader,pm)
G(pm_,skos.broader,pm)


foo=vbs.FederalGovernmentPolicy
lfoo=u"Política do governo federal"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.FederalGovernmentProgram
lfoo=u"Programa do governo federal"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.PlanningAndBudgetingCycle
lfoo=u"Ciclo de planejamento e orçamento"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.FreeTechnology
lfoo=u"Tecnologia livre"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.SourceCode
lfoo=u"Código fonte"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.SocialParticipation
lfoo=u"Participação social"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.PSPB
lfoo=u"Portal do Software Público Brasileiro"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))
G(foo,skos.altLabel,L(u"PSPB",lang="pt"))
G(foo,skos.altLabel,L(u"Portal do Software Público Brasileiro (PSPB)",lang="pt"))

foo=vbs.HistoricallyExcludedGroup
lfoo=u"Grupo historicamente excluído"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.VulnerableGroup
lfoo=u"Grupo vulnerável"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.InstitutionalSupport
lfoo=u"Apoio institucional"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.PublicAgent
lfoo=u"Agente público"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.FederatedEntity
lfoo=u"Ente federado"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.DirectFederalAdministration
lfoo=u"Administração pública federal direta"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.IndirectFederalAdministration
lfoo=u"Administração pública federal indireta"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.Decree
lfoo=u"Decreto"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.PublicPolicy
lfoo=u"Política pública"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

# TTM Habilitar?
#foo=vbs.PublicProgram
#lfoo=u"Programa público"
#G(foo,rdf.type,skos.Concept)
#G(foo,skos.prefLabel,L(lfoo,lang="pt"))
#

foo=vbs.SectorialPolicy
lfoo=u"Política setorial"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.SectorialProgram
lfoo=u"Programa setorial"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.SGPR
lfoo=u"SGPR"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))
G(foo,skos.altLabel,L(u"Secretaria-Geral da Presidência da República",lang="pt"))
G(foo,skos.altLabel,L(u"Secretaria-Geral da Presidência da República (SGPR)",lang="pt"))

snps=vbs.SNPS
G(snps,rdf.type,skos.Concept)
G(snps,skos.prefLabel,L(u"SNPS",lang="pt"))
G(snps,skos.altLabel,L(u"Sistema Nacional de Participação Social",lang="pt"))
G(snps,skos.altLabel,L(u"Sistema Nacional de Participação Social (SNPS)",lang="pt"))
G(snps,skos.altLabel,L(u"Sistema Nacional de Participação Social - SNPS",lang="pt"))

cgps=vbs.CGPS
G(cgps,rdf.type,skos.Concept)
G(cgps,skos.prefLabel,L(u"CGPS",lang="pt"))
G(cgps,skos.altLabel,L(u"Comitê Governamental de Participação Social",lang="pt"))
G(cgps,skos.altLabel,L(u"Comitê Governamental de Participação Social (SNPS)",lang="pt"))
G(cgps,skos.altLabel,L(u"Comitê Governamental de Participação Social - SNPS",lang="pt"))

foo=vbs.Monitoring
lfoo=u"Monitoramento"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.Implementation
lfoo=u"Implementação"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.Coordination
lfoo=u"Coordenação"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.TechnicalAndAdministrativeSupport
lfoo=u"Suporte técnico-administrativo"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.MinistryAct
lfoo=u"Ato do ministro"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.CivilSocietyElectedRepresentative
lfoo=u"Representante eleito pela sociedade civil"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.CivilSocietyNominatedRepresentative
lfoo=u"Representante indicado pela sociedade civil"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

sp=vbs.Parity
lsp=u"Paridade"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.scopeNote,L(u"paridade é um conceito local, podendo por exemplo, ser considerada proporção igual de membros do governo e da sociedade ou proporção igual entre dois segmentos ou setores que são considerados prioritários pelo Conselho",lang="pt"))

foo=vbs.Attribution
lfoo=u"Atribuição"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.Competence
lfoo=u"Competência"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.Nature
lfoo=u"Natureza"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.Diversity
lfoo=u"Diversidade"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.Turnover
lfoo=u"Rotatividade"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.Theme
lfoo=u"Tema"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.ActPublicity
lfoo=u"Publicidade do ato"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.Member
lfoo=u"Membro"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.RelevantPublicServiceProvision
lfoo=u"Provisão de serviço público relevante"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.NormativeCharacterResolution
lfoo=u"Resolução normativa"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))
G(foo,skos.altLabel,L(u"Resolução de caráter normativo",lang="pt"))

foo=vbs.DeliberativeNature
lfoo=u"Natureza deliberativa"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.ConsultiveNature
lfoo=u"Natureza consultiva"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.Entity
lfoo=u"Entidade"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.Representative
lfoo=u"Representante"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

mc=vbs.renewal
lmc=u"Recondução"
G(mc,rdf.type,skos.Concept)
G(mc,skos.prefLabel,L(lmc,lang="pt"))
G(mc,skos.scopeNote,L(u"Quando há 'limite de mandato', há limite para recondução.",lang="pt"))
G(mc,skos.scopeNote,L(u"Este conceito foi trazido do campo dos conselhos, pode ser aplicável em outros contextos.",lang="pt"))

bl=vbs.Bylaws
lbl=u"Regimento interno" #SKOS
G(bl,rdf.type,skos.Concept)
G(bl,skos.prefLabel,L(lbl,lang="pt"))
G(bl,skos.altLabel,L(u"Estatuto",lang="pt"))

foo=vbs.GovernmentPartnershipCelebration
lfoo=u"Celebração de parceria com a administração pública"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.EarmarkedAppropriations # TTM Melhorar
lfoo=u"Dotações consignadas"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.BoardFund # TTM Melhorar
lfoo=u"Fundo do conselho"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.Counselor # TTM Melhorar
lfoo=u"Conselheiro"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.Selection
lfoo=u"Seleção"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.Evaluation
lfoo=u"Avaliação"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.TransparentChoiceCriteria
lfoo=u"Critério transparente de escolha"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.ConveningDocument
lfoo=u"Documento convocatório"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.Autonomy
lfoo=u"Autonomia"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

foo=vbs.Delegate
lfoo=u"Delegado"
G(foo,rdf.type,skos.Concept)
G(foo,skos.prefLabel,L(lfoo,lang="pt"))

sp=vbs.ConferenceStep
lsp=u"Etapa de conferência"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
sn=u"Uma etapa é um evento participativo e também é chamada de conferência, enquanto 'a' conferência é o processo todo"
G(sp,skos.scopeNote,L(sn,lang="pt"))
G(sp,skos.broader,vbs.Conference)







































