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
f=open("../txt/vbsConferencia.txt", "wb")
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

    q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de . ?de skos:prefLabel ?lde }"%(cc,)
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

        #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc2,)
        q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de . ?de skos:prefLabel ?lde }"%(cc2,)
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

            #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc3,)
            q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de . ?de skos:prefLabel ?lde }"%(cc3,)
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

                #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc4,)
                q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de . ?de skos:prefLabel ?lde }"%(cc4,)
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
conceitos=sorted(conceitos,key=lambda s: s.replace(u"á",u"a").replace(u"Á",u"a").replace(u"Ó",u"o").replace(u"ó",u"o").encode("utf8").lower())

f=open("../txt/vbsConferenciaPodada.txt", "wb")
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

    #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de . }"%(cc,)
    q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de . ?de skos:prefLabel ?lde }"%(cc,)
    res=g.query(PREFIX+q)
    pls=[rr[0] for rr in res]
    for pl in pls:
        print (u" termo relacionado: %s"%(pl,)).encode("utf8")

f.close()

f=open("../txt/vbsConferenciaPalavras.txt", "wb")
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
f=open("../txt/vbsConselho.txt", "wb")
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

    q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de . ?de skos:prefLabel ?lde }"%(cc,)
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

        #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc2,)
        q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc2,)
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

            #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc3,)
            q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc3,)
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

                #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc4,)
                q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc4,)
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
conceitos=sorted(conceitos,key=lambda s: s.replace(u"á",u"a").replace(u"Á",u"a").replace(u"Ó",u"o").replace(u"ó",u"o").encode("utf8").lower())

f=open("../txt/vbsConselhoPodada.txt", "wb")
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

    #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de . }"%(cc,)
    q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc,)
    res=g.query(PREFIX+q)
    pls=[rr[0] for rr in res]
    for pl in pls:
        print (u" termo relacionado: %s"%(pl,)).encode("utf8")

f.close()

f=open("../txt/vbsConselhoPalavras.txt", "wb")
sys.stdout = f
for cc in conceitos:
    print (u"%s"%(cc,)).encode("utf8")

f.close()

#########################3
# Ouvidorias TTM

store="../rdf/vbsOuvidoria.rdf"
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
f=open("../txt/vbsOuvidoria.txt", "wb")
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

    q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de . ?de skos:prefLabel ?lde }"%(cc,)
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

        #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc2,)
        q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc2,)
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

            #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc3,)
            q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc3,)
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

                #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc4,)
                q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc4,)
                res=g.query(PREFIX+q)
                pls=[rr[0] for rr in res]
                for pl in pls:
                    print (u"          termo relacionado: %s"%(pl,)).encode("utf8")





                q=("SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l .  ?s skos:broader ?cc . ?cc skos:prefLabel '%s'@pt  }"%(cc4,))
                res=g.query(PREFIX+q)
                conceitos____=[rr[0] for rr in res]
                cp5=sorted(conceitos____,key=lambda s: s.replace(u"á",u"a").replace(u"Á",u"a").replace(u"ã",u"a").replace(u"Ó",u"o").replace(u"ó",u"o").replace(u"é",u"e").replace(u"í",u"i").replace(u"ú",u"ú").replace(u"ç",u"c").encode("utf8").lower())
                print "boo", cp5
                for cc5 in cp5:
                    print u"+++++++++++++++++++++1 ", cc5
                    print u"            |--> %s"%(cc5,)
f.close()

sys.stdout=foobar
print "feito arquivo com vocabulario"


PREFIX="""PREFIX skos: <http://www.w3.org/2004/02/skos/core#>"""

q="SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l . }"
res=g.query(PREFIX+q)
conceitos=[rr[0] for rr in res]
conceitos=sorted(conceitos,key=lambda s: s.replace(u"á",u"a").replace(u"Á",u"a").replace(u"Ó",u"o").replace(u"ó",u"o").encode("utf8").lower())

f=open("../txt/vbsOuvidoriaPodada.txt", "wb")
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

    #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de . }"%(cc,)
    q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc,)
    res=g.query(PREFIX+q)
    pls=[rr[0] for rr in res]
    for pl in pls:
        print (u" termo relacionado: %s"%(pl,)).encode("utf8")

f.close()

f=open("../txt/vbsOuvidoriaPalavras.txt", "wb")
sys.stdout = f
for cc in conceitos:
    print (u"%s"%(cc,)).encode("utf8")

f.close()

##################
## PNPS TTM

store="../rdf/vbsPNPS.rdf"
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
f=open("../txt/vbsPNPS.txt", "wb")
#sys.stdout = foobar
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

    q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de . ?de skos:prefLabel ?lde }"%(cc,)
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

        #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc2,)
        q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc2,)
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

            #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc3,)
            q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc3,)
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

                #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc4,)
                q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc4,)
                res=g.query(PREFIX+q)
                pls=[rr[0] for rr in res]
                for pl in pls:
                    print (u"          termo relacionado: %s"%(pl,)).encode("utf8")





                q=("SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l .  ?s skos:broader ?cc . ?cc skos:prefLabel '%s'@pt  }"%(cc4,))
                res=g.query(PREFIX+q)
                conceitos____=[rr[0] for rr in res]
                cp5=sorted(conceitos____,key=lambda s: s.replace(u"á",u"a").replace(u"Á",u"a").replace(u"ê",u"a").replace(u"ã",u"a").replace(u"Ó",u"o").replace(u"ó",u"o").replace(u"é",u"e").replace(u"í",u"i").replace(u"ú",u"ú").replace(u"ç",u"c").encode("utf8").lower())
                print "boo", cp5
                for cc5 in cp5:
                    print ("         |--> %s"%(cc5,)).encode("utf8")


                    q="SELECT ?al WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:altLabel ?al . }"%(cc5,)
                    res=g.query(PREFIX+q)
                    pls=[rr[0] for rr in res]
                    for pl in pls:
                        print (u"          forma alternativa: %s"%(pl,)).encode("utf8")
                    q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:definition ?de . }"%(cc5,)
                    res=g.query(PREFIX+q)
                    pls=[rr[0] for rr in res]
                    for pl in pls:
                        print (u"          definição: %s"%(pl,)).encode("utf8")
                    q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:scopeNote ?de . }"%(cc5,)
                    res=g.query(PREFIX+q)
                    pls=[rr[0] for rr in res]
                    for pl in pls:
                        print (u"          nota de escopo: %s"%(pl,)).encode("utf8")

                    #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc4,)
                    q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc5,)
                    res=g.query(PREFIX+q)
                    pls=[rr[0] for rr in res]
                    for pl in pls:
                        print (u"          termo relacionado: %s"%(pl,)).encode("utf8")

                    q=("SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l .  ?s skos:broader ?cc . ?cc skos:prefLabel '%s'@pt  }"%(cc5,))
                    res=g.query(PREFIX+q)
                    conceitos____=[rr[0] for rr in res]
                    cp6=sorted(conceitos____,key=lambda s: s.replace(u"á",u"a").replace(u"Á",u"a").replace(u"ê",u"a").replace(u"ã",u"a").replace(u"Ó",u"o").replace(u"ó",u"o").replace(u"é",u"e").replace(u"í",u"i").replace(u"ú",u"ú").replace(u"ç",u"c").encode("utf8").lower())
                    print "boo", cp5
                    for cc6 in cp6:
                        print u"+++++++++++++++++++++1 ", cc6
                        print u"            |--> %s"%(cc6,)






f.close()

sys.stdout=foobar
print "feito arquivo com vocabulario"


PREFIX="""PREFIX skos: <http://www.w3.org/2004/02/skos/core#>"""

q="SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l . }"
res=g.query(PREFIX+q)
conceitos=[rr[0] for rr in res]
conceitos=sorted(conceitos,key=lambda s: s.replace(u"á",u"a").replace(u"Á",u"a").replace(u"Ó",u"o").replace(u"ó",u"o").encode("utf8").lower())

f=open("../txt/vbsPNPSPodada.txt", "wb")
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

    #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de . }"%(cc,)
    q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc,)
    res=g.query(PREFIX+q)
    pls=[rr[0] for rr in res]
    for pl in pls:
        print (u" termo relacionado: %s"%(pl,)).encode("utf8")

f.close()

f=open("../txt/vbsPNPSPalavras.txt", "wb")
sys.stdout = f
for cc in conceitos:
    print (u"%s"%(cc,)).encode("utf8")

f.close()
sys.stdout = foobar
print "feito arquivos com vocabulario da PNPS"

##################
## MESA TTM

store="../rdf/vbsMesaDeDialogo.rdf"
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
f=open("../txt/vbsMesaDeDialogo.txt", "wb")
#sys.stdout = foobar
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

    q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de . ?de skos:prefLabel ?lde }"%(cc,)
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

        #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc2,)
        q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc2,)
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

            #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc3,)
            q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc3,)
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

                #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc4,)
                q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc4,)
                res=g.query(PREFIX+q)
                pls=[rr[0] for rr in res]
                for pl in pls:
                    print (u"          termo relacionado: %s"%(pl,)).encode("utf8")





                q=("SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l .  ?s skos:broader ?cc . ?cc skos:prefLabel '%s'@pt  }"%(cc4,))
                res=g.query(PREFIX+q)
                conceitos____=[rr[0] for rr in res]
                cp5=sorted(conceitos____,key=lambda s: s.replace(u"á",u"a").replace(u"Á",u"a").replace(u"ê",u"a").replace(u"ã",u"a").replace(u"Ó",u"o").replace(u"ó",u"o").replace(u"é",u"e").replace(u"í",u"i").replace(u"ú",u"ú").replace(u"ç",u"c").encode("utf8").lower())
                print "boo", cp5
                for cc5 in cp5:
                    print ("         |--> %s"%(cc5,)).encode("utf8")


                    q="SELECT ?al WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:altLabel ?al . }"%(cc5,)
                    res=g.query(PREFIX+q)
                    pls=[rr[0] for rr in res]
                    for pl in pls:
                        print (u"          forma alternativa: %s"%(pl,)).encode("utf8")
                    q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:definition ?de . }"%(cc5,)
                    res=g.query(PREFIX+q)
                    pls=[rr[0] for rr in res]
                    for pl in pls:
                        print (u"          definição: %s"%(pl,)).encode("utf8")
                    q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:scopeNote ?de . }"%(cc5,)
                    res=g.query(PREFIX+q)
                    pls=[rr[0] for rr in res]
                    for pl in pls:
                        print (u"          nota de escopo: %s"%(pl,)).encode("utf8")

                    #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc4,)
                    q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc5,)
                    res=g.query(PREFIX+q)
                    pls=[rr[0] for rr in res]
                    for pl in pls:
                        print (u"          termo relacionado: %s"%(pl,)).encode("utf8")

                    q=("SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l .  ?s skos:broader ?cc . ?cc skos:prefLabel '%s'@pt  }"%(cc5,))
                    res=g.query(PREFIX+q)
                    conceitos____=[rr[0] for rr in res]
                    cp6=sorted(conceitos____,key=lambda s: s.replace(u"á",u"a").replace(u"Á",u"a").replace(u"ê",u"a").replace(u"ã",u"a").replace(u"Ó",u"o").replace(u"ó",u"o").replace(u"é",u"e").replace(u"í",u"i").replace(u"ú",u"ú").replace(u"ç",u"c").encode("utf8").lower())
                    print "boo", cp5
                    for cc6 in cp6:
                        print u"+++++++++++++++++++++1 ", cc6
                        print u"            |--> %s"%(cc6,)






f.close()

sys.stdout=foobar
print "feito arquivo com vocabulario"


PREFIX="""PREFIX skos: <http://www.w3.org/2004/02/skos/core#>"""

q="SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l . }"
res=g.query(PREFIX+q)
conceitos=[rr[0] for rr in res]
conceitos=sorted(conceitos,key=lambda s: s.replace(u"á",u"a").replace(u"Á",u"a").replace(u"Ó",u"o").replace(u"ó",u"o").encode("utf8").lower())

f=open("../txt/vbsMesaDeDialogoPodada.txt", "wb")
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

    #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de . }"%(cc,)
    q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc,)
    res=g.query(PREFIX+q)
    pls=[rr[0] for rr in res]
    for pl in pls:
        print (u" termo relacionado: %s"%(pl,)).encode("utf8")

f.close()

f=open("../txt/vbsMesaDeDialogoPalavras.txt", "wb")
sys.stdout = f
for cc in conceitos:
    print (u"%s"%(cc,)).encode("utf8")

f.close()
sys.stdout = foobar
print "feito arquivos com vocabulario da PNPS"

##################
## DOCS TTM

store="../rdf/vbsDocumentacaoVBS.rdf"
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
f=open("../txt/vbsDocumentacaoVBS.txt", "wb")
#sys.stdout = foobar
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

    q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de . ?de skos:prefLabel ?lde }"%(cc,)
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

        #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc2,)
        q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc2,)
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

            #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc3,)
            q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc3,)
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

                #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc4,)
                q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc4,)
                res=g.query(PREFIX+q)
                pls=[rr[0] for rr in res]
                for pl in pls:
                    print (u"          termo relacionado: %s"%(pl,)).encode("utf8")





                q=("SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l .  ?s skos:broader ?cc . ?cc skos:prefLabel '%s'@pt  }"%(cc4,))
                res=g.query(PREFIX+q)
                conceitos____=[rr[0] for rr in res]
                cp5=sorted(conceitos____,key=lambda s: s.replace(u"á",u"a").replace(u"Á",u"a").replace(u"ê",u"a").replace(u"ã",u"a").replace(u"Ó",u"o").replace(u"ó",u"o").replace(u"é",u"e").replace(u"í",u"i").replace(u"ú",u"ú").replace(u"ç",u"c").encode("utf8").lower())
                print "boo", cp5
                for cc5 in cp5:
                    print ("         |--> %s"%(cc5,)).encode("utf8")


                    q="SELECT ?al WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:altLabel ?al . }"%(cc5,)
                    res=g.query(PREFIX+q)
                    pls=[rr[0] for rr in res]
                    for pl in pls:
                        print (u"          forma alternativa: %s"%(pl,)).encode("utf8")
                    q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:definition ?de . }"%(cc5,)
                    res=g.query(PREFIX+q)
                    pls=[rr[0] for rr in res]
                    for pl in pls:
                        print (u"          definição: %s"%(pl,)).encode("utf8")
                    q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:scopeNote ?de . }"%(cc5,)
                    res=g.query(PREFIX+q)
                    pls=[rr[0] for rr in res]
                    for pl in pls:
                        print (u"          nota de escopo: %s"%(pl,)).encode("utf8")

                    #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc4,)
                    q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc5,)
                    res=g.query(PREFIX+q)
                    pls=[rr[0] for rr in res]
                    for pl in pls:
                        print (u"          termo relacionado: %s"%(pl,)).encode("utf8")

                    q=("SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l .  ?s skos:broader ?cc . ?cc skos:prefLabel '%s'@pt  }"%(cc5,))
                    res=g.query(PREFIX+q)
                    conceitos____=[rr[0] for rr in res]
                    cp6=sorted(conceitos____,key=lambda s: s.replace(u"á",u"a").replace(u"Á",u"a").replace(u"ê",u"a").replace(u"ã",u"a").replace(u"Ó",u"o").replace(u"ó",u"o").replace(u"é",u"e").replace(u"í",u"i").replace(u"ú",u"ú").replace(u"ç",u"c").encode("utf8").lower())
                    print "boo", cp5
                    for cc6 in cp6:
                        print u"+++++++++++++++++++++1 ", cc6
                        print u"            |--> %s"%(cc6,)






f.close()

sys.stdout=foobar
print "feito arquivo com vocabulario"


PREFIX="""PREFIX skos: <http://www.w3.org/2004/02/skos/core#>"""

q="SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l . }"
res=g.query(PREFIX+q)
conceitos=[rr[0] for rr in res]
conceitos=sorted(conceitos,key=lambda s: s.replace(u"á",u"a").replace(u"Á",u"a").replace(u"Ó",u"o").replace(u"ó",u"o").encode("utf8").lower())

f=open("../txt/vbsDocumentacaoVBSPodada.txt", "wb")
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

    #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de . }"%(cc,)
    q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc,)
    res=g.query(PREFIX+q)
    pls=[rr[0] for rr in res]
    for pl in pls:
        print (u" termo relacionado: %s"%(pl,)).encode("utf8")

f.close()

f=open("../txt/vbsDocumentacaoVBSPalavras.txt", "wb")
sys.stdout = f
for cc in conceitos:
    print (u"%s"%(cc,)).encode("utf8")

f.close()
sys.stdout = foobar
print "feito arquivos com vocabulario da Documentacao de referencia"

##################
## DOCS e Resultados de conferências TTM

store="../rdf/vbsConferenciaDocsRes.rdf"
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
f=open("../txt/vbsConferenciaDocsRes.txt", "wb")
#sys.stdout = foobar
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

    q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de . ?de skos:prefLabel ?lde }"%(cc,)
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

        #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc2,)
        q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc2,)
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

            #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc3,)
            q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc3,)
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

                #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc4,)
                q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc4,)
                res=g.query(PREFIX+q)
                pls=[rr[0] for rr in res]
                for pl in pls:
                    print (u"          termo relacionado: %s"%(pl,)).encode("utf8")





                q=("SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l .  ?s skos:broader ?cc . ?cc skos:prefLabel '%s'@pt  }"%(cc4,))
                res=g.query(PREFIX+q)
                conceitos____=[rr[0] for rr in res]
                cp5=sorted(conceitos____,key=lambda s: s.replace(u"á",u"a").replace(u"Á",u"a").replace(u"ê",u"a").replace(u"ã",u"a").replace(u"Ó",u"o").replace(u"ó",u"o").replace(u"é",u"e").replace(u"í",u"i").replace(u"ú",u"ú").replace(u"ç",u"c").encode("utf8").lower())
                print "boo", cp5
                for cc5 in cp5:
                    print ("         |--> %s"%(cc5,)).encode("utf8")


                    q="SELECT ?al WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:altLabel ?al . }"%(cc5,)
                    res=g.query(PREFIX+q)
                    pls=[rr[0] for rr in res]
                    for pl in pls:
                        print (u"          forma alternativa: %s"%(pl,)).encode("utf8")
                    q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:definition ?de . }"%(cc5,)
                    res=g.query(PREFIX+q)
                    pls=[rr[0] for rr in res]
                    for pl in pls:
                        print (u"          definição: %s"%(pl,)).encode("utf8")
                    q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:scopeNote ?de . }"%(cc5,)
                    res=g.query(PREFIX+q)
                    pls=[rr[0] for rr in res]
                    for pl in pls:
                        print (u"          nota de escopo: %s"%(pl,)).encode("utf8")

                    #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc4,)
                    q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc5,)
                    res=g.query(PREFIX+q)
                    pls=[rr[0] for rr in res]
                    for pl in pls:
                        print (u"          termo relacionado: %s"%(pl,)).encode("utf8")

                    q=("SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l .  ?s skos:broader ?cc . ?cc skos:prefLabel '%s'@pt  }"%(cc5,))
                    res=g.query(PREFIX+q)
                    conceitos____=[rr[0] for rr in res]
                    cp6=sorted(conceitos____,key=lambda s: s.replace(u"á",u"a").replace(u"Á",u"a").replace(u"ê",u"a").replace(u"ã",u"a").replace(u"Ó",u"o").replace(u"ó",u"o").replace(u"é",u"e").replace(u"í",u"i").replace(u"ú",u"ú").replace(u"ç",u"c").encode("utf8").lower())
                    print "boo", cp5
                    for cc6 in cp6:
                        print u"+++++++++++++++++++++1 ", cc6
                        print u"            |--> %s"%(cc6,)






f.close()

sys.stdout=foobar
print "feito arquivo com vocabulario"


PREFIX="""PREFIX skos: <http://www.w3.org/2004/02/skos/core#>"""

q="SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l . }"
res=g.query(PREFIX+q)
conceitos=[rr[0] for rr in res]
conceitos=sorted(conceitos,key=lambda s: s.replace(u"á",u"a").replace(u"Á",u"a").replace(u"Ó",u"o").replace(u"ó",u"o").encode("utf8").lower())

f=open("../txt/vbsConferenciaDocsResPodada.txt", "wb")
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

    #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de . }"%(cc,)
    q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc,)
    res=g.query(PREFIX+q)
    pls=[rr[0] for rr in res]
    for pl in pls:
        print (u" termo relacionado: %s"%(pl,)).encode("utf8")

f.close()

f=open("../txt/vbsConferenciaDocsResPalavras.txt", "wb")
sys.stdout = f
for cc in conceitos:
    print (u"%s"%(cc,)).encode("utf8")

f.close()
sys.stdout = foobar
print "feito arquivos com vocabulario dos documentos e resultados de conferencias"

##################
## consultas públicas TTM

store="../rdf/vbsConsulta.rdf"
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
f=open("../txt/vbsConsulta.txt", "wb")
#sys.stdout = foobar
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

    q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de . ?de skos:prefLabel ?lde }"%(cc,)
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

        #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc2,)
        q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc2,)
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

            #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc3,)
            q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc3,)
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

                #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc4,)
                q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc4,)
                res=g.query(PREFIX+q)
                pls=[rr[0] for rr in res]
                for pl in pls:
                    print (u"          termo relacionado: %s"%(pl,)).encode("utf8")





                q=("SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l .  ?s skos:broader ?cc . ?cc skos:prefLabel '%s'@pt  }"%(cc4,))
                res=g.query(PREFIX+q)
                conceitos____=[rr[0] for rr in res]
                cp5=sorted(conceitos____,key=lambda s: s.replace(u"á",u"a").replace(u"Á",u"a").replace(u"ê",u"a").replace(u"ã",u"a").replace(u"Ó",u"o").replace(u"ó",u"o").replace(u"é",u"e").replace(u"í",u"i").replace(u"ú",u"ú").replace(u"ç",u"c").encode("utf8").lower())
                print "boo", cp5
                for cc5 in cp5:
                    print ("         |--> %s"%(cc5,)).encode("utf8")


                    q="SELECT ?al WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:altLabel ?al . }"%(cc5,)
                    res=g.query(PREFIX+q)
                    pls=[rr[0] for rr in res]
                    for pl in pls:
                        print (u"          forma alternativa: %s"%(pl,)).encode("utf8")
                    q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:definition ?de . }"%(cc5,)
                    res=g.query(PREFIX+q)
                    pls=[rr[0] for rr in res]
                    for pl in pls:
                        print (u"          definição: %s"%(pl,)).encode("utf8")
                    q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:scopeNote ?de . }"%(cc5,)
                    res=g.query(PREFIX+q)
                    pls=[rr[0] for rr in res]
                    for pl in pls:
                        print (u"          nota de escopo: %s"%(pl,)).encode("utf8")

                    #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?s2 . ?s2 skos:prefLabel ?de . }"%(cc4,)
                    q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc5,)
                    res=g.query(PREFIX+q)
                    pls=[rr[0] for rr in res]
                    for pl in pls:
                        print (u"          termo relacionado: %s"%(pl,)).encode("utf8")

                    q=("SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l .  ?s skos:broader ?cc . ?cc skos:prefLabel '%s'@pt  }"%(cc5,))
                    res=g.query(PREFIX+q)
                    conceitos____=[rr[0] for rr in res]
                    cp6=sorted(conceitos____,key=lambda s: s.replace(u"á",u"a").replace(u"Á",u"a").replace(u"ê",u"a").replace(u"ã",u"a").replace(u"Ó",u"o").replace(u"ó",u"o").replace(u"é",u"e").replace(u"í",u"i").replace(u"ú",u"ú").replace(u"ç",u"c").encode("utf8").lower())
                    print "boo", cp5
                    for cc6 in cp6:
                        print u"+++++++++++++++++++++1 ", cc6
                        print u"            |--> %s"%(cc6,)






f.close()

sys.stdout=foobar
print "feito arquivo com vocabulario"


PREFIX="""PREFIX skos: <http://www.w3.org/2004/02/skos/core#>"""

q="SELECT ?l WHERE {?s a skos:Concept. ?s skos:prefLabel ?l . }"
res=g.query(PREFIX+q)
conceitos=[rr[0] for rr in res]
conceitos=sorted(conceitos,key=lambda s: s.replace(u"á",u"a").replace(u"Á",u"a").replace(u"Ó",u"o").replace(u"ó",u"o").encode("utf8").lower())

f=open("../txt/vbsConsultaPodada.txt", "wb")
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

    #q="SELECT ?de WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de . }"%(cc,)
    q="SELECT ?lde WHERE {?s a skos:Concept. ?s skos:prefLabel '%s'@pt .  ?s skos:related ?de .  ?de skos:prefLabel ?lde }"%(cc,)
    res=g.query(PREFIX+q)
    pls=[rr[0] for rr in res]
    for pl in pls:
        print (u" termo relacionado: %s"%(pl,)).encode("utf8")

f.close()

f=open("../txt/vbsConsultaPalavras.txt", "wb")
sys.stdout = f
for cc in conceitos:
    print (u"%s"%(cc,)).encode("utf8")

f.close()
sys.stdout = foobar
print "feito arquivos com vocabulario da consulta publica"


