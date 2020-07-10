import pandas as pd

def read_data(file_name):
    return pd.read_csv(file_name)

data = read_data("Terry_Stops.csv")

# Columns
# ['Subject Age Group', 'Subject ID', 'GO / SC Num', 'Terry Stop ID',
#      'Stop Resolution', 'Weapon Type', 'Officer ID', 'Officer YOB',
#      'Officer Gender', 'Officer Race', 'Subject Perceived Race',
#      'Subject Perceived Gender', 'Reported Date', 'Reported Time',
#      'Initial Call Type', 'Final Call Type', 'Call Type', 'Officer Squad',
#      'Arrest Flag', 'Frisk Flag', 'Precinct', 'Sector', 'Beat']

full_df = data[['Subject Age Group', 'Stop Resolution', 'Weapon Type', 'Officer Gender', 'Officer Race',
            'Subject Perceived Race', 'Subject Perceived Gender', 'Initial Call Type', 'Final Call Type',
            'Call Type', 'Arrest Flag', 'Frisk Flag']]

# total terry stops
rid_unknown = (full_df['Subject Perceived Race'] != 'Unknown')
rid_dash = (full_df['Subject Perceived Race'] != '-')
stops_df = full_df[rid_unknown & rid_dash]
total_stops = len(stops_df)

print("Total Number of Terry Stops: " + str(total_stops))
print()

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

sus_stop = stops_df['Initial Call Type'] == 'SUSPICIOUS STOP - OFFICER INITIATED ONVIEW'
# sus_person = stops_df['Initial Call Type'] == 'SUSPICIOUS PERSON, VEHICLE OR INCIDENT'
# disturbance = stops_df['Initial Call Type'] == 'DISTURBANCE, MISCELLANEOUS/OTHER'
traffic_stop = stops_df['Initial Call Type'] == 'TRAFFIC STOP - OFFICER INITIATED ONVIEW'

stops_df = stops_df[traffic_stop]
# total_reasoning = len(reasoning_df)
# print('Total Stopped (w/ sus reasoning): ' + str(total_reasoning))


# filtered -- subject race is black and call type is ONVIEW (police viewing)
def subject_race(df, race):
    # (df['Officer Race'] == 'White') & (df['Officer Gender'] == 'M')
    df = df[(df['Call Type'] == 'ONVIEW')]
    race_df = df[(df['Subject Perceived Race'] == race) & (df['Subject Perceived Gender'] == 'Male')]
    return race_df

black_subject = subject_race(stops_df, 'Black or African American')
total_black_subject = len(black_subject)
print('Total Black: ' + str(total_black_subject))



black_frisk = black_subject[black_subject['Frisk Flag'] == 'Y']
print('Black Frisked: ' + str(len(black_frisk) / total_black_subject * 100))

black_arrest = black_subject[black_subject['Arrest Flag'] == 'Y']
print('Black Arrested: ' + str(len(black_arrest) / total_black_subject * 100))
print()

white_subject = subject_race(stops_df, 'White')
total_white_subject = len(white_subject)
print('Total White: ' + str(total_white_subject))

white_frisk = white_subject[white_subject['Frisk Flag'] == 'Y']
print('White Frisked: ' + str(len(white_frisk) / total_white_subject * 100))

white_arrest = white_subject[white_subject['Arrest Flag'] == 'Y']
print('White Arrested: ' + str(len(white_arrest) / total_white_subject * 100))