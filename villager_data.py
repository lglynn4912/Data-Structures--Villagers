"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    
    file = open(filename) 
    species = set()
    for line in file:
        line.strip()
        villager_characteristics = line.split("|")[1]
        species.add(villager_characteristics)
    
    return species

all_species('villagers.csv')


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """
    file = open(filename)
    villagers = []
    species = search_string
    for line in file:
        line.strip()
        char = line.split('|')
        if species == char[1]:
            villagers.append(char[0])
    return villagers

get_villagers_by_species('villagers.csv', 'Bird')


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
education = []
fitness = []
nature = []
music = []
play = []
fashion = []
name = []
    file = open(filename)
    for line in file:
        line.strip()
        char = line.split("|")
        if char[3] == "Education":
            education.append(char[0])
        elif char[3] == "Fitness":
            fitness.append(char[0])
        elif char[3] == 'Nature':
            nature.append(char[0])
        elif char[3] == "Music":
            music.append(char[0])
        elif char[3] == "Play":
            play.append(char[0])
        elif char[3] == "Fashion":                

    return []


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
