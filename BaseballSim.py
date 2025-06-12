import tkinter
import random

root = tkinter.Tk()
root.title("Baseball Game")
root.minsize(600, 400)

player_stats_file = open('player_statistics.txt', 'r')  

canvas = tkinter.Canvas(root, bg="light blue", height=300, width=600)
canvas.pack()

label_outs = tkinter.Label(root, text="Outs: 0", font=('Helvetica', 18, 'bold'), bg='light blue')
label_outs.pack()

label_runs = tkinter.Label(root, text="Runs: 0", font=('Helvetica', 18, 'bold'), bg='light blue')
label_runs.pack()

def read_player_stats():
    indi_list = []
    for _ in range(9):
        line = player_stats_file.readline().strip() 
        if not line:  
            break
        player_info = line.split()  
        indi_list.extend(player_info)  
    return indi_list

def display_result(is_hit):
    canvas.delete("all")  
    if is_hit:
        canvas.create_text(300, 150, text='HE HIT!!!', font=('Helvetica', 36, 'bold'), fill='green')
    else:
        canvas.create_text(300, 150, text='STRIKE!!', font=('Helvetica', 36, 'bold'), fill='red')

def swing():
    global outs, runs, current_index

    if outs >= 3:
        return 

    if float(indi_list[current_index + 5]) * 100 < random.randrange(100):
        display_result(True)
        runs += 1
    else:
        display_result(False)
        outs += 1

    label_outs.config(text=f"Outs: {outs}")
    label_runs.config(text=f"Runs: {runs}")

    current_index = (current_index + 6) % len(indi_list)

    if outs >= 3:
        end_game() 

    update_display()  

def start_game():
    global indi_list, current_index, outs, runs

    indi_list = read_player_stats()  
    current_index, outs, runs = 0, 0, 0

    update_display() 

def update_display():
    label_outs.config(text=f"Outs: {outs}")
    label_runs.config(text=f"Runs: {runs}")

    print('\nOuts:', outs, '\nRuns:', runs, '\nBatting:', indi_list[current_index], '    OBP:', indi_list[current_index + 5],
          '\nOn Deck:', indi_list[(current_index + 6) % len(indi_list)])

    if current_index >= 6:
        print('Previous:', indi_list[(current_index - 6) % len(indi_list)])
    else:
        print('Previous: None')

def end_game():
    game_over_label = tkinter.Label(root, text="Game Over!", font=('Helvetica', 24, 'bold'), fg='red', bg='light blue')
    game_over_label.pack()
    swing_button.config(state='disabled')  

swing_button = tkinter.Button(root, text="Swing", font=('Helvetica', 16, 'bold'), command=swing)
swing_button.pack(pady=10)

start_button = tkinter.Button(root, text="Start Game", font=('Helvetica', 16, 'bold'), command=start_game)
start_button.pack(pady=10)

root.mainloop()

player_stats_file.close()
