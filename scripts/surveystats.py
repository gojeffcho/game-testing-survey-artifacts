##
# surveystats.py
#
# Runs analyses (delta comparisons, Mann-Whitney U-tests) and outputs their results to output/.
# Creates graphs for demographics, project information, and project responses and writes them to graphs/.
#
# Input:
#    data/Indie.csv
#    data/Non-Indie.csv
#    output/output.csv
#
# Output:
#    output/mannwhitney.csv
#    output/deltas.csv
#    graphs/*
##

# Standard Python libraries
from collections import Counter
import os
import statistics

# Custom Python libraries
import matplotlib.pyplot as plt
import numpy as np
import pingouin as pn
import scipy.stats as stats

# User-defined
from config import CONFIG
import utils


def main():

    # Sanity check
    if not os.path.exists(os.path.join(CONFIG['OUTPUT_DIR'], 'output.csv')):
        print('Error: critical source files not found. Make sure you have run `python3 csv-cleanup.py` first before running this script.')
        return

    # Set the style for matplotlib graphs
    set_plot_style()

    # Extract data from the separated indie and non-indie source files
    indies = utils.extract_grouped_csv(CONFIG['DATA_DIR'], CONFIG['INDIEFILE'])
    others = utils.extract_grouped_csv(CONFIG['DATA_DIR'], CONFIG['NONINDIEFILE'])

    # Ensure folders for output files exist; create blank output files
    utils.create_output_folder(CONFIG['GRAPH_DIR']) # Create graphs dir if not exists
    utils.create_output_folder(os.path.join(CONFIG['GRAPH_DIR'], CONFIG['BOX_DIR']))  # Create boxplots dir if not exists
    utils.create_output_folder(os.path.join(CONFIG['GRAPH_DIR'], CONFIG['BAR_DIR']))  # Create graphs dir if not exists
    deltafile = os.path.join(CONFIG['OUTPUT_DIR'], CONFIG['DELTAS'])
    mwfile = os.path.join(CONFIG['OUTPUT_DIR'], CONFIG['MANNWHITNEY'])
    with open(deltafile, 'w') as f:
        f.write('Prompt, Delta, Non-Indie Median, Indie Median\n')    # Headers for CSV
    with open(mwfile, 'w') as f:
        f.write('Prompt, U-Statistic, Effect Size, P-Value, Indie Median, Non-Indie Median, Outcome\n')    # Headers for CSV

    # Perform the analyses and generate graphs
    for col in CONFIG['COLS']:
        mann_whitney(indies[col], others[col], col)
        # mann_whitney2(indies[col], others[col], col) # This version uses `pingouin` to confirm CLES, outputs to stdout
        compute_deltas(indies[col], others[col], col)
        make_bargraphs(indies[col], others[col], col)
        make_boxplots(indies[col], others[col], col)

    # Generate various demographic and project info graphs
    graph_experience_boxplot()
    graph_roles_held()
    graph_project_info_games()
    graph_project_info_engines()
    graph_project_info_teams()
    graph_project_info_budget()

    return


def compute_deltas(indies: list, others: list, qname: str):
    """
    Calculate the delta between Likert response medians for indies and non-indies. Writes the results to output/.

    Args:
         indies (List[int]): List of Likert responses from indies
         others (List[int]): List of Likert responses from non-indies
         qname (str): Codename of the prompt being analyzed
    """
    # Remove all `0` within each group for this prompt
    indiedata = get_likerts_without_zeroes(indies)
    otherdata = get_likerts_without_zeroes(others)

    indiemed = statistics.median(indiedata)
    othermed = statistics.median(otherdata)

    deltafile = os.path.join(CONFIG['OUTPUT_DIR'], CONFIG['DELTAS'])
    with open(deltafile, 'a') as f:
        f.write(f'{qname}, {othermed - indiemed}, {othermed}, {indiemed}\n')


def count_likerts(likertlist: list):
    """ A function to count occurrences of each Likert response.

    Arg:
        likertlist (List): list of Likert responses in numeric format

    Return:
        List[int, int, int, int, int, int]: list of counts of Likert responses, position == Likert value
    """
    likerts = Counter()

    for likert in likertlist:
        likerts[likert] += 1

    return [likerts[0], likerts[1], likerts[2], likerts[3], likerts[4], likerts[5]]


def get_likerts_without_zeroes(likertlist: list):
    """ Removes all zeroes from input list of Likert values and returns the resulting list. """

    return [i for i in likertlist if i > 0]


def graph_experience_boxplot():
    """ Create boxplot for length of game development experience by game/studio type. """

    # Extract demographic data from cleaned-up survey output
    data = utils.extract_grouped_csv(CONFIG['OUTPUT_DIR'], 'output.csv')
    gamedev_years = data['Years Active in Games Industry']
    indie_years = data['Years of Indie Exp'].fillna(0)
    aa_years = data['Years of AA Exp'].fillna(0)
    aaa_years = data['Years of AAA Exp'].fillna(0)

    data = [gamedev_years, indie_years, aa_years, aaa_years]

    f, ax = plt.subplots()
    bp = ax.boxplot(data, patch_artist=True)
    ax.xaxis.set_ticks(np.arange(1, 5, 1))
    ax.xaxis.set_ticklabels(['Game Dev', 'Indie', 'AA', 'AAA'], color='gray')
    plt.ylabel('Experience in Years', color='gray')

    c = 'white'
    for patch, color in zip(bp['boxes'], [c, c, c, c]):
        patch.set_facecolor(color)

    for median in bp['medians']:
        median.set(linewidth=3, color='black')

    black = ax.plot([], [], marker='|', color='blue', ls="none")[0]
    ax.legend([black], ['Median'], loc='upper right', framealpha=1, frameon=True)
    plt.gray()

    filename = os.path.join(CONFIG['GRAPH_DIR'], 'xp-box.png')
    plt.savefig(filename, bbox_inches='tight', pad_inches=0)
    plt.close()


def graph_roles_held():
    """ Create bar graph for the number of respondents who held each type of role in the past. """

    # Extract demographic data from cleaned-up survey output
    data = utils.extract_grouped_csv(CONFIG['OUTPUT_DIR'], 'output.csv')
    roles = data['Roles Held']
    rolecount = Counter()

    # Count up roles held; only count one Other per respondent
    for role in roles:
        r = role[1:-1].split(',')
        for each in r:
            if each.strip()[1:-1] == 'Dev/Prog/Eng':
                rolecount['Dev'] += 1
            elif each.strip()[1:-1] == 'QA':
                rolecount['QA'] += 1
            elif each.strip()[1:-1] == 'Lead/Prod/Mgr':
                rolecount['Lead'] += 1
            elif each.strip()[1:-1] == 'Designer/ProdOwner':
                rolecount['Designer'] += 1
            else:
                rolecount['Other'] += 1
                break

    labels = ['Lead', 'Designer', 'QA', 'Dev', 'Other']
    counts = [rolecount['Lead'], rolecount['Designer'], rolecount['QA'], rolecount['Dev'], rolecount['Other']]

    fig = plt.figure(figsize=(5, 3.7))
    bars = plt.bar(labels, counts)

    for bar in bars:
        bar.set_color('white')
        bar.set_edgecolor('black')
        bar.set_linewidth(1)

    plt.ylabel('Respondents who held role', color='gray')

    filename = os.path.join(CONFIG['GRAPH_DIR'], 'role-bar.png')
    plt.savefig(filename, bbox_inches='tight', pad_inches=0)
    plt.close(fig)


def graph_project_info_budget():
    """ Create bar graphs for budget ranges on various projects. """

    # Extract demographic data from cleaned-up survey output
    data = utils.extract_grouped_csv(CONFIG['OUTPUT_DIR'], 'output.csv')
    budgets = data['P1 Team Size'].append(data['P2 Team Size'].dropna()).append(data['P3 Team Size'].dropna())
    budgetcount = Counter()

    # Count up the different types
    for budget in budgets:
        if budget == 'Under $1M USD':
            budgetcount['Low'] += 1
        elif budget == '$1M - $10M USD':
            budgetcount['Medium'] += 1
        elif budget == 'Over $10M USD':
            budgetcount['Large'] += 1
        elif budget == 'Unknown':
            budgetcount['Unknown'] += 1

    budgetlabel = ['<$1M', '$1M-10M', '>$10M', 'Unknown']
    budgetcount = [10, 2, 9, 1]

    fig, ax = plt.subplots(figsize=(5, 4))
    x = 0.7 + np.arange(len(budgetlabel))
    w = 0.8
    bars = ax.bar(x, budgetcount, width=w)

    for bar in bars:
        bar.set_color('white')
        bar.set_edgecolor('black')
        bar.set_linewidth(1)

    plt.ylabel('Count', color='gray')
    plt.xlabel('Game Budget Range', color='gray')
    plt.xticks(x, budgetlabel)
    plt.yticks(np.arange(11, step=2))

    filename = os.path.join(CONFIG['GRAPH_DIR'], 'budget-bar.png')
    plt.savefig(filename, bbox_inches='tight', pad_inches=0)
    plt.close(fig)


def graph_project_info_engines():
    """ Create bargraph for what engines were used on the various projects. """

    # Extract demographic data from cleaned-up survey output
    data = utils.extract_grouped_csv(CONFIG['OUTPUT_DIR'], 'output.csv')
    engines = data['P1 Engine'].append(data['P2 Engine'].dropna()).append(data['P3 Engine'].dropna())
    enginecount = Counter()

    # Count up the different types
    for engine in engines:
        if engine == 'Unity':
            enginecount['Unity'] += 1
        elif engine == 'Unreal' or engine == 'Unreal Engine 4' or engine == 'Unreal 4':
            enginecount['Unreal'] += 1
        elif engine == 'Custom Engine' or engine == 'Frostbite' or engine == 'Proprietary':
            enginecount['Other'] += 1

    enginelabel = ['Unity', 'Unreal', 'Proprietary']
    enginecounts = [enginecount['Unity'], enginecount['Unreal'], enginecount['Other']]

    fig, ax = plt.subplots(figsize=(5, 4))
    x = 0.7 + np.arange(len(enginelabel))
    w = 0.8
    bars = ax.bar(x, enginecounts, width=w)

    for bar in bars:
        bar.set_color('white')
        bar.set_edgecolor('black')
        bar.set_linewidth(1)

    plt.ylabel('Count', color='gray')
    plt.xlabel('Game Engine', color='gray')
    plt.xticks(x, enginelabel)
    plt.yticks(np.arange(9, step=2))

    filename = os.path.join(CONFIG['GRAPH_DIR'], 'engine-bar.png')
    plt.savefig(filename, bbox_inches='tight', pad_inches=0)
    plt.close(fig)


def graph_project_info_games():
    """ Create bar graph for the number of game submitted by type. """

    # Extract demographic data from cleaned-up survey output
    data = utils.extract_grouped_csv(CONFIG['OUTPUT_DIR'], 'output.csv')
    types = data['P1 Type'].append(data['P2 Type'].dropna()).append(data['P3 Type'].dropna())
    typecount = Counter()

    # Count up the different types
    for thistype in types:
        if thistype == 'Indie Game':
            typecount['Indie'] += 1
        elif thistype == 'AA Game':
            typecount['AA'] += 1
        elif thistype == 'AAA Game':
            typecount['AAA'] += 1

    typelabel = ['Indie', 'AA', 'AAA']
    typecount = [typecount['Indie'], typecount['AA'], typecount['AAA']]

    fig, ax = plt.subplots(figsize=(5, 4))
    x = 0.7 + np.arange(len(typelabel))
    w = 0.8
    bars = ax.bar(x, typecount, width=w)

    for bar in bars:
        bar.set_color('white')
        bar.set_edgecolor('black')
        bar.set_linewidth(1)

    plt.ylabel('Count', color='gray')
    plt.xlabel('Game Type', color='gray')
    plt.xticks(x, typelabel)
    plt.yticks(np.arange(11, step=2))

    filename = os.path.join(CONFIG['GRAPH_DIR'], 'gamestype-bar.png')
    plt.savefig(filename, bbox_inches='tight', pad_inches=0)
    plt.close(fig)


def graph_project_info_teams():
    """ Create bar graphs for the different size ranges of teams. """

    # Extract demographic data from cleaned-up survey output
    data = utils.extract_grouped_csv(CONFIG['OUTPUT_DIR'], 'output.csv')
    teamsize = data['P1 Team Size'].append(data['P2 Team Size'].dropna()).append(data['P3 Team Size'].dropna())
    teamcount = Counter()

    # Count up the different types
    for team in teamsize:
        if team == '1 - 49':
            teamcount['S'] += 1
        elif team == '50 - 99':
            teamcount['M'] += 1
        elif team == '100 - 499':
            teamcount['L'] += 1
        elif team == '500 or more':
            teamcount['XL'] += 1

    teamlabel = ['1-49', '50-99', '100-499', '500+']
    teamcount = [11, 1, 8, 2]

    fig, ax = plt.subplots(figsize=(5, 4))
    x = 0.7 + np.arange(len(teamcount))
    w = 0.8
    bars = ax.bar(x, teamcount, width=w)

    for bar in bars:
        bar.set_color('white')
        bar.set_edgecolor('black')
        bar.set_linewidth(1)

    plt.ylabel('Count', color='gray')
    plt.xlabel('Team Size', color='gray')
    plt.xticks(x, teamlabel)
    plt.yticks(np.arange(13, step=2))

    filename = os.path.join(CONFIG['GRAPH_DIR'], 'team-bar.png')
    plt.savefig(filename, bbox_inches='tight', pad_inches=0)
    plt.close(fig)


def make_bargraphs(indies: list, others: list, qname: str):
    """
    Generate bargraphs of Likert responses for all questions with subgraphs for indies and non-indies.
    Saves the resulting graph to /graphs/bargraphs/

    Args:
        indies (List[int]): List of Likert responses from indies
        others (List[int]): List of Likert responses from non-indies
        qname (str): Codename of the prompt being analyzed

    Return:
        None
    """
    labels = ['NA', 'SD', 'D', 'N', 'A', 'SA']  # Labels corresponding to Likert responses
    x = np.arange(len(labels))
    width = .5

    indies_count = count_likerts(indies)
    others_count = count_likerts(others)

    # Make the plots
    f, axis = plt.subplots(1, 2, figsize=(4, 3))
    axis[0].bar(x - width/2, indies_count, color='white', edgecolor='black', linewidth=1)
    axis[0].set_ylim(bottom=0, top=max(max(indies_count), max(others_count)))
    axis[1].bar(x + width/2, others_count, color='white', edgecolor='black', linewidth=1)

    # Style correction for secondary plot
    axis[1].grid(color='w', linestyle='solid', axis='y')
    axis[0].sharey(axis[1])
    axis[0].set_ylabel('Count', color='gray')

    qnum = qname_to_qnum(qname)
    f.suptitle(f'{qnum}')
    axis[0].set_title('Indies', color='gray')
    axis[1].set_title('Non-Indies', color='gray')
    axis[0].set_xticks(np.arange(6), ('NA', 'SD', 'D', 'N', 'A', 'SA'), rotation=45)
    axis[1].set_xticks(np.arange(6), ('NA', 'SD', 'D', 'N', 'A', 'SA'), rotation=45)
    axis[1].yaxis.set_label_position('right')
    axis[1].yaxis.tick_right()

    filename = os.path.join(CONFIG['GRAPH_DIR'], CONFIG['BAR_DIR'], f'{qname}-sep.png')
    plt.savefig(filename)
    plt.close(f)


def make_boxplots(indies: list, others: list, qname: str):

    # Remove all `0` within each group for this prompt
    indiedata = get_likerts_without_zeroes(indies)
    otherdata = get_likerts_without_zeroes(others)

    data = [indiedata, otherdata]

    f = plt.figure(figsize=(4, 2))
    ax = f.add_subplot(111)
    bp = ax.boxplot(data, positions=[1, 1.5], widths=0.4, vert=0, patch_artist=True, labels=['Indie','Non-\nIndie'])
    ax.xaxis.set_ticks(np.arange(1, 6, 1))
    ax.xaxis.set_ticklabels(['SD (1)', 'D (2)', 'N (3)', 'A (4)', 'SA (5)'])
    plt.tick_params(left=False)

    c = 'white'
    for patch, color in zip(bp['boxes'], [c, c, c, c]):
        patch.set_facecolor(color)

    for median in bp['medians']:
        median.set(linewidth=3, color='black')

    qnum = qname_to_qnum(qname)
    plt.title(f'{qnum}')
    filename = os.path.join(CONFIG['GRAPH_DIR'], CONFIG['BOX_DIR'], f'{qname}-box.png')
    plt.savefig(filename)
    plt.close(f)


def mann_whitney(indies: list, others: list, qname: str):

    # Remove all `0` within each group for this prompt
    indiedata = get_likerts_without_zeroes(indies)
    otherdata = get_likerts_without_zeroes(others)

    n1 = len(indiedata)
    n2 = len(otherdata)

    # Perform Mann-Whitney
    u, p = stats.mannwhitneyu(indiedata, otherdata, alternative='two-sided', method='auto')
    feffect = u/(n1 * n2)

    mwfile = os.path.join(CONFIG['OUTPUT_DIR'], CONFIG['MANNWHITNEY'])
    with open(mwfile, 'a') as f:
        f.write(f'{qname}, {u}, {feffect:.2f}, {p}, '
                f'{statistics.median(indiedata):.1f}, {statistics.median(otherdata):.1f},'
                f'{"REJECT" if p <= CONFIG["ALPHA"] else "FAIL TO REJECT"}\n')


def mann_whitney2(indiedata: list, nonindiedata: list, qname: str):

    # Remove all `0` within each group for this prompt
    indiedata = [i for i in indiedata if i > 0]
    nonindiedata = [i for i in nonindiedata if i > 0]

    # Perform Mann-Whitney
    mwustat = pn.mwu(nonindiedata, indiedata, alternative='two-sided')

    print(f'{qname} Medians: {statistics.median(indiedata):.1f} Indie | {statistics.median(nonindiedata):.1f} Non-Indie')
    print(mwustat)

    if mwustat['p-val'].MWU <= CONFIG['ALPHA']:
        print(f'[ALPHA] Reject H_0: medians are not equal @ alpha={CONFIG["ALPHA"]}.')
    else:
        print(f'[ALPHA] Fail to reject H_0: medians are equal @ alpha={CONFIG["ALPHA"]}.')

    print()


def num_to_letter(num: str):
    """ Takes the number portion of a survey prompt and transforms it to the corresponding number.
    e.g., 1 -> a, 2 -> b, etc.

    Arg:
        num (char): the number to transform

    Return:
        char: the character corresponding to `num`

    """
    if num == 0:    # Quick fix works because 10 is the max num in our dataset >_>
        num = 10
    return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'][int(num) - 1]


def qname_to_qnum(qname: str):
    """
    Take a given question code (e.g. Perf1) and translate it to its corresponding question number (e.g. Q22-a).

    Arg:
        qname (str): The question code to translate

    Return:
        qnum (str): The question number after translation
    """
    qnum = '('
    if qname[:4] == 'Perf':
        qnum += f'Q22-{num_to_letter(qname[-1])})'
    elif qname[:4] == 'Plan':
        qnum += f'Q24-{num_to_letter(qname[-1])})'
    elif qname[:5] == 'Goals':
        qnum += f'Q26-{num_to_letter(qname[-1])})'
    elif qname[:4] == 'Auto':
        qnum += f'Q28-{num_to_letter(qname[-1])})'
    elif qname[:4] == 'Tool':
        qnum += f'Q30-{num_to_letter(qname[-1])})'
    elif qname[:3] == 'Out':
        qnum += f'Q32-{num_to_letter(qname[-1])})'
    elif qname[:3] == 'Res':
        qnum += f'Q34-{num_to_letter(qname[-1])})'

    return qnum


def set_plot_style():
    """
    Sets the default plot style for matplotlib.
    Source: https://jakevdp.github.io/PythonDataScienceHandbook/04.11-settings-and-stylesheets.html
    """
    IPython_default = plt.rcParams.copy()

    plt.rc('axes', facecolor='#E6E6E6', edgecolor='none',
           axisbelow=True, grid=True)
    plt.rc('grid', color='w', linestyle='solid')
    plt.rc('xtick', direction='out', color='gray')
    plt.rc('ytick', direction='out', color='gray')
    plt.rc('patch', edgecolor='#E6E6E6')
    plt.rc('lines', linewidth=2)


main()
