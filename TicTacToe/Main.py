'''Lets make a game of tic-tac-toe!'''
#Will need the tkinter GUI design tools
from tkinter import *
#And the random functions
import random

'''
For this project we will need some functions to handle the
different aspects of the game loop(hint hint)
'''
'''next_turn will handle  keeping an eye on wether a winner has been found yet, or not'''
def next_turn(row, column): #Define a new function called next_turn which accepts 2 arguments, row and column
    global player   #Fetch the global variable called player, to use in this function

    #if the buttons on row and column text are all blank, and check_winner function
    #returns false, proceed with the following:
    if buttons[row][column]['text'] == "" and check_winner() is False:
        #if player(active player) is currently players[0] (player 1), then:
        if player == players[0]:
            #fill in the buttons text with the players symbol
            buttons[row][column]['text'] = player

            #now we check if there is a winner with the check_winner function
            #if no winner is found, then proceed.
            if check_winner() is False:
                #set the active, player to player 2
                player = players[1]
                #change the label to inform its the next players turn.
                turn_label.config(text=(players[1]+" turn"))
            #otherwise, if check_winner returns True, then
            elif check_winner() is True:
                #change the label to inform the player won!
                turn_label.config(text=(players[0]+" WINS!"))
            #otherwise, if check_winner returns with "Tie"
            elif check_winner() == "Tie":
                #change the label to inform as such.
                turn_label.config(text=("Its a tie! :O"))
        #Once player 1s turn has been processed, we move on to player 2
        else:
            #Fill in the chosen button with player 2s symbol and:
            buttons[row][column]['text'] = player
            #if check_winner returns false then:
            if check_winner() is False:
                #switch active player back to player 1
                player = players[0]
                #and inform of this.
                turn_label.config(text=(players[0]+" turn.."))
            #otherwise, if check_winner returns True
            elif check_winner() is True:
                #inform the players who won!
                turn_label.config(text=(players[1]+" WINS!"))
            #otherwise, if check_winner returns "Tie"
            elif check_winner() == "Tie":
                #inform the players of such
                turn_label.config(text=("Its a tie :O"))

'''Check winner is in charge of, checking if someone won!(wow!)'''
def check_winner():#Define new function called_check_winner
    '''
    In order to check for a winner we have to go through all possible
    win conditions in a game of tic tac toe
    that is to say, any possible way a player can get 3 in a line.
    [x][x][x]|[x][ ][ ]|[x][ ][ ]|
    [ ][ ][ ]|[x][ ][ ]|[ ][x][ ]|  ETC ETC ETC
    [ ][ ][ ]|[x][ ][ ]|[ ][ ][x]|
    We will do this using for loops to check all 3 rows
    all 3 columns, and both diagonal possible win conditions
    if they have matching symbols
    '''

    #First, we check the rows
    for row in range(3): #for the row variable in the range of 3
        #if the buttons on row 1, 2 or 3 match in symbols, and is NOT blank
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            #And heres a tiny buttons, turn the given row with matching symbols, buttons, all green!
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            #Then someone has won, and return as True
            return True
    #Repeat this process for the columns, litteraly a copy paste job.
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    #if there is neither a matching row or column, check the diagonals!
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] !="":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] !="":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    #If there are STILL no matching lines of 3, then check if there are
    #any empty spaces left with empty_spaces function
    #If this returns false, then its a tie!
    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")

        return "Tie"
    #Otherwise if nothing else, there is no winner(yet) and the game continues.
    else:
        return False

'''This function below will be in charge of checking
the grid for empty spaces.'''
def empty_spaces():     #Define function called empty_spaces
    spaces = 9          #Set up a local variable that will handle the amount of spaces avaible, set it to 9(fields)
    for row in range(3):    #This will check the buttons in each row(range 3)
        for column in range(3): #This will check the buttons in each column (range 3)
            if buttons[row][column]['text'] != "": #Check the text, and see if it is NOT equal to an empty space
                spaces -=1 #If this is the case, set spaces -=1
    if spaces == 0: #If spaces = 0, we will return false, and
        return False#there are no spaces left.
    else: #Otherwise
        return True #return true, then it is a tie.

'''
This function will handle the ability to start a new game
'''
def new_game():
    global player   #First we will grab the global variable player

    player = random.choice(players) #set player to a new random choice (between x or o

    turn_label.config(text=player+" turn")  #Change the label to tell which players turn it is

    #This part will check all rows and columns, and clear them of text.
    for row in range(3):    #Check all 3 rows
        for column in range(3): #check all 3 columns
            buttons[row][column].config(text="",bg="#F0F0F0") #set their text to blank, and color to F0F0F0

'''Below is the main block of code that handles the game window.'''
window = Tk()               #Create a new window called window, using Tk
window.title("Tic-Tac-Toe") #Set the title of the window
players = ["x","o"]         #Set up a variable called players, with two values, x and o
player = random.choice(players)    #Set up a variable
buttons = [[0,0,0],                #set up buttons as 3 2d lists, that all holds a value of 0
           [0,0,0],                #This will be our play-space as illustrated
           [0,0,0]]

#create a label called turn_label, the text wil lstart out as player(value) +" turn"
turn_label = Label(text=player + " turn", font=('consolas', 40))
#place the label to the top of the window
turn_label.pack(side="top")

#create a button called reset_button, when pressed, command new_game will be executed
reset_button = Button(text = "restart", font=('consolas',20),command=new_game)
reset_button.pack(side="top")

'''Now to create a new frame, this frame
will hold the play-board, the 9 buttons that make up the game'''
frame = Frame(window)   #Create a frame called frame, attatch to window
frame.pack()            #pack the frame to the window

for row in range(3):    #check the rows in range of 3
    for column in range(3): #check columns in range of 3
        buttons[row][column] = Button(frame,    #for these rows/columns, create buttons for each index, attach to frame
                                      text="",  #set their text to be blank
                                      font=('consolas',40), #just font
                                      width=5,  #set width ...
                                      height=2, #... and height, to make them uniform
                                      #When pressed, execute a lambda function that updates each buttons state, and iniates the next_turn function
                                      command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row, #Place all the new buttons in a grid
                                  column=column) #in accordance to their position in row/column

window.mainloop()   #FINALLY, show the window!