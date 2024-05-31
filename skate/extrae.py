import os
import fitz  # Esta es la librería pymupdf que habéis instalado
import re
import pandas as pd

from datetime import datetime

def convert_date(date_str):
    # Define el formato de la fecha de entrada
    input_format = '%a %d %b %Y'
    # Define el formato de la fecha de salida
    output_format = '%d/%m/%Y'
    
    # Convierte la cadena de fecha al objeto datetime
    date_obj = datetime.strptime(date_str, input_format)
    # Formatea el objeto datetime a la cadena deseada
    formatted_date = date_obj.strftime(output_format)
    
    return formatted_date

def atleat(line):
    
    # Define a regular expression pattern to match an integer at the start of the line
    pattern = r'^\d+\s+[A-Za-z]+\s+[A-Za-z]+'
    match = re.match(pattern, line)
    return bool(match)

def atleat1(line):
    
    # Define a regular expression pattern to match an integer at the start of the line
    pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)$'
    match = re.match(pattern, line)
    return bool(match)

def recognize_start_time(text):
    """
    Recognizes if the input text matches the pattern 'Start Time HH:MM'.
    
    Parameters:
    text (str): The text to check.
    
    Returns:
    bool: True if the text matches the pattern, False otherwise.
    """
    # Define the regular expression pattern
    pattern = r'^Start Time ([01]\d|2[0-3]):[0-5]\d$'
    
    # Use re.match to check if the pattern matches the entire text
    match = re.match(pattern, text)
    
    # Return True if there is a match, otherwise False
    return bool(match)

def extract_data_from_pdf(pdf_path, f):
    data = []
    


    try:
        document = fitz.open(pdf_path)
        text = ""
        for page_num in range(len(document)):
            page = document.load_page(page_num)
            text = page.get_text('text')
            
            lines = text.split('\n')
            '''if (page_num == 0):'''
            head = lines[0] + ',' + lines[1] + ','  
            i = 11
            while i<len(lines):
                head1 = lines[i] + ',' + lines[i+1] + ',' + lines[i+2] + ',' + lines[i+3] + ',' + lines[i+4]+ ','
                if(atleat1(lines[i+5])):
                    head2 = ',' + lines[i+5]+ ','+ lines[i+6]+ ','+ lines[i+7]+ ','
                    inc = 8
                else:
                    head2 = lines[i+5]+ ','+ lines[i+6]+ ','+ lines[i+7]+ ','+ lines[i+8]+ ','
                    inc = 9
                f.write( head + head1 + '\n')
                '''if(atleat(lines[i])):
                    print(lines[i])
                    f.write( '\n' + head + lines[i]+ ',')
                elif(lines[i] == ' '):
                    print(lines[i])
                    f.write( lines[i]+',') 
                elif(atleat1(lines[i])):
                    print(lines[i])
                    f.write( lines[i]+',')   '''
                i = i+inc
            

            #lines = text.split('\n')
            # print(lines[0])
            # print(lines[1])
            # print(lines[2])
            # print(lines[3])
            # print(lines[4])
            # print(lines[5])
            # print(lines[6])
            # print("********************************")
            

            #     parts = line.split()
            #     # for part in parts:
            #     #     print(part)
            #     if len(parts) > 6:  # Simplistic check to ensure the line has enough parts
                    
            #         rank = parts[0]
            #         # print(parts[0])
            #         heat_name = parts[1]
            #         # print(parts[1])
            #         full_name = parts[2]
            #         # print(parts[2])
            #         nf_code = parts[3]
            #         # print(parts[3])
            #         best_score = parts[4]
            #         # print(parts[4])
            #         run1 = parts[5]
            #         # print(parts[5])
            #         run2 = parts[6]
            #         # print(parts[6])
            #         run3 = parts[7] if len(parts) > 7 else None
            #         data.append([rank, heat_name, full_name, nf_code, best_score, run1, run2, run3])
            # print("*****************************")
        
        
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return pd.DataFrame()
        # Assuming the format is consistent, use a simple string processing to extract relevant data
        
        
        # for pos in range(0, len(lines)):
        #     if (len(lines[pos]) > 2 and starts_with_integer(lines[pos])):
        #         pos1 = pos + 2
        #         while not starts_with_integer(lines[pos1]):
        #             pos1 = pos1 + 1
        #         print(f"{lines[pos]} {lines[pos+1]}")
        #         for pos2 in range(pos + 2, pos1):
        #             print(f"{lines[pos2]}")
        #         pos = pos1


        
        

def read_pdfs_in_directory(directory,f):
    all_dataframes = []
    for root, _, files in os.walk(directory):
        for file in files:
            
            if file.endswith('.pdf'):
                pdf_path = os.path.join(root, file)
                print(pdf_path)
                df = extract_data_from_pdf(pdf_path,f)
                all_dataframes.append(df)
    
    # if all_dataframes:
    #     combined_df = pd.concat(all_dataframes, ignore_index=True)
    #     return combined_df
    # else:
        #return pd.DataFrame()
    return all_dataframes

# Example usage
directory_path = "C:\\Users\\Miguel Alejandro\\Documents\\3er Año\\Segundo Período\\Simulación\\Surf-and-Skate-Prediction-Model-for-2024-Olympics\\Skate"
f = open("Results WST SHARJAH - STREET 2022 WORLD CHAMPIONSHIPS.txt", "w")
combined_dataframe = read_pdfs_in_directory(directory_path, f)
f.close()
#print(combined_dataframe)