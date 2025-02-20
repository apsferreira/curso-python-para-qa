import requests
import pandas as pd
import xml.etree.ElementTree as ET
import os

# URL do arquivo JSON
url = "https://jsonplaceholder.typicode.com/users"

# Caminho da pasta onde os arquivos serão salvos
output_dir = r"C:\temp\curso-python-para-qa\contribuicoes\gabriel_tavares\aula-7\projeto-qa-3\logs"

# Diretório existe
os.makedirs(output_dir, exist_ok=True)

# Baixar o JSON
def download_json(url):
    response = requests.get(url)
    response.raise_for_status()  # Levanta um erro se a requisição falhar
    return response.json()

# JSON para CSV
def json_to_csv(json_data, csv_file):
    df = pd.DataFrame(json_data)
    df.to_csv(csv_file, index=False)
    print(f"Arquivo CSV salvo como: {csv_file}")

# JSON para XML
def json_to_xml(json_data, xml_file):
    root = ET.Element("users")
    
    for user in json_data:
        user_element = ET.SubElement(root, "user")
        for key, value in user.items():
            child = ET.SubElement(user_element, key)
            child.text = str(value)
    
    tree = ET.ElementTree(root)
    tree.write(xml_file)
    print(f"Arquivo XML salvo como: {xml_file}")

if __name__ == "__main__":
    json_data = download_json(url)
    
    # Caminhos dos arquivos
    csv_file_path = os.path.join(output_dir, "users.csv")
    xml_file_path = os.path.join(output_dir, "users.xml")
    
    # Converter para CSV
    json_to_csv(json_data, csv_file_path)
    
    # Converter para XML
    json_to_xml(json_data, xml_file_path)