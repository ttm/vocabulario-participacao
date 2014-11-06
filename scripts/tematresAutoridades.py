#-*- coding: utf-8 -*-
f=open("../fontes/autoridades.csv","rb")
ff=f.readlines()
l=[fff.split(";") for fff in ff]
ll=[lll[1][1:-1].strip() for lll in l[1:]]
f=open("../txt/tematresAutoridades.txt","wb")
for palavra in set(ll):
    #termo = ET.SubElement(foo, "node")
    #termo.set("id",str(conta_id))
    #conta_id+=1
    # Para deixar em caixa alta somente as palavras mais
    # significativas, conforme modelo recebido
    #palavra_=" ".join(w.capitalize() if w not in ["com",u"não","ad","dos","ou","de","e","da","do","na","no","ao",u"à"] else w for w in palavra.split()).replace("Sac","SAC").replace("(sistema","(Sistema").replace("Lai","LAI").replace("(lei","(Lei").replace("Ogu","OGU").replace("(ouvidoria","(Ouvidoria")
    #termo.set("label",palavra_.decode("utf-8"))
    #termo.set("label",palavra_.encode("utf-8"))
    #termo.set("label",palavra_)
    f.write(palavra.decode("utf-8").encode("utf-8")+"\n")
f.close()

