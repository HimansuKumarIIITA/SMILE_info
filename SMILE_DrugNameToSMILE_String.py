import requests

def get_smiles_from_pubchem(drug_name):
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{drug_name}/property/CanonicalSMILES/TXT"
    response = requests.get(url)
    return response.text.strip()

# Read drug names from file
with open("drug_names.txt", "r") as f:
    drugs = [line.strip() for line in f]

# Open the output file for writing
with open("DrugToSMILE.txt", "w") as output:
    for drug in drugs:
        try:
            smiles = get_smiles_from_pubchem(drug)
            output.write(f"{smiles}\t{drug}\n")  # \t creates a tab-separated value
            print(f"Successfully fetched for {drug}")
        except:
            print(f"Failed to fetch for {drug}")
