CONFIG = {}

# Path to program folder; overwritten from main upon program run
CONFIG['BASE_DIR'] = '.'

# Folder names and filepaths
CONFIG['DATA_DIR']      = 'data'
CONFIG['OUTPUT_DIR']    = 'output'
CONFIG['GRAPH_DIR']     = 'graphs'
CONFIG['BAR_DIR']       = 'bargraphs'
CONFIG['BOX_DIR']       = 'boxplots'

CONFIG['INPUTFILE']     = 'Video Game Testing Survey FINAL.csv'
CONFIG['INDIEFILE']     = 'Indie.csv'
CONFIG['NONINDIEFILE']  = 'Non-Indie.csv'
CONFIG['MANNWHITNEY']   = 'mannwhitney.csv'
CONFIG['DELTAS']        = 'deltas.csv'

# Analysis Parameters
CONFIG['ALPHA']     = 0.025


# Likert Prompt Column Names
CONFIG['COLS'] = ['Perf1', 'Perf2', 'Perf3', 'Perf4', 'Perf5', 'Perf6', 'Perf7', 'Perf8',
                  'Plan1', 'Plan2', 'Plan3', 'Plan4', 'Plan5', 'Plan6', 'Plan7', 'Plan8', 'Plan9',
                  'Goals1', 'Goals2', 'Goals3', 'Goals4',
                  'Auto1', 'Auto2', 'Auto3', 'Auto4', 'Auto5', 'Auto6', 'Auto7', 'Auto8', 'Auto9', 'Auto10',
                  'Tools1', 'Tools2', 'Tools3', 'Tools4', 'Tools5', 'Tools6',
                  'Out1', 'Out2', 'Out3', 'Out4', 'Out5', 'Out6',
                  'Res1', 'Res2', 'Res3', 'Res4', 'Res5', 'Res6', 'Res7', 'Res8', 'Res9']


# CSV Header

CONFIG['CSV_HEADER'] = [
    'ID',
    'Date',
    'Years Active in Games Industry',
    'Roles Held',
    'Years of Indie Exp',
    'Years of AA Exp',
    'Years of AAA Exp',
    'Age',
    'Country',

    'P1 Nick',
    'P1 Type',
    'P1 Primary Role',
    'P1 Other Roles',
    'P1 Engine',
    'P1 Time On Project',
    'P1 Team Size',
    'P1 Budget',
    'P1 Publisher',
    'P1 Project Duration',

    'P1 Test Performance Narrative',
    'P1 Performance 1',
    'P1 Performance 2',
    'P1 Performance 3',
    'P1 Performance 4',
    'P1 Performance 5',
    'P1 Performance 6',
    'P1 Performance 7',
    'P1 Performance 8',

    'P1 Test Planning Narrative',
    'P1 Planning 1',
    'P1 Planning 2',
    'P1 Planning 3',
    'P1 Planning 4',
    'P1 Planning 5',
    'P1 Planning 6',
    'P1 Planning 7',
    'P1 Planning 8',
    'P1 Planning 9',

    'P1 Test Goals',
    'P1 Goals 1',
    'P1 Goals 2',
    'P1 Goals 3',
    'P1 Goals 4',

    'P1 Test Automation Narrative',
    'P1 Automation 1',
    'P1 Automation 2',
    'P1 Automation 3',
    'P1 Automation 4',
    'P1 Automation 5',
    'P1 Automation 6',
    'P1 Automation 7',
    'P1 Automation 8',
    'P1 Automation 9',
    'P1 Automation 10',

    'P1 Test Tools',
    'P1 Tools 1',
    'P1 Tools 2',
    'P1 Tools 3',
    'P1 Tools 4',
    'P1 Tools 5',
    'P1 Tools 6',

    'P1 Test Output Narrative',
    'P1 Output 1',
    'P1 Output 2',
    'P1 Output 3',
    'P1 Output 4',
    'P1 Output 5',
    'P1 Output 6',

    'P1 Test Resources',
    'P1 Resources 1',
    'P1 Resources 2',
    'P1 Resources 3',
    'P1 Resources 4',
    'P1 Resources 5',
    'P1 Resources 6',
    'P1 Resources 7',
    'P1 Resources 8',
    'P1 Resources 9',

    'P1 Additional Info',

    'P2 Nick',
    'P2 Type',
    'P2 Primary Role',
    'P2 Other Roles',
    'P2 Engine',
    'P2 Time On Project',
    'P2 Team Size',
    'P2 Budget',
    'P2 Publisher',
    'P2 Project Duration',

    'P2 Test Performance Narrative',
    'P2 Performance 1',
    'P2 Performance 2',
    'P2 Performance 3',
    'P2 Performance 4',
    'P2 Performance 5',
    'P2 Performance 6',
    'P2 Performance 7',
    'P2 Performance 8',

    'P2 Test Planning Narrative',
    'P2 Planning 1',
    'P2 Planning 2',
    'P2 Planning 3',
    'P2 Planning 4',
    'P2 Planning 5',
    'P2 Planning 6',
    'P2 Planning 7',
    'P2 Planning 8',
    'P2 Planning 9',

    'P2 Test Goals',
    'P2 Goals 1',
    'P2 Goals 2',
    'P2 Goals 3',
    'P2 Goals 4',

    'P2 Test Automation Narrative',
    'P2 Automation 1',
    'P2 Automation 2',
    'P2 Automation 3',
    'P2 Automation 4',
    'P2 Automation 5',
    'P2 Automation 6',
    'P2 Automation 7',
    'P2 Automation 8',
    'P2 Automation 9',
    'P2 Automation 10',

    'P2 Test Tools',
    'P2 Tools 1',
    'P2 Tools 2',
    'P2 Tools 3',
    'P2 Tools 4',
    'P2 Tools 5',
    'P2 Tools 6',

    'P2 Test Output Narrative',
    'P2 Output 1',
    'P2 Output 2',
    'P2 Output 3',
    'P2 Output 4',
    'P2 Output 5',
    'P2 Output 6',

    'P2 Test Resources',
    'P2 Resources 1',
    'P2 Resources 2',
    'P2 Resources 3',
    'P2 Resources 4',
    'P2 Resources 5',
    'P2 Resources 6',
    'P2 Resources 7',
    'P2 Resources 8',
    'P2 Resources 9',

    'P2 Additional Info',

    'P3 Nick',
    'P3 Type',
    'P3 Primary Role',
    'P3 Other Roles',
    'P3 Engine',
    'P3 Time On Project',
    'P3 Team Size',
    'P3 Budget',
    'P3 Publisher',
    'P3 Project Duration',

    'P3 Test Performance Narrative',
    'P3 Performance 1',
    'P3 Performance 2',
    'P3 Performance 3',
    'P3 Performance 4',
    'P3 Performance 5',
    'P3 Performance 6',
    'P3 Performance 7',
    'P3 Performance 8',

    'P3 Test Planning Narrative',
    'P3 Planning 1',
    'P3 Planning 2',
    'P3 Planning 3',
    'P3 Planning 4',
    'P3 Planning 5',
    'P3 Planning 6',
    'P3 Planning 7',
    'P3 Planning 8',
    'P3 Planning 9',

    'P3 Test Goals',
    'P3 Goals 1',
    'P3 Goals 2',
    'P3 Goals 3',
    'P3 Goals 4',

    'P3 Test Automation Narrative',
    'P3 Automation 1',
    'P3 Automation 2',
    'P3 Automation 3',
    'P3 Automation 4',
    'P3 Automation 5',
    'P3 Automation 6',
    'P3 Automation 7',
    'P3 Automation 8',
    'P3 Automation 9',
    'P3 Automation 10',

    'P3 Test Tools',
    'P3 Tools 1',
    'P3 Tools 2',
    'P3 Tools 3',
    'P3 Tools 4',
    'P3 Tools 5',
    'P3 Tools 6',

    'P3 Test Output Narrative',
    'P3 Output 1',
    'P3 Output 2',
    'P3 Output 3',
    'P3 Output 4',
    'P3 Output 5',
    'P3 Output 6',

    'P3 Test Resources',
    'P3 Resources 1',
    'P3 Resources 2',
    'P3 Resources 3',
    'P3 Resources 4',
    'P3 Resources 5',
    'P3 Resources 6',
    'P3 Resources 7',
    'P3 Resources 8',
    'P3 Resources 9',

    'P3 Additional Info',

    'QA - Helpful',
    'QA - Painful',
    'QA - Wants'
]