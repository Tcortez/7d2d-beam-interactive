# 7 Days to Die - Beam Interactive (Python)
## YOU MUST INSTALL PYTHON 3.3 or ABOVE

_These instructions have been tested and work on Windows/Linux/mac_

1. Download and install Python 3.3 or above
   * Follow instructions at - https://www.python.org/downloads/

2. Go to - https://github.com/WatchBeam/beam-interactive-python
    * Download the files and folders _(will download beam-interactive-python-master.zip)_
    * Unzip the files into an easy to remember location _(will create a folder called beam-interactive-python-master)_

3. Download our files _(telnet.py & interactive.py)_
  * Download the files and folders _(will download 7d2d-beam-interactive-python.zip)_
  * Unzip the files into an easy to remember location _(will create a folder called 7d2d-beam-interactive-python)_
  * Open the newly unzipped folder and copy telnet.py & interactive.py
  * Paste our files in the folder created in step 2 _(beam-interactive-python-master - you can change the folder name)_

4. Open cmd(windows) or terminal(linux/unix)
   * cd to the directory where you unziped the files in step 2.
    * Run setup.py script _(from the files you just downloaded)_
        * py -3 setup.py install _(windows)_
        * python3 setup.py install _(linux/unix)_
    * Install requests module
         * pip3 install requests _(window/linux/unix)_
            * _If if it warns about pip being outdated update it_

5. Open the interactive.py script _(open with text editor of your choosing)_
   * Change the info on line's 6 - 16
   * Save the changes

6. Open the telnet.py script
   * Change the info on line's 4 - 6
   * Save the changes

7. Open cmd(windows) or terminal(linux/unix)
   * cd to the directory where you unziped the files in step 2.
   * Run the interactive script
      * py -3 interactive.py _(windows)_
      * python3 interactive.py _(linux/unix)_

8. (Optional) Make a file name "start.bat"(windows) or "start.sh"(linux/unix)
