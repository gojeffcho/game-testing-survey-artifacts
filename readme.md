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
│      │──mannwhitney.txt
│      │──medians.txt
│      └──project_information_graphs\
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
- `mannwhitney.txt` is the output of running Mann-Whitney U-tests using `Scipy.stats.mannwhitneyu()`
- `medians.txt` is the output of our medians comparison, where `delta = Median_nonindie - Median_indie`
- `project_information_graphs\` contains four graphs of data from project information responses