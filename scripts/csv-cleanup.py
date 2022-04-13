##
# csv-cleanup.py
#
# Takes the CSV export from the Game Testing Survey and cleans it up for
# ease of analysis.
#
# Input:
#    data/Video Game Testing Survey.csv
#
# Output:
#    output/output.csv
##


# Standard Python libraries
import csv          # used for writing to CSV
import os           # used for directory access and file listing

# User-defined modules
from config import CONFIG
from SurveyResponse import SurveyResponse
import utils


def main():

    # Set base path info
    cwd = os.getcwd()
    CONFIG['BASE_DIR'] = cwd

    #  Load the Demographic and Projects Data
    print('Extracing data from CSV...')
    csv_read = utils.extract_csv(utils.get_input_path(), CONFIG['INPUTFILE']) # Only pulls valid entries
    responses = get_responses(csv_read)

    # Write outputs
    utils.create_output_folder()    # Create dir if not exists
    filename = f"{os.path.join(CONFIG['BASE_DIR'], CONFIG['OUTPUT_DIR'], 'output.csv')}"
    write_responses(filename, responses)

    # Confirm the projects loaded
    projects = []
    for i in range(len(responses)):
        response = responses[i]
        projects.append(response.p1)

        if response.p2.type != '':
            projects.append(response.p2)

        if response.p3.type != '':
            projects.append(response.p3)

    # Print number of projects loaded along with the nicknames (OBFUSCATED for artifacts)
    print(f'{len(projects)} projects loaded.')
    for project in projects:
        print(project.nick)


def get_responses(csv_read):
    """
    Gets all responses from the read-in CSV file and turns them into SurveyResponse objects.

        Input:
            csv_read (List): CSV input data

        Output:
            responses (List[SurveyResponse]): List of SurveyResponses, each element a project response
    """
    responses = []

    for each in csv_read:
        response = SurveyResponse(each)
        responses.append(response)

    return responses


def write_responses(filename, responses):
    """
    Write the output to file.

    Input:
        filename (os.Path or String): name of the output file
        responses (List[SurveyResponse]): List of SurveyResponses, each element a project response

    Output:
        output/output.csv (cleaned up data file for analysis)
    """
    with open(filename, 'w', newline='') as csv_out:
        outwriter = csv.writer(csv_out)
        outwriter.writerow(CONFIG['CSV_HEADER'])

        for response in responses:
            response.output(outwriter)


main()
