# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 09:15:21 2025

@author: ClimateLeadGroup
"""

import os
import re
import subprocess

# Definir las rutas de los folders
input_folder = "MOMF_models"
output_folder = "MUIO_models"

# Verificar si el folder de entrada existe
if not os.path.exists(input_folder) or not os.path.isdir(input_folder):
    print(f"La carpeta '{input_folder}' no existe o no es un directorio.")
    exit()

# Crear la carpeta de salida si no existe
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Expresiones regulares para encontrar valores específicos
region_pattern = re.compile(r"set REGION :=\s*(\w+)\s*;")
discount_rate_pattern = re.compile(r"(param DiscountRate default [\d.]+ :=)")

# Iterar sobre los archivos en la lista
files_list = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

for file_name in files_list:
    input_file_path = os.path.join(input_folder, file_name)

    # Reemplazar la extensión .txt por .xlsx para el archivo de salida
    output_file_name = file_name.replace('.txt', '.xlsx')
    output_file_path = os.path.join(output_folder, output_file_name)
    
    with open(input_file_path, "r") as file:
        lines = file.readlines()

    region = None
    df_default_value = None
    modified_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]

        # Buscar la región
        match_region = region_pattern.search(line)
        if match_region:
            region = match_region.group(1)

        # Buscar DiscountRate default value
        match_discount = discount_rate_pattern.search(line)
        if match_discount:
            df_default_value = re.search(r"[\d.]+", line).group()  # Extraer el número

            # Verificar si la siguiente línea es ";"
            if i + 1 < len(lines) and lines[i + 1].strip() == ";":
                modified_lines.append(line)  # Agregar la línea actual
                modified_lines.append(f"{region} {df_default_value}\n")  # Insertar nueva línea
                modified_lines.append(";\n")  # Mantener el ";"
                i += 1  # Saltar la línea ";", ya que la agregamos manualmente
            else:
                modified_lines.append(line)
        else:
            modified_lines.append(line)

        i += 1

    # Guardar el archivo con los cambios
    with open(input_file_path, "w") as file:
        file.writelines(modified_lines)

    print(f"Archivo modificado y guardado: {file_name}")

    # Ejecutar el comando en la terminal con la nueva extensión
    command = f'otoole convert datafile excel {input_file_path} {output_file_path} config.yaml'
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Conversión exitosa: {output_file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error en la conversión de {file_name}: {e}")
