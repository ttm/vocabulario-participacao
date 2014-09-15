#!python3
#-*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
#from xml.etree import ElementTree as ET
root = ET.Element('node')
root.set("id","vocab_part")
root.set("label",u"vocabulário controlado para biblioteca de participação social")
foo= ET.SubElement(root, "isComposedBy")
termo = ET.SubElement(foo, "node")
termo.set("id","oid")
termo.set("label","otermo")
tree = ET.ElementTree(root)
tree.write('vp.xml', xml_declaration=True, encoding='utf-8')
# para deixar bem formatado:
# ! xmllint --format - 
