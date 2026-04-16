#itech210-sp2026-final
1   ) create your virtual environment
1.1) in your terminal run the command: py -m venv env
1.2) activate your virtual environment with the command: env\Scripts\Activate
1.2.1) it is properly activated if you see (env) in your terminal before your path
1.3) add env/ and .env/ to your git ignore file

2) requirements txt
2.1)use the command: pip freeze > requirements.txt
2.1.1) this captures all of your imports and requirements and puts them in the requirements.txt file
2.2) use the command: pip install -r requirements.txt
2.2.1) this installs all of the requirements needed from the requirements.txt file

#Sites:
https://www.spritefusion.com
https://opengameart.org


#Checkpoint 1-4/2/2026
In the readme.md file I want you to write out the idea for your game level and how it is centered around Native Mythology.  I am looking for a 100 to 200 word description.

My game is based on Native Mythology as well as a local story from a nearby community where my mother grew up. The level will take place as an escape level from a witch who has taken you prisoner from trying to ice fish before spring has arrived.
This is based on the story of an old witch or shunned lady who practiced bad medicine and was sent to an island, the story goes she would take kids who wondered too far during winters over the ice. I want to make a game where you see a page that shows you trying to fish and being watched, then waking up in an empty hut, then the actual game is escaping from the island as night is ending while over the ice to make it back to shore to your family who is looking for you. In this game I will make the witch who will send little goombas aka a wendigo type creature that comes at you, for coins I will make a feather the points that help you and fish that restore life (not sure if this will work but will try to make it work). Should the player fail the levels or die during the run, it will give you a end of game. The player should have 6 hearts and no more. The level will have ice pockets that the player must jump over and for items to jump on the player will jumpt on to branches from trees that have fell in the water which might block the pathway from avoiding it so you have to jump. I want to make a timer of 5 minutes to get back to shore. The player will go against the wendigo creatures but in the final section (last 25 seconds) before the shore, they have to outrun the witch who is faster than goombas(again not sure if this will work but will try to make it work). The game will end when the player gets to shore and reunites with their family as the sun is coming up. You will get a score and game over happy ending scene. 

#Checkpoint 2-4/9/2026
For this check point you will need to have developed a test level using primitive blocks and implement player movement.  The level doesn't have to be big, complex, or in any way resemble your final level design.  This is more about creating a space to get player movement correct and feeling good.  Player should be able to move left and right and jump.  These should all feel smooth.  currently there is no momentum or friction with the provided base movement, and the player can freely move in the air.  You may or may not want to change that.
There will be no hand in for this assignment.  I will use your repo and the commit history

Rubric:

10 points - player movement is implemented, there is a temporary level, and the game is playable
0 points - anything else

#Checkpoint 3-4/16/2026
By now you have player movement and basic collisions implements.  This week you are going to make the official level for your game.  Use the sprite map creator we have used in class to create your map and implement it in your game.

Tips:

set your tilesize to 32 or 16.
You may need to open your sprite sheet in paint and scale it to a multiple of 32 or 16
The game in python is based on 32x32 pixel tile size.  Make your map width and height an even multiple of that to make things easier
your map MUST be bigger than the game view.  
it will take a few tries to get one you like.  
test it in the game before you turn it in.  jump gaps or alignments might be a bit off if you don't test first
be careful with diagonal movement.  We haven't covered it specifically in class
Once you map, make sure to implement it into the game, make sure it moves with your character appropriately, and make sure you add the colliders for the ground and obstacles correctly.  I should be able to explore the whole map in game.

There is no turn in for this, I will use your commit history.

Rubric:

10 points - Level is implemented, it is bigger than a single screen, has the camera properly implemented, and colliders properly implemented.
0 points - anything else

#Checkpoint 4-4/30/2026
Now that we have a playable level, it is time to add in ways to score points, beat the level, and ways to die.

For this checkpoint you will add in coins or something analogous so the player can collect points.  You will also implement enemies.  No need to go wild here.  1 or 2 enemies will suffice.  The player should properly interact with them; gain points when collecting coins, kill enemy if jumping on them, die if enemy touches player, etc...

Note:  this may feel easy but don't forget you will also need to create behavior for the enemies.  do them follow the player? do they just move left?  do they bounce up and down?  This will take a bit of thought and research to implement.

There will be no hand in for this checkpoint.  I will use your commit history.

Rubric:

10 points - player can interact with coins*, enemies, and beat the level
0 points - anything else

