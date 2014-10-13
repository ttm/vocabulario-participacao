#-*- coding: utf8 -*-
from OD import *
from dateutil.parser import parse
import rdflib as r
#doc = ODSReader("films.ods")
doc = ODSReader("../fontes/base_dados_conselhos_nacionais_normas_ipea_2013.ods")
table = doc.getSheet("Estrutura")
head= table[0]
body=table[1:]
# 3 grupos de colunas:
# 0-19 -> G1 - informações gerais
# 20-27 -> G2 - quantizações básicas
# 28-34 -> G3 - gestão do conselho

g = r.Graph()
g.namespace_manager.bind("xsd", r.namespace.XSD)    
g.namespace_manager.bind("obs", "http://purl.org/socialparticipation/obs/")    
rdf = r.namespace.RDF
obs = r.Namespace("http://purl.org/socialparticipation/obs/")
xsd = r.namespace.XSD

def G(S,P,O):
    g.add((S,P,O))
L=r.Literal
cons=obs.Council
for cc in body:
    uri=cons+"#"+cc[0]
    G(uri,rdf.type,cons)
    G(uri,obs.abbreviation,L(cc[0])) # inversamente funcional e funcional
    G(uri,obs.name,L(cc[1])) # inversamente funcional e funcional
    G(uri,obs.bond,L(cc[2])) # funcional
    G(uri,obs.yearCreated,L(cc[3],datatype=xsd.gYear)) # funcional
    G(uri,obs.creationAct,L(cc[4])) # inversamente funcional? e funcional TTM
    G(uri,obs.creationActType,L(cc[5])) # funcional, ["Lei","Portaria","Decreto"] itens para o qual vale criar classe
    if cc[6]=="Sim":
        G(uri,obs.reformulation,L(True)) # funcional, o que eh esa coluna? TTM
        G(uri,obs.reformulationYear,L(cc[7],datatype=xsd.gYear)) # funcional
        G(uri,obs.reformulationAct,L(cc[8],datatype=xsd.gYear)) # funcional
        G(uri,obs.reformulationActType,L(cc[9])) # funcional, só Decreto, mas provavel que também valha Lei ou Portaria
    else:
        G(uri,obs.reformulation,L(False)) # funcional
    G(uri,obs.regulationAct,L(cc[10])) # funcional, o que eh esa coluna? TTM
    G(uri,obs.thematicArea,L(cc[11])) # funcional: Políticas sociais, Infraestrutura e recursos naturais, Desenvolvimento econômico, Garantia de direitos
    if cc[12]!=u"Sem informação":
        G(uri,obs.disposition,L(cc[12])) # funcional, consultivo ou deliberativo
    if cc[13]!=u"Sem informação":
        G(uri,obs.meetingsFrequency,L(cc[12])) # funcional: 'Trimestralmente', 'Bimestralmente', 'Mensalmente', 'Semestralmente'
    if cc[14]!=u"Sem informação":
        if cc[14]!=u"Sim":
            G(uri,obs.executiveSecretary,L(True)) # funcional
        else:
            G(uri,obs.executiveSecretary,L(False)) # funcional
    if cc[15]!=u"Sem informação":
        if cc[15]!=u"Sim":
            G(uri,obs.commission,L(True)) # funcional
        else:
            G(uri,obs.commission,L(False)) # funcional
    if cc[16]!=u"Sim":
        G(uri,obs.conference,L(True)) # funcional
    else:
        G(uri,obs.conference,L(False)) # funcional
    if cc[17]!=u"Não se aplica":
        G(uri,obs.conferencesCount,L(cc[17])) # funcional
    if cc[18]!=u"Não se vincula a nenhuma lei ou política":
        G(uri,obs.linkedPolicy,L(cc[18])) # funcional
        G(uri,obs.policy,L(cc[19])) # funcional
    G(uri,obs.membersCount,L(int(cc[20]))) # funcional
    G(uri,obs.governmentMembersCount,L(int(cc[21]))) # funcional
    G(uri,obs.civilSocietyMembersCount,L(int(cc[22]))) # funcional
    G(uri,obs.civilSocietySeletionMethod,L(cc[23])) # funcional
    if cc[24]=="Sim":
        G(uri,obs.limitedMandate,L(True)) # funcional
    else:
        G(uri,obs.limitedMandate,L(False)) # funcional
    if cc[25]=="Sim":
        G(uri,obs.parity,L(True)) # funcional
    else:
        G(uri,obs.parity,L(False)) # funcional
    G(uri,obs.governmentRepresentativesProportion,L(float(cc[26].replace(",",".")))) # funcional
    G(uri,obs.civilSocietyRepresentativesProportion,L(float(cc[27].replace(",",".")))) # funcional
    if cc[28]!=u"Sem informação":
        G(uri,obs.presidencySelectionMethod,L(cc[28])) # funcional
    if cc[29]=="Sim":
        G(uri,obs.internalGovernanceBody,L(True)) # funcional
        G(uri,obs.internalGovernanceBodyName,L(cc[30])) # funcional
        G(uri,obs.internalGovernanceBodyMemberCriterion,L(cc[31])) # funcional
    else:
        G(uri,obs.internalGovernanceBody,L(False)) # funcional
    if cc[32]!=u"Sem informação":
        G(uri,obs.agendaPreparation,L(cc[32]))
    if cc[33]!=u"Sem informação":
        if cc[33]=="Sim":
            G(uri,obs.presidentialQualityVote,L(True))
        else:
            G(uri,obs.presidentialQualityVote,L(False))
    if cc[34]!=u"Sem informação":
        if cc[34]=="Sim":
            G(uri,obs.adReferendumDecisions,L(True))
        else:
            G(uri,obs.adReferendumDecisions,L(False))

f=open("../rdf/conselhos.rdf","wb")
f.write(g.serialize())
f.close()
