"""
Firstname: LAVANYA
Lastname: SASIKALA
Username: lsasikala
StudentID: 156621211
Email: lsasikala@senecacollege.ca
"""

import sys
from random import randint

# 1 Marks
def rolldice():
    """
    function: rolldice prints two random numbers between 1 and 6 simulate two dices rolling. 
    The function should also print output of the numbers generated (Eg: 6 and 6) 
    return: int:total (total of two random numbers) 
    """
    trial1 =randint(1,6)            #Random number generation representing first roll dice
    trial2 =randint(1,6)            #Random number generation representing first roll dice
    print(str(trial1) + " and " + str(trial2))      #Printing the result of roll dice
    total = trial1 + trial2             #Adding the random numbers to reresent the score 
    return total                #Returning total, result of each round for each player.



# 1 Marks 
def getplayers(): 
    """
    function:This functions asks user to provide an input of number of players. 
    Based on the number of players asks player names and create a list of player names and return player names
    If user entered invalid input for number of players (eg: string (a)) it throws an error and asks to retry 
    :return list:players (list of playernames entered by user)
    """
    players =  []               # Players list Initialization
    isCorrect = True
    while isCorrect:            #while loop for getting the number of players
        playerCount = input("Please enter the number of players: ")     #Prompt user for player number input
        if playerCount.isnumeric() and int(playerCount) > 1:            #Checking whether the input is valid
            count = int(playerCount)
            isCorrect = False
        else:
            print("Invalid input please try again")
    i = 1
    #while True:
        #if playerCount.isnumeric() and int(playerCount) > 1:
    while count != 0:                                           #while loop for getting the player names.
        playerName = input (f"Please enter player #{i} name: ")
        players.append(playerName)                              #player name added to the player list.
        count= count-1
        i=i+1
           # else:
                #print("Invalid input please try again")
                #break

    #print ("Players are:", players)
    return players                          #The function returns the list of players.

# 1 Marks 
def getrounds(): 
    """
    function: This function asks user to enter the number of rounds they going to play 
    Based on the number of rounds entered as long it is valid return the number of rounds otherwise keep asking until a valid number entered. 
    :return int:roundcount (number of rounds)
    """
    # Implement your function here
    isCorrect =True
    while isCorrect:
        roundcount = input ("Please enter how many rounds the players wish to play: ")   #Prompting user for the number of rounds to play
        if roundcount.isdigit() and int(roundcount) >0:             #Checking for the validity of input data
            isCorrect =False
                
                
        else:
            print ("Invalid input please try again")
                
    #print ("Roundcount=" + roundcount)            
    return int(roundcount)                      #Returning the number of rounds.
        

# 4 Marks 
def setgame():
    """
    function: This functions use the getplayers() function and getrounds() function to get player list and round count
    Using the above values setup a two dimensional (2D) list called game. The game list will have lists elements for each round and player 
    Eg: [[score1_1, score1_2, score1_3], [score2_1, score2_2, score2_3], [score3_1, score3_2, score3_3]]
    In this above example score1_1 is player1's score for round 1. Score3_1 is player 3's score for round 1. Score 2_3 is player 2's score for round3 
    Hence each list element in game will represent a player
    Each score (int) element in the nested list element will represent a round for that player
    Finally return a gameset list which has the game list, players list, and number of rounds
    return: list:gameset (Eg gameset returned will be a list [game, players, roundcount]. In the gameset list game is lit, players is list and roundcount is integer)
    """ 
    players = getplayers() # Calling getplayers and getting player list 
    roundcount = getrounds() # Calling getrounds and getting roundcount 
    # Implement your function here 
    gameset = []            #Initializing gameset list to null. 
    game = []               #Initializing game list to null.
    for player in range(len(players)):      #For each player , and for each round, the initial values of game list is set to 0. 
        roundscore =[]                      #initializing a list called roundscore for representing the scores of each player .
        for j in range (roundcount):
            roundscore.append(0)              #roundscore list is set to 0
        game.append(roundscore)                #game list is set to 0.
    gameset = [game,players,roundcount]         #gameset list is set with list elements game list, player list and no:of rounds.
    #print ("game is",game)
    #print("gameset is", gameset)
    return gameset                      #Returning gameset list.



# 1 Marks 
def asktoroll(player): 
    """
    function: This function takes player name and asks player to hit enter to roll the dice. 
    When user hit enter calls the rolldice function and returns a score 
    :param string:player (player input is string called player name)
    :return int:score (Returns score from roll dice)
    """
    # Implement your function here 
    #for player in range players:
    iscorrect = True
    while iscorrect:
        user_input = input(f"{player}! Hit enter once you are ready to roll your dices!")   #Prompting user to press enter key to start roll dice
        if user_input =="":   #Checking the validity of the input
            iscorrect = False
            roundscore =rolldice()   #Calling rolldice function
        else:
            print("Invalid input.Try again)")
    #print("Roundscore=" + str(roundscore))
    return roundscore
        

# 2 Marks 
def findwinner(game, players):
    """
    function: This function takes game list (2D list) and the player list as input parameters. Goes through the game and find the player that has the highest score
    Return the winning player name as string. If more than one player winning (eg: same score) return a winner string with all players comma seperated (Eg: John, Kate)
    :param list:game (Game list)
    :param list:players (Players list)
    :return string:winner (Winning players name as string)
    """ 
    # Implement your function here 
    winnerscore = 0
   
    sumlist =[]                 #A list to store the total score of all rounds of each player.
    for player in range (len(players)):
        sum = 0
        for i in range (len(game[0])):
            sum += game[player][i]        #Calculating sum of scores of all rounds of each player
        sumlist.append(sum)                #Updating sumlist 
        #print("Total of"+ players[player]+"is: "+ str(sum))
    #print ("sumlist is", sumlist)
    winnerscore =max(sumlist)         #Finding the max value in the sumlist
    #print("Winnerscore ="+ str(winnerscore))
    for i in range (len(sumlist)):        #Finding the position of the max value in sumlist
        if sumlist[i]==max(sumlist):
             print("Congratulations " +players[i] + "! You are our Winner!")   #The position of max value in sum list is the position of the player who scored max in playerlist


# 5 Marks 
def rungame():
    """
    function: This function runs the game 
    It sets the game first using setgame() function. It gets the game, players and roundcount from setgame
    It prints the header and Round 1 begining score card first with inital scores set to 0
    It then asks use to roll dices using asktoroll function for all rounds and players 
    When the game finish it prompts for continuation and if chose to continue run the game again otherwise terminate.
    """

    # The next 5 lines are to get you started 
    # Implement the rest of the code 
    gameset = setgame() # Calling the setgame to get game info 
    game = gameset[0] # Getting game list 
    players = gameset[1] # Getting playerlist 
    roundcount = gameset[2] # Getting roundcount 
    #print("*" * 20)
    #print("Round1")
    #print(f"{'*'*20} Round 1 {'*' *20}")
    printgame(game, players, 0, roundcount) # Calling printgame to print the first score card. 
    for i in range(roundcount):
        roundnum= i+1
        #print("Iteration for round is" +str(i))
        for player in range (len(players)):
            #print("Iteration for player is" +str(player))
            #print ("player is" +players[player])
            roundscore =  asktoroll(players[player])              #Calling asktoroll() for rolling the dice, the sum of random numbers is storedin roundscore
           # game=game.append(roundscore)
            game[player][i]=roundscore                          #Updating game list
        printgame(game, players, roundnum, roundcount)          #Calling print function to print the 2D tble.
    findwinner(game,players)                                    #Calling the findwinner() for declaring the winner.
    #print("rungame output: ",game )
    # 
    print("Would you like to play another game?")               #Prompting user whether to start new game.
    print("[1] Yes")
    print("[2] No")
    #user_input = input("Your choice:")
    #print("userinput is:" +user_input)
    iscorrect = True
    while iscorrect:
        user_input = input("Your choice:")         #If user ioption is 1 , rungame() is again called and the process continues
        if (int(user_input) ==1):
            iscorrect = False
            rungame()
        elif (int(user_input)==2):              #If no, then exit from th eprogram
            iscorrect = False
            break
        else:
            print("Invalid option. Try again")


# 5 Marks
def printgame(game, players, roundnum, roundcount): 
    """
    This function takes in game list, players list, round number (aka which round is active), totalround count as input parameters
    The function prints left aligned pretty table of the game with Rounds in columns and players in rows 
    Sample Output:
    ****************** End of Round 3 ******************
            Round 1   Round 2   Round 3   Total     
    Appla     8         7         4         19        
    Applb     11        5         8         24        
    Applc     9         3         5         17        
    Appld     8         8         7         23        
    ****************************************************
    The Stars and the Round title (End of Round) are calculated and aligned as number of rounds changes. 
    This function does not return anything
    """
    total = 0
    #rowstring = ""      
    header = " "* 15
    if(roundnum==0):
        print(f"{'*'*20} Round1 {'*'*20}")         
    else:
        print(f"{'*' * 20} End of Round {roundnum} {'*' *20}")
    for i in range (roundcount):
        #header +=f"Round" + str(i+1) + "" *25
        header += f"Round {i+1:<15}"                  #Printing Round1  round2 etc headers
    header += "Total" + "" *5                          #Printing total header
    print (header)
    for player in range (len(players)):
        rowstring = ""                              # A string to store the scores of one round of each player.
        total = 0
        for i in range(roundcount):
           # print("player value is"+str(player))
           # print("roundcount value is"+str(i))
            #rowstring = ""
            score = game[player][i]
            total +=score
            score =f"{score:<20}"
            #print("score =:"+ str(score))
            #total +=score
            #rowstring.append(score)
            rowstring+=str(score)
           # print("Rowstring is:" +rowstring)
        #rowstring+= str(total)
        print(f"{players[player]:<10}  {rowstring} {str(total):<20}")   #Printing the scores of each player in each round along with total
    print(f"{'*'*75}")
    
    #for i in range (roundcount+1):    
        
    #print(rowstring,total)




def game():
    """
    function: Game function to run game 
    """
    rungame() # calling run game 

if __name__ == "__main__":
    """
    Main code block to run the code
    """
    game() # calling game in main block