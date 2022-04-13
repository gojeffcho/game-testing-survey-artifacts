# Standard Python libraries
import csv
import os           # used for directory access and file listing
import pandas as pd

# User-defined modules
from config import CONFIG


def create_output_folder(dirname=CONFIG['OUTPUT_DIR']):
    """ Create the output/ folder if it does not exist."""

    if not os.path.exists(os.path.join(CONFIG['BASE_DIR'], dirname)):
        os.makedirs(os.path.join(CONFIG['BASE_DIR'], dirname))

    return


def extract_csv(input_path, input_filename=None):
    """ Open the input file and extract the raw text from it without processing.
    Arg:
        input_path (Path): the full path to the file or folder
        input_filename (String): Optional, the name the file in that folder
    Return:
        csv (List[String]) the extracted csv
    """
    csv_list = []
    dqs = 0

    if input_filename:
        input_path = os.path.join(input_path, input_filename)

    with open(input_path, 'r', newline='') as input_data:
        csv_read = csv.reader(input_data)
        for entry in csv_read:
            if entry[-1] and entry[0].isnumeric():
                if entry[0] == '13332819753' \
                        or entry[0] == '13335702947' \
                        or entry[0] == '13338603411':
                    dqs += 1
                else:
                    csv_list.append(entry)

            elif entry[10] == 'No' or entry[11] == 'No': # Disqualification cases
                dqs += 1

    print(f'{len(csv_list)} entries printed; {dqs} disqualified')

    return csv_list


def extract_grouped_csv(input_path, input_filename=None):
    if input_filename:
        input_path = os.path.join(input_path, input_filename)

    with open(input_path, 'r', newline='') as input_data:
        csv_read = pd.read_csv(input_data)

    return csv_read


def get_input_path():
    """ Returns the filepath to the root of the input folder.
    Return:
        input_path (Path): filepath to input folder
    """
    return os.path.join(CONFIG['BASE_DIR'], CONFIG['DATA_DIR'])
