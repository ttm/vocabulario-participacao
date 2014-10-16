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

store="../rdf/vbsConferencia.rdf"
g = r.Graph()
g.load(store)
#g.namespace_manager.bind("vbs", "http://purl.org/socialparticipation/vbs/")    
#g.namespace_manager.bind("rdf", r.namespace.RDF)    
#g.namespace_manager.bind("rdfs", r.namespace.RDFS)    
#g.namespace_manager.bind("xsd", r.namespace.XSD)    
#g.namespace_manager.bind("skos", r.namespace.SKOS)    

#conf=vbs.ConferenceStep
#G(conf,rdf.type,skos.Concept)
#

PREFIX="""PREFIX skos: <http://www.w3.org/2004/02/skos/core#>"""

q="SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l . }"
res=g.query(PREFIX+q)
conceitos=[rr[0] for rr in res]



q="SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l . FILTER NOT EXISTS { ?s skos:broader ?o  }  }"
res=g.query(PREFIX+q)
conceitosPai=[rr[0] for rr in res]

cp=sorted(conceitosPai,key=lambda s: s.replace(u"á",u"a").replace(u"Á",u"a").replace(u"Ó",u"o").replace(u"ó",u"o").encode("utf8").lower())

import sys
f=open("../rdf/vbsConferencia.txt", "wb")
foobar=sys.stdout
sys.stdout = f

for cc in cp:
    print (u"|--> %s"%(cc,)).encode("utf8")

    q="SELECT ?al WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:altLabel ?al . }"%(cc,)
    res=g.query(PREFIX+q)
    pls=[rr[0] for rr in res]
    for pl in pls:
        print (u" forma alternativa: %s"%(pl,)).encode("utf8")
    q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:definition ?de . }"%(cc,)
    res=g.query(PREFIX+q)
    pls=[rr[0] for rr in res]
    for pl in pls:
        print (u" definição: %s"%(pl,)).encode("utf8")
    q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:scopeNote ?de . }"%(cc,)
    res=g.query(PREFIX+q)
    pls=[rr[0] for rr in res]
    for pl in pls:
        print (u" nota de escopo: %s"%(pl,)).encode("utf8")

    q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de . }"%(cc,)
    res=g.query(PREFIX+q)
    pls=[rr[0] for rr in res]
    for pl in pls:
        print (u" termo relacionado: %s"%(pl,)).encode("utf8")


    q=("SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l .  ?s skos:broader ?cc . ?cc skos:prefLabel '%s'@pt  }"%(cc,))
    res=g.query(PREFIX+q)
    conceitos_=[rr[0] for rr in res]
    cp2=sorted(conceitos_,key=lambda s: s.replace(u"á",u"a").replace(u"Á",u"a").replace(u"Ó",u"o").replace(u"ó",u"o").encode("utf8").lower())
    for cc2 in cp2:
        print ("   |--> %s"%(cc2,)).encode("utf8")

        q="SELECT ?al WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:altLabel ?al . }"%(cc2,)
        res=g.query(PREFIX+q)
        pls=[rr[0] for rr in res]
        for pl in pls:
            print (u"    forma alternativa: %s"%(pl,)).encode("utf8")
        q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:definition ?de . }"%(cc2,)
        res=g.query(PREFIX+q)
        pls=[rr[0] for rr in res]
        for pl in pls:
            print (u"    definição: %s"%(pl,)).encode("utf8")
        q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:scopeNote ?de . }"%(cc2,)
        res=g.query(PREFIX+q)
        pls=[rr[0] for rr in res]
        for pl in pls:
            print (u"    nota de escopo: %s"%(pl,)).encode("utf8")

        q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc2,)
        res=g.query(PREFIX+q)
        pls=[rr[0] for rr in res]
        for pl in pls:
            print (u"    termo relacionado: %s"%(pl,)).encode("utf8")




        q=("SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l .  ?s skos:broader ?cc . ?cc skos:prefLabel '%s'@pt  }"%(cc2,))
        res=g.query(PREFIX+q)
        conceitos__=[rr[0] for rr in res]
        cp3=sorted(conceitos__,key=lambda s: s.replace(u"á",u"a").replace(u"Á",u"a").replace(u"Ó",u"o").replace(u"ó",u"o").encode("utf8").lower())
        for cc3 in cp3:
            print ("     |--> %s"%(cc3,)).encode("utf8")


            q="SELECT ?al WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:altLabel ?al . }"%(cc3,)
            res=g.query(PREFIX+q)
            pls=[rr[0] for rr in res]
            for pl in pls:
                print (u"       forma alternativa: %s"%(pl,)).encode("utf8")
            q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:definition ?de . }"%(cc3,)
            res=g.query(PREFIX+q)
            pls=[rr[0] for rr in res]
            for pl in pls:
                print (u"       definição: %s"%(pl,)).encode("utf8")
            q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:scopeNote ?de . }"%(cc3,)
            res=g.query(PREFIX+q)
            pls=[rr[0] for rr in res]
            for pl in pls:
                print (u"       nota de escopo: %s"%(pl,)).encode("utf8")

            q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc3,)
            res=g.query(PREFIX+q)
            pls=[rr[0] for rr in res]
            for pl in pls:
                print (u"       termo relacionado: %s"%(pl,)).encode("utf8")


            q=("SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l .  ?s skos:broader ?cc . ?cc skos:prefLabel '%s'@pt  }"%(cc3,))
            res=g.query(PREFIX+q)
            conceitos___=[rr[0] for rr in res]
            cp4=sorted(conceitos___,key=lambda s: s.replace(u"á",u"a").replace(u"Á",u"a").replace(u"Ó",u"o").replace(u"ó",u"o").encode("utf8").lower())
            for cc4 in cp4:
                print ("         |--> %s"%(cc4,)).encode("utf8")


                q="SELECT ?al WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:altLabel ?al . }"%(cc4,)
                res=g.query(PREFIX+q)
                pls=[rr[0] for rr in res]
                for pl in pls:
                    print (u"          forma alternativa: %s"%(pl,)).encode("utf8")
                q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:definition ?de . }"%(cc4,)
                res=g.query(PREFIX+q)
                pls=[rr[0] for rr in res]
                for pl in pls:
                    print (u"          definição: %s"%(pl,)).encode("utf8")
                q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:scopeNote ?de . }"%(cc4,)
                res=g.query(PREFIX+q)
                pls=[rr[0] for rr in res]
                for pl in pls:
                    print (u"          nota de escopo: %s"%(pl,)).encode("utf8")

                q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc4,)
                res=g.query(PREFIX+q)
                pls=[rr[0] for rr in res]
                for pl in pls:
                    print (u"          termo relacionado: %s"%(pl,)).encode("utf8")





                q=("SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l .  ?s skos:broader ?cc . ?cc skos:prefLabel '%s'@pt  }"%(cc4,))
                res=g.query(PREFIX+q)
                conceitos____=[rr[0] for rr in res]
                cp5=sorted(conceitos____,key=lambda s: s.replace(u"á",u"a").replace(u"Á",u"a").replace(u"Ó",u"o").replace(u"ó",u"o").encode("utf8").lower())
                for cc5 in cp5:
                    print "+++++++++++++++++++++1 "
                    print "            |--> %s"%(cc5,)
f.close()

sys.stdout=foobar
print "feito arquivo com vocabulario"


PREFIX="""PREFIX skos: <http://www.w3.org/2004/02/skos/core#>"""

q="SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l . }"
res=g.query(PREFIX+q)
conceitos=[rr[0] for rr in res]

f=open("../rdf/vbsConferenciaPodada.txt", "wb")
foobar=sys.stdout
sys.stdout = f


for cc in conceitos:
    print (u"%s"%(cc,)).encode("utf8")

    q="SELECT ?al WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:altLabel ?al . }"%(cc,)
    res=g.query(PREFIX+q)
    pls=[rr[0] for rr in res]
    for pl in pls:
        print (u" forma alternativa: %s"%(pl,)).encode("utf8")
    q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:definition ?de . }"%(cc,)
    res=g.query(PREFIX+q)
    pls=[rr[0] for rr in res]
    for pl in pls:
        print (u" definição: %s"%(pl,)).encode("utf8")
    q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:scopeNote ?de . }"%(cc,)
    res=g.query(PREFIX+q)
    pls=[rr[0] for rr in res]
    for pl in pls:
        print (u" nota de escopo: %s"%(pl,)).encode("utf8")

    q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de . }"%(cc,)
    res=g.query(PREFIX+q)
    pls=[rr[0] for rr in res]
    for pl in pls:
        print (u" termo relacionado: %s"%(pl,)).encode("utf8")

f.close()

f=open("../rdf/vbsConferenciaPalavras.txt", "wb")
sys.stdout = f
for cc in conceitos:
    print (u"%s"%(cc,)).encode("utf8")

f.close()


##############################
# Conselhos


store="../rdf/vbsConselho.rdf"
g = r.Graph()
g.load(store)

PREFIX="""PREFIX skos: <http://www.w3.org/2004/02/skos/core#>"""

q="SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l . }"
res=g.query(PREFIX+q)
conceitos=[rr[0] for rr in res]



q="SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l . FILTER NOT EXISTS { ?s skos:broader ?o  }  }"
res=g.query(PREFIX+q)
conceitosPai=[rr[0] for rr in res]

cp=sorted(conceitosPai,key=lambda s: s.replace(u"á",u"a").replace(u"Á",u"a").replace(u"Ó",u"o").replace(u"ó",u"o").encode("utf8").lower())

import sys
f=open("../rdf/vbsConselho.txt", "wb")
sys.stdout = f

for cc in cp:
    print (u"|--> %s"%(cc,)).encode("utf8")

    q="SELECT ?al WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:altLabel ?al . }"%(cc,)
    res=g.query(PREFIX+q)
    pls=[rr[0] for rr in res]
    for pl in pls:
        print (u" forma alternativa: %s"%(pl,)).encode("utf8")
    q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:definition ?de . }"%(cc,)
    res=g.query(PREFIX+q)
    pls=[rr[0] for rr in res]
    for pl in pls:
        print (u" definição: %s"%(pl,)).encode("utf8")
    q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:scopeNote ?de . }"%(cc,)
    res=g.query(PREFIX+q)
    pls=[rr[0] for rr in res]
    for pl in pls:
        print (u" nota de escopo: %s"%(pl,)).encode("utf8")

    q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de . }"%(cc,)
    res=g.query(PREFIX+q)
    pls=[rr[0] for rr in res]
    for pl in pls:
        print (u" termo relacionado: %s"%(pl,)).encode("utf8")


    q=("SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l .  ?s skos:broader ?cc . ?cc skos:prefLabel '%s'@pt  }"%(cc,))
    res=g.query(PREFIX+q)
    conceitos_=[rr[0] for rr in res]
    cp2=sorted(conceitos_,key=lambda s: s.replace(u"á",u"a").replace(u"Á",u"a").replace(u"Ó",u"o").replace(u"ó",u"o").encode("utf8").lower())
    for cc2 in cp2:
        print ("   |--> %s"%(cc2,)).encode("utf8")

        q="SELECT ?al WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:altLabel ?al . }"%(cc2,)
        res=g.query(PREFIX+q)
        pls=[rr[0] for rr in res]
        for pl in pls:
            print (u"    forma alternativa: %s"%(pl,)).encode("utf8")
        q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:definition ?de . }"%(cc2,)
        res=g.query(PREFIX+q)
        pls=[rr[0] for rr in res]
        for pl in pls:
            print (u"    definição: %s"%(pl,)).encode("utf8")
        q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:scopeNote ?de . }"%(cc2,)
        res=g.query(PREFIX+q)
        pls=[rr[0] for rr in res]
        for pl in pls:
            print (u"    nota de escopo: %s"%(pl,)).encode("utf8")

        q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc2,)
        res=g.query(PREFIX+q)
        pls=[rr[0] for rr in res]
        for pl in pls:
            print (u"    termo relacionado: %s"%(pl,)).encode("utf8")




        q=("SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l .  ?s skos:broader ?cc . ?cc skos:prefLabel '%s'@pt  }"%(cc2,))
        res=g.query(PREFIX+q)
        conceitos__=[rr[0] for rr in res]
        cp3=sorted(conceitos__,key=lambda s: s.replace(u"á",u"a").replace(u"Á",u"a").replace(u"Ó",u"o").replace(u"ó",u"o").encode("utf8").lower())
        for cc3 in cp3:
            print ("     |--> %s"%(cc3,)).encode("utf8")


            q="SELECT ?al WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:altLabel ?al . }"%(cc3,)
            res=g.query(PREFIX+q)
            pls=[rr[0] for rr in res]
            for pl in pls:
                print (u"       forma alternativa: %s"%(pl,)).encode("utf8")
            q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:definition ?de . }"%(cc3,)
            res=g.query(PREFIX+q)
            pls=[rr[0] for rr in res]
            for pl in pls:
                print (u"       definição: %s"%(pl,)).encode("utf8")
            q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:scopeNote ?de . }"%(cc3,)
            res=g.query(PREFIX+q)
            pls=[rr[0] for rr in res]
            for pl in pls:
                print (u"       nota de escopo: %s"%(pl,)).encode("utf8")

            q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc3,)
            res=g.query(PREFIX+q)
            pls=[rr[0] for rr in res]
            for pl in pls:
                print (u"       termo relacionado: %s"%(pl,)).encode("utf8")


            q=("SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l .  ?s skos:broader ?cc . ?cc skos:prefLabel '%s'@pt  }"%(cc3,))
            res=g.query(PREFIX+q)
            conceitos___=[rr[0] for rr in res]
            cp4=sorted(conceitos___,key=lambda s: s.replace(u"á",u"a").replace(u"Á",u"a").replace(u"Ó",u"o").replace(u"ó",u"o").encode("utf8").lower())
            for cc4 in cp4:
                print ("         |--> %s"%(cc4,)).encode("utf8")


                q="SELECT ?al WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:altLabel ?al . }"%(cc4,)
                res=g.query(PREFIX+q)
                pls=[rr[0] for rr in res]
                for pl in pls:
                    print (u"          forma alternativa: %s"%(pl,)).encode("utf8")
                q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:definition ?de . }"%(cc4,)
                res=g.query(PREFIX+q)
                pls=[rr[0] for rr in res]
                for pl in pls:
                    print (u"          definição: %s"%(pl,)).encode("utf8")
                q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:scopeNote ?de . }"%(cc4,)
                res=g.query(PREFIX+q)
                pls=[rr[0] for rr in res]
                for pl in pls:
                    print (u"          nota de escopo: %s"%(pl,)).encode("utf8")

                q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc4,)
                res=g.query(PREFIX+q)
                pls=[rr[0] for rr in res]
                for pl in pls:
                    print (u"          termo relacionado: %s"%(pl,)).encode("utf8")





                q=("SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l .  ?s skos:broader ?cc . ?cc skos:prefLabel '%s'@pt  }"%(cc4,))
                res=g.query(PREFIX+q)
                conceitos____=[rr[0] for rr in res]
                cp5=sorted(conceitos____,key=lambda s: s.replace(u"á",u"a").replace(u"Á",u"a").replace(u"Ó",u"o").replace(u"ó",u"o").encode("utf8").lower())
                for cc5 in cp5:
                    print "+++++++++++++++++++++1 "
                    print "            |--> %s"%(cc5,)
f.close()

sys.stdout=foobar
print "feito arquivo com vocabulario"


PREFIX="""PREFIX skos: <http://www.w3.org/2004/02/skos/core#>"""

q="SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l . }"
res=g.query(PREFIX+q)
conceitos=[rr[0] for rr in res]

f=open("../rdf/vbsConselhoPodada.txt", "wb")
foobar=sys.stdout
sys.stdout = f


for cc in conceitos:
    print (u"%s"%(cc,)).encode("utf8")

    q="SELECT ?al WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:altLabel ?al . }"%(cc,)
    res=g.query(PREFIX+q)
    pls=[rr[0] for rr in res]
    for pl in pls:
        print (u" forma alternativa: %s"%(pl,)).encode("utf8")
    q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:definition ?de . }"%(cc,)
    res=g.query(PREFIX+q)
    pls=[rr[0] for rr in res]
    for pl in pls:
        print (u" definição: %s"%(pl,)).encode("utf8")
    q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:scopeNote ?de . }"%(cc,)
    res=g.query(PREFIX+q)
    pls=[rr[0] for rr in res]
    for pl in pls:
        print (u" nota de escopo: %s"%(pl,)).encode("utf8")

    q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de . }"%(cc,)
    res=g.query(PREFIX+q)
    pls=[rr[0] for rr in res]
    for pl in pls:
        print (u" termo relacionado: %s"%(pl,)).encode("utf8")

f.close()

f=open("../rdf/vbsConselhoPalavras.txt", "wb")
sys.stdout = f
for cc in conceitos:
    print (u"%s"%(cc,)).encode("utf8")

f.close()


