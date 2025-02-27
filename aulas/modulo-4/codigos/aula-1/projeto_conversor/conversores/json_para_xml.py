import json
import xml.etree.ElementTree as ET

def json_para_xml(json_file, xml_file):
    with open(json_file, "r") as arquivo_json:
        dados = json.load(arquivo_json)

    root = ET.Element("usuarios")

    for usuario in dados:
        usuario_elemento = ET.SubElement(root, "usuario")

        id_elemento = ET.SubElement(usuario_elemento, "id")
        id_elemento.text = str(usuario["id"])

        nome_elemento = ET.SubElement(usuario_elemento, "nome")
        nome_elemento.text = str(usuario["nome"])

        email_elemento = ET.SubElement(usuario_elemento, "email")
        email_elemento.text = str(usuario["email"])

    tree = ET.ElementTree(root)
    tree.write(xml_file)

    print("arquivo json convertido para xml | arquivo usuarios.xml criado")