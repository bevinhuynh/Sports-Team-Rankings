
from pathlib import Path
import csv
from sportclub import SportClub
from typing import List, Tuple

total_lines_read = 0
def readFile(file: Path) -> List[Tuple[str, str, str]]:
    """Read a CSV file and return its content

    A good CSV file will have the header "City,Team Name,Sport" and appropriate content.

    Args:
        file: a path to the file to be read

    Returns:
        a list of tuples that each contain (city, name, sport) of the SportClub

    Raises:
        ValueError: if the reading csv has missing data (empty fields)  
    """
    list_of_tuples = []
    with open(file, newline ='') as csvfile:
        content = csv.reader(csvfile, delimiter=',')
        current_lines_read = 0
        list_to_tuple = []
        for index, row in enumerate(content):
            if index == 0:
                if row[0] != 'City' or row[1] != 'Team Name' or row[2] != 'Sport':
                    raise ValueError
            elif row[0] == '' or row[1] == '' or row[2]=='':
                raise ValueError
            elif len(row)!= 3:
                raise ValueError
            elif row[0].isspace() == True or row[1].isspace() == True or row[2].isspace() == True:
                raise ValueError
            else:
                list_to_tuple.append(row[0])
                list_to_tuple.append(row[1])
                list_to_tuple.append(row[2])
                x = tuple(list_to_tuple)
                list_of_tuples.append(x)
                list_to_tuple = []
    return list_of_tuples
    


def readAllFiles() -> List[SportClub]:
    """Read all the csv files in the current working directory to create a list of SportClubs that contain unique SportClubs with their corresponding counts

    Take all the csv files in the current working directory, calls readFile(file) on each of them, and accumulates the data gathered into a list of SportClubs.
    Create a new file called "report.txt" in the current working directory containing the number of good files and good lines read. 
    Create a new file called "error_log.txt" in the current working directory containing the name of the error/bad files read.

    Returns:
        a list of unique SportClub objects with their respective counts
    """
    final_list = []
    list_of_clubs = []
    list_of_clubs2 = []
    rough_list = []
    path = Path().cwd()
    list_of_good_files =[]
    badfiles = 0
    badfiles_list = []
    for i in Path(path).glob('*csv'):
        try:
            file_is_read = readFile(i)
            list_of_good_files.append(i)
                #creates the sportclubs from the tuples and puts it in a list
            for club in file_is_read:
                list_of_clubs.append(club)
            #if file read is bad
        except ValueError:
            badfiles = badfiles + 1
            full_file_path = str(i)
            file_name = full_file_path.split('/')[-1]
            badfiles_list.append(file_name)
    #creates the report.txt
    total_lines = 0
    current_lines = 0
    for i in list_of_good_files:
        with open(i,'r', newline ='') as myCSVfile:
            one_file = csv.reader(myCSVfile)
            for line in one_file:
                current_lines = current_lines + 1
        total_lines = (total_lines + current_lines) -1
        current_lines = 0
    report_file = open('report.txt', "w")
    report_file.write(f'Number of files read: {len(list_of_good_files)}\n')
    report_file.write(f'Number of lines read: {total_lines}\n')
    #creates an empty error.txt
    if badfiles == 0:
        error_file = open('error_log.txt','w')
    else:
    #creates error.txt with all the error files
        error_file = open('error_log.txt','w')
        for bad_file in badfiles_list:
            if bad_file != 'survey_database.csv':
                error_file.write(f'{bad_file}\n')
    for i in list_of_clubs:
        y = list(i)
        list_of_clubs2.append(y)
    #getting the count of all the SportClubs
    team_counter = 0
    for one_team in list_of_clubs2:
        for second_team in reversed(list_of_clubs2):
            if one_team[0] == second_team[0] and one_team[1] == second_team[1] and one_team[2]== second_team[2]:
                team_counter = team_counter + 1
        one_team.append(team_counter)
        rough_list.append(one_team)
        team_counter = 0
    rough_list2 = []
    for x in rough_list:
        if x not in rough_list2:
            rough_list2.append(x)
    for i in rough_list2:
        x = SportClub(i[0],i[1],i[2],i[3])
        final_list.append(x)

    
    return final_list
    
