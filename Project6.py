###############################################################
# CSE 231 project #6
#
# program that deals with characters from a video game called Genshin
# this program will read character data from a file and filter characters based on given criteria
# 
#function to open the csv file
#function to read the file and return master list of characters
#function to get characters by a certain criteria
#function to get characters by multiple criteria
#function to get list of all possible regions
#function to sort characters by name and rarity
#function to display the characters in a nice format
#function to get an option from user
#main function to call all other functions
###############################################################

import csv
from operator import itemgetter

#constant variables to use as reference 
NAME = 0
ELEMENT = 1
WEAPON = 2
RARITY = 3
REGION = 4

#displayed menu to user
MENU = "\nWelcome to Genshin Impact Character Directory\n\
        Choose one of below options:\n\
        1. Get all available regions\n\
        2. Filter characters by a certain criteria\n\
        3. Filter characters by element, weapon, and rarity\n\
        4. Quit the program\n\
        Enter option: "

#given constants
INVALID_INPUT = "\nInvalid input"

CRITERIA_INPUT = "\nChoose the following criteria\n\
                 1. Element\n\
                 2. Weapon\n\
                 3. Rarity\n\
                 4. Region\n\
                 Enter criteria number: "

VALUE_INPUT = "\nEnter value: "

ELEMENT_INPUT = "\nEnter element: "
WEAPON_INPUT = "\nEnter weapon: "
RARITY_INPUT = "\nEnter rarity: "

HEADER_FORMAT = "\n{:20s}{:10s}{:10s}{:<10s}{:25s}"
ROW_FORMAT = "{:20s}{:10s}{:10s}{:<10d}{:25s}"


def open_file():
    '''A function that opens the csv file and returns file pointer
    parameters: none
    returns: filepointer'''
    prompt = input("Enter file name: ")
    while True:
        try:
            #try opening the name of the file given
            fp = open(prompt)
            #return that file if it is found
            return fp
            break
        except FileNotFoundError:
            #if file is not found, try asking again
            print("\nError opening file. Please try again.")
            prompt = input("Enter file name: ")

def read_file(fp):
    '''A function to read the file pointer returned by open_file and returns master list of characters
    fp : file pointer returned by open_file
    returns: master list of characters'''
    reader = csv.reader(fp)
    #skip header row
    next(reader)
    #empty list that the characters will be appended to.
    list_of_tuples = []
    #read through each line
    for line in reader:
        #name is at index 0
        name_str = str(line[0])
        #element at index 2
        element_str = str(line[2])
        #weapon at index 3
        weapon_str = str(line[3])
        #rarity is at index 1
        rarity_int = int(line[1])
        #region is at index 4
        region_str = str(line[4])
        #if region empty, assign value None
        if region_str == '':
            region_str = None
            #change order
        char_tuple = (name_str, element_str, weapon_str, rarity_int, region_str)
        #append to list
        list_of_tuples.append(char_tuple)
        #print(list_of_tuples)
    return list_of_tuples

def get_characters_by_criterion (list_of_tuples, criteria, value):
    '''function to get characters by a certain criteria
    list_of_tuples: master list returned by read_file
    criteria: what character attribute to filter on
    value: specific value to filter on
    returns: characters that match the given criteria'''
    criteria_int = int(criteria)
    new_list = []
    #empty_list
    for a_tuple in list_of_tuples:
        if list_of_tuples == []: #if given list is empty, return empty list
            return new_list
        if criteria_int == ELEMENT: #element
            value_str = str(value) #convert value to string
            value_str_low = value_str.lower() #make value lowercase
            if a_tuple[1] != None: #disregard the Value of None
                if a_tuple[1].lower() == value_str_low:
                    new_list.append(a_tuple) #append to empty list
        if criteria_int == WEAPON: #weapon
            value_str = str(value) #convert value to string
            value_str_low = value_str.lower() #make value lowercase
            if a_tuple[2] != None: #disregard None value
                if a_tuple[2].lower() == value_str_low:
                    new_list.append(a_tuple) #append to empty list
        if criteria_int == RARITY: #rarity
            value_int = int(value) #convert value to int if == rarity
            if a_tuple[3] != None: #disregard None value
                if a_tuple[3] == value_int:
                    new_list.append(a_tuple) #append to empty list
        if criteria_int == REGION: #region
            value_str = str(value) #make value a string
            value_str_low = value_str.lower() #make value lowercase
            if a_tuple[4] != None: #disregard None value
                if a_tuple[4].lower() == value_str_low:
                    new_list.append(a_tuple) #append to empty list
    return new_list
        
def get_characters_by_criteria(master_list, element, weapon, rarity):
    '''function to get characters by multiple criteria
    master_list: main list of all characters
    element: what element to filter on
    weapon: what weapon to filter on
    rarity: what rarity to filter on
    returns: list of characters that match the given criteria'''
    element_filter = get_characters_by_criterion(master_list, ELEMENT, element) #filter by element first
    weapon_filter = get_characters_by_criterion(element_filter, WEAPON, weapon) #filter by weapon second
    rarity_filter = get_characters_by_criterion(weapon_filter, RARITY, rarity) #filter by rarity last
    return rarity_filter 

def get_region_list  (master_list):
    '''function to get list of all possible regions
    master_list: list of ll characters and their attributes
    returns: list of all regions, sorted'''
    region_list = []
    #loop through master list
    for a_tuple in master_list:
        if a_tuple[4] != None: #dont include None
            if a_tuple[4] not in region_list: #check and see if the region is not in the initial empty list
                region_list.append(a_tuple[4]) #if it is not, append it to the list. This tackles duplicate issue
        sorted_list = sorted(region_list) #sort regions for more accurate testing
    return sorted_list

def sort_characters (list_of_tuples):
    '''function to sort characters by name and rarity
    list of tuples: given list of characters
    returns: given list of characters, sorted'''
    # had a difficult time figuring out how to return an empty list, if necessary, so I added many differnt if statements
    if list_of_tuples == []:
        return []
    for a_tuple in list_of_tuples:
        name_sorted = sorted(list_of_tuples)
        if name_sorted == []:
            return []
        name_and_rarity_sorted = sorted(name_sorted, key=itemgetter(3), reverse=True)
        if name_and_rarity_sorted == []:
            return []
    return name_and_rarity_sorted


def display_characters (list_of_tuples):
    '''function to display the characters in a nice format
    list of tuples: given list of characters;
    returns: characters dislayed nicely'''
    # if the given list is empty, return nothing to print
    if list_of_tuples == []:
        print("\nNothing to print.")
    else:
        #given format for headers
        print("\n{:20s}{:10s}{:10s}{:<10s}{:25s}".format("Character", "Element", "Weapon", "Rarity", "Region"))
        for a_tuple in list_of_tuples:
            #if region is None, display "N/A"
            if a_tuple[4] == None:
                print("{:20s}{:10s}{:10s}{:<10d}{:25s}".format(a_tuple[0], a_tuple[1], a_tuple[2], a_tuple[3], "N/A"))
            else:
                #dispaly characters
                print("{:20s}{:10s}{:10s}{:<10d}{:25s}".format(a_tuple[0], a_tuple[1], a_tuple[2], a_tuple[3], a_tuple[4]))

def get_option():
    '''function to get an option from user on what the program will display
    parameters: none
    returns: integer'''
    #print given menu prompt
    prompt = input(MENU)
    #see if input is an integer between 1 and 4
    try:
        prompt_int = int(prompt)
        if 1<= prompt_int <=4:
            return prompt_int
        #if not, display invalid input
        else:
            print(INVALID_INPUT)
    except ValueError:
        print(INVALID_INPUT)
  
def main():
    '''main function to call other functions
    parameters: none
    returns: nothing'''
    #call open file
    fp = open_file()
    #get master list from read_file
    master_list = read_file(fp)
    #get option from user
    user_option = get_option()
    #while the option is not 4, run main loop
    while user_option != 4:
        if user_option == 1: #regions
            #if the option is 1, call get_region_list and display regions
            grab_regions = get_region_list(master_list)
            print("\nRegions:")
            seperator = ", "
            #this will display the regions comma seperated
            print(seperator.join(grab_regions))
        elif user_option == 2: #criterion
            #get criteria from user and convert to an int, also check if it is between 1 and 4
            criteria_prompt = input(CRITERIA_INPUT)
            criteria_prompt_int = int(criteria_prompt)
            while not(1 <= criteria_prompt_int <= 4):
                print(INVALID_INPUT)
                criteria_prompt = input(CRITERIA_INPUT)
                criteria_prompt_int = int(criteria_prompt) 
            #prompt for a value          
            value_prompt = input(VALUE_INPUT)
            #if the criteria is rarity, then convert the value to an integer, if error, then reprompt
            if criteria_prompt_int == RARITY:
                while True:
                    try:
                        value_prompt = int(value_prompt)
                        break
                    except ValueError:
                        print(INVALID_INPUT)
                        value_prompt = input(VALUE_INPUT)
            #call get_chars_by_criterion with the user given parameters, then sort and display the results                 
            chars_by_criterion = get_characters_by_criterion(master_list, criteria_prompt_int, value_prompt)
            sort_chars = sort_characters(chars_by_criterion)
            display_chars = display_characters(sort_chars)
        elif user_option == 3: #criteria
            # get element, weapon, and rarity parameters from user
            element_input = input(ELEMENT_INPUT)
            weapon_input = input(WEAPON_INPUT)
            rarity_input = input(RARITY_INPUT)
            # convert rarity to an integer, if error, reprompt
            while True:
                try:
                    rarity_input_int = int(rarity_input)
                    break
                except ValueError:
                    print(INVALID_INPUT)
                    rarity_input = input(RARITY_INPUT)
            #call get_chars_by_criteria with the user given parameters, then sort and display the results        
            chars_by_criteria = get_characters_by_criteria(master_list, element_input, weapon_input, rarity_input_int)
            sort_chars = sort_characters(chars_by_criteria)
            display_chars = display_characters(sort_chars)
        #end the program
        user_option = get_option()

# DO NOT CHANGE THESE TWO LINES
#These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__":
    main()
    
