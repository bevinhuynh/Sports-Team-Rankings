import csv
from sportclub import SportClub
from typing import List, Iterable

def separateSports(all_clubs: List[SportClub]) -> Iterable[List[SportClub]]:
    list_of_sports = []
    list_of_teams = []
    final_list = []
    for i in all_clubs:
        if i.sport not in list_of_sports:
            list_of_sports.append(i.sport)
    for i in list_of_sports:
        for y in all_clubs:
            if y.sport == i:
                list_of_teams.append(y)
        final_list.append(list_of_teams)
        list_of_teams = []

    return final_list
    


    
    
        
    """Separate a list of SportClubs into their own sports

    For example, given the list [SportClub("LA", "Lakers", "NBA"), SportClub("Houston", "Rockets", "NBA"), SportClub("LA", "Angels", "MLB")],
    return the iterable [[SportClub("LA", "Lakers", "NBA"), SportClub("Houston", "Rockets", "NBA")], [SportClub("LA", "Angels", "MLB")]]

    Args:
        all_clubs: A list of SportClubs that contain SportClubs of 1 or more sports.

    Returns:
        An iterable of lists of sportclubs that only contain clubs playing the same sport. 
    """
    # TODO: Complete the function
    return [[]]  # erase this


def sortSport(sport: List[SportClub]) -> List[SportClub]:
    one_team = []
    final_teams = []
    rough_number_list = []
    final_number_list = []
    #for i in sport:
    #    print(i)
    for i in sport:
        number = i.count
        rough_number_list.append(i.count)
    for i in rough_number_list:
        if i not in final_number_list:
            final_number_list.append(i)
    final_number_list.sort()
    final_number_list.reverse()
    for number in final_number_list:
        one_team = []
        for team in sport:
            if team.count == number:
                one_team.append(team)
        one_team.sort()
        for i in one_team:
            final_teams.append(i)
        
    



    #for i in x:
    #    print(i)
   # print()
    return final_teams
    """Sort a list of SportClubs by the inverse of their count and their name

    For example, given the list [SportClub("Houston", "Rockets", "NBA", 80), SportClub("LA", "Warriors", "NBA", 130), SportClub("LA", "Lakers", "NBA", 130)] 
    return the list [SportClub("LA", "Lakers", "NBA", 130), SportClub("LA", "Warriors", "NBA", 130), SportClub("Houston", "Rockets", "NBA", 80)]

    Args:
        sport: A list of SportClubs that only contain clubs playing the same sport

    Returns:
        A sorted list of the SportClubs  
    """
    # TODO: Complete the function
    # hint: check documentation for sorting lists 
    # ( https://docs.python.org/3/library/functions.html#sorted , https://docs.python.org/3/howto/sorting.html#sortinghowto )


def outputSports(sorted_sports: Iterable[List[SportClub]]) -> None:
    with open('survey_database.csv', 'w', newline = '') as myCSVfile:
        writeToMyCSV = csv.writer(myCSVfile)
        writeToMyCSV.writerow(['City', 'Team Name', 'Sport', 'Number of Times Picked'])
        for i in sorted_sports:
            for index, y in enumerate(i):
                if index != 3:
                    writeToMyCSV.writerow([y.city,y.name,y.sport,y.count])
                else:
                    break
        myCSVfile.close()
    """Create the output csv given an iterable of list of sorted clubs

    Create the csv "survey_database.csv" in the current working directory, and output the information:
    "City,Team Name,Sport,Number of Times Picked" for the top 3 teams in each sport.

    Args:
        sorted_sports: an Iterable of different sports, each already sorted correctly
    """
    # TODO: Complete the function
