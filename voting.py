# Write documentation for this file 
"""
Write documentation for this module here.
"""
# import functions to build out ballots for testing purposes
from data import *

# Prelab
def count_appearances(element, l):
    """Counts the number of times that element appears in list l.

    >>> count_appearances('Eve', ['Abe', 'Eve', 'Fred', 'Eve', 'Eve'])
    3
    >>> count_appearances('Fred', ['Abe', 'Eve', 'Fred', 'Eve', 'Eve'])
    1
    >>> count_appearances('Rohit', ['Abe', 'Eve', 'Fred', 'Eve', 'Eve'])
    0
    """
    #we define an empty variable which we will keep accumulating values to
    count = 0
    for n in l:
        if n == element:
            count = count+1
    return count 


# Prelab
def first_appearance(element, l):
    """Computes the index where element first appears in list l.

    If the element doesn't appear in the list at all, then the
    function should return -1.

    >>> first_appearance('c', ['a', 'b', 'c', 'd'])
    2
    >>> first_appearance('b', ['a', 'b', 'c', 'b', 'd'])
    1
    >>> first_appearance('f', ['a', 'b', 'c', 'b', 'd'])
    -1
    """
    #we create a for loo[ that loops through every value in our list 
    for n in range(0, len(l)):
        # we use a conditional statement, such that the function returns the index of the element that it takes
        if element == l[n]:
            return n 
    return -1


# Part 1.1
def first_choice_votes(ballots):
    """Computes the first choice of voters from a list of strings. 


    >>> first_choice_votes([['Ali', 'jack'], ['yasmine', 'emily']])
    ['Ali', 'yasmine']
    >>> first_choice_votes([['Ghali', 'lina'], ['Katie', 'James']])
    ['Ghali', 'Katie']
    """
    # we start by defining an empty list that will keep taking values
    names = []
    #we use a for loop to loop through our list
    for list in ballots:
#our first_choice is just the first element in the list
        first_choice = list[0]
        names = names + [first_choice]
    return names 

    




# Part 1.2
def most_votes(votes):
    """Computes the names that appear the most number of times.

    >>> most_votes(['ghali', 'lina', 'yasmine', 'lina', 'med'])
    ['lina']
    >>> most_votes(['tima', 'yasmine', 'tima' , 'med'])
    ['tima']
    """
    # we define an empty variable that we will compare our count to
    max_votes = 0
    # we use an empty list that we will add to
    max_name = []
    #we use a for loop to go over every value in the list
    for name in votes:
        count  = count_appearances(name, votes)
        if count>max_votes:
            max_votes = count
            max_name = [name]
        elif count == max_votes:
            if name not in max_name :

                max_name = max_name + [name]
        
    return max_name




# Part 1.4
def candidates(ballots):
    """Computes the names of all candidates .

    >>> candidates([['ali', 'ghali'], ['liza'], ['liza', 'yas']])
    ['ali', 'ghali', 'liza', 'yas']
    >>> candidates([['lina', 'med'], ['yasmine', 'med'], ['tims', 'lina']])
    ['lina', 'med', 'yasmine', 'tims']
    """
    #we use an empty list that will take values 
    names =[]
    #we use a for loop to go over every value in the list
    for ballot in ballots:
        for person in ballot:
            #we use a conditional statement so that we make sure the names don't repeat
            if person not in names:
                names.append(person)
        
    return names
    




# Part 2.1
def least_votes(candidates, votes):
    """Computes the names of the candidates who appeared the least number of times.

    Put doctests here
    >>> least_votes(['med', 'tima', 'yas'], ['yas', 'tima','tima'])
    ['med']
    >>> least_votes(['ghali', 'hamza', 'yas', 'yas'], ['yas', 'ghali'])
    ['hamza']
    """
    #we use a variable that we will compare our count to
    least_votes= len(votes)
    #we use an empty list that will take the names of the candidates
    least_name = []
    #we use a for loop that will go over every element 
    for name in candidates:
        count  = count_appearances(name, votes)
        if count < least_votes:
            least_votes = count
            least_name = [name]
        elif count == least_votes:
            if name not in least_name :

                least_name = least_name + [name]
        
    return least_name

   


# Part 2.2
def majority(votes):
    """Computes the names of the candidate with the majority of votes

    >>> majority(['tima', 'tima', 'ali'])
    'tima'
    >>> majority(['lina', 'lina', 'tima', 'ali'])
    ''
    """
    #we use our function most_votes to shorten the process
    winner = most_votes(votes)
    # we use a conditional statement to check if there is only one candidate in our list
    if len(winner) == 1:
        #if so, we can use call our function to count how many times the person appeared in the list
        count = count_appearances(winner,votes)
        #if the count is higher than the length of the list over 2 then it is a mojority winner
        if count > len(votes)//2:
            return winner[0]
        #OTHERWISE, IT RETURNS AN EMPTY STRING
    return ''
       


# Part 2.3
def eliminate_candidates(candidates, ballots):
    """Computes the updated list of candidates after eliminating some candidate

    >>> eliminate_candidates(['sam'], [['sam', 'yas', 'med'], ['med', 'sam', 'yas']])
    [['yas', 'med'], ['med', 'yas']]
    >>> eliminate_candidates(['becky'], [['becky', 'sam', 'yas'], ['yas', 'becky', 'sam'], ['sam', 'becky', 'yas']])
    [['sam', 'yas'], ['yas', 'sam'], ['sam', 'yas']]
    """
    #we create an empty list which will be the final list
    updated_ballot =[]
    #we use a for loop to iterate over every element in our ballots 
    for list in ballots:
        #we add an empty list under our for loop to add the candidates that won't be eliminated
        updated_list =[]
        for person in list:
            #we use a conditional statement to ensure that the updated list won't take the elements in our candidates parameter
            if person not in candidates :
                updated_list = updated_list + [person]
        updated_ballot = updated_ballot + [updated_list]
    return updated_ballot

def run_doctests():
    """ This function allows us to run the doctests included in the functions 
    above when the file is run as a script
    """
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    # run the doctests included in the functions above when run as a script
    run_doctests()