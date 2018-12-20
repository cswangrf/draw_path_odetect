# excellenteam-erez-python-paths-team-AAKO

Paths project made to help the Startup ODDETECT to analyze 
their data the project get from the user CSV file that include 
the data that the camera realized
and a picture that photographed by the camera.

The file should be in a specific format, this project will give the user 
the opportunity to choose which paths from the data file he want to see.

Their is 4 main filters that the user want to analyze the paths by using them:
* Time filter - show you all the paths that was during specific time in every day in the file.
* Date Filter - show you the paths during a specific date and time
* Location Filter - includes every paths that passed in this specific location.
* Multi Location Filter - the user can choose more than one location.

    The user can choose more than one filter in the same time.
    the user can see all of the paths he want in the same time or he can see each path alone.  

## Getting Started / Installation

python packages we have used:

pandas , matplotlib , pyQt5 , tkinter

## How to run

To run the project for development and testing purposes
 you need to run the main file. 

## Project Map

The project build using MVC patterns, their is five main packages:
* Views - here is the code that view the Gui to the user.
* Models - here you can find every function that processor 
the data in to get what the user need.
* Controllers - this is the main process that includes every 
connecting between the Views and Models.
* data - here we save the data after reduction to a pickle file.
* Test - here we saved the testing to check the correctness of the code.

    Also their is a file (settings.py) is very important to optimize the filtering process
 
 ######For handling several filters we used decorator design pattern
