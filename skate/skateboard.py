import os
import pdfplumber
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def leer_y_mostrar_csv(ruta_archivo):
    # Leer el archivo CSV en un DataFrame
    df = pd.read_csv(ruta_archivo)
    
    # Mostrar todos los elementos del DataFrame
    pd.set_option('display.max_rows', None)  # Mostrar todas las filas
    pd.set_option('display.max_columns', None)  # Mostrar todas las columnas
    print(df)


def get_pdf_links(url):
    pdf_links = []

    # Realizar la solicitud GET a la URL
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Parsear el HTML de la página
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontrar todos los enlaces <a> que apunten a archivos PDF
        for link in soup.find_all('a', href=True):
            if link['href'].endswith('.html'):
                pdf_links.append(link['href'])

    return pdf_links
    
def comienza_con_entero(linea):
    try:
        primer_caracter = linea.strip()[0]
        int(primer_caracter)
        return True
    except ValueError:
        return False


def pdf_to_text(input_path, output_path):
    with open(output_path, 'a', encoding='utf-8') as text_file:
        text_file.write("last_name,first_name,total" + '\n')
        with pdfplumber.open(input_path) as pdf:
            text = ''
            page = 0
            for page in range(0,len(pdf.pages)):
                savelines = ""
                text += pdf.pages[page].extract_text()
                lines = text.split('\n')
                for line in lines:
                    if comienza_con_entero(line) and line[2] != ".":
                        lines = line.split(" ")
                        print(len(lines))
                        if (len(lines)> 5):
                            if comienza_con_entero(lines[len(lines)-1]):
                                count = len(lines)
                            else:
                                count = len(lines)-1
                            lista = [""] * 15
                            lista[14] = lines[count-1]    
                            for i in range(0,4):
                                lista[i] = lines[i]
                            pos = 4
                            if lines[pos].isalpha():
                                lista[4] = lines[pos]
                                pos = 5
                            if lines[pos].isdigit():
                                lista[5] = lines[pos]
                                pos = 6
                            j = 6
                            for i in range(pos,count-1):
                                lista[j] = lines[i]
                                j = j+1
                            
                            if lista[1].isdigit():
                              for i in range(2,13):
                                lista[i-1] = lista[i]  
                            #outline = ",".join(lista)
                            max = 0.0
                            for i in range(2,15):
                                if is_float(lista[i]):
                                    val = float(lista[i])
                                    if val > max:
                                        max = val
                            outline = lista[1] + "," + lista[2] + "," + str(max)
                            
                            outline = outline+ '\n'
                            print(outline)
                            text_file.write(outline)
                    else:
                        savelines = savelines + ", " + line
    
    
def is_float(string):
    pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)$'
    return bool(re.match(pattern, string))       

def process_all_pdfs(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    pdf_files = [f for f in os.listdir(input_folder) if f.endswith('.pdf')]

    for pdf_file in pdf_files:

        input_path = os.path.join(input_folder, pdf_file)
        output_file_name = "data.csv"# os.path.splitext(pdf_file)[0] + '.txt'
        output_path = os.path.join(output_folder, output_file_name)

        pdf_to_text(input_path, output_path)
        print(f'Converted {pdf_file} to {output_file_name} \n')
    
    leer_y_mostrar_csv(output_path)

# Ejemplo de uso
input_folder = 'datos'
output_folder = 'texts'
process_all_pdfs(input_folder, output_folder)


'''pdf_links = get_pdf_links("https://www.worldskate.org/skateboarding/results/category/1222-results.html")

if pdf_links:
    print("Enlaces a archivos PDF encontrados:")
    for link in pdf_links:
        if (link.find("/results/") != -1):
            print(link)
else:
    print("No se encontraron enlaces a archivos PDF en la página.")'''

