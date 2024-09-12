##import tkinter
##import random
##
##root = tkinter.Tk()
##root.title("Baseball Game")  # Optional: Set a title for the window
##
### Set minimum size of the window
##root.minsize(300, 150)  # Adjust these dimensions as per your preference
##
### Assume player_stats_file is defined correctly and opened for reading
##player_stats_file = open('player_statistics.txt', 'r')  # Corrected the filename
##
### Create the Canvas widget with increased width
##canvas = tkinter.Canvas(root, bg="white", height=300, width=600)  # Increased width to 600
##canvas.pack()  # Pack the canvas once
##
### Function to read player statistics and prepare indi_list
##def read_player_stats():
##    indi_list = []
##    # Read player statistics into a list
##    for _ in range(9):
##        line = player_stats_file.readline().strip()  # Read each line and strip newline characters
##        if not line:  # If end of file is reached
##            break
##        player_info = line.split()  # Split the line into individual elements
##        indi_list.extend(player_info)  # Extend the indi_list with player_info elements
##    return indi_list
##
### Function to display hit or strike on canvas
##def display_result(is_hit):
##    canvas.delete("all")  # Clear previous content on canvas
##    if is_hit:
##        canvas.create_text(300, 150, text='HE HIT!!!', font=('Helvetica', 30, 'bold'), fill='green')  # Adjusted position for wider canvas
##    else:
##        canvas.create_text(300, 150, text='STRIKE!!', font=('Helvetica', 30, 'bold'), fill='red')  # Adjusted position for wider canvas
##
### Function to start the game
##def start_game(start):
##    indi_list = read_player_stats()  # Get player data
##    current_index, outs, runs = 0, 0, 0
##    
##    if start == 'Y':
##        print("""
## ██████   █████  ███    ███ ███████     ███████ ████████  █████  ██████  ████████ 
##██       ██   ██ ████  ████ ██          ██         ██    ██   ██ ██   ██    ██    
##██   ███ ███████ ██ ████ ██ █████       ███████    ██    ███████ ██████     ██    
##██    ██ ██   ██ ██  ██  ██ ██               ██    ██    ██   ██ ██   ██    ██    
## ██████  ██   ██ ██      ██ ███████     ███████    ██    ██   ██ ██   ██    ██                                                                                                                                                                    
##""")
##        while outs < 3:  # Continue until there are 3 outs
##            print('\nOuts:', outs, '\nRuns:', runs, '\nBatting:', indi_list[current_index], '    OBP:', indi_list[current_index + 5],
##                  '\nOn Deck:', indi_list[(current_index + 6) % len(indi_list)])
##            
##            if current_index >= 6:
##                print('Previous:', indi_list[(current_index - 6) % len(indi_list)])
##            else:
##                print('Previous: None')
##
##            commence = input('Enter to swing')
##            if commence == '':
##                if float(indi_list[current_index + 5]) * 100 < random.randrange(100):
##                    # Update canvas content for hit
##                    display_result(True)
##                    runs += 1
##                else:
##                    # Update canvas content for strike
##                    display_result(False)
##                    outs += 1
##
##                root.update()  # Update the GUI to show changes
##
##            # Move to the next player's data
##            current_index = (current_index + 6) % len(indi_list)
##        print("""
## ██████   █████  ███    ███ ███████      ██████  ██    ██ ███████ ██████  
##██       ██   ██ ████  ████ ██          ██    ██ ██    ██ ██      ██   ██ 
##██   ███ ███████ ██ ████ ██ █████       ██    ██ ██    ██ █████   ██████  
##██    ██ ██   ██ ██  ██  ██ ██          ██    ██  ██  ██  ██      ██   ██ 
## ██████  ██   ██ ██      ██ ███████      ██████    ████   ███████ ██   ██                                                                                                                                                     
##""")
##        
### Start the game based on user input
##start_game(input('Are you ready? (Type Y to start) '))
##
### Close the file after reading
##player_stats_file.close()
##
### Start the main event loop
##root.mainloop()
##
### Close the file after reading
##player_stats_file.close()
##import tkinter
##import random
##
##root = tkinter.Tk()
##root.title("Baseball Game")
##
### Set minimum size of the window
##root.minsize(600, 400)
##
### Assume player_stats_file is defined correctly and opened for reading
##player_stats_file = open('player_statistics.txt', 'r')  # Corrected the filename
##
### Create the Canvas widget with increased width
##canvas = tkinter.Canvas(root, bg="white", height=300, width=600)
##canvas.pack()
##
### Labels for displaying game information
##label_outs = tkinter.Label(root, text="Outs: 0", font=('Helvetica', 14))
##label_outs.pack()
##
##label_runs = tkinter.Label(root, text="Runs: 0", font=('Helvetica', 14))
##label_runs.pack()
##
### Function to read player statistics and prepare indi_list
##def read_player_stats():
##    indi_list = []
##    # Read player statistics into a list
##    for _ in range(9):
##        line = player_stats_file.readline().strip()  # Read each line and strip newline characters
##        if not line:  # If end of file is reached
##            break
##        player_info = line.split()  # Split the line into individual elements
##        indi_list.extend(player_info)  # Extend the indi_list with player_info elements
##    return indi_list
##
### Function to display hit or strike on canvas
##def display_result(is_hit):
##    canvas.delete("all")  # Clear previous content on canvas
##    if is_hit:
##        canvas.create_text(300, 150, text='HE HIT!!!', font=('Helvetica', 30, 'bold'), fill='green')
##    else:
##        canvas.create_text(300, 150, text='STRIKE!!', font=('Helvetica', 30, 'bold'), fill='red')
##
### Function to handle swing button press
##def swing():
##    global outs, runs, current_index
##
##    if outs >= 3:
##        return  # Don't swing if game is over
##
##    if float(indi_list[current_index + 5]) * 100 < random.randrange(100):
##        # Update canvas content for hit
##        display_result(True)
##        runs += 1
##    else:
##        # Update canvas content for strike
##        display_result(False)
##        outs += 1
##
##    label_outs.config(text=f"Outs: {outs}")
##    label_runs.config(text=f"Runs: {runs}")
##
##    # Move to the next player's data
##    current_index = (current_index + 6) % len(indi_list)
##
##    if outs >= 3:
##        end_game()  # Check if game is over after swing
##
##    update_display()  # Update display after swing
##
### Function to start the game
##def start_game():
##    global indi_list, current_index, outs, runs
##
##    indi_list = read_player_stats()  # Get player data
##    current_index, outs, runs = 0, 0, 0
##
##    print("Game started.")
##    print("""
## ██████   █████  ███    ███ ███████     ███████ ████████  █████  ██████  ████████ 
##██       ██   ██ ████  ████ ██          ██         ██    ██   ██ ██   ██    ██    
##██   ███ ███████ ██ ████ ██ █████       ███████    ██    ███████ ██████     ██    
##██    ██ ██   ██ ██  ██  ██ ██               ██    ██    ██   ██ ██   ██    ██    
## ██████  ██   ██ ██      ██ ███████     ███████    ██    ██   ██ ██   ██    ██                                                                                                                                                                    
##    """)
##
##    update_display()  # Initial display update
##
### Function to update GUI display
##def update_display():
##    label_outs.config(text=f"Outs: {outs}")
##    label_runs.config(text=f"Runs: {runs}")
##
##    print('\nOuts:', outs, '\nRuns:', runs, '\nBatting:', indi_list[current_index], '    OBP:', indi_list[current_index + 5],
##          '\nOn Deck:', indi_list[(current_index + 6) % len(indi_list)])
##
##    if current_index >= 6:
##        print('Previous:', indi_list[(current_index - 6) % len(indi_list)])
##    else:
##        print('Previous: None')
##
### Function to end the game
##def end_game():
##    print("""
## ██████   █████  ███    ███ ███████      ██████  ██    ██ ███████ ██████  
##██       ██   ██ ████  ████ ██          ██    ██ ██    ██ ██      ██   ██ 
##██   ███ ███████ ██ ████ ██ █████       ██    ██ ██    ██ █████   ██████  
##██    ██ ██   ██ ██  ██  ██ ██          ██    ██  ██  ██  ██      ██   ██ 
## ██████  ██   ██ ██      ██ ███████      ██████    ████   ███████ ██   ██                                                                                                                                                     
##    """)
##    # Implement GUI updates or other game over actions if needed
##    # For simplicity, just print the game over message
##
### Button to swing
##swing_button = tkinter.Button(root, text="Swing", font=('Helvetica', 14), command=swing)
##swing_button.pack()
##
### Button to start the game
##start_button = tkinter.Button(root, text="Start Game", font=('Helvetica', 14), command=start_game)
##start_button.pack()
##
### Start the main event loop
##root.mainloop()
##
### Close the file after reading
##player_stats_file.close()
import tkinter
import random

root = tkinter.Tk()
root.title("Baseball Game")
root.minsize(600, 400)

# Assume player_stats_file is defined correctly and opened for reading
player_stats_file = open('player_statistics.txt', 'r')  # Corrected the filename

# Create the Canvas widget with increased width
canvas = tkinter.Canvas(root, bg="light blue", height=300, width=600)
canvas.pack()

# Labels for displaying game information
label_outs = tkinter.Label(root, text="Outs: 0", font=('Helvetica', 18, 'bold'), bg='light blue')
label_outs.pack()

label_runs = tkinter.Label(root, text="Runs: 0", font=('Helvetica', 18, 'bold'), bg='light blue')
label_runs.pack()

# Function to read player statistics and prepare indi_list
def read_player_stats():
    indi_list = []
    # Read player statistics into a list
    for _ in range(9):
        line = player_stats_file.readline().strip()  # Read each line and strip newline characters
        if not line:  # If end of file is reached
            break
        player_info = line.split()  # Split the line into individual elements
        indi_list.extend(player_info)  # Extend the indi_list with player_info elements
    return indi_list

# Function to display hit or strike on canvas
def display_result(is_hit):
    canvas.delete("all")  # Clear previous content on canvas
    if is_hit:
        canvas.create_text(300, 150, text='HE HIT!!!', font=('Helvetica', 36, 'bold'), fill='green')
    else:
        canvas.create_text(300, 150, text='STRIKE!!', font=('Helvetica', 36, 'bold'), fill='red')

# Function to handle swing button press
def swing():
    global outs, runs, current_index

    if outs >= 3:
        return  # Don't swing if game is over

    if float(indi_list[current_index + 5]) * 100 < random.randrange(100):
        # Update canvas content for hit
        display_result(True)
        runs += 1
    else:
        # Update canvas content for strike
        display_result(False)
        outs += 1

    label_outs.config(text=f"Outs: {outs}")
    label_runs.config(text=f"Runs: {runs}")

    # Move to the next player's data
    current_index = (current_index + 6) % len(indi_list)

    if outs >= 3:
        end_game()  # Check if game is over after swing

    update_display()  # Update display after swing

# Function to start the game
def start_game():
    global indi_list, current_index, outs, runs

    indi_list = read_player_stats()  # Get player data
    current_index, outs, runs = 0, 0, 0

    update_display()  # Initial display update

# Function to update GUI display
def update_display():
    label_outs.config(text=f"Outs: {outs}")
    label_runs.config(text=f"Runs: {runs}")

    print('\nOuts:', outs, '\nRuns:', runs, '\nBatting:', indi_list[current_index], '    OBP:', indi_list[current_index + 5],
          '\nOn Deck:', indi_list[(current_index + 6) % len(indi_list)])

    if current_index >= 6:
        print('Previous:', indi_list[(current_index - 6) % len(indi_list)])
    else:
        print('Previous: None')

# Function to end the game
def end_game():
    game_over_label = tkinter.Label(root, text="Game Over!", font=('Helvetica', 24, 'bold'), fg='red', bg='light blue')
    game_over_label.pack()
    swing_button.config(state='disabled')  # Disable swing button

# Button to swing
swing_button = tkinter.Button(root, text="Swing", font=('Helvetica', 16, 'bold'), command=swing)
swing_button.pack(pady=10)

# Button to start the game
start_button = tkinter.Button(root, text="Start Game", font=('Helvetica', 16, 'bold'), command=start_game)
start_button.pack(pady=10)

# Start the main event loop
root.mainloop()

# Close the file after reading
player_stats_file.close()