# -*- coding: utf-8 -*-
"""team_productivity.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LjLDsUI0K3BvyDiTmntRl-FIjW-92Srn
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

team_df = pd.read_csv('productivity.csv')
team_df.head()

team_df.drop(['Timestamp', 'Email Address'], axis = 1, inplace = True)
team_df.head()

dict = {'1. What is your Office Duration (in hours)?': 'office_duration',
        '2. How long have you been working as a developer?': 'working_as_developer',
        '3. How often do you participate in decision making?': 'decision_making',
        '4. Do your teammates motivate you in your work?':'motivated_teammate',
        '5. Are you satisfied with your career growth?':'career_growth',
        '6. Number of Projects last year (approximately)?':'number_of_projects',
        '7. How is your relationship with your teammates?':'relationship_with_teammates',
        "8. Do you think scrum meetings increase your team's productivity?":'scrum_meetings_productivity',
        '9. How often do you cross deadline?':'cross_deadline',
        '10. How often do you work overtime?':'work_overtime',
        '11. How often do you hangout as a team?':'hangout_as_team',
        '12. With how many teams are you involved with currently?':'teams_involved',
        '13. Are your team leaders friendly?':'team_leaders_friendly',
        '14. Gender Diversity':'gender_diversity',
        '15. Average age of the teammates':'avg_age',
        '16. With how many teams have you been with until now?':'teams_no'}

team_df.rename(columns=dict,
          inplace=True)
print(team_df.head())

print(team_df)
print(team_df.info())
print(team_df.describe())

print('office_duration: \n', team_df.office_duration.value_counts())
print('working_as_developer: \n', team_df.working_as_developer.value_counts())
print('decision_making: \n', team_df.decision_making.value_counts())
print('motivated_teammate: \n', team_df.motivated_teammate.value_counts())
print('career_growth: \n', team_df.career_growth.value_counts())
print('number_of_projects: \n', team_df.number_of_projects.value_counts())
print('relationship_with_teammates: \n', team_df.relationship_with_teammates.value_counts())
print('scrum_meetings_productivity: \n', team_df.scrum_meetings_productivity.value_counts())
print('cross_deadline: \n', team_df.cross_deadline.value_counts())
print('work_overtime: \n', team_df.work_overtime.value_counts())
print('hangout_as_team: \n', team_df.hangout_as_team.value_counts())
print('teams_involved: \n', team_df.teams_involved.value_counts())
print('team_leaders_friendly: \n', team_df.team_leaders_friendly.value_counts())
print('gender_diversity: \n', team_df.gender_diversity.value_counts())
print('avg_age: \n', team_df.avg_age.value_counts())
print('teams_no: \n', team_df.teams_no.value_counts())

# office_duration
team_df.loc[team_df["office_duration"] == "6 hours or less", "office_duration"] = 1
team_df.loc[team_df["office_duration"] == "7 hours", "office_duration"] = 2
team_df.loc[team_df["office_duration"] == "8 hours", "office_duration"] = 3
team_df.loc[team_df["office_duration"] == "9 hours", "office_duration"] = 4
team_df.loc[team_df["office_duration"] == "10 hours or more", "office_duration"] = 5

# working_as_developer
team_df.loc[team_df["working_as_developer"] == "Less than 1 year", "working_as_developer"] = 1
team_df.loc[team_df["working_as_developer"] == "1 - 2 years", "working_as_developer"] = 2
team_df.loc[team_df["working_as_developer"] == "3 - 6 years", "working_as_developer"] = 3
team_df.loc[team_df["working_as_developer"] == "7 - 10 years", "working_as_developer"] = 4
team_df.loc[team_df["working_as_developer"] == "More than 10 years", "working_as_developer"] = 5

# decision_making
team_df.loc[team_df["decision_making"] == "Never", "decision_making"] = 1
team_df.loc[team_df["decision_making"] == "Rarely", "decision_making"] = 2
team_df.loc[team_df["decision_making"] == "Sometimes", "decision_making"] = 3
team_df.loc[team_df["decision_making"] == "Often", "decision_making"] = 4
team_df.loc[team_df["decision_making"] == "Always", "decision_making"] = 5

# motivated_teammate
team_df.loc[team_df["motivated_teammate"] == "Never", "motivated_teammate"] = 1
team_df.loc[team_df["motivated_teammate"] == "Rarely", "motivated_teammate"] = 2
team_df.loc[team_df["motivated_teammate"] == "Sometimes", "motivated_teammate"] = 3
team_df.loc[team_df["motivated_teammate"] == "Often", "motivated_teammate"] = 4
team_df.loc[team_df["motivated_teammate"] == "Always", "motivated_teammate"] = 5

# career_growth
team_df.loc[team_df["career_growth"] == "Strongly Disagree", "career_growth"] = 1
team_df.loc[team_df["career_growth"] == "Disagree", "career_growth"] = 2
team_df.loc[team_df["career_growth"] == "Neutral", "career_growth"] = 3
team_df.loc[team_df["career_growth"] == "Agree", "career_growth"] = 4
team_df.loc[team_df["career_growth"] == "Strongly Agree", "career_growth"] = 5

# number_of_projects
team_df.loc[team_df["number_of_projects"] == "Less than 2", "number_of_projects"] = 1
team_df.loc[team_df["number_of_projects"] == "2 - 4", "number_of_projects"] = 2
team_df.loc[team_df["number_of_projects"] == "5 - 7", "number_of_projects"] = 3
team_df.loc[team_df["number_of_projects"] == "8 - 10", "number_of_projects"] = 4
team_df.loc[team_df["number_of_projects"] == "More than 10", "number_of_projects"] = 5

# relationship_with_teammates
team_df.loc[team_df["relationship_with_teammates"] == "Poor", "relationship_with_teammates"] = 1
team_df.loc[team_df["relationship_with_teammates"] == "Bad", "relationship_with_teammates"] = 2
team_df.loc[team_df["relationship_with_teammates"] == "Average", "relationship_with_teammates"] = 3
team_df.loc[team_df["relationship_with_teammates"] == "Good", "relationship_with_teammates"] = 4
team_df.loc[team_df["relationship_with_teammates"] == "Excellent", "relationship_with_teammates"] = 5

# scrum_meetings_productivity
team_df.loc[team_df["scrum_meetings_productivity"] == "Strongly Disagree", "scrum_meetings_productivity"] = 1
team_df.loc[team_df["scrum_meetings_productivity"] == "Disagree", "scrum_meetings_productivity"] = 2
team_df.loc[team_df["scrum_meetings_productivity"] == "Neutral", "scrum_meetings_productivity"] = 3
team_df.loc[team_df["scrum_meetings_productivity"] == "Agree", "scrum_meetings_productivity"] = 4
team_df.loc[team_df["scrum_meetings_productivity"] == "Strongly Agree", "scrum_meetings_productivity"] = 5

# cross_deadline
team_df.loc[team_df["cross_deadline"] == "Never", "cross_deadline"] = 1
team_df.loc[team_df["cross_deadline"] == "Rarely", "cross_deadline"] = 2
team_df.loc[team_df["cross_deadline"] == "Sometimes", "cross_deadline"] = 3
team_df.loc[team_df["cross_deadline"] == "Often", "cross_deadline"] = 3
team_df.loc[team_df["cross_deadline"] == "Always", "cross_deadline"] = 5

# work_overtime
team_df.loc[team_df["work_overtime"] == "Never", "work_overtime"] = 1
team_df.loc[team_df["work_overtime"] == "Rarely", "work_overtime"] = 2
team_df.loc[team_df["work_overtime"] == "Sometimes", "work_overtime"] = 3
team_df.loc[team_df["work_overtime"] == "Often", "work_overtime"] = 4
team_df.loc[team_df["work_overtime"] == "Always", "work_overtime"] = 5

# hangout_as_team

team_df.loc[team_df["hangout_as_team"] == "Never", "hangout_as_team"] = 1
team_df.loc[team_df["hangout_as_team"] == "Rarely", "hangout_as_team"] = 2
team_df.loc[team_df["hangout_as_team"] == "Sometimes", "hangout_as_team"] = 3
team_df.loc[team_df["hangout_as_team"] == "Often", "hangout_as_team"] = 4
team_df.loc[team_df["hangout_as_team"] == "Always", "hangout_as_team"] = 5


# team_leaders_friendly
team_df.loc[team_df["team_leaders_friendly"] == "Strongly Disagree", "team_leaders_friendly"] = 1
team_df.loc[team_df["team_leaders_friendly"] == "Disagree", "team_leaders_friendly"] = 2
team_df.loc[team_df["team_leaders_friendly"] == "Neutral", "team_leaders_friendly"] = 3
team_df.loc[team_df["team_leaders_friendly"] == "Agree", "team_leaders_friendly"] = 4
team_df.loc[team_df["team_leaders_friendly"] == "Strongly Agree", "team_leaders_friendly"] = 5

# gender_diversity
team_df.loc[team_df["gender_diversity"] == "High male dominance(above 80% male)", "gender_diversity"] = 1
team_df.loc[team_df["gender_diversity"] == "Moderate male dominance(60%-80% male)", "gender_diversity"] = 2
team_df.loc[team_df["gender_diversity"] == "Balanced(around 50% male and 50% female)", "gender_diversity"] = 3
team_df.loc[team_df["gender_diversity"] == "Moderate female dominance(60%-80% female)", "gender_diversity"] = 4
team_df.loc[team_df["gender_diversity"] == "High female dominance(above 80% female)", "gender_diversity"] = 5


# avg_age
team_df.loc[team_df["avg_age"] == "21 - 25", "avg_age"] = 1
team_df.loc[team_df["avg_age"] == "26 - 30", "avg_age"] = 2
team_df.loc[team_df["avg_age"] == "31 - 35", "avg_age"] = 3
team_df.loc[team_df["avg_age"] == "35 - 40", "avg_age"] = 4
team_df.loc[team_df["avg_age"] == "More than 40", "avg_age"] = 5

# teams_no
team_df.loc[team_df["teams_no"] == "Less than 3", "teams_no"] = 1
team_df.loc[team_df["teams_no"] == "3 - 6", "teams_no"] = 2
team_df.loc[team_df["teams_no"] == "7 - 10", "teams_no"] = 3
team_df.loc[team_df["teams_no"] == "11 - 14", "teams_no"] = 4
team_df.loc[team_df["teams_no"] == "More than 14", "teams_no"] = 5


team_df.head()

# data type change
team_df = team_df.astype({"office_duration": int, "working_as_developer": int, "decision_making": int,
                          "motivated_teammate": int, "career_growth": int, "number_of_projects": int,
                          "relationship_with_teammates": int, "scrum_meetings_productivity": int, "cross_deadline": int,
                          "work_overtime": int, "hangout_as_team": int, "teams_involved": int,
                          "team_leaders_friendly": int, "gender_diversity": int, "avg_age": int,
                          "teams_no": int})
team_df.head()

team_df.info()

team_df.describe()

team_df['Productivity1'] = team_df['decision_making']
team_df.head()

team_df['Productivity2'] = team_df['career_growth']
team_df.head()

team_df['Productivity3'] = team_df['number_of_projects']
team_df.head()

# team_df.drop(['Productivity'], axis = 1, inplace = True)
# team_df.head()

import numpy as np
team_df['Productivity'] = np.nan
team_df.loc[(team_df['Productivity1'] >= 3) & (team_df['Productivity2'] >= 3), 'Productivity'] = 'High'
team_df.loc[(team_df['Productivity1'] < 3) | (team_df['Productivity2'] < 3), 'Productivity'] = 'Low'
team_df

team_df['TeamWork1'] = team_df['working_as_developer']
team_df['TeamWork2'] = team_df['motivated_teammate']
team_df['TeamWork3'] = team_df['scrum_meetings_productivity']
team_df['TeamWork4'] = team_df['hangout_as_team']
team_df['TeamWork5'] = team_df['team_leaders_friendly']
team_df['TeamWork6'] = team_df['teams_no']
team_df.head()

import numpy as np
team_df['TeamWork'] = np.nan
team_df.loc[(team_df['TeamWork3'] >= 3) & (team_df['TeamWork4'] >= 3) & (team_df['TeamWork5'] >= 3), 'TeamWork'] = 'Good'
team_df.loc[(team_df['TeamWork3'] < 3) | (team_df['TeamWork4'] < 3) | (team_df['TeamWork5'] < 3), 'TeamWork'] = 'Poor'
team_df

team_df.loc[(team_df['TeamWork1'] >= 2) & (team_df['TeamWork2'] > 4) & (team_df['TeamWork3'] >= 4) & (team_df['TeamWork5'] > 4), 'TeamWork'] = 'Good'
team_df.loc[(team_df['Productivity1'] >= 3) & (team_df['Productivity3'] == 2), 'Productivity'] = 'High'
team_df.loc[(team_df['Productivity1'] <4) & (team_df['Productivity2'] < 4) & team_df(['Productivity3'] == 1), 'Productivity'] = 'Low'
team_df

team_df['Productivity_Teamwork'] = team_df['Productivity'].str.cat(team_df['TeamWork'], sep =" ")
team_df

print('Count: \n', team_df.Productivity_Teamwork.value_counts())

team_df.to_csv('final1.csv')



team_df.corr(method ='pearson')

team_df.corr(method ='kendall')

team_df.corr(method='spearman')

sns.heatmap(team_df.corr(method ='spearman'), cmap='Reds', annot=True, linewidths=0.5, linecolor='yellow', xticklabels=1)
plt.title('Correlation Matrix');

sns.heatmap(team_df.corr(method="spearman").loc[['number_of_projects','career_growth','decision_making','motivated_teammate','scrum_meetings_productivity'],
                                                ['number_of_projects','career_growth','decision_making','motivated_teammate','scrum_meetings_productivity']],
            cmap='Reds', annot=True, linewidths=0.5, linecolor='yellow', xticklabels=1)

sns.heatmap(team_df.corr(method="spearman").loc[['number_of_projects','career_growth'],
                                                ['office_duration','cross_deadline','work_overtime']],
            cmap='Reds', annot=True, linewidths=0.5, linecolor='yellow', xticklabels=1)

# Commented out IPython magic to ensure Python compatibility.
import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (10, 6)
matplotlib.rcParams['figure.facecolor'] = '#00000000'

df = pd.read_csv('productivity.csv')
df.drop(['Timestamp', 'Email Address'], axis = 1, inplace = True)
df.head()

dict = {'1. What is your Office Duration (in hours)?': 'office_duration',
        '2. How long have you been working as a developer?': 'working_as_developer',
        '3. How often do you participate in decision making?': 'decision_making',
        '4. Do your teammates motivate you in your work?':'motivated_teammate',
        '5. Are you satisfied with your career growth?':'career_growth',
        '6. Number of Projects last year (approximately)?':'number_of_projects',
        '7. How is your relationship with your teammates?':'relationship_with_teammates',
        "8. Do you think scrum meetings increase your team's productivity?":'scrum_meetings_productivity',
        '9. How often do you cross deadline?':'cross_deadline',
        '10. How often do you work overtime?':'work_overtime',
        '11. How often do you hangout as a team?':'hangout_as_team',
        '12. With how many teams are you involved with currently?':'teams_involved',
        '13. Are your team leaders friendly?':'team_leaders_friendly',
        '14. Gender Diversity':'gender_diversity',
        '15. Average age of the teammates':'avg_age',
        '16. With how many teams have you been with until now?':'teams_no'}

df.rename(columns=dict,
          inplace=True)
print(df.head())

px.histogram(df, x='number_of_projects', color='decision_making', title='number_of_projects vs decision_making') #done

px.histogram(df, x='number_of_projects', color='career_growth', title='number_of_projects vs career_growth') #done

px.histogram(df, x='number_of_projects', color='relationship_with_teammates', title='number_of_projects vs relationship_with_teammates')

px.histogram(df, x='number_of_projects', color='scrum_meetings_productivity', title='number_of_projects vs scrum_meetings_productivity')

px.histogram(df, x='number_of_projects', color='teams_involved', title='number_of_projects vs teams_involved')

px.histogram(df, x='number_of_projects', color='team_leaders_friendly', title='number_of_projects vs team_leaders_friendly')

px.histogram(df, x='number_of_projects', color='gender_diversity', title='number_of_projects vs gender_diversity')

px.histogram(df, x='working_as_developer', color='decision_making', title='working_as_developer vs decision_making') #done

px.histogram(df, x='working_as_developer', color='career_growth', title='working_as_developer vs career_growth')

px.histogram(df, x='working_as_developer', color='teams_no', title='working_as_developer vs teams_no')

px.histogram(df, x='career_growth', color='scrum_meetings_productivity', title='career_growth vs scrum_meetings_productivity') #done

px.histogram(df, x='career_growth', color='teams_involved', title='career_growth vs teams_involved')

px.histogram(df, x='career_growth', color='team_leaders_friendly', title='career_growth vs team_leaders_friendly')

px.histogram(df, x='motivated_teammate', color='hangout_as_team', title='motivated_teammate vs hangout_as_team')

px.histogram(df, x='working_as_developer', color='teams_involved', title='working_as_developer vs teams_involved')

px.histogram(df, x='team_leaders_friendly', color='motivated_teammate', title='team_leaders_friendly vs motivated_teammate')

px.histogram(df, x='teams_no', color='decision_making', title='teams_no vs decision_making')

