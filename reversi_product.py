import tkinter as tk
from tkinter import messagebox
import random


# create the opening array with default positions
def create_opening_array():
    board = [["" for j in range(8)] for i in range(8)]
    board[3][3] = "⚫️"
    board[3][4] = "⚪️"
    board[4][3] = "⚪️"
    board[4][4] = "⚫️"
    return board


# create list of dictionaries of Tkinter buttons
def create_buttons():
    buttons_list = [{i: tk.Button(head_window, borderwidth=0.5, width=8, height=3) for i in range(8)} for j in range(8)]
    return buttons_list


# 8 functions to check legal moves in every direction straight and diagonal.
# The functions return a dictionary whose key is the legal location and the value is a list of all the locations that
# will be affected
def left_to_right(main_array, your_color, other_color):
    legal_moves_dict = {}
    rows = [[] for _ in range(8)]
    # create multiply list for every legal move, the list created in the match list in 'rows'
    for row in range(8):
        for col in range(8):
            if main_array[row][col] == your_color:
                rows[row].append([(row, col)])
            if main_array[row][col] == other_color and rows[row] != [] and col - 1 == rows[row][-1][-1][1]:
                rows[row][-1].append((row, col))
    # run on the list and create dictionary according the list
    for i in range(8):
        for j in range(len(rows[i])):
            if rows[i][j][-1][1] + 1 < 8 and len(rows[i][j]) > 1:
                if main_array[rows[i][j][-1][0]][rows[i][j][-1][1] + 1] == "":
                    legal_moves_dict[(rows[i][j][-1][0], rows[i][j][-1][1] + 1)] = rows[i][j][1:]
    return legal_moves_dict


def top_to_bottom(board, your_color, other_color):
    location_dict = {}
    cols = [[] for i in range(8)]
    for row in range(8):
        for col in range(8):
            if board[row][col] == your_color:
                cols[col].append([(row, col)])
            if board[row][col] == other_color and cols[col] != [] and row - 1 == cols[col][-1][-1][0]:
                cols[col][-1].append((row, col))
    for i in range(8):
        for j in range(len(cols[i])):
            if cols[i][j][-1][0] + 1 < 8 and len(cols[i][j]) > 1:
                if board[cols[i][j][-1][0] + 1][cols[i][j][-1][1]] == "":
                    location_dict[(cols[i][j][-1][0] + 1, cols[i][j][-1][1])] = cols[i][j][1:]

    return location_dict


def right_to_left(board, your_color, other_color):
    location_dict = {}
    rows = [[] for i in range(8)]
    for row in range(7, -1, -1):
        for col in range(7, -1, -1):
            if board[row][col] == your_color:
                rows[row].append([(row, col)])
            if board[row][col] == other_color and rows[row] != [] and col + 1 == rows[row][-1][-1][1]:
                rows[row][-1].append((row, col))
    for i in range(8):
        for j in range(len(rows[i])):
            if rows[i][j][-1][1] - 1 > -1 and len(rows[i][j]) > 1:
                if board[rows[i][j][-1][0]][rows[i][j][-1][1] - 1] == "":
                    location_dict[(rows[i][j][-1][0], rows[i][j][-1][1] - 1)] = rows[i][j][1:]

    return location_dict


def bottom_to_top(board, your_color, other_color):
    location_dict = {}
    cols = [[] for i in range(8)]
    for row in range(7, -1, -1):
        for col in range(7, -1, -1):
            if board[row][col] == your_color:
                cols[col].append([(row, col)])
            if board[row][col] == other_color and cols[col] != [] and row + 1 == cols[col][-1][-1][0]:
                cols[col][-1].append((row, col))
    for i in range(8):
        for j in range(len(cols[i])):
            if len(cols[i][j]) > 1 and cols[i][j][-1][0] - 1 > -1:
                if board[cols[i][j][-1][0] - 1][cols[i][j][-1][1]] == "":
                    location_dict[(cols[i][j][-1][0] - 1, cols[i][j][-1][1])] = cols[i][j][1:]

    return location_dict


def top_right_to_bottom_left(board, your_color, other_color):
    location_dict = {}
    ups = [[] for i in range(15)]
    for row in range(8):
        for col in range(8):
            if board[row][col] == your_color:
                ups[row + col].append([(row, col)])
            if board[row][col] == other_color and ups[row + col] != [] and row - 1 == ups[row + col][-1][-1][
                0] and col + 1 == ups[row + col][-1][-1][1]:
                ups[row + col][-1].append((row, col))
    for i in range(15):
        for j in range(len(ups[i])):
            if len(ups[i][j]) > 1 and ups[i][j][-1][1] - 1 > -1 and ups[i][j][-1][0] != 7:
                if board[ups[i][j][-1][0] + 1][ups[i][j][-1][1] - 1] == "":
                    location_dict[(ups[i][j][-1][0] + 1, ups[i][j][-1][1] - 1)] = ups[i][j][1:]
    return location_dict


def top_left_to_bottom_right(board, your_color, other_color):
    location_dict = {}
    down = [[] for i in range(15)]
    for row in range(8):
        for col in range(8):
            if board[row][col] == your_color:
                down[(row - col) + 7].append([(row, col)])
            if board[row][col] == other_color and down[(row - col) + 7] != [] and row - 1 == \
                    down[(row - col) + 7][-1][-1][0] and col - 1 == down[(row - col) + 7][-1][-1][1]:
                down[(row - col) + 7][-1].append((row, col))
    for i in range(15):
        for j in range(len(down[i])):
            if len(down[i][j]) > 1 and down[i][j][-1][1] + 1 < 8 and down[i][j][-1][0] != 7:
                if board[down[i][j][-1][0] + 1][down[i][j][-1][1] + 1] == "":
                    location_dict[(down[i][j][-1][0] + 1, down[i][j][-1][1] + 1)] = down[i][j][1:]
    return location_dict


def bottom_left_to_top_right(board, your_color, other_color):
    location_dict = {}
    ups = [[] for i in range(15)]
    for row in range(7, -1, -1):
        for col in range(8):
            if board[row][col] == your_color:
                ups[row + col].append([(row, col)])
            if board[row][col] == other_color and ups[row + col] != [] and row + 1 == ups[row + col][-1][-1][
                0] and col - 1 == ups[row + col][-1][-1][1]:
                ups[row + col][-1].append((row, col))
    for i in range(15):
        for j in range(len(ups[i])):
            if len(ups[i][j]) > 1 and ups[i][j][-1][1] != 7 and ups[i][j][-1][0] != 0:
                if board[ups[i][j][-1][0] - 1][ups[i][j][-1][1] + 1] == "":
                    location_dict[(ups[i][j][-1][0] - 1, ups[i][j][-1][1] + 1)] = ups[i][j][1:]
    return location_dict


def bottom_right_to_top_left(board, your_color, other_color):
    location_dict = {}
    down = [[] for i in range(15)]
    for row in range(7, -1, -1):
        for col in range(7, -1, -1):
            if board[row][col] == your_color:
                down[(row - col) + 7].append([(row, col)])
            if board[row][col] == other_color and down[(row - col) + 7] != [] and row + 1 == \
                    down[(row - col) + 7][-1][-1][0] and col + 1 == down[(row - col) + 7][-1][-1][1]:
                down[(row - col) + 7][-1].append((row, col))
    for i in range(15):
        for j in range(len(down[i])):
            if len(down[i][j]) > 1 and down[i][j][-1][1] != 0 and down[i][j][-1][0] != 0:
                if board[down[i][j][-1][0] - 1][down[i][j][-1][1] - 1] == "":
                    location_dict[(down[i][j][-1][0] - 1, down[i][j][-1][1] - 1)] = down[i][j][1:]
    return location_dict


# organized all the legal positions functions to 2 order dictionaries
def final_organized_legal_locations(board, your_color, other_color):
    a = left_to_right(board, your_color, other_color)
    b = right_to_left(board, your_color, other_color)
    c = top_to_bottom(board, your_color, other_color)
    d = bottom_to_top(board, your_color, other_color)
    e = top_left_to_bottom_right(board, your_color, other_color)
    f = top_right_to_bottom_left(board, your_color, other_color)
    g = bottom_left_to_top_right(board, your_color, other_color)
    h = bottom_right_to_top_left(board, your_color, other_color)

    dicts = [a, b, c, d, e, f, g, h]
    location_including_affected = {}

    for key in set().union(*dicts):
        box = []
        for dic in dicts:
            if key in dic:
                box += dic[key]
        location_including_affected[key] = box
    location_with_number_of_affected = {}
    for key in location_including_affected.keys():
        location_with_number_of_affected[key] = str(len(location_including_affected[key]))
    return location_including_affected, location_with_number_of_affected


# set the colors according the user choice
def colors(user_choice):
    global user_color, computer_color
    user_color = user_choice
    if user_choice == "⚪️":
        computer_color = "⚫️"
    else:
        computer_color = "⚪️"
    handle_user_torn()


# empty function for blocked buttons
def empty():
    pass


# the function run over all the buttons and update the color, text and the functionality
def update_buttons_functionality_according_the_data(legal_location_dictionaries):
    global buttons_list_1
    for row in range(8):
        for col in range(8):
            if (row, col) in legal_location_dictionaries.keys():
                a = legal_location_dictionaries[(row, col)]
                buttons_list_1[row][col].config(command=lambda row=row, col=col: handle_click((row, col)), bg="#E9FAFA",
                                                text=a)
                buttons_list_1[row][col].update()
            else:
                buttons_list_1[row][col].config(command=empty, bg="#FEFEFE")


# change color of specific location
def change_color_in_specific_location(row, col, color):
    global main_array, buttons_list_1
    main_array[row][col] = color


# change the main array according the move
def update_the_main_array_according_the_move(position_tuple, to_color):
    global main_array, legal_moves_includes_affected
    for key in legal_moves_includes_affected.keys():
        if key == position_tuple:
            for coin in legal_moves_includes_affected[key]:
                main_array[coin[0]][coin[1]] = to_color


# update the buttons (text) according the main array
def write_the_buttons_according_main_array():
    global main_array, buttons_list_1
    for row in range(8):
        for col in range(8):
            buttons_list_1[row][col].config(text=main_array[row][col])


# (Tkinter function) grid the buttons in their locations
def grid_buttons():
    global main_array, buttons_list_1
    for row in range(8):
        for col in range(8):
            buttons_list_1[row][col].grid(row=row, column=col)


# colored the buttons white
def to_white():
    global buttons_list_1
    for row in range(8):
        for col in range(8):
            buttons_list_1[row][col].config(bg="#FEFEFE")


def update_coins_to_check():
    global main_array, sides_locations, computer_color
    check = 0
    for row in range(8):
        for col in range(8):
            if main_array[row][col] == computer_color and (((row + 1, col + 1) in sides_locations and (
                    row + 1, col) in sides_locations and (row, col + 1) in sides_locations) or (
                                                                   (row - 1, col - 1) in sides_locations and (
                                                                   row - 1, col) in sides_locations and (
                                                                           row, col - 1) in sides_locations) or (
                                                                   (row + 1, col - 1) in sides_locations and (
                                                                   row + 1, col) in sides_locations and (
                                                                           row, col - 1) in sides_locations) or (
                                                                   (row - 1, col + 1) in sides_locations and (
                                                                   row - 1, col) in sides_locations and (
                                                                           row, col + 1) in sides_locations)):
                if (row, col) not in sides_locations:
                    sides_locations.add((row, col))
                    check += 1
    if check > 0:
        update_coins_to_check()


# choose the best move for computer
def highest_button(legal_moves_with_counter):
    update_coins_to_check()
    global main_array, sides_locations, legal_moves_includes_affected, user_color
    for key in legal_moves_with_counter:
        if ((key[0] - 1, key[1] - 1) in sides_locations and (key[0], key[1] - 1) in sides_locations and (
                key[0] - 1, key[1]) in sides_locations) or \
                ((key[0] + 1, key[1]) in sides_locations and (key[0] + 1, key[1]) in sides_locations and (
                        key[0], key[1] + 1) in sides_locations) or \
                ((key[0] + 1, key[1] - 1) in sides_locations and (key[0] + 1, key[1]) in sides_locations and (
                        key[0], key[1] - 1) in sides_locations) or \
                ((key[0] - 1, key[1] + 1) in sides_locations and (key[0] - 1, key[1]) in sides_locations and (
                        key[0], key[1] + 1) in sides_locations):
            sides_locations.add(key)
            return key
    for primer_key, to_flip in legal_moves_includes_affected.items():
        for key in to_flip:
            if ((key[0] - 1, key[1] - 1) in sides_locations and (key[0], key[1] - 1) in sides_locations and (
                    key[0] - 1, key[1]) in sides_locations) or \
                    ((key[0] + 1, key[1]) in sides_locations and (key[0] + 1, key[1]) in sides_locations and (
                            key[0], key[1] + 1) in sides_locations) or \
                    ((key[0] + 1, key[1] - 1) in sides_locations and (key[0] + 1, key[1]) in sides_locations and (
                            key[0], key[1] - 1) in sides_locations) or \
                    ((key[0] - 1, key[1] + 1) in sides_locations and (key[0] - 1, key[1]) in sides_locations and (
                            key[0], key[1] + 1) in sides_locations):
                return primer_key
    for key in legal_moves_with_counter:
        if ((key[0] == 7 or key[0] == 0) and main_array[key[0]][key[1] - 1] == user_color and
                main_array[key[0]][key[1] + 1] == user_color):
            return key
        elif ((key[1] == 7 or key[1] == 0) and main_array[key[0] + 1][key[1]] == user_color and
              main_array[key[0] - 1][key[1]] == user_color):
            return key
    return random.choice(list(legal_moves_with_counter.keys()))


# number of legal moves
def possible_moves(legal_moves):
    return len(legal_moves) > 0


# coins counter (to check who won)
def coins_counter():
    global user_color, computer_color, main_array
    user_coins = 0
    computer_coins = 0
    for row in range(8):
        for col in range(8):
            if main_array[row][col] == user_color:
                user_coins += 1
            elif main_array[row][col] == computer_color:
                computer_coins += 1
    return user_coins, computer_coins


# handle end game, check who won, present appropriate message and clear the main array and the buttons
def handle_end_game():
    global main_array, buttons_list_1, user_color, computer_color, legal_moves_includes_affected, sides_locations
    user_coins, computer_coins = coins_counter()
    messagebox.showinfo("end message", f'computer have {computer_coins} coins\nyou have {user_coins} coins')
    for row in range(8):
        for col in range(8):
            buttons_list_1[row][col].destroy()
    main_array = create_opening_array()
    buttons_list_1 = create_buttons()
    sides_locations = {(-1, -1), (0, -1), (1, -1), (2, -1), (3, -1), (4, -1), (5, -1), (6, -1), (7, -1), (8, -1),
                       (8, -1), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8),
                       (-1, -1), (-1, 0), (-1, 1), (-1, 2), (-1, 3), (-1, 4), (-1, 5), (-1, 6), (-1, 7), (-1, 8),
                       (-1, 8), (0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8)}


def handle_user_torn():
    global user_color, computer_color, main_array, buttons_list_1, legal_moves_includes_affected, counter_of_pass_turns
    grid_buttons()
    legal_moves_includes_affected, legal_moves_with_counter = final_organized_legal_locations(main_array, user_color,
                                                                                              computer_color)
    possible = possible_moves(legal_moves_with_counter)
    if possible:
        counter_of_pass_turns = 0
        write_the_buttons_according_main_array()
        update_buttons_functionality_according_the_data(legal_moves_with_counter)
        grid_buttons()
    else:
        counter_of_pass_turns += 1
        if counter_of_pass_turns < 2:
            messagebox.showinfo("passing message", "you have no options\nyour torn pass")
            computer_torn()
        else:
            handle_end_game()


# handle click
def handle_click(position_tuple):
    global buttons_list_1, main_array, computer_color, user_color, legal_moves_includes_affected
    change_color_in_specific_location(position_tuple[0], position_tuple[1], user_color)
    update_the_main_array_according_the_move(position_tuple, user_color)
    write_the_buttons_according_main_array()
    to_white()
    grid_buttons()
    head_window.after(800, computer_torn)


def computer_torn_after_delay(computer_choice):
    global computer_color
    update_the_main_array_according_the_move(computer_choice, computer_color)
    write_the_buttons_according_main_array()
    grid_buttons()
    handle_user_torn()


def computer_torn():
    global main_array, buttons_list_1, computer_color, user_color, legal_moves_includes_affected, counter_of_pass_turns
    legal_moves_includes_affected, legal_moves_with_counter = final_organized_legal_locations(main_array,
                                                                                              computer_color,
                                                                                              user_color)
    possible = possible_moves(legal_moves_with_counter)
    if possible:
        counter_of_pass_turns = 0
        computer_choice = highest_button(legal_moves_with_counter)
        change_color_in_specific_location(computer_choice[0], computer_choice[1], computer_color)
        write_the_buttons_according_main_array()
        grid_buttons()
        head_window.after(100, lambda: computer_torn_after_delay(computer_choice))
    else:
        counter_of_pass_turns += 1
        if counter_of_pass_turns < 2:
            messagebox.showinfo("passing message", "computer have no options\ncomputer torn pass")
            handle_user_torn()
        else:
            handle_end_game()


# initializing variables
computer_color = ""
user_color = ""
main_array = create_opening_array()
legal_moves_includes_affected = {}
counter_of_pass_turns = 0

# all the sides locations
sides_locations = {(-1, -1), (0, -1), (1, -1), (2, -1), (3, -1), (4, -1), (5, -1), (6, -1), (7, -1), (8, -1),
                   (8, -1), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8),
                   (-1, -1), (-1, 0), (-1, 1), (-1, 2), (-1, 3), (-1, 4), (-1, 5), (-1, 6), (-1, 7), (-1, 8),
                   (-1, 8), (0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8)}

# create main window
head_window = tk.Tk()

head_window.geometry("510x433")
head_window.config(bg="#C6E0E2")
color_label = tk.Label(head_window, borderwidth=0, background="#C6E0E2", text="Choose your color\n", fg="#477276",
                       font=("david", 20))
color_label.place(y=200, x=155)
white = tk.Button(head_window, borderwidth=0, background="#FCFDFD", font=3, width=8, height=2,
                  command=lambda: colors("⚪️"))
black = tk.Button(head_window, borderwidth=0, background="#060606", font=3, width=8, height=2,
                  command=lambda: colors("⚫️"))
white.place(x=110, y=280)
black.place(x=300, y=280)
buttons_list_1 = create_buttons()
head_window.mainloop()
