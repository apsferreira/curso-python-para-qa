import json
import xml.etree.ElementTree as ET

tree = ET.parse("usuarios.xml")
root = tree.getroot()

usuarios = []

for usuario in root.findall("usuario"):
    id_usuario = usuario.find("id").text
    nome = usuario.find("nome").text
    email = usuario.find("email").text
    usuarios.append({"id": id_usuario, "nome": nome, "email": email})

with open("usuarios_convertidos.json", "w") as arquivo_json:
    json.dump(usuarios, arquivo_json, indent=4)


print("dados convertidos de xml para json")