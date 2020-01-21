# CreateKosamaWorkouts

This was a quick home project to take some old workout files in Excel files, and turn them into something useful. 

# main.py

Processes the excel files, and outputs the usable data into json text files in the /workouts folder.

# workout.py

A very simple GUI for presenting those workout files. Allows the user to select the workout to execute, then starts a timer for that workout.

# config.json

Tells main.py where to look for excel files, and how many to look for.

# TODO
- Make the GUI prettier with more of an introduction for the workout.
- Be smarter about processing the files. Several excel files do not produce an actual workout file.
