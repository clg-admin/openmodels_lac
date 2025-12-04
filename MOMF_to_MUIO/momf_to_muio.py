# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 09:15:21 2025

@author: ClimateLeadGroup
"""

import os
import re
import subprocess

# Define folder paths
input_folder = "MOMF_models"
output_folder = "MUIO_models"

# Check if input folder exists
if not os.path.exists(input_folder) or not os.path.isdir(input_folder):
    print(f"Folder '{input_folder}' does not exist or is not a directory.")
    exit()

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Regular expressions to find specific values
region_pattern = re.compile(r"set REGION :=\s*(\w+)\s*;")
discount_rate_pattern = re.compile(r"(param DiscountRate default [\d.]+ :=)")

# Iterate over files in the input folder
files_list = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

for file_name in files_list:
    input_file_path = os.path.join(input_folder, file_name)

    # Replace .txt extension with .xlsx for output file
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

        # Find the region
        match_region = region_pattern.search(line)
        if match_region:
            region = match_region.group(1)

        # Find DiscountRate default value
        match_discount = discount_rate_pattern.search(line)
        if match_discount:
            df_default_value = re.search(r"[\d.]+", line).group()  # Extract the number

            # Check if next line is ";"
            if i + 1 < len(lines) and lines[i + 1].strip() == ";":
                modified_lines.append(line)  # Add current line
                modified_lines.append(f"{region} {df_default_value}\n")  # Insert new line
                modified_lines.append(";\n")  # Keep the ";"
                i += 1  # Skip the ";" line since we added it manually
            else:
                modified_lines.append(line)
        else:
            modified_lines.append(line)

        i += 1

    # Save the modified file
    with open(input_file_path, "w") as file:
        file.writelines(modified_lines)

    print(f"File modified and saved: {file_name}")

    # Execute otoole conversion command
    command = f'otoole convert datafile excel {input_file_path} {output_file_path} config.yaml'
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Conversion successful: {output_file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Conversion error for {file_name}: {e}")
