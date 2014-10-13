#-*- coding: utf8 -*-
from OD import *
from dateutil.parser import parse
import rdflib as r
#doc = ODSReader("films.ods")
doc = ODSReader("../fontes/base_dados_conferencias_nacionais_ipea_2013.ods")
table = doc.getSheet(u"Dados_Conferências_Nacionais")
head= table[0]
body=table[1:]

g = r.Graph()
g.namespace_manager.bind("xsd", r.namespace.XSD)    
g.namespace_manager.bind("obs", "http://purl.org/socialparticipation/obs/")    
rdf = r.namespace.RDF
obs = r.Namespace("http://purl.org/socialparticipation/obs/")
xsd = r.namespace.XSD

conf=obs.Conference
def G(S,P,O):
    g.add((S,P,O))
L=r.Literal

i=1
for cc in body:
    uri=conf+"#"+str(i)
    G(uri,rdf.type,conf)
    G(uri,obs.name,L(cc[0])) # funcional
    G(uri,obs.edition,L(cc[1])) # funcional
    G(uri,obs.year,L(cc[2],datatype=xsd.gYear)) # funcional
    if cc[3]!="Corresponsabilidade":
        G(uri,obs.responsibleBody,L(cc[3])) # funcional
    else:
        G(uri,obs.responsibleBody,L(cc[4])) # funcional
    G(uri,obs.role,L(cc[5])) # funcional
    G(uri,obs.thematicArea,L(cc[6])) # funcional: Políticas sociais, Infraestrutura e recursos naturais, Desenvolvimento econômico, Garantia de direitos, Apoio à Gestão
    if cc[7] not in (u"Sem informação",u"Não se aplica"):
        G(uri,obs.callType,L(cc[7]))
        G(uri,obs.callAct,L(cc[8]))
    if cc[9]==u"Sim":
        G(uri,obs.schedulingPurpose,L(True))
    elif cc[9]==u"Não":
        G(uri,obs.schedulingPurpose,L(False))
    if cc[10]==u"Sim":
        G(uri,obs.evaluationPurpose,L(True))
    elif cc[10]==u"Não":
        G(uri,obs.evaluationPurpose,L(False))
    if cc[11]==u"Sim":
        G(uri,obs.participationPurpose,L(True))
    elif cc[11]==u"Não":
        G(uri,obs.participationPurpose,L(False))
    if cc[12]==u"Sim":
        G(uri,obs.propositionPurpose,L(True))
    elif cc[12]==u"Não":
        G(uri,obs.propositionPurpose,L(False))
    G(uri,obs.theme,L(cc[13]))
    if cc[14]!=u"Sem informação":
        G(uri,obs.thematicAxes,L(cc[14])) # vira parsear e colocar eixo por eixo
    if cc[15]==u"Sim":
        G(uri,obs.freePhases,L(True))
    elif cc[15]==u"Não":
        G(uri,obs.freePhases,L(False))
    if cc[16]==u"Sim":
        G(uri,obs.virtualPhases,L(True))
    elif cc[16]==u"Não":
        G(uri,obs.virtualPhases,L(False))
    if cc[17]==u"Sim":
        G(uri,obs.sectorPhases,L(True))
    elif cc[17]==u"Não":
        G(uri,obs.sectorPhases,L(False))
    if cc[18]==u"Sim":
        G(uri,obs.intercityPhases,L(True))
    elif cc[18]==u"Não":
        G(uri,obs.intercityPhases,L(False))
    if cc[19]==u"Sim":
        G(uri,obs.municipalPhases,L(True))
    elif cc[19]==u"Não":
        G(uri,obs.municipalPhases,L(False))
    if cc[20]==u"Sim":
        G(uri,obs.statePhases,L(True))
    elif cc[20]==u"Não":
        G(uri,obs.statePhases,L(False))
    if cc[21]==u"Sim":
        G(uri,obs.extraordinaryPhases,L(True))
    elif cc[21]==u"Não":
        G(uri,obs.extraordinaryPhases,L(False))
    if cc[22] not in (u"Sem informação",u"Não se aplica"):
        G(uri,obs.realizationPeriod,L("P%sM"%(cc[22].split()[0],),datatype=xsd.duration))
    if cc[23]==u"Sim":
        G(uri,obs.linkedCouncil,L(True))
        G(uri,obs.council,L(cc[24]))
    elif cc[23]==u"Não":
        G(uri,obs.linkedCouncil,L(False))
    if cc[25]!=u"Sem informação":
        G(uri,obs.nationalOrganizationComission,L(cc[25]))
    if cc[26]!=".":
        G(uri,obs.nongovernmentalVacanciesNationalOrganizationComission,L(int(cc[26])))
    if cc[27]!=".":
        G(uri,obs.governmentalVacanciesNationalOrganizationComission,L(int(cc[27])))
    if cc[28]!=".":
        G(uri,obs.councilVacanciesNationalOrganizationComission,L(int(cc[28])))
    if cc[29]==u"Sim":
        G(uri,obs.plenary,L(True))
    elif cc[29]==u"Não":
        G(uri,obs.plenary,L(False))
    if cc[30]==u"Sim":
        G(uri,obs.workGroups,L(True))
    elif cc[30]==u"Não":
        G(uri,obs.workGroups,L(False))
    if cc[31]==u"Sim":
        G(uri,obs.intermediaryPlenary,L(True))
    elif cc[31]==u"Não":
        G(uri,obs.intermediaryPlenary,L(False))
    if cc[32]==u"Sim":
        G(uri,obs.lectures,L(True))
    elif cc[32]==u"Não":
        G(uri,obs.lectures,L(False))
    if cc[33]==u"Sim":
        G(uri,obs.workshops,L(True))
    elif cc[33]==u"Não":
        G(uri,obs.workshops,L(False))
    if cc[34]==u"Sim":
        G(uri,obs.municipalPhasesProposalsLimit,L(True))
    elif cc[34]==u"Não":
        G(uri,obs.municipalPhasesProposalsLimit,L(False))
    if cc[35].strip().isalnum():
        G(uri,obs.municipalPhasesProposalsLimitCount,L(int(cc[35])))
    if cc[36]==u"Sim":
        G(uri,obs.statePhasesProposalsLimit,L(True))
    elif cc[36]==u"Não":
        G(uri,obs.statePhasesProposalsLimit,L(False))
    if cc[37].strip().isalnum():
        G(uri,obs.statePhasesProposalsLimitCount,L(int(cc[37])))
    if cc[38]==u"Sim":
        G(uri,obs.nationalPhaseWorkGroupProposalsLimit,L(True))
    elif cc[38]==u"Não":
        G(uri,obs.nationalPhaseWorkGroupProposalsLimit,L(False))
    if cc[39].strip().isalnum():
        G(uri,obs.nationalPhaseWorkGroupProposalsLimitCount,L(int(cc[39])))
    if cc[40]==u"Sim":
        G(uri,obs.nationalPhaseProposalsLimit,L(True))
    elif cc[40]==u"Não":
        G(uri,obs.nationalPhaseProposalsLimit,L(False))
    if cc[41].strip().isalnum():
        G(uri,obs.nationalPhaseProposalsLimitCount,L(int(cc[41])))
    if cc[42]==u"Sim":
        G(uri,obs.nationalPhaseProposalsPriorization,L(True))
    elif cc[42]==u"Não":
        G(uri,obs.nationalPhaseProposalsPriorization,L(False))
    if cc[43]==u"Sim":
        G(uri,obs.nationalPhaseNewProposalsFormulation,L(True))
    elif cc[43]==u"Não":
        G(uri,obs.nationalPhaseNewProposalsFormulation,L(False))
    if cc[44].strip().isalnum():
        G(uri,obs.regimentDelegatesCount,L(int(cc[44])))
    if cc[45].strip().isalnum():
        G(uri,obs.regimentNongovernmentalVacanciesCount,L(int(cc[45])))
    if cc[46].strip().isalnum():
        G(uri,obs.regimentGovernmentalVacanciesCount,L(int(cc[46])))
    if cc[47]==u"Sim":
        G(uri,obs.quotasPrediction,L(True))
    elif cc[47]==u"Não":
        G(uri,obs.quotasPrediction,L(False))
    if (u"Não se aplica" not in cc[48]) and (u"Sem informação" not in cc[48]):
        G(uri,obs.womenQuota,L(cc[48]))
    if (u"Não se aplica" not in cc[49]) and (u"Sem informação" not in cc[49]):
        G(uri,obs.ethnicQuota,L(cc[49]))
    if (u"Não se aplica" not in cc[50]) and (u"Sem informação" not in cc[50]):
        G(uri,obs.otherQuota,L(cc[50]))
    if (u"Não se aplica" not in cc[51]) and (u"Sem informação" not in cc[51]):
        G(uri,obs.otherQuotaSpecification,L(cc[51]))
    if cc[52]==u"Sim":
        G(uri,obs.nativeDelegatesQuotaPrediction,L(True))
    elif cc[52]==u"Não":
        G(uri,obs.nativeDelegatesQuotaPrediction,L(False))
    if cc[53].strip().isalnum():
        G(uri,obs.nativeDelegatesQuotaCount,L(int(cc[53])))
    if (u"Não se aplica" not in cc[54]) and (u"Sem informação" not in cc[54]):
        G(uri,obs.nativeDelegatesQuotaSpecification,L(cc[54]))
    if cc[55]==u"Sim":
        G(uri,obs.guestVacanciesPrediction,L(True))
    elif cc[55]==u"Não":
        G(uri,obs.guestVacanciesPrediction,L(False))
    if cc[56].strip().isalnum():
        G(uri,obs.participantsCount,L(int(cc[56].strip().isalnum())))
    if cc[57].strip().isalnum():
        G(uri,obs.municipalitiesCount,L(int(cc[57].strip().isalnum())))
    if cc[58].strip().isalnum():
        G(uri,obs.nationalPhaseParticipantsCount,L(int(cc[58].strip().isalnum())))
    if cc[59].strip().isalnum():
        G(uri,obs.nationalPhaseWomenCount,L(int(cc[59].strip().isalnum())))
    if cc[60].strip().isalnum():
        G(uri,obs.nationalPhaseMenCount,L(int(cc[60].strip().isalnum())))
    if cc[61].strip().isalnum():
        G(uri,obs.unidentifiedPersonsCount,L(int(cc[61].strip().isalnum())))
    if cc[62]!=u"Não se aplica":
        G(uri,obs.nationalPhaseCountReference,L(cc[62]))
    if cc[63].strip().isalnum():
        G(uri,obs.nationalPhaseApprovedProposalsCount,L(int(cc[63].strip().isalnum())))

f=open("../rdf/conferencias.rdf","wb")
f.write(g.serialize())
f.close()
