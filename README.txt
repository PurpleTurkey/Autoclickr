A simple autoclicker for python3
This program uses libraries: pyautogui, keyboard and time
Created by PurpleTurkeys

-------------------------------------------------------------------------

HOW TO USE:

clicker = Autoclickr(True, 0, 'left', 'right') 
clicker.run() # Automatically loops

---------------------------------------------------------------------------

PARAMETERS

(True, 0, 'left', 'right')

1 - The first parameter indicates whether the clicker is enabled or disabled. It must be defined as enabled (True) to work.
2 - The second parameter is a time delay (in seconds), between clicks. If this is set to 0, there will be no delay. (Max cps of 10)
3 - The 3rd parameter takes a key which will be used to enable the clicker (All keys usable in the 'keyboard' library will work)
4 - The 4th parameter takes a key which will be used to disable the clicker (All keys usable in the 'keyboard' library will work)