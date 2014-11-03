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



consu=vbs.PublicConsultation
lconsu=u"Consulta pública" # SKOS TTM
G(consu,rdf.type,skos.Concept)
G(consu,skos.prefLabel,L(lconsu,lang="pt"))
G(consu,skos.altLabel,L(u"Consulta pública federal",lang="pt"))
G(consu,skos.definition,L(u"mecanismo participativo, a se realizar em prazo definido, de caráter consultivo, aberto a qualquer interessado, que visa a receber contribuições por escrito da sociedade civil sobre determinado assunto, na forma definida no seu ato de convocação (PNPS)",lang="pt"))


sp=vbs.Theme ###
lsp=u"Tema" # SKOS
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))

sp=vbs.thematicAxix
lsp=u"Eixo temático"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.broader,sp)

sp=vbs.ConsultationMethodology
lsp=u"Metodologia de consulta pública"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.altLabel,L(u"Procedimento metodológico",lang="pt"))
sp_=sp

sp=vbs.ParticipativeMoment
lsp=u"Momento participativo"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.related,sp_)

sp_=vbs.InteractionZone
lsp_=u"Zona de interação"
G(sp,rdf.type,skos.Concept)
G(sp,skos.prefLabel,L(lsp,lang="pt"))
G(sp,skos.related,sp_)


f=open("../rdf/vbsConsulta.rdf","wb")
f.write(g.serialize())
f.close()

f=open("../rdf/vbsConsulta.ttl","wb")
f.write(g.serialize(format="turtle"))
f.close()

