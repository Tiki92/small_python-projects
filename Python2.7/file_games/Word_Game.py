
import operator

##Create the best word to score the moast points


def sort_dict(d, reverse=True):
    return sorted(d.iteritems(), reverse=reverse, \
                    key=operator.itemgetter(1))


def rank_words_from_File(f):
    """
        Takes in a file, then ranks all the words within the file
        
        Args: a file
        
        Return: A Dictionary of all the words as the Key 
                and the ranking as the value
    """
    word_dict = {}
    words = []
    for line in f:
        list_of_words = line.split()
        for w in list_of_words:
            words.append(w.lower())

    for word in words:
        if word_dict.has_key(word):
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    
    return word_dict


def main():
    # Title
    print 'The Word Game'
    print '='*30
    print ""
    
    # Game Setup
    f = open('alice.txt', 'rU')
    print 'Loading Words....'
    orig_ranked_words_dict = rank_words_from_File(f)
    f.close()
    
    print 'Loading Complete!!!'
    print 'Game Starting...'
    print ""

    #Game Loops
    while True: # loop for each Game
        # Determine what the round limit is
        while True:
            try:
                round_limit = int(raw_input('Choose Game Length, how many Rounds? [enter a number larger than 0]: '))

                if int(round_limit) <= 0:
                    print 'Answer must be more than 0, Please try again!'
                    print ""
                else:
                    break
            except:
                print 'An Error Occured, make sure you enter an Integer.'
                print ""
                
        # Setup initial Variables
        points = [0,0]
        cur_player = 1
        cur_word = ""
        cur_round = 1
        round_over = False
        
        # Important  Create a copy of the Dictionary
        ranked_words_dict = orig_ranked_words_dict.copy()

        while True: # loop for each Round
            print 'Round', cur_round
            print 'Player 1: %d    Player 2: %d' % (points[0],points[1])
            print ""
            print ""

            while True: # loop for each word

                if len(cur_word) > 0:
                    print ""
                    print ""
                    print (" "*5)+'Current String =  "%s"' % cur_word
                    print ""
                
                # Get the new letter
                new_letter = str(raw_input('Player %d, Please enter a letter: ' % cur_player))
                if len(new_letter) > 1:
                    new_letter = new_letter[0]
                # Add it to the current Word
                cur_word = str(cur_word)+str(new_letter).lower()
            
                # Check if word in Ranked Word Dict
                potential_word = False
                for key, value in ranked_words_dict.items():
                    #found = re.match(str(cur_word), str(key))
                    #if found:    #  alice
                    if len(cur_word) <= len(key) and str(cur_word) == str(key[:len(cur_word)]):
                        potential_word = True
                    if str(cur_word) == str(key) and len(cur_word)>3:
                        round_over = True
                        round_points = value
                        del ranked_words_dict[key]

                # Check if the cur_word is not valid using the variable potential_word
                if potential_word == False:
                    round_over = True
                    round_points = int(5)

                    print ""
                    print ""
                    print '%s - will not make valid word, Player %d lost that Round!!' % \
                                (cur_word,cur_player)
                    

                # Check if round_over is True
                if round_over:
                    # Statement to determine list position of winning player
                    if cur_player == 2:
                        p = 0
                        winning_player = 1
                    else:
                        p = 1
                        winning_player = 2
                        

                    # Assign points to winning player
                    points[p] += round_points
                    
                    print ""
                    print "!#YAH#!"*10
                    print ""
                    
                    print (" "*15)+'Winning Word = "%s"' % cur_word
                    print (" "*4)+'Player %d just won that Round!!! (%d points)' % \
                                (winning_player,round_points)
                    
                    print ""
                    print "!#YAH#!"*10
                    print ""
                    
                    cur_word = ""
                    # Exit Round
                    
                    break

                else:
                    # Change the player
                    if cur_player == 1:
                        cur_player = 2
                    else:
                        cur_player = 1


            # Back inside of the Rounds Loop
            if cur_round == round_limit:
                print ""
                print 'Round Limit Reached'
                print ""
                print 'Player 1: %d    Player 2: %d' % (points[0],points[1])
                print ""
                print ""
                if points[0] > points[1]:
                    print 'Player 1 WINS !!!!'
                elif points[0] < points[1]:
                    print 'Player 2 WINS !!!!'
                else:
                    print "It's a TIE !!!!"
                print ""
                
                break
                
            else:
                round_over = False
                cur_round += 1
                
        # Back in the Game Loop
        user_input = str(raw_input('Type "q" to quit or "<any key>" to play again: '))
        if user_input.lower() == 'q':
            break


    # The Game has been exited
    print ""
    print ""
    print 'Thank You for Playing!!!'



if __name__ == '__main__':
    main()

