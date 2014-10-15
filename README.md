# Vocabulário Controlado para Biblioteca Digital de Participação Social

## Perguntas novas:
* Para as URIs é fortemente recomendado usar nomes em ingles, para facilitar reuso mesmo. Tudo bem as URIs estarem com nomes em ingles? Ex: http://purl.org/socialparticipation/Council no lugar de http://purl.org/socialparticipation/Conselho
* Querem que inclua no vocabulário o nome de cada conferência e conselho? Somente os nacionais? De órgãos federais, como ministérios?
* Preferem área política ou área temática?

## Fontes:

* Lista de palavras-chave usadas nas publicacoes do IPEA passada por email pela Joana
* Decreto PNPS
* Incidência no Participa.br
* Comunidades Dublin Core / outras
* OPA/OPS, que era o VCPS. Ver VCGE tb.
* LCSH
* .doc do IPEA, email posterior, com vocabulário controlado
 

## Formato:

Repassado pelo Ricardo Poppi como exemplo para formatar vocabulário.

### Versões atuais:

* Com todas as palavras de todos estes vocabulários (vocabulario/vp-lista.xml)
* Separada por fonte (IPEA, LCSH, etc) via hierarquia interna do vocabulário (vocabulario/vp-fonte.xml)

### Versões planejadas:
* Com seleção coesa, com critérios anotados para as remoções.
* Fruto dos retornos da equipe do participa.br (este vocabulário está ainda germinando).

## Pastas e arquivos:

* Na pasta fontes/, as fontes dos trabalhos.
* Na pasta vocabulario/, as versões do vocabulario.
* Na pasta bibliografia/, arquivos e documentos de importância imediata para o trabalho feito.
* Na pasta scripts/ os scripts que fazem o xml ou outras representações do vocabulário.
 * triplificaConferencias.py e triplificaConselhos.py triplificam os dados em fontes/base\_dados...ipea..ods

## Descrição, estratégia e etapa:

Este vocabulário foi levantado pelas fontes apontadas pela equipe do Participa.br
e outras partes ligadas à Secretaria Geral da Presidência da República
para etiquetar documentos da biblioteca digital de participação social, sendo elaborada.

A estratégia para realização do vocabulário é bastante dependente do uso inicial que dela terá,
pois tanto a biblioteca quanto este vocabulário estão surgindo no momento desta escrita.
Assim, foram levantadas algumas versões que combinam o repertório inicial levantado de vocabulários
com classificação (fonte) e filtragem (seleção) iniciais.
Há também forte embasamento com o conhecimento aprofundado de alguns
membros da equipe do participa.br e da SNAS.

A etapa atual é de entrega deste vocabulário para a comunidade ligada à biblioteca digital de participação social.
Os primeiros retornos sobre este levantamento ainda estão por vir.
A comunidade de biblioteconomia e ciência da informação possui provavelmente
a maior herança de melhora e ampliação de acesso à informação, e os rumos
deste vocabulário podem ser os mais diversos, com potenciais novas versões,
 formatações, amadurecimentos e usos.

### Próximos passos

* Consideração dos thesaurus e vocabulários controlados maiores, como o LCSH, o Vocabulário controlado do IPEA e o VCGE.
* Possível implementação em SKOS.
* Consideração dos vocabulários de comunidades dedicadas (dublin core, w3c, etc).
* Orientação do prof. Fernando para condução do trabalho. Em resumo:
 * A formatação é esta?
 * Recomenda uma seleção de antemão destes termos?
 * Onde estão os termos de referência?
 * Como prefere conduzir o trabalho?

## Contato:

Equipe do http://participa.br
Canal IRC: #labmacambira @ Freenode
