import requests
import argparse

def get_smiles_from_pubchem(drug_name):
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{drug_name}/property/CanonicalSMILES/TXT"
    response = requests.get(url)
    return response.text.strip()

def main(input_file, output_file):
    # Read drug names from file
    with open(input_file, "r") as f:
        drugs = [line.strip() for line in f]
    
    with open(output_file, "w") as out:
        for drug in drugs:
            try:
                smiles = get_smiles_from_pubchem(drug)
                out.write(f"{drug}: {smiles}\n")
            except:
                out.write(f"Failed to fetch for {drug}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch SMILES strings for drug names.")
    parser.add_argument("-i", "--input", help="Input txt file with drug names", required=True)
    parser.add_argument("-o", "--output", help="Output txt file to save drug name and SMILES string", required=True)

    args = parser.parse_args()

    main(args.input, args.output)
