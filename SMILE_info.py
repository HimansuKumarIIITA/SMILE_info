import requests
import time
import csv
import argparse

def get_name_from_smiles(smiles):
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/{smiles}/property/Title/TXT"
    response = requests.get(url)
    return response.text.strip()

def main(input_file, output_file):
    smiles_list = []
    with open(input_file, "r", encoding='latin1', errors='replace') as f:
        reader = csv.reader(f)
        next(reader)  # skip header if there's one
        for row in reader:
            smiles_list.append(row[0])

    results = []

    for i, smiles in enumerate(smiles_list):
        try:
            name = get_name_from_smiles(smiles)
            results.append([smiles, name])
            print(f"Fetched {i+1}/{len(smiles_list)}: {smiles} -> {name}")
            
            time.sleep(0.5)
            
        except Exception as e:
            print(f"Error fetching name for SMILES {smiles}: {e}")
            results.append([smiles, "Error"])

    with open(output_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["SMILES", "Name"])
        writer.writerows(results)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch chemical names for a list of SMILES strings.")
    parser.add_argument('-i', '--input', help="Input CSV file containing SMILES strings.", required=True)
    parser.add_argument('-o', '--output', help="Output CSV file to save results.", required=True)
    args = parser.parse_args()

    main(args.input, args.output)
