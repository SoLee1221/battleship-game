<h1>Unreal Battleships game</h1>  

Unreal Battleships game is a python coded game, which runs on Heroku  

Players can try to sink all battleships of the computer before the computer sinks theirs.  
Each battle ships takes one square on the board and there is a total of 3 battleships for the player and computer.  

<h3>How to play</h3>  

Unreal battleships is a classic pen and paper game.  
More information can be found on this website about battleships game https://en.wikipedia.org/wiki/Battleship.  
In Unreal battleships you are presented with rules and welcome message.  
Each player (computer and player) have 3 ships each and the opponent has to sink them all in order to win.  
There are indications showing if a player or computer has taken their turn by showing symbols such as "x"  
hit an empty slot but missed. The second indication is "*" which is if a player or computer has hit a ship.  
The last two indications are *@* for ships and "." for empty spaces.
The player will take turns with the computer having guesses on sinking each others ships.  

<h3>Features</h3>  

• Randomises ships for both computer and player.  
• Doesn't allow user to input numbers that are bigger or smaller than the actual board.  
• Doesn't allow user to input strings when numbers are only needed for playing the game.  
• When users have already guessed a spot that they have already shot, it outputs a message indicating the user they have already guessed that.  
• Shows a message when player and computer miss each time they shoot.  
• Shows message each time player or computer have sunk the other persons ship.  
• At the begining it allows player to randomise their ships until they are happy with the positions.  
• Once game is over if player or computer sinks all ships, it allows player to play again.

<h3>Future features</h3>  

• Allows players to insert names.  
• Allows more than 1 player to play instead of vs computer.  
• Allow players to put ships where they like.  
• Increase the amount of ships.  
• Limited amount of rounds.  

<h3>Data model</h3>  

I created a simple board for both player and computer with a fixed size for both computer and player.  
whole_board stores how big the board should be for both computer and player, it also stores in the sybols for ships and hidden ships for the computer (player_board) (ai_board).  
guess_col and guess_row is where the inputs are taken in by user and computer to show where they are trying to shoot.

<h3>Testing</h3>

• I have tested for player board to print.  
• I have tested for computer board to print with player board.  
• I have tested for user input to only be integers.  
• I have tested for user not able to input string.
• I have tested for user not able to put numbers bigger or smaller than the actual board.  
• I have tested for sybols such as "@" "*" "X" "." to show for both computer and player.  
• I have tested for computer's ships to be hidden from player to prevent cheating.  
• I have tested for the print statements for row and col print correctly.  
• I have tested for number of rounds are on going to until the game ends.  
• I have tested for when a player or computer hits a ship it prints the correct statement.  
• I have tested for when a player or computer misses it prints the correct statement.  
• I have tested for when player has input invald data it prints the correct statement.  
• I have tested for when game is over player is able to play again.  
• I have tested for before the game starts the player is able to reset its ships position if wanted.  
• I have tested for when player wants to change ship position before game starts it loops so player can keep changing position of ships until they are satisfied with the output they have.  
• I have tested for when computer shoots a spot it doesn't crash the system.  
• I have tested for when player has already shot a spot it's still their turn until a valid input is given.  

<h3>Bugs</h3>

• Heroku deployment isn't showing the promp until 1 or 2 inputs, i have tested this on locally with no problems and on other interpreters.

<h3>Validator testing</h3>

• PEP8  
• No errors was found from pep8online.com  

<h3>Deployment</h3>

• Steps for deployment.  
• open heroku by going on dashboard.heroku.com  
• After opening Heroku
• On the right side click "New" with arrow point up and down beside it  
• After clicking "New" click "create new app"  
• Once you have clicked "create new app" you then fill in the relevant data to you  
• Once that is done first go to the "settings" tab and click on "settings" scroll down until you see a part that says add builpack.  
• You want to first select "Python" then click "save changes"  
• After you selected python go back to add buildpack and select "nodejs" then click "save changes".  
• It's important that "python" is showing on top "nodejs" you can click and drag to change order.  
• Next you can scroll up and go to the "deploy" section.  
• The deployment method you want to select is "Github" and confirm that you want to connect to "Github".  
• Go to search for repository to connect to and search for your repository with the correct file name you saved it to and click connect.  
• Once that is done you scroll down and click on "Enable automatic deploys" and then after that click on deploy branch.  

<h3>Credits</h3>

• Wikipedia for more details about battleships game.  
• Inspiration from code institute battleship readme.  









