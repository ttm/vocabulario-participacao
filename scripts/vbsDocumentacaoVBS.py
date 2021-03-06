#-*- coding: utf-8 -*-
import rdflib as r, pygraphviz as gv, sys
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

ouv=vbs.SocialLibrary # SKOS
louv =u"Bibioteca social"
G(ouv,rdf.type,skos.Concept)
G(ouv,skos.prefLabel,L(louv,lang="pt"))
G(ouv,skos.altLabel,L(u"Biblioteca digital",lang="pt"))
G(ouv,skos.altLabel,L(u"Biblioteca Digital de Participação Social",lang="pt"))
G(ouv,skos.altLabel,L(u"Biblioteca de participação",lang="pt"))
G(ouv,skos.altLabel,L(u"Biblioteca semântica de participação social",lang="pt"))
G(ouv,skos.altLabel,L(u"Biblioteca de participação social",lang="pt"))

ouv=vbs.SocialLibraryManagementCommittee# SKOS
louv =u"Comitê gestor da bibliteca social"
G(ouv,rdf.type,skos.Concept)

def C(uriref,labels,broaders=[]):
    G(uriref,rdf.type,skos.Concept)
    if type(labels)==type(u"astring"):
        G(uriref,skos.prefLabel,L(labels,lang="pt"))
    else:
        G(uriref,skos.prefLabel,L(labels[0],lang="pt"))
        for label in labels[1:]:
            G(uriref,skos.altLabel,L(label,lang="pt"))
    if broaders:
        if type(broaders) in [type(range(5)),type((3,4,5))]:
            for broader in broaders:
                G(uriref,skos.broader,broader)
        else:
            G(uriref,skos.broader,broaders)

louv =u"Caderno de respostas"
ouv=vbs.ResponsesNotebook# SKOS
C(ouv,louv)
ouv=vbs.Proceedings# SKOS
louv =u"Anais"
C(ouv,louv)
ouv=vbs.Minute # SKOS
louv =u"Ata"
C(ouv,louv)

C(vbs.Deal,[u"Acordo",u"Parceria"])
C(vbs.Partnership,u"Parceria")
C(vbs.ConferenceProceedings,u"Anais de conferência")
C(vbs.Presentation,u"Apresentação")
C(vbs.JournalArticle,[u"Artigo em periódico",u"Artigo de periódico"],vbs.AcademicWork)
C(vbs.MeetingMinute,u"Ata de reunião")

C(vbs.Act,u"Ato")
C(vbs.ExplanatoryMemorandum,u"Exposição de motivos",vbs.Act)
C(vbs.Resolution,[u"Resolução",u"Deliberação"],vbs.Act)
C(vbs.Motion,u"Moção",vbs.Act)
C(vbs.Recommendation,u"Recomendação",vbs.Act)

C(vbs.NormativeAct,u"Ato normativo")
C(vbs.Audiovisual,u"Audiovisual")
C(vbs.Newslleter,[u"Boletim informativo",u"Boletim"])
C(vbs.Bulletin,u"Boletim")
C(vbs.Booklet,u"Cartilha")
C(vbs.Convening,[u"Convocatória",u"Documento convocatório"])
C(vbs.Speech,u"Discurso")
C(vbs.ReferenceDocuments,[u"Texto-base",u"Documentos de referência",u"Documento-base"])
C(vbs.Recomendations,u"Recomendações")
C(vbs.Interview,u"Entrevista")
C(vbs.Guide,u"Guia")
C(vbs.Book,u"Livro")
C(vbs.BookChapter,u"Capítulo de livro")
C(vbs.Manual,u"Manual")
C(vbs.Lecture,u"Palestra")
C(vbs.Convention,[u"Convênio",u"Parceria"])
C(vbs.SocialMovementsAgenda,u"Pauta dos Movimentos Sociais")
C(vbs.ActionPlan,u"Plano de Ação")
C(vbs.Politics,u"Política")
C(vbs.InnovativePractice,u"Prática inovadora")
C(vbs.Accountability,u"Prestação de contas")
C(vbs.Bylaws,u"Regimento")
C(vbs.Regulation,u"Regulamento")
C(vbs.Report,[u"Relatório",u"Relato"])
C(vbs.experience,u"de experiência")
C(vbs.Journal,[u"Revista",u"Periódico"])
C(vbs.Screenplay,u"Roteiro")
C(vbs.Systematization,u"Sistematização")
C(vbs.MembershipTerm,u"Termo de adesão")
C(vbs.CNPS,u"Compromisso Nacional de Participação Social")

C(vbs.AcademicWork,u"Trabalho acadêmico")
C(vbs.Thesis,u"Tese",vbs.AcademicWork)
C(vbs.Dissertation,u"Dissertação",vbs.AcademicWork)
C(vbs.Monography,u"Monografia",vbs.AcademicWork)

C(vbs.EventPresentedWork,u"Trabalho apresentados em evento")
C(vbs.Video,u"Vídeo")
C(vbs.Guidance,u"Diretriz")
C(vbs.Community,u"Comunidade")
C(vbs.Subcommunity,u"Subcomunidade",vbs.Community)
C(vbs.Collection,u"Coleção")
C(vbs.FinalReport,u"Relatório final")
C(vbs.SNAS,[u"SNAS",u"Secretaria Nacional de Articulação Social"])
C(vbs.PNPS,[u"PNPS",u"Política Nacional de Participação Social"])
C(vbs.SNPS,[u"SNPS",u"Sistema Nacional de Participação Social"])
C(vbs.Participabr,[u"Participa.br",u"Portal participa.br",u"participabr"])
C(vbs.Web30,u"Web 3.0")
C(vbs.IBICT,[u"IBICT",u"Instituto Brasileiro de Informação em Ciência e Tecnologia"])
C(vbs.CGPS,[u"CGPS",u"Comitê Governamental de Participação Social"])
C(vbs.SGPR,[u"SGPR",u"Secretaria-Geral da Presidência da República"])
C(vbs.EducationalAndTrainingProcesses,u"Processos Educativos e Formativos")
C(vbs.PopularEducation,u"Educação Popular")
C(vbs.CivilSociety,u"Sociedade civil")
C(vbs.PublicAdministration,u"Administração pública")
C(vbs.SocialParticipation,u"Participação social")
C(vbs.PublicPolicy,u"Política pública")
C(vbs.Citizenship,u"Cidadania")
C(vbs.CorruptionFighting,u"Combate à corrupção")
C(vbs.SocialControl,u"Controle social")
C(vbs.Democracy,u"Democracia")
C(vbs.DirectDemocracy,u"Democracia Direta",vbs.Democracy)
C(vbs.ParticipativeDemocracy,u"Democracia Participativa",vbs.Democracy)
C(vbs.Inequality,u"Desigualdade")
C(vbs.SolidarityEconomy,u"Economia solidária")
C(vbs.PopularSolidarityEconomy,u"Economia popular solidária",vbs.SolidarityEconomy)
C(vbs.PopularForum,u"Fórum popular")
C(vbs.GuaranteeOfRights,u"Garantia de direitos")
C(vbs.DemocraticManagement,u"Gestão democrática")
C(vbs.ParticipativeManagement,u"Gestão participativa")
C(vbs.ElectronicGovernment,u"Governo Eletrônico")
C(vbs.PoliticalInclusion,u"Inclusão política")
C(vbs.ParticipatoryInstitution,u"Instituição participativa")
C(vbs.StateSocietyInterface,u"Interface socioestatal")
C(vbs.DialogMethodology,u"Metodologia de diálogo")
C(vbs.ParticipationMethodology,u"Metodologia de participação")
C(vbs.SocialMovement,u"Movimento social")
C(vbs.ParticipatoryBudgeting,u"Orçamento participativo")
C(vbs.LocalParticipation,u"Participação local")
C(vbs.PoliticalParticipation,u"Participação política")
C(vbs.PopularParticipation,u"Participação popular")
C(vbs.PublicPolicy,u"Política pública")
C(vbs.FormativeProcess,u"Processo formativo")
C(vbs.Representation,[u"Representação",u"Representação política"])
C(vbs.RepresentationAndParticipation,u"Representação e participação")
C(vbs.SocialResponsibility,u"Responsabilidade social")
C(vbs.CivilSociety,u"Sociedade civil")
C(vbs.SocialParticipationManagement,u"Gestão da Participação Social")

C(vbs.ParticipationInstancesAndMechanisms,u"Instâncias e Mecanismos de Participação Social")
C(vbs.ONG,[u"ONG",u"Organização não governamental"])
C(vbs.SocialParticipationStudyAndResearch,u"Estudo e Pesquisa em Participação Social")
C(vbs.Other,u"Outros")
C(vbs.Law,u"Lei")
C(vbs.Decree,u"Decreto")
C(vbs.WorkPlan,u"Plano de trabalho")
C(vbs.FGPS,[u"FGPS",u"Fórum Governamental de Participação Social"])
C(vbs.SocialParticipationNormativeFramework,u"Marco normativo de participação social")
C(vbs.FederalBudget,u"Orçamento federal")
C(vbs.GovernmentProgram,u"Programa governamental")
C(vbs.OtherFormsOfExpression,u"Outras formas de manifestação")
C(vbs.Publication,u"Publicação")
C(vbs.DisseminationArticle,u"Artigo de divulgação")
C(vbs.Pamphlet,u"Cartilha")
C(vbs.Book,u"Livro")
C(vbs.OtherDocumentsIssuedByCounsil,u"Outros documentos editados pelo conselho")
C(vbs.GovernmentProgramWithSocialParticipation,u"Programa governamental com participação social")
C(vbs.SocialParticipationPortal,u"Portal de participação social")
C(vbs.Brochure,u"Folheto")
C(vbs.Training,u"Treinamento")
C(vbs.Ordinance,u"Portaria")
C(vbs.TechnicalReport,u"Relatório técnico")
C(vbs.ResearchReport,u"Relatório de pesquisa")
C(vbs.SocialParticipationJournal,u"Revista de participação social")
C(vbs.DigitalFormat,u"Formato digital")
C(vbs.Dictionary,u"Dicionário")
C(vbs.Collection,[u"Coletânea",u"Antologia"])
C(vbs.JudicialDecision,u"Decisão judicial")
C(vbs.OfficialAct,u"Ato oficial")
C(vbs.Treaty,u"Tratado")
C(vbs.PNPSImplementationEvaluationReport,u"Relatório de avaliação da implementação da PNPS")
C(vbs.OrientationToParticipants,u"Orientação aos participantes")
C(vbs.referral,u"de referência")
C(vbs.results,u"de resultados")
C(vbs.resolutions,u"de resoluções")
C(vbs.regulations,u"regimentos")
C(vbs.Conclusion,u"Conclusão")
C(vbs.discussion,u"de debate")
C(vbs.ConsultationObject,[u"Objeto de consulta",u"Proposta de consulta",u"Proposta colocada em consulta"])
C(vbs.Study,u"Estudo")
C(vbs.TechnicalMaterial,u"Material técnico")
C(vbs.RegulatoryImpactDocument,u"Documento de impacto regulatório")
C(vbs.RightsAssignmentToSGPR,u"Cessão de Direitos à SGPR")
C(vbs.SocialParticipationJournal,u"Revista de Participação Social")
C(vbs.CollaborationNetwork,u"Rede de Colaboração")
C(vbs.EndUser,u"Usuário final")
C(vbs.NamesList,[u"Lista de nomes",u"Relação de nomes"])
C(vbs.AttendanceList,u"Lista de presença")
C(vbs.Legislation,u"Legislação")
C(vbs.Invitation,u"Convite")
C(vbs.Opinion,u"Parecer")
C(vbs.Shipping,u"Despacho")
C(vbs.RegularMeeting,u"Reunião ordinária")
C(vbs.AnnualReport,u"Relatório anual")
C(vbs.annual,u"anual")
C(vbs.biennial,u"bienal")
C(vbs.calendar,[u"Calendário",u"Agenda"])
C(vbs.Inform,u"Informe")
C(vbs.CoveragePlan,u"Plano de cobertura")
C(vbs.coverage,u"de cobertura")
C(vbs.ProvisionalMeasure,u"Medida provisória")
C(vbs.Folder,u"Folder")
C(vbs.InternalRegiment,u"Regimento interno")
C(vbs.approved,u"aprovado")
C(vbs.Course,u"Curso")
C(vbs.Expedient,u"Expediente")
C(vbs.OrderOfTheDay,u"Ordem do dia")
C(vbs.SubjectDiscussed,u"Assunto abordado")
C(vbs.Handout,u"Apostila")
C(vbs.management,u"de gestão")
C(vbs.DOU,[u"DOU",u"Diário Oficial da União"])
C(vbs.Annex,u"Anexo")
C(vbs.Composition,u"Composição")
C(vbs.Agenda,u"Pauta")
C(vbs.Table,u"Tabela")
C(vbs.Plenary,u"Plenária")
C(vbs.Balance,[u"Balanço",u"Balanço geral"])
C(vbs.national,u"nacional")
C(vbs.Goals,u"Metas")
C(vbs.Resume,u"Resumo")
C(vbs.Proposal,u"Proposta")
C(vbs.Release,u"Release")
C(vbs.Guidelines,u"Orientações")
C(vbs.Colloquium,u"Colóquio")
C(vbs.Slides,u"Slides")
C(vbs.preliminary,u"preliminar")
C(vbs.managerial,u"gerencial")
C(vbs.Systematization,u"Sistematização")
C(vbs.Contributions,u"Contribuições")
C(vbs.Project,u"Projeto")
C(vbs.Monitoring,u"Monitoramento")
C(vbs.Data,u"Dados")
C(vbs.Changes,u"Alterações")
C(vbs.Response,u"Resposta")
C(vbs.LAI,[u"LAI",u"Lei de Acesso à Informação"])
C(vbs.Notebook,u"Caderno")
C(vbs.Letter,u"Carta")
C(vbs.Summary,u"Síntese") # de reunião 
C(vbs.Text,u"Texto")
C(vbs.Thinking,u"Reflexões")
C(vbs.Evaluation,u"Avaliação")
C(vbs.Architecture,u"Arquitetura")

ta=vbs.PolicyArea
lta=u"Área de política" # SKOS
C(ta,lta)

sp=vbs.SocialPolicies
lsp=u"Políticas sociais" # SKOS TTM
C(sp,lsp,ta)

C(vbs.SocialCare,u"assistência social",sp)
C(vbs.Culture,u"cultura",sp)
C(vbs.Health,u"saúde",sp)
C(vbs.FoodAndNutritionSecurity,u"segurança alimentar e nutricional",sp)

sp=vbs.EconomicDevelopment ###
lsp=u"Desenvolvimento econômico" # SKOS
C(sp,lsp,ta)

C(vbs.LocalProductiveArrangements,u"Arranjos produtivos locais",sp)
C(vbs.TechnicalAssitanceAndRuralExtension,u"assistência técnica e extensão rural",sp)
C(vbs.RegionalDevelopment,u"desenvolvimento regional",sp)
C(vbs.SustainableAndSolidaryRuralDevelopment,u"desenvolvimento rural sustentável e solidário",sp)

sp=vbs.GuaranteeOfRights ###
lsp=u"Garantia de direitos" # SKOS
C(sp,lsp,ta)

C(vbs.ChildrenAndAdolescents,u"criança e adolescente",sp)
C(vbs.Education,u"educação",sp)
C(vbs.Youth,u"juventude",sp)
C(vbs.LGBT,[u"LGBT",u"Lésbicas, Gays, Bissexuais e Transgêneros"],sp)

#- Garantias de Direitos (criança e adolescente, Educação,juventude, LGBT, mulheres e pessoa idosa)
sp=vbs.Infrastructure ###
lsp=u"Infraestrutura" # SKOS
C(sp,lsp,ta)
C(vbs.Cities,u"cidades",sp)

sp=vbs.NaturalResources ###
lsp=u"Recursos naturais" # SKOS
C(sp,lsp,ta)
C(vbs.Environment,u"meio ambiente",sp)
C(vbs.WaterResources,u"recursos hídricos",sp)

C(vbs.RecommendationsAndPropositionsReport,u"Relatório de recomendações e proposições")

f=open("../rdf/vbsDocumentacaoVBS.rdf","wb")
f.write(g.serialize())
f.close()
f=open("../rdf/vbsDocumentacaoVBS.ttl","wb")
f.write(g.serialize(format="turtle"))
f.close()
