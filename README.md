# Vocabulário da Biblioteca (semântica de participação) Social

## Perguntas novas:
* Quando levantamos o nome de cada conferência e conselho? Somente os nacionais? De órgãos federais, como ministérios? (pegar referência na thread puxada pela Carmen)
* Uma conferência (com suas etapas e noção de processo) é um bom exemplo de trilha participativa? 
* Algum nome para um conceito que junta mecanismos e instancias participativas? "elaborações participativas"? "entidades participativas"?
* Ambiente virtual de participação social é mecanismo participativo segundo a PNPS, certo? Talvez seja o único caso de se considerar este mecanismo também uma instância participativa?

## Fontes:

* Produtos de consultores PNUD, em especial da Carmen Roncy, Fernando Cruz e Fabrício Solagna.
* Entrevistas com especialistas: Clovis, Paula, Fabrício, Fernando, Carmen, Lígia, Pedro Pontual.
* Decreto PNPS
* Workshop 20/10/2014 puxado pela SGPR para contribuições de especialistas.
* Para melhor consideração:
 * Lista de palavras-chave usadas nas publicacoes do IPEA passada por email pela Joana
 * OPA/OPS, que era o VCPS. Ver VCGE tb.
 * LCSH
 * .doc do IPEA, email posterior, com vocabulário controlado
 * Comunidades Dublin Core / outras
 * Incidência no Participa.br

 

## Formato:

XML usado pelo DSPACE. OWL e SKOS em RDF/XML e RDF/Turtle. OWL também é acompanhado pelo diagrama (.dot) e figuras deste
que apresentam as relações como encontradas no domínio. Não está sendo usadas restrição alguma de classe, universais
ou existenciais. Tampouco axiomas de propriedade. Isso permite maior flexibilidade neste momento inicial,
e simplifica as inferências para relações de subclasse (rdfs:subClassOf) e subpropriedade (rdfs:subPropertyOf).
O vocabulário não possui diagrama, mas formatos em texto simples são apresentados com informações adicionais e em árvore,
sem as relações de árvore e somente os termos.

### Versões antigas:

* Com todas as palavras de todos estes vocabulários (vocabulario/vp-lista.xml)
* Separada por fonte (IPEA, LCSH, etc) via hierarquia interna do vocabulário (vocabulario/vp-fonte.xml)

### Versões planejadas:
* Com seleção coesa, nuclear, com critérios anotados para as remoções.
* Fruto de mais retornos da equipe do participa.br e outras fontes (este vocabulário está ainda germinando).

## Pastas e arquivos:

* Na pasta fontes/, algumas fontes dos trabalhos.
* Na pasta vocabulario/, versões do vocabulario para DSPACE.
* Na pasta rdf/, versões do vocabulario e ontologia em RDF (SKOS e OWL).
* Na pasta rdf/, versões do vocabulario texto simples, com 3 grados de enriquecimento informacional: 1) comente os verbetes; 2) verbetes com informações adicionais; 3) verbetes em árvore com informações adicionais.
* Na pasta bibliografia/, alguns arquivos e documentos de importância imediata para o trabalho feito.
* Na pasta scripts/ os scripts que fazem o xml ou outras representações do vocabulário.
 * Por exemplo: triplificaConferencias.py e triplificaConselhos.py triplificam os dados em fontes/base\_dados...ipea..ods.
 * Os scripts com início "vbs" levantam o vocabulário da biblioteca social e entregam SKOS em RDF/XML e RDF/Turtle (ex: vbsOuvidorias.py, vbsConselhos.py, vbsConferencias.py, vbsPNPS.py geram arquivos rdf/vbs\*)
 * Os scripts com início "obs" levantam a ontologia da biblioteca social e entregam OWL em RDF/XML e RDF/Turtle (ex: vbsOuvidorias.py, vbsConselhos.py, vbsConferencias.py, vbsPNPS.py geram arquivos rdf/obs\*) junto aos diagramas (figs/\*.dot) e figuras (figs/\*.png). 
 * Scripts com começo "dspace" aproveitam os SKOS produzidos para entregar um XML no formato usado pelo DSPACE (vocabulario/\*).
 * vocabTexto.py aproveita os SKOS produzidos para entregar vocabulário em texto simples (rdf/\*.txt) com a árvore taxonômica e informações adicionais, somente com as informações adicionais e verbetes em sequência.

## Descrição, estratégia e etapa:

Estes vocabulários foram levantados pelas fontes apontadas pela equipe do Participa.br
e outras partes ligadas à Secretaria Geral da Presidência da República
para etiquetar documentos da biblioteca digital de participação social, sendo elaborada.

A estratégia para realização do vocabulário é bastante dependente do uso inicial que dela terá,
pois tanto a biblioteca quanto este vocabulário estão surgindo no momento desta escrita.
Há forte embasamento com o conhecimento aprofundado de alguns
membros da equipe do participa.br e da SNAS.

A etapa atual é de entrega deste vocabulário para a comunidade ligada à biblioteca digital de participação social.
Os primeiros retornos sobre este levantamento são positivos e estão sendo estudados para serem integralmente contemplados.
A comunidade de biblioteconomia e ciência da informação possui provavelmente
a maior herança de melhora e ampliação de acesso à informação, e os rumos
deste vocabulário podem ser os mais diversos, com potenciais novas versões,
 formatações, amadurecimentos e usos.

### Próximos passos

* Consideração dos thesaurus e vocabulários controlados maiores, como o LCSH, o Vocabulário controlado do IPEA e o VCGE.
* Consideração dos vocabulários de comunidades dedicadas (dublin core, w3c, etc).
* Adicionar provenance aos vocábulos skos para saber fonte do termo.
* Fazer uso explícito de subgrafos para as ontologias e de concept schemes para os vocabulários skos. Ver voiD.

## Contato:

Equipe do http://participa.br
Canal IRC: #labmacambira @ Freenode
