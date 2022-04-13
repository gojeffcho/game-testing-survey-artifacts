# Game Testing Survey Artifacts

This repo contains artifacts for _Bughunting on a Budget: Improving Quality Assurance Practices and Tools for Indie Game Developers_. Below is a description of the layout of this repo and pertinent information for interpreting the contents.

### File Layout

```
repo
│
│──qualitative\
│      │──indie_codes_and_themes.pdf
│      │──nonindie_codes_and_themes.pdf
│      └──open_text_responses.xlsx 
│
│──quantitative\
│      │──demographic_information_graphs\
│      │──likert_bargraphs_by_type\
│      │──likert_boxplots_by_type\
│      │──mannwhitney.csv
│      │──deltas.csv
│      └──project_information_graphs\
│
│──scripts\
│      │──config.py
│      │──data\
│      │──csv-cleanup.py
│      └──surveystats.py
│
└──response_data_processed.csv
```

### Prompt Codes to Survey Questions
In some of the intermediary materials, we refer to prompts using codes (e.g., `Perf1`) instead of specifying the survey question (e.g., `(Q22-a)`). The table below shows the conversions between codes and question numbers:

| Code     | Question   | Category | 
|----------|------------|----------|
| Perf 1-8 | (Q22, a-h) | _Performance_ |
| Plan 1-9 | (Q24, a-i) | _Planning_ | 
| Goals 1-4 | (Q26, a-d) | _Goals_ | 
| Auto 1-10 | (Q28, a-j) | _Automation_ | 
| Tools 1-6 | (Q30, a-f) | _Tools_ | 
| Out 1-6 | (Q32, a-f) | _Outputs/Results_ | 
| Res 1-9 | (Q34, a-i) | _Resources_ |


### Contents

##### Root Directory

- `qualitative\` contains files from the qualitative analysis.

- `quantitative\` contains files from the quantitative analysis.

- `scripts\` contains the Python scripts for performing analyses and generating graphs.

- `response_data_processed.csv` is the output from the survey, cleaned up and anonymized. Responses under the Likert-like scale prompts are: (-1) Unknown, (0) Not Applicable, (1) Strongly Disagree, (2) Disagree, (3) Neither agree nor disagree, (4) Agree, or (5) Strongly Agree.

##### Qualitative

- `indie_codes_and_themes.pdf` is the export of the mindmap where codes from indie open-ended text responses were organized into themes.  

  * Themes branch from the central 'Indie' block and are [BRACKETED AND CAPITALIZED]
  * Codes are in regular case  
  * Two or more `+`s preceding a code mean that the code was mentioned as many times as there are plus-symbols
  * An `IV:` prefix is attached to codes that were captured in vivo, or in the respondent's own words
  * Dotted lines connect codes that were related in the responses, such as a cause-and-effect relationship.

- `nonindie_codes_and_themes.pdf` is the same as above but for non-indies.

- `open_text_responses.xlsx` is the Excel sheet where responses were coded. 

  * Codes are written in-line with the text in **[bold, bracketed]** format. 
  * Underlined portions were salient examples, some of which were quoted in the thesis


##### Quantitative

- `demographic_information_graphs\` contains two graphs from demographic information responses
- `likert_bargraphs_by_type\` contains 52 bar graphs of indie and non-indie responses per prompt
  * `NA` on the x-axis is the sum of both `0` and `-1` responses for that prompt
- `likert_boxplots_by_type\` contains 52 boxplots of indie and non-indie responses per prompt
  * The bold line on each boxplot is the median
- `mannwhitney.csv` is the output of running Mann-Whitney U-tests using `Scipy.stats.mannwhitneyu()`
- `deltas.csv` is the output of our medians comparison, where `delta = Median_nonindie - Median_indie`
- `project_information_graphs\` contains four graphs of data from project information responses


##### Scripts

- `config.py` contains runtime configuration parameters for the script and should not be changed. The `CONFIG['ALPHA']` parameter sets the alpha level for the Mann-Whitney U-tests
- `data\` contains the input files needed for analysis and graph generation.
  - `Video Game Testing Survey FINAL.csv` is the data export from the survey
  - `Indie.csv` is the manually-separated data for Indie responses
  - `Non-Indie.csv` is the manually-separated data for Non-Indie responses
- `csv-cleanup.py` takes the survey data export and cleans it up in preparation for analyses and graphs
- `requirements.txt` shows the package requirements for these scripts
- `SurveyResponse.py` is a data class for handling survey data
- `surveystats.py` is the script that performs analyses and generates graphs
- `utils.py` is a collection of utilities used for these scripts.


### Running the Scripts

##### Overview

These scripts run the analyses and create the graphs used in the thesis. Using these scripts involves a two-step process due to a manual step we take in between for classifying and organizing the projects received. 

##### Prerequisites

- These scripts were written using Python 3.8.9 and we recommend using Python 3.8 or higher.
- Required packages and the version we use:
  - matplotlib 3.5.1
  - numpy 1.22.0
  - pandas 1.3.5
  - scipy 1.8.0
  
They can all be installed using a single command: `python3 -m pip install -r requirements.txt`

##### Survey Data Cleanup

Usage: `python3 csv-cleanup.py`

This command, issued in the `scripts/` folder, takes the survey data export and transforms it into a more readable and usable format. The output from this script is saved to `output/output.csv` and the format of the output is nearly identical to the `response_data_processed.csv` in the root directory. The latter file is slightly manually processed to better organize the second and third projects submitted by some respondents.

##### Analyses and Graphs

Usage: `python3 surveystats.py`

This command, issued in the `scripts/` folder, runs the delta comparisons and Mann-Whitney U-tests and outputs their results to `output/deltas.csv` and `output/mannwhitney.csv` respectively. These are identical to the files found in the `quantitative/` directory. They also generate all of the demographic, project information, and prompt-based graphs which are saved to `graphs/`. These graphs are also identical to the ones found in the `quantitative` director. Note that these scripts use prompt codes for convenience, which can be converted to survey question numbers using the table provided above.