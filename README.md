# 7 Days to Die - ScottyBot Integration (Python)
## YOU MUST INSTALL PYTHON 3.3 or ABOVE

_This was created to give streamers a little more control than using the Beam Interactive. With Beam Interactive you are using Sparks to interact with the streamer. If something goes wrong the streamer has no way of refunding Sparks. Sparks are only gained by watching streams and takes a while to get a decent amount. Most streamers dont want to be trolled so bad that they cant enjoy the game and will set their interactions at a high spark cost. This will disscourage the viewer from interacting. With ScottyBot integration the streamer has full control over the costs and viewers can earn points easier and in more ways than they can with Sparks._

### CAVEATS
    NOTE: YOU MUST HAVE A DEDICATED SERVER WITH TELNET ENABLED, THIS WILL NOT CONNECT TO GAME CLIENT!
        
        you should have a serverconfig.xml file with the following lines:
        <property name="TelnetPassword" value="<TELNET_PASSWORD>"/>
        <property name="TelnetPort" value="<TELNET_PORT>"/>
        <property name="TelnetEnabled" value="true"/>

_These instructions have been tested and work on Windows/Linux/mac_

1. Download and install Python 3.3 or above
   * Follow instructions at - https://www.python.org/downloads/

2. Download our files _(telnet.py, scottyint.py & items.py)_
  * Download the files and folders _(will download 7d2d-beam-interactive-python.zip)_
  * Unzip the files into an easy to remember location _(will create a folder called 7d2d-beam-interactive-python)_
  * Open the newly unzipped folder and copy telnet.py & interactive.py
  * Paste our files in the folder created in step 2 _(beam-interactive-python-master - you can change the folder name)_

3. Open the scottyint.py script _(open with text editor of your choosing)_
   * Change the info on line's 14 & 18 - 21
   * Save the changes

4. Open cmd(windows) or terminal(linux/unix)
   * cd to the directory where you unziped the files in step 2.
   * Run the scottyint script
      * py -3 scottyint.py _(windows)_
      * python3 scottyint.py _(linux/unix)_

_If you get module errors when trying to run_

5. Open cmd(windows) or terminal(linux/unix)
   * Install module modules you are missing
         * pip3 install <module> _(window/linux/unix)_ _If if it warns about pip being outdated update it_
         * **MODULES USED**
            * websocket
            * _thread
            * time
            * sys
            * json
            * os
            * random
            * telnetlib
            * re
	

## You have to add the following commands and costs to Scotty Bot. _(costs are up to you)_
_Below are the commands that are in the scottyint.py file. You can name your commands whatever you want in Scotty Bot, but you will have to manually change them to match in the scottyint.py file._

## _Helpful Items_

1. !item
    * Spawns a RANDOM item from every spawanable item in the game

2. !health
    * Spawns a RANDOM Health item
    
3. !food
    * Spawns a RANDOM food item

4. !animal
    * Spawns a RANDOM animal _(except bears)_

5. !quest
	* Spawns a RANDOM quest
	
6. !airdrop
    * Spawns an airdrop

7. !weapon
    * Spawns a RANDOM weapon _(ammunition also included)_

8. !explosives
	* Spawns a RANDOM explosive item

9. !clothes
	* Spawns a RANDOM piece of clothing
	
10. !tool
	* Spawns a RANDOM tool

## _Harmful Items_

1. !enemy 
    * Spawns a RANDOM zombie _(including hornets, dogs, bears, and zombie bears)_

2. !feral
    * Spawns a feral
    
3. !screamer
	* Spawns a screamer
	
4. !horde
	* Spawns a wandering horde

### MORE TO COME....

## _Helpful or Harmful_

1. !buff
	* Still decideing how these will work
	* 
2. !debuff
	* Still decideing how these will work


