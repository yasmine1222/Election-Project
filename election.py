# Implements different voting rules

# import functions from voting module
from data import *
from voting import *

# Part 1.3
def plurality(ballots):
    """
    Takes as input ballot data as a list of lists of strings, and
    returns a list of strings of names of candidates who get the most votes.

    >>> from data import *
    >>> plurality(aamir_beth_chris_ballots())
    ['Aamir']
    >>> plurality(ava_bob_cid_ballots())
    ['Ava']
    >>> plurality(character_ballots())
    ['Scarlett OHara', 'Samwise Gamgee']
    """
    #we use our helper function to find the voters' first choices
    thefirsts = first_choice_votes(ballots)
    #we use our other helper function to get the candidates who got the most votes
    winner = most_votes(thefirsts)
    return winner
    


# Part 1.5
#  Note: You may wish to add a borda_score helper function here...
def borda_score(candidate, ballots):
    """ Computes the borda score of a candidate.

    >>> from data import *
    >>> borda_score('Ava', ava_bob_cid_ballots())
    37
    >>> borda_score('Bob', ava_bob_cid_ballots())
    42
    >>> borda_score('Cid', ava_bob_cid_ballots())
    47
    """ 
    #we start with an empty variable that will take more values
    count = 0
    #we use a for loop to go over our list
    for list in ballots:
        score = len(list)-first_appearance(candidate, list)
        count = count + score
    return count






    
def borda(ballots):
    """
    Takes as input ballot data as list of lists of strings, and
    returns a list of strings of the names of candidates with the
    maximum borda score.

    >>> from data import *
    >>> borda(aamir_beth_chris_ballots())
    ['Aamir']
    >>> borda(ava_bob_cid_ballots())
    ['Cid']
    >>> borda(character_ballots())
    ['Harry Potter']
    """
    #we start with an empty variable that will take more values later
    max_count = 0 
    #we start with an empty list that will take more names of people with the max borda score
    max_name = []
    people = candidates(ballots)
    for candidate in people:
            #we use our helper function to get the count of everyone's score
            count = borda_score(candidate, ballots)
            if count> max_count:
                max_count= count
                max_name = [candidate]
                #we use an elif statement to make sure the names don't repeat
            elif count == max_count:
                if candidate not in max_name:

                    max_name = max_name + [candidate]
    return max_name
    
            
   


# Part 2.4
def ranked_choice(ballots):
    """Takes as input ballot data as list of lists of strings, and
    returns the winner of the election based on ranked-choice
    voting as a list of strings of names.

    >>> from data import *
    >>> ranked_choice(aamir_beth_chris_ballots())
    ['Aamir']
    >>> ranked_choice(ava_bob_cid_ballots())
    ['Bob']
    >>> ranked_choice(character_ballots())
    ['Scarlett OHara']
    >>> ranked_choice([['Abe', 'Betsy', 'Carmen'], ['Betsy', 'Abe', 'Carmen'], ['Carmen', 'Abe', 'Betsy']])
    ['Abe', 'Betsy', 'Carmen']
    >>> ranked_choice([['Sierra', 'Tao', 'Una'], ['Sierra', 'Tao', 'Una'], ['Tao', 'Sierra', 'Una'], ['Tao', 'Sierra', 'Una']])
    ['Sierra', 'Tao']
    """
    while True:
        #we call our funct first_choice_votes 
        first_choice_votes_candidates = first_choice_votes(ballots)
        # we use majority to check if there is a majority winner
        winner = majority(first_choice_votes_candidates)
        #we use a conditional statement to make sure the output of majority is not an empty string and that there is actually a majority winner
        if winner != "":
            return winner
        #we call the function candidates to list the candiditaes in our ballots
        my_candidates = candidates(ballots)
        #we check if the length of the ballots is equal to the length of the first_choice_votes list
        if len(my_candidates) == len(least_votes(my_candidates, first_choice_votes_candidates)):
            candidates_in_tie= candidates(ballots)
            return candidates_in_tie
        #otherwise we eliminate the candidates with the least first choice votes
        least_first_choice_votes_candidates = least_votes(candidates_in_tie ,ballots)
        final_list = eliminate_candidates(least_first_choice_votes_candidates, ballots)
        #we update our original ballot
        ballots = final_list
    

    

# Part 2.5
def condorcet(ballots):
    """OPTIONAL (JUST FOR FUN): Takes as input ballot data as list of 
    lists of strings, and returns the winner of the election 
    as a string (or empty string if there is no winner).  
    """
    # replace this with your code!

def run_doctests():
    """ This function allows us to run the doctests included in the functions 
    above when the file is run as a script
    """
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    # run the doctests included in the functions above when run as a script
    run_doctests()

    #Read in our ice cream ballots and run our election algorithms for Part 1.
    print('Ice-cream flavor class election results:')
    class_ballots = ice_cream_ballots()
    print('Plurality winner:     ' + str(plurality(class_ballots)))
    print('Borda winner:         ' + str(borda(class_ballots)))

   # Read in our ice cream ballots and run our election algorithms for Part 2.
    print('Ranked-choice winner: ' + str(ranked_choice(class_ballots)))

    #Eliminate the winning flavor and try the algorithms again (after completing Part 2).
    winning_flavor = plurality(class_ballots)[0]
    new_ballots = eliminate_candidates([winning_flavor], class_ballots)
    print()
    print('Updated ice cream flavor election results:')
    print('Plurality winner:     ' + str(plurality(new_ballots)))
    print('Borda winner:         ' + str(borda(new_ballots)))
    print('Ranked-choice winner: ' + str(ranked_choice(new_ballots)))

    # Uncomment the following line if you complete the extra credit.
    #print('Condorcet winner:     ' + str(condorcet(class_ballots)))
