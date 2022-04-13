class SurveyResponse:
    """
    A data class representing one entry (row) in the survey responses.
    Validates some data as part of the process.
    """

    def __init__(self, row):
        self.id = int(row[0])
        self.date = row[2]
        self.years_active = float(row[12])

        self.roles_held = []
        if row[13]:
            self.roles_held.append('None')
        if row[14]:
            self.roles_held.append('Dev/Prog/Eng')
        if row[15]:
            self.roles_held.append('QA')
        if row[16]:
            self.roles_held.append('Lead/Prod/Mgr')
        if row[17]:
            self.roles_held.append('Designer/ProdOwner')
        if row[18]:
            self.roles_held.append(row[18])

        self.indie_exp_in_past_decade = int(row[19]) if row[19] else None
        self.aa_exp_in_past_decade = int(row[20]) if row[20] else None
        self.aaa_exp_in_past_decade = int(row[21]) if row[21] else None
        self.age_range = row[22]
        self.country = row[30]

        self.p1 = GameProject(row[33:108])
        self.p2 = GameProject()
        self.p3 = GameProject()

        if row[108] == 'Yes':
            self.p2 = GameProject(row[109:184])
        if row[184] == 'Yes':
            self.p3 = GameProject(row[185:260])

        self.qa_help = row[260]
        self.qa_pain = row[261]
        self.qa_want = row[262]

    def output(self, csv_writer):

        csv_writer.writerow(
            [self.id,
            self.date,
            self.years_active,
            self.roles_held,
            self.indie_exp_in_past_decade,
            self.aa_exp_in_past_decade,
            self.aaa_exp_in_past_decade,
            self.age_range,
            self.country,

            self.p1.nick,
            self.p1.type,
            self.p1.role,
            self.p1.other_roles,
            self.p1.engine,
            self.p1.worktime,
            self.p1.teamsize,
            self.p1.budget,
            self.p1.publisher,
            self.p1.project_duration,

            self.p1.test_performance,
            convert_likert(self.p1.perf1),
            convert_likert(self.p1.perf2),
            convert_likert(self.p1.perf3),
            convert_likert(self.p1.perf4),
            convert_likert(self.p1.perf5),
            convert_likert(self.p1.perf6),
            convert_likert(self.p1.perf7),
            convert_likert(self.p1.perf8),

            self.p1.test_planning,
            convert_likert(self.p1.plan1),
            convert_likert(self.p1.plan2),
            convert_likert(self.p1.plan3),
            convert_likert(self.p1.plan4),
            convert_likert(self.p1.plan5),
            convert_likert(self.p1.plan6),
            convert_likert(self.p1.plan7),
            convert_likert(self.p1.plan8),
            convert_likert(self.p1.plan9),

            self.p1.test_goals,
            convert_likert(self.p1.goals1),
            convert_likert(self.p1.goals2),
            convert_likert(self.p1.goals3),
            convert_likert(self.p1.goals4),

            self.p1.test_automation,
            convert_likert(self.p1.auto1),
            convert_likert(self.p1.auto2),
            convert_likert(self.p1.auto3),
            convert_likert(self.p1.auto4),
            convert_likert(self.p1.auto5),
            convert_likert(self.p1.auto6),
            convert_likert(self.p1.auto7),
            convert_likert(self.p1.auto8),
            convert_likert(self.p1.auto9),
            convert_likert(self.p1.auto10),

            self.p1.test_tools,
            convert_likert(self.p1.tools1),
            convert_likert(self.p1.tools2),
            convert_likert(self.p1.tools3),
            convert_likert(self.p1.tools4),
            convert_likert(self.p1.tools5),
            convert_likert(self.p1.tools6),

            self.p1.test_output,
            convert_likert(self.p1.output1),
            convert_likert(self.p1.output2),
            convert_likert(self.p1.output3),
            convert_likert(self.p1.output4),
            convert_likert(self.p1.output5),
            convert_likert(self.p1.output6),

            self.p1.test_resources,
            convert_likert(self.p1.res1),
            convert_likert(self.p1.res2),
            convert_likert(self.p1.res3),
            convert_likert(self.p1.res4),
            convert_likert(self.p1.res5),
            convert_likert(self.p1.res6),
            convert_likert(self.p1.res7),
            convert_likert(self.p1.res8),
            convert_likert(self.p1.res9),

            self.p1.additional_info,

            ########
            ## P2 ##
            ########

            self.p2.nick,
            self.p2.type,
            self.p2.role,
            self.p2.other_roles,
            self.p2.engine,
            self.p2.worktime,
            self.p2.teamsize,
            self.p2.budget,
            self.p2.publisher,
            self.p2.project_duration,

            self.p2.test_performance,
            convert_likert(self.p2.perf1),
            convert_likert(self.p2.perf2),
            convert_likert(self.p2.perf3),
            convert_likert(self.p2.perf4),
            convert_likert(self.p2.perf5),
            convert_likert(self.p2.perf6),
            convert_likert(self.p2.perf7),
            convert_likert(self.p2.perf8),

            self.p2.test_planning,
            convert_likert(self.p2.plan1),
            convert_likert(self.p2.plan2),
            convert_likert(self.p2.plan3),
            convert_likert(self.p2.plan4),
            convert_likert(self.p2.plan5),
            convert_likert(self.p2.plan6),
            convert_likert(self.p2.plan7),
            convert_likert(self.p2.plan8),
            convert_likert(self.p2.plan9),

            self.p2.test_goals,
            convert_likert(self.p2.goals1),
            convert_likert(self.p2.goals2),
            convert_likert(self.p2.goals3),
            convert_likert(self.p2.goals4),

            self.p2.test_automation,
            convert_likert(self.p2.auto1),
            convert_likert(self.p2.auto2),
            convert_likert(self.p2.auto3),
            convert_likert(self.p2.auto4),
            convert_likert(self.p2.auto5),
            convert_likert(self.p2.auto6),
            convert_likert(self.p2.auto7),
            convert_likert(self.p2.auto8),
            convert_likert(self.p2.auto9),
            convert_likert(self.p2.auto10),

            self.p2.test_tools,
            convert_likert(self.p2.tools1),
            convert_likert(self.p2.tools2),
            convert_likert(self.p2.tools3),
            convert_likert(self.p2.tools4),
            convert_likert(self.p2.tools5),
            convert_likert(self.p2.tools6),

            self.p2.test_output,
            convert_likert(self.p2.output1),
            convert_likert(self.p2.output2),
            convert_likert(self.p2.output3),
            convert_likert(self.p2.output4),
            convert_likert(self.p2.output5),
            convert_likert(self.p2.output6),

            self.p2.test_resources,
            convert_likert(self.p2.res1),
            convert_likert(self.p2.res2),
            convert_likert(self.p2.res3),
            convert_likert(self.p2.res4),
            convert_likert(self.p2.res5),
            convert_likert(self.p2.res6),
            convert_likert(self.p2.res7),
            convert_likert(self.p2.res8),
            convert_likert(self.p2.res9),

            self.p2.additional_info,

            ########
            ## P3 ##
            ########

            self.p3.nick,
            self.p3.type,
            self.p3.role,
            self.p3.other_roles,
            self.p3.engine,
            self.p3.worktime,
            self.p3.teamsize,
            self.p3.budget,
            self.p3.publisher,
            self.p3.project_duration,

            self.p3.test_performance,
            convert_likert(self.p3.perf1),
            convert_likert(self.p3.perf2),
            convert_likert(self.p3.perf3),
            convert_likert(self.p3.perf4),
            convert_likert(self.p3.perf5),
            convert_likert(self.p3.perf6),
            convert_likert(self.p3.perf7),
            convert_likert(self.p3.perf8),

            self.p3.test_planning,
            convert_likert(self.p3.plan1),
            convert_likert(self.p3.plan2),
            convert_likert(self.p3.plan3),
            convert_likert(self.p3.plan4),
            convert_likert(self.p3.plan5),
            convert_likert(self.p3.plan6),
            convert_likert(self.p3.plan7),
            convert_likert(self.p3.plan8),
            convert_likert(self.p3.plan9),

            self.p3.test_goals,
            convert_likert(self.p3.goals1),
            convert_likert(self.p3.goals2),
            convert_likert(self.p3.goals3),
            convert_likert(self.p3.goals4),

            self.p3.test_automation,
            convert_likert(self.p3.auto1),
            convert_likert(self.p3.auto2),
            convert_likert(self.p3.auto3),
            convert_likert(self.p3.auto4),
            convert_likert(self.p3.auto5),
            convert_likert(self.p3.auto6),
            convert_likert(self.p3.auto7),
            convert_likert(self.p3.auto8),
            convert_likert(self.p3.auto9),
            convert_likert(self.p3.auto10),

            self.p3.test_tools,
            convert_likert(self.p3.tools1),
            convert_likert(self.p3.tools2),
            convert_likert(self.p3.tools3),
            convert_likert(self.p3.tools4),
            convert_likert(self.p3.tools5),
            convert_likert(self.p3.tools6),

            self.p3.test_output,
            convert_likert(self.p3.output1),
            convert_likert(self.p3.output2),
            convert_likert(self.p3.output3),
            convert_likert(self.p3.output4),
            convert_likert(self.p3.output5),
            convert_likert(self.p3.output6),

            self.p3.test_resources,
            convert_likert(self.p3.res1),
            convert_likert(self.p3.res2),
            convert_likert(self.p3.res3),
            convert_likert(self.p3.res4),
            convert_likert(self.p3.res5),
            convert_likert(self.p3.res6),
            convert_likert(self.p3.res7),
            convert_likert(self.p3.res8),
            convert_likert(self.p3.res9),

            self.p3.additional_info,

            self.qa_help,
            self.qa_pain,
            self.qa_want]
        )


class GameProject:
    def __init__(self, row=None):

        if row:
            self.nick = row[0]
            self.type = row[1]
            self.role = row[2] if row[2] != 'Other (please specify)' else row[3]
            self.other_roles = []
            if row[4]:
                self.other_roles.append('Dev/Prog/Eng')
            if row[5]:
                self.other_roles.append('QA')
            if row[6]:
                self.other_roles.append('Lead/Prod/Mgr')
            if row[7]:
                self.other_roles.append('Designer/ProdOwner')
            if row[8]:
                self.other_roles.append(row[8])

            self.engine = row[9]
            self.worktime = row[10]
            self.teamsize = row[11]
            self.budget = row[12]
            self.publisher = row[13]
            self.project_duration = row[14]

            self.test_performance = row[15]
            self.perf1 = row[16]
            self.perf2 = row[17]
            self.perf3 = row[18]
            self.perf4 = row[19]
            self.perf5 = row[20]
            self.perf6 = row[21]
            self.perf7 = row[22]
            self.perf8 = row[23]

            self.test_planning = row[24]
            self.plan1 = row[25]
            self.plan2 = row[26]
            self.plan3 = row[27]
            self.plan4 = row[28]
            self.plan5 = row[29]
            self.plan6 = row[30]
            self.plan7 = row[31]
            self.plan8 = row[32]
            self.plan9 = row[33]

            self.test_goals = row[34]
            self.goals1 = row[35]
            self.goals2 = row[36]
            self.goals3 = row[37]
            self.goals4 = row[38]

            self.test_automation = row[39]
            self.auto1 = row[40]
            self.auto2 = row[41]
            self.auto3 = row[42]
            self.auto4 = row[43]
            self.auto5 = row[44]
            self.auto6 = row[45]
            self.auto7 = row[46]
            self.auto8 = row[47]
            self.auto9 = row[48]
            self.auto10 = row[49]

            self.test_tools = row[50]
            self.tools1 = row[51]
            self.tools2 = row[52]
            self.tools3 = row[53]
            self.tools4 = row[54]
            self.tools5 = row[55]
            self.tools6 = row[56]

            self.test_output = row[57]
            self.output1 = row[58]
            self.output2 = row[59]
            self.output3 = row[60]
            self.output4 = row[61]
            self.output5 = row[62]
            self.output6 = row[63]

            self.test_resources = row[64]
            self.res1 = row[65]
            self.res2 = row[66]
            self.res3 = row[67]
            self.res4 = row[68]
            self.res5 = row[69]
            self.res6 = row[70]
            self.res7 = row[71]
            self.res8 = row[72]
            self.res9 = row[73]

            self.additional_info = row[74]

        else:
            self.nick = 'N/A'
            self.type = ''
            self.role = ''
            self.other_roles = []

            self.engine = ''
            self.worktime = ''
            self.teamsize = ''
            self.budget = ''
            self.publisher = ''
            self.project_duration = ''

            self.test_performance = ''
            self.perf1 = ''
            self.perf2 = ''
            self.perf3 = ''
            self.perf4 = ''
            self.perf5 = ''
            self.perf6 = ''
            self.perf7 = ''
            self.perf8 = ''

            self.test_planning = ''
            self.plan1 = ''
            self.plan2 = ''
            self.plan3 = ''
            self.plan4 = ''
            self.plan5 = ''
            self.plan6 = ''
            self.plan7 = ''
            self.plan8 = ''
            self.plan9 = ''

            self.test_goals = ''
            self.goals1 = ''
            self.goals2 = ''
            self.goals3 = ''
            self.goals4 = ''

            self.test_automation = ''
            self.auto1 = ''
            self.auto2 = ''
            self.auto3 = ''
            self.auto4 = ''
            self.auto5 = ''
            self.auto6 = ''
            self.auto7 = ''
            self.auto8 = ''
            self.auto9 = ''
            self.auto10 = ''

            self.test_tools = ''
            self.tools1 = ''
            self.tools2 = ''
            self.tools3 = ''
            self.tools4 = ''
            self.tools5 = ''
            self.tools6 = ''

            self.test_output = ''
            self.output1 = ''
            self.output2 = ''
            self.output3 = ''
            self.output4 = ''
            self.output5 = ''
            self.output6 = ''

            self.test_resources = ''
            self.res1 = ''
            self.res2 = ''
            self.res3 = ''
            self.res4 = ''
            self.res5 = ''
            self.res6 = ''
            self.res7 = ''
            self.res8 = ''
            self.res9 = ''

            self.additional_info = ''


def convert_likert(raw):
    val = None

    if raw == 'Strongly Agree':
        val = 5
    elif raw == 'Somewhat Agree':
        val = 4
    elif raw == 'Neither Agree nor Disagree':
        val = 3
    elif raw == 'Somewhat Disagree':
        val = 2
    elif raw == 'Strongly Disagree':
        val = 1
    elif raw == 'N/A':
        val = 0
    elif raw == 'Unknown':
        val = -1

    return val
