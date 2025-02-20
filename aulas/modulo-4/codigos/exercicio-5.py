import xml.etree.ElementTree as ET

tree = ET.parse("dados_usuarios.xml")
root = tree.getroot()

for usuario in root.findall("usuario"):
    nome = usuario.find("nome").text
    print(f"Nome: {nome}")