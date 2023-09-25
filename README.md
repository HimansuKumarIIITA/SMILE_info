# SMILE_info
Leveraging the power of the PubChem API, this tool streamlines the conversion between SMILES strings and chemical names, assisting chemists and researchers in their endeavors.

The SMILE_info repository facilitates users in retrieving information related to SMILE strings and their corresponding drug names. It comprises two primary modules:

a. **SMILE_info.py**: Accepts a list of SMILES strings and retrieves their respective chemical names.

b. **SMILE_DrugNameToSMILE_String.py**: Converts drug names to their corresponding SMILE strings.

### Usage

- For **SMILE_info.py**:
    - Users must provide the input file using the `-i` option and save the results with the `-o` option.
    - The input CSV file should have one SMILE string on each line.
    ```bash
    python SMILE_info.py -i /path/to/input/file.csv -o /path/to/output/file.csv
    ```

    **Example**: 
    ```bash
    python SMILE_info.py -i SmileString.csv -o output.csv
    ```

- For **SMILE_DrugNameToSMILE_String.py**:
    - Users must provide the input file using the `-i` option and save the results with the `-o` option.
    - The input text file should list one drug name on each line.
    ```bash
    python SMILE_DrugNameToSMILE_String.py -i input_file.txt -o output_file.txt
    ```

    **Example**: 
    ```bash
    python SMILE_DrugNameToSMILE_String.py -i drug_names.txt -o output_drug_smiles.txt
    ```

