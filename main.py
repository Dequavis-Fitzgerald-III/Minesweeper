"""This module Runs Minesweeper"""

from random import randint, choice
from sqlite3 import connect
from time import time
from tkinter import Canvas, Frame, Label, SOLID, Tk, Button, messagebox, Entry, W, PhotoImage, CENTER
from webbrowser import open

from apscheduler.schedulers.background import BackgroundScheduler
from tkmacosx import Button as BUTTON

# region Global variables
global Moves
global States
global Num_Of_Flags
global Flag_Exists
global Button_Called
global logged_in_name


# endregion

def Main():
    """This function Runs the beginner level game of Minesweeper"""
    # region Global Variables
    global Moves
    global States
    global Flag_Exists
    global Button_Called
    global Num_Of_Flags
    Moves = 0
    Num_Of_Flags = 0
    start_time = time()

    # endregion

    # region Accounts:
    def Accounts():
        """deals with the accounts functionality called when the login button is pressed"""

        def quit_accounts():
            """destroys the window"""
            ws.destroy()

        def account_screen():
            """lets the user see account information"""
            global logged_in_name

            def quit_account_screen():
                """destroys the account screen window and changes the Login Button"""
                new_window.destroy()
                change_login_button()

            # region Music Links
            def BBM11():
                open("https://soundcloud.com/twofriendsmixes6/bb11?utm_source=clipboard&utm_medium=text"
                     "&utm_campaign=social_sharing")

            def meme():
                open("https://youtu.be/dQw4w9WgXcQ")

            def BBM20():
                open(
                    "https://soundcloud.com/bigbootiemix/bb20?utm_source=clipboard&utm_medium=text&utm_campaign"
                    "=social_sharing")

            def WholeLotta():
                open(
                    "https://soundcloud.com/ledzeppelin/whole-lotta-love-1?utm_source=clipboard&utm_medium=text"
                    "&utm_campaign=social_sharing")

            def Buzzin():
                open(
                    "https://soundcloud.com/juliancastellanos/the-boys-are-buzzin-vol-3?utm_source=clipboard"
                    "&utm_medium=text&utm_campaign=social_sharing")

            def playlist1():
                open("https://open.spotify.com/playlist/7AKKYeElOlah8FTzZf9lyh?si=d97b6c24b62548a8")

            # endregion

            name = str(logged_in_name)
            highscore1 = ""
            highscore2 = ""
            highscore3 = ""
            highscore4 = ""
            highscore5 = ""
            GamesPlayed = ""
            GamesWon = ""
            con = connect('ACCOUNTS.db')
            c = con.cursor()
            sql = "Select * from user WHERE name = ?"
            data = [name]
            for row in c.execute(sql, data):
                highscore1 = row[2]
                highscore2 = row[3]
                highscore3 = row[4]
                highscore4 = row[5]
                highscore5 = row[6]
                GamesPlayed = row[7]
                GamesWon = row[8]
            try:
                WinRate = round((int(GamesWon) / int(GamesPlayed)) * 100)
                WinRate = str(WinRate) + "%"
            except ValueError:
                WinRate = "N/A"

            new_window = Tk()
            new_window.title(f'{name}: Account Information')
            new_window.geometry('700x575')
            new_window.config(bg='Purple')
            f_f = ('Times New Roman', 20)
            f_g = ('Times New Roman', 50)
            # region widgets for window
            login_frame = Frame(new_window, bd=2, bg='purple', relief=SOLID, padx=12, pady=10)
            name_label = Label(login_frame, text=f"Hi {name}", bg='green', font=f_g)
            name_label.place(relx=0.5, rely=0.5, anchor=CENTER)
            login_frame.place(x=0, y=0, height=100, width=700)
            leave_button = Button(new_window, width=20, text='Exit', bg="Green", font=f_f, relief=SOLID, cursor='hand2',
                                  command=quit_account_screen)
            high_score_frame = Frame(new_window, bd=2, bg='green', relief=SOLID, padx=10, pady=10)
            Label(high_score_frame, text=f"fastest time 1 is {highscore1}", bg='light blue', font=f_f).grid(row=0,
                                                                                                            column=0,
                                                                                                            sticky=W,
                                                                                                            pady=10)
            Label(high_score_frame, text=f"fastest time 2 is {highscore2}", bg='light blue', font=f_f).grid(row=1,
                                                                                                            column=0,
                                                                                                            sticky=W,
                                                                                                            pady=10)
            Label(high_score_frame, text=f"fastest time 3 is {highscore3}", bg='light blue', font=f_f).grid(row=2,
                                                                                                            column=0,
                                                                                                            sticky=W,
                                                                                                            pady=10)
            Label(high_score_frame, text=f"fastest time 4 is {highscore4}", bg='light blue', font=f_f).grid(row=3,
                                                                                                            column=0,
                                                                                                            sticky=W,
                                                                                                            pady=10)
            Label(high_score_frame, text=f"fastest time 5 is {highscore5}", bg='light blue', font=f_f).grid(row=4,
                                                                                                            column=0,
                                                                                                            sticky=W,
                                                                                                            pady=10)
            games_frame = Frame(new_window, bd=2, bg='green', relief=SOLID, padx=10, pady=10)
            Label(games_frame, text=f"Games played: {GamesPlayed}", bg='light blue', font=f_f).grid(row=0, column=0,
                                                                                                    sticky=W,
                                                                                                    pady=10)
            Label(games_frame, text=f"Games won: {GamesWon}", bg='light blue', font=f_f).grid(row=1, column=0, sticky=W,
                                                                                              pady=10)
            Label(games_frame, text=f"Win Rate: {WinRate}", bg='light blue', font=f_f).grid(row=2, column=0, sticky=W,
                                                                                            pady=10)
            new_frame = Frame(new_window, bd=2, bg='green', relief=SOLID, padx=5, pady=10)
            meme_btn = Button(new_frame, width=20, text='Alpha Music', font=f_f, relief=SOLID,
                              cursor='hand2',
                              command=meme)
            BBM11_btn = Button(new_frame, width=20, text='Big Bootie Vol.11', font=f_f,
                               relief=SOLID,
                               cursor='hand2',
                               command=BBM11)
            BBM20_btn = Button(new_frame, width=20, text='Big Bootie Vol.20', font=f_f,
                               relief=SOLID,
                               cursor='hand2',
                               command=BBM20)
            wholelotta_btn = Button(new_frame, width=20, text='Whole Lotta Love', font=f_f,
                                    relief=SOLID,
                                    cursor='hand2',
                                    command=WholeLotta)
            Buzzin_btn = Button(new_frame, width=20, text='Buzzin', font=f_f, relief=SOLID,
                                cursor='hand2',
                                command=Buzzin)
            playlist1_btn = Button(new_frame, width=20, text=':)', font=f_f, relief=SOLID,
                                   cursor='hand2',
                                   command=playlist1)
            BBM11_btn.grid(row=1, column=1, pady=5, padx=12)
            meme_btn.grid(row=2, column=2, pady=5, padx=12)
            Buzzin_btn.grid(row=2, column=1, pady=5, padx=12)
            BBM20_btn.grid(row=1, column=2, pady=5, padx=12)
            wholelotta_btn.grid(row=3, column=1, pady=5, padx=12)
            playlist1_btn.grid(row=3, column=2, pady=5, padx=12)
            leave_button.place(x=600, y=525, height=50, width=100)
            high_score_frame.place(x=0, y=100, height=275, width=200)
            games_frame.place(x=500, y=100, height=175, width=175)
            new_frame.place(x=100, y=400, width=475, height=150)
            new_window.mainloop()
            # endregion

        def register():
            """lets the user register a new account"""
            top_frame.destroy()
            login_btn.destroy()
            register_btn.destroy()

            def Add_Account():
                """adds the details the user submitted into the SQL file"""
                warn = ""
                check_counter = 0
                if len(register_pwd.get()) < 8 or len(register_pwd.get()) > 12:
                    warn = "password must be between 8 and 12 characters"
                else:
                    check_counter += 1
                if register_name.get() == "":
                    warn = "Name can't be empty"
                else:
                    check_counter += 1
                if register_pwd.get() == "":
                    warn = "Password can't be empty"
                else:
                    check_counter += 1
                if pwd_again.get() == "":
                    warn = "Re-enter password can't be empty"
                else:
                    check_counter += 1
                if register_pwd.get() != pwd_again.get():
                    warn = "Passwords didn't match!"
                else:
                    check_counter += 1
                if check_counter == 5:
                    con = connect('ACCOUNTS.db')
                    cur = con.cursor()
                    cur.execute(
                        "INSERT INTO user VALUES (:name,:password,:HighScore,:HighScore2,:HighScore3,:HighScore4,"
                        ":HighScore5,:GamesPlayed,:GamesWon)",
                        {
                            'name': register_name.get(),
                            'password': register_pwd.get(),
                            'HighScore': '',
                            'HighScore2': '',
                            'HighScore3': '',
                            'HighScore4': '',
                            'HighScore5': '',
                            'GamesPlayed': '',
                            'GamesWon': ''
                        })
                    con.commit()
                    messagebox.showinfo('confirmation', 'Record Saved')
                    quit_accounts()

                else:
                    messagebox.showerror('Error ', warn)

            # region Registration window
            register_frame = Frame(ws, bd=2, bg='white', relief=SOLID, padx=4, pady=10)
            Label(register_frame, text="Register your details", bg='white', font=font_g).grid(padx=4, pady=10)
            register_frame.place(x=0, y=0, width=500, height=100)
            Register_frame = Frame(ws, bd=2, bg='white', relief=SOLID, padx=10, pady=10)
            Label(Register_frame, text="Enter Name", bg='white', font=font_f).grid(row=0, column=0, sticky=W, pady=2)
            Label(Register_frame, text="Enter Password", bg='white', font=font_f).grid(row=1, column=0, sticky=W,
                                                                                       pady=2)
            Label(Register_frame, text="Re-Enter Password", bg='white', font=font_f).grid(row=2, column=0, sticky=W,
                                                                                          pady=2)
            register_name = Entry(Register_frame, font=font_f)
            register_pwd = Entry(Register_frame, font=font_f, show='*')
            pwd_again = Entry(Register_frame, font=font_f, show='*')
            enter_btn = Button(Register_frame, width=16, text='Register', font=font_f, relief=SOLID, cursor='hand2',
                               command=Add_Account)
            return_btn = Button(Register_frame, width=50, text='Return', font=font_f, relief=SOLID, cursor='hand2',
                                command=lambda: [quit_accounts(), Accounts()])
            register_name.grid(row=0, column=1, pady=3, padx=12)
            register_pwd.grid(row=1, column=1, pady=3, padx=12)
            pwd_again.grid(row=2, column=1, pady=3, padx=12)
            enter_btn.grid(row=3, column=1, pady=5, padx=12)
            return_btn.place(x=0, y=125, width=150, height=75)
            Register_frame.place(x=0, y=150, width=500, height=225)
            # endregion

        def login():
            top_frame.destroy()
            login_btn.destroy()
            register_btn.destroy()

            def login_response():
                """validates the users inputs using SQL file,logs in if their details match an account"""
                name = []
                pwd = []
                con = connect('ACCOUNTS.db')
                c = con.cursor()
                for row in c.execute("Select * from user"):
                    name.append(row[0])
                    pwd.append(row[1])

                uname = name_tf.get()
                upwd = pwd_tf.get()
                check_counter = 0
                warn = ""
                if uname == "":
                    warn = "Name can't be empty"
                else:
                    check_counter += 1
                if upwd == "":
                    warn = "Password can't be empty"
                else:
                    check_counter += 1
                if check_counter == 2:
                    x = 0
                    for o in range(len(name)):
                        if uname == name[o] and upwd == pwd[o]:
                            global logged_in_name
                            logged_in_name = uname
                            quit_accounts()
                            account_screen()
                            x = 1
                    if x == 0:
                        messagebox.showerror('Login Status', 'invalid username or password')
                        login()
                else:
                    messagebox.showerror('', warn)
                    login()

            # region Login window
            login_frame = Frame(ws, bd=2, bg='white', relief=SOLID, padx=12, pady=10)
            Label(login_frame, text="Enter login details", bg='white', font=font_g).grid(padx=10, pady=10)
            login_frame.place(x=0, y=0, width=500, height=100)
            # widgets for login frame
            Login_frame = Frame(ws, bd=2, bg='white', relief=SOLID, padx=10, pady=10)
            Label(Login_frame, text="Enter Name", bg='white', font=font_f).grid(row=0, column=0, sticky=W, pady=10)
            Label(Login_frame, text="Enter Password", bg='white', font=font_f).grid(row=1, column=0, sticky=W, pady=10)
            name_tf = Entry(Login_frame, font=font_f)
            pwd_tf = Entry(Login_frame, font=font_f, show='*')
            enter_btn = Button(Login_frame, width=16, text='Login', font=font_f, relief=SOLID, cursor='hand2',
                               command=login_response)
            return_btn = Button(Login_frame, width=50, text='Return', font=font_f, relief=SOLID, cursor='hand2',
                                command=lambda: [quit_accounts(), Accounts()])
            name_tf.grid(row=0, column=1, pady=5, padx=10)
            pwd_tf.grid(row=1, column=1, pady=5, padx=10)
            enter_btn.grid(row=3, column=1, pady=10, padx=10)
            return_btn.place(x=0, y=125, width=150, height=75)
            Login_frame.place(x=0, y=150, width=500, height=225)
            # endregion

        try:
            global logged_in_name
            account_screen()
        except NameError:
            # region Physical Account Window
            ws = Tk()
            ws.title('Log in and Registration System')
            ws.geometry('500x450')
            ws.config(bg='Purple')
            font_f = ('Times New Roman', 20)
            font_g = ('Times New Roman', 50)

            # top frame for banner heading
            top_frame = Frame(ws, bd=2, bg='Pink', relief=SOLID, padx=5, pady=5)
            Label(top_frame, text="Account Manager", bg="Turquoise", font=font_g).grid(padx=3, pady=10)
            top_frame.place(x=45, y=50, width=390, height=100)

            # buttons
            login_btn = Button(ws, width=20, text='Login', bg="Green", font=font_f, relief=SOLID, cursor='hand',
                               command=login)
            login_btn.place(x=350, y=175, width=125, height=60)

            register_btn = Button(ws, width=20, text='Register', bg="Green", font=font_f, relief=SOLID, cursor='hand2',
                                  command=register)
            register_btn.place(x=350, y=275, width=125, height=60)

            exit_btn = Button(ws, width=20, text='Exit', bg="Green", font=font_f, relief=SOLID, cursor='hand2',
                              command=quit_accounts)
            exit_btn.place(x=300, y=400, width=200, height=50)
            ws.mainloop()
            # endregion

    # endregion

    # region functions to restart, end game(loss/win) and update database:
    def restart():
        """This function restarts the game, resets variables and adds one to games played"""
        # region increment games_played by 1
        global logged_in_name
        try:
            name = str(logged_in_name)
            con = connect('ACCOUNTS.db')
            c = con.cursor()
            data = [name]
            sql = "UPDATE user SET GamesPlayed = (GamesPlayed + 1) WHERE name = ? "
            c.execute(sql, data)
            con.commit()
        except NameError:
            warn = "log in to save your results"
            messagebox.showinfo("info", warn)
        # endregion
        Board.destroy()
        sched.shutdown(wait=False)
        Main()

    def game_over():
        """This function lets the user know they have lost then calls restart"""
        warn = "GAME OVER"
        messagebox.showinfo("info", warn)
        restart()

    def check_highscore(name):
        time_elapsed = round(time() - start_time, 1)
        # region fill variables
        highscore1 = 0
        highscore2 = 0
        highscore3 = 0
        highscore4 = 0
        highscore5 = 0
        con = connect('ACCOUNTS.db')
        c = con.cursor()
        sql = "Select * from user WHERE name = ?"
        Data = [name]
        for row in c.execute(sql, Data):
            name = str(row[0])
            if row[2] != "":
                highscore1 = int(row[2])
            if row[3] != "":
                highscore2 = int(row[3])
            if row[4] != "":
                highscore3 = int(row[4])
            if row[5] != "":
                highscore4 = int(row[5])
            if row[6] != "":
                highscore5 = int(row[6])

        # endregion
        if time_elapsed < highscore1:
            highscore5 = highscore4
            highscore4 = highscore3
            highscore3 = highscore2
            highscore2 = highscore1
            highscore1 = time_elapsed
        elif time_elapsed < highscore2:
            highscore5 = highscore4
            highscore4 = highscore3
            highscore3 = highscore2
            highscore2 = time_elapsed
        elif time_elapsed < highscore3:
            highscore5 = highscore4
            highscore4 = highscore3
            highscore3 = time_elapsed
        elif time_elapsed < highscore4:
            highscore5 = highscore4
            highscore4 = time_elapsed
        elif time_elapsed < highscore5:
            highscore5 = time_elapsed

        data = [highscore1, highscore2, highscore3, highscore4, highscore5, name]
        sql = "UPDATE user SET HighScore = ?, HighScore2 = ?, HighScore3 = ?, HighScore4 = ?, HighScore5 = ? " \
              "WHERE name = ? "
        c.execute(sql, data)
        con.commit()

    def WinCheck():
        """this function checks to see if the game has been won and must be called after every moved"""
        # region Checking Algorithm:
        Un_pressed = 0
        if button1.winfo_exists():
            Un_pressed += 1
        if button2.winfo_exists():
            Un_pressed += 1
        if button3.winfo_exists():
            Un_pressed += 1
        if button4.winfo_exists():
            Un_pressed += 1
        if button5.winfo_exists():
            Un_pressed += 1
        if button6.winfo_exists():
            Un_pressed += 1
        if button7.winfo_exists():
            Un_pressed += 1
        if button8.winfo_exists():
            Un_pressed += 1
        if button9.winfo_exists():
            Un_pressed += 1
        if button10.winfo_exists():
            Un_pressed += 1
        if button11.winfo_exists():
            Un_pressed += 1
        if button12.winfo_exists():
            Un_pressed += 1
        if button13.winfo_exists():
            Un_pressed += 1
        if button14.winfo_exists():
            Un_pressed += 1
        if button15.winfo_exists():
            Un_pressed += 1
        if button16.winfo_exists():
            Un_pressed += 1
        if button17.winfo_exists():
            Un_pressed += 1
        if button18.winfo_exists():
            Un_pressed += 1
        if button19.winfo_exists():
            Un_pressed += 1
        if button20.winfo_exists():
            Un_pressed += 1
        if button21.winfo_exists():
            Un_pressed += 1
        if button22.winfo_exists():
            Un_pressed += 1
        if button23.winfo_exists():
            Un_pressed += 1
        if button24.winfo_exists():
            Un_pressed += 1
        if button25.winfo_exists():
            Un_pressed += 1
        if button26.winfo_exists():
            Un_pressed += 1
        if button27.winfo_exists():
            Un_pressed += 1
        if button28.winfo_exists():
            Un_pressed += 1
        if button29.winfo_exists():
            Un_pressed += 1
        if button30.winfo_exists():
            Un_pressed += 1
        if button31.winfo_exists():
            Un_pressed += 1
        if button32.winfo_exists():
            Un_pressed += 1
        if button33.winfo_exists():
            Un_pressed += 1
        if button34.winfo_exists():
            Un_pressed += 1
        if button35.winfo_exists():
            Un_pressed += 1
        if button36.winfo_exists():
            Un_pressed += 1
        if button37.winfo_exists():
            Un_pressed += 1
        if button38.winfo_exists():
            Un_pressed += 1
        if button39.winfo_exists():
            Un_pressed += 1
        if button40.winfo_exists():
            Un_pressed += 1
        if button41.winfo_exists():
            Un_pressed += 1
        if button42.winfo_exists():
            Un_pressed += 1
        if button43.winfo_exists():
            Un_pressed += 1
        if button44.winfo_exists():
            Un_pressed += 1
        if button45.winfo_exists():
            Un_pressed += 1
        if button46.winfo_exists():
            Un_pressed += 1
        if button47.winfo_exists():
            Un_pressed += 1
        if button48.winfo_exists():
            Un_pressed += 1
        if button49.winfo_exists():
            Un_pressed += 1
        if button50.winfo_exists():
            Un_pressed += 1
        if button51.winfo_exists():
            Un_pressed += 1
        if button52.winfo_exists():
            Un_pressed += 1
        if button53.winfo_exists():
            Un_pressed += 1
        if button54.winfo_exists():
            Un_pressed += 1
        if button55.winfo_exists():
            Un_pressed += 1
        if button56.winfo_exists():
            Un_pressed += 1
        if button57.winfo_exists():
            Un_pressed += 1
        if button58.winfo_exists():
            Un_pressed += 1
        if button59.winfo_exists():
            Un_pressed += 1
        if button60.winfo_exists():
            Un_pressed += 1
        if button61.winfo_exists():
            Un_pressed += 1
        if button62.winfo_exists():
            Un_pressed += 1
        if button63.winfo_exists():
            Un_pressed += 1
        if button64.winfo_exists():
            Un_pressed += 1
        if button65.winfo_exists():
            Un_pressed += 1
        if button66.winfo_exists():
            Un_pressed += 1
        if button67.winfo_exists():
            Un_pressed += 1
        if button68.winfo_exists():
            Un_pressed += 1
        if button69.winfo_exists():
            Un_pressed += 1
        if button70.winfo_exists():
            Un_pressed += 1
        # endregion

        if Un_pressed == 10:
            global Moves
            global logged_in_name
            print("You Won!!!\nYou did it in " + str(Moves) + " moves :)")
            warn = ("You Won!!!\nYou did it in " + str(Moves) + " moves :)")
            messagebox.showinfo("info", warn)
            try:
                check_highscore(logged_in_name)
                name = str(logged_in_name)
                con = connect('ACCOUNTS.db')
                c = con.cursor()
                data = [name]
                sql = "UPDATE user SET GamesWon = (GamesWon + 1) WHERE name = ? "
                c.execute(sql, data)
                con.commit()
            except NameError:
                warn = "log in to save your results"
                messagebox.showinfo("info", warn)
            restart()

    # endregion

    # region Creating Variable Lists:
    States = [0 for _ in range(71)]
    Flag_Exists = [False for _ in range(71)]
    Button_Called = [False for _ in range(71)]
    # endregionx

    # region Grid Building with states:
    Mine_List = []
    for i in range(1, 11):
        num = (randint(1, 70))
        while num in Mine_List:
            num = (randint(1, 70))
        Mine_List.append(num)
    for _, MINE in enumerate(Mine_List):
        States[MINE] = 9
    print(Mine_List)

    normal_cases = [12, 13, 14, 15, 16, 17, 18, 19, 22, 23, 24, 25, 26, 27, 28, 29, 32, 33, 34, 35, 36, 37, 38, 39,
                    42,
                    43,
                    44, 45, 46, 47, 48, 49, 52, 53, 54, 55, 56, 57, 58, 59]
    left_side = [11, 21, 31, 41, 51]
    right_side = [20, 30, 40, 50, 60]
    top_side = [2, 3, 4, 5, 6, 7, 8, 9]
    bottom_side = [62, 63, 64, 65, 66, 67, 68, 69]
    lands = []
    for i in range(len(States)):
        if i not in Mine_List:
            if i in normal_cases:
                if States[i - 11] == 9:
                    States[i] += 1
                if States[i - 10] == 9:
                    States[i] += 1
                if States[i - 9] == 9:
                    States[i] += 1
                if States[i - 1] == 9:
                    States[i] += 1
                if States[i + 1] == 9:
                    States[i] += 1
                if States[i + 9] == 9:
                    States[i] += 1
                if States[i + 10] == 9:
                    States[i] += 1
                if States[i + 11] == 9:
                    States[i] += 1
            elif i == 1:
                if States[i + 1] == 9:
                    States[i] += 1
                if States[i + 10] == 9:
                    States[i] += 1
                if States[i + 11] == 9:
                    States[i] += 1
            elif i == 10:
                if States[i - 1] == 9:
                    States[i] += 1
                if States[i + 9] == 9:
                    States[i] += 1
                if States[i + 10] == 9:
                    States[i] += 1
            elif i == 61:
                if States[i - 10] == 9:
                    States[i] += 1
                if States[i - 9] == 9:
                    States[i] += 1
                if States[i + 1] == 9:
                    States[i] += 1
            elif i == 70:
                if States[i - 11] == 9:
                    States[i] += 1
                if States[i - 10] == 9:
                    States[i] += 1
                if States[i - 1] == 9:
                    States[i] += 1
            elif i in left_side:
                if States[i - 10] == 9:
                    States[i] += 1
                if States[i - 9] == 9:
                    States[i] += 1
                if States[i + 1] == 9:
                    States[i] += 1
                if States[i + 10] == 9:
                    States[i] += 1
                if States[i + 11] == 9:
                    States[i] += 1
            elif i in right_side:
                if States[i - 11] == 9:
                    States[i] += 1
                if States[i - 10] == 9:
                    States[i] += 1
                if States[i - 1] == 9:
                    States[i] += 1
                if States[i + 9] == 9:
                    States[i] += 1
                if States[i + 10] == 9:
                    States[i] += 1
            elif i in top_side:
                if States[i - 1] == 9:
                    States[i] += 1
                if States[i + 1] == 9:
                    States[i] += 1
                if States[i + 9] == 9:
                    States[i] += 1
                if States[i + 10] == 9:
                    States[i] += 1
                if States[i + 11] == 9:
                    States[i] += 1
            elif i in bottom_side:
                if States[i - 11] == 9:
                    States[i] += 1
                if States[i - 10] == 9:
                    States[i] += 1
                if States[i - 9] == 9:
                    States[i] += 1
                if States[i - 1] == 9:
                    States[i] += 1
                if States[i + 1] == 9:
                    States[i] += 1
            if States[i] == 0 and i != 0:
                lands.append(i)
    print(States)

    # endregion

    # region Placing each square:
    def mine_placer(input1, input2):
        """places mines"""
        mine_frame = Frame(Board, bg='red', relief=SOLID)
        Label(mine_frame, image=img_mine).grid()
        mine_frame.place(x=input1, y=input2, width=100, height=100)

    def number1_placer(input1, input2):
        """places 1's"""
        one_frame = Frame(Board, relief=SOLID)
        Label(one_frame, image=img_one, ).grid()
        one_frame.place(x=input1, y=input2, width=100, height=100)

    def number2_placer(input1, input2):
        """places 2's"""
        two_frame = Frame(Board, relief=SOLID)
        Label(two_frame, image=img_two).grid()
        two_frame.place(x=input1, y=input2, width=100, height=100)

    def number3_placer(input1, input2):
        """places 3's"""
        three_frame = Frame(Board, relief=SOLID)
        Label(three_frame, image=img_three).grid()
        three_frame.place(x=input1, y=input2, width=100, height=100)

    def number4_placer(input1, input2):
        """places 4's"""
        four_frame = Frame(Board, relief=SOLID)
        Label(four_frame, image=img_four).grid()
        four_frame.place(x=input1, y=input2, width=100, height=100)

    def number5_placer(input1, input2):
        """places 5's"""
        five_frame = Frame(Board, relief=SOLID)
        Label(five_frame, image=img_five).grid()
        five_frame.place(x=input1, y=input2, width=100, height=100)

    def number6_placer(input1, input2):
        """places 6's"""
        six_frame = Frame(Board, relief=SOLID)
        Label(six_frame, image=img_six).grid()
        six_frame.place(x=input1, y=input2, width=100, height=100)

    def number7_placer(input1, input2):
        """places 7's"""
        seven_frame = Frame(Board, relief=SOLID)
        Label(seven_frame, image=img_seven).grid()
        seven_frame.place(x=input1, y=input2, width=100, height=100)

    def number8_placer(input1, input2):
        """places 8's"""
        eight_frame = Frame(Board, relief=SOLID)
        Label(eight_frame, image=img_eight).grid()
        eight_frame.place(x=input1, y=input2, width=100, height=100)

    def land_placer(input1, input2):
        """places lands"""
        land_frame = Frame(Board, relief=SOLID)
        Label(land_frame, image=img_land).grid()
        land_frame.place(x=input1, y=input2, width=100, height=100)

    # endregion

    # region Physical Grid Building:
    Board = Tk()
    Board.title("Minesweeper Beginner Level")
    Board.config(bg='grey')
    Board.geometry("1500x1500")
    g = ('Times New Roman', 50)
    canvas = Canvas(Board)
    canvas.pack()
    mines_left_frame = Frame(Board, bd=2, bg='black', relief=SOLID, padx=12, pady=10)
    mines_left_frame.place(x=217, y=0, width=200, height=100)
    mines_left_label = Label(mines_left_frame, text="Mines: 10", font=('Times New Roman', 43), fg='white', bg='black')
    mines_left_label.pack()
    restart_button = BUTTON(Board, text='Restart', fg='white', bd=5, font=('Times New Roman', 35),
                            bg='light blue',
                            relief=SOLID,
                            cursor='hand2',
                            command=restart)
    restart_button.place(x=567, y=0, width=300, height=100)
    timer_frame = Frame(Board, bd=2, bg='black', relief=SOLID, padx=12, pady=10)
    timer_frame.place(x=1017, y=0, width=200, height=100)
    timer_label = Label(timer_frame, text="0 Secs", fg='white', font=g, bg='black')
    timer_label.pack()
    exit_button = BUTTON(Board, text='EXIT', fg='white', bd=5, font=g, bg='purple', width=20, relief=SOLID,
                         cursor='hand2',
                         command=exit)
    exit_button.place(x=1235, y=735, width=200, height=100)
    login_button = BUTTON(Board, text='LOGIN', fg='white', bd=5, font=g, bg='purple', width=20, relief=SOLID,
                          cursor='hand2',
                          command=Accounts)
    login_button.place(x=0, y=0, width=200, height=100)
    img_mine = PhotoImage(file='Mine.png')
    img_land = PhotoImage(file='Land.png')
    img_one = PhotoImage(file='One.png')
    img_two = PhotoImage(file='Two.png')
    img_three = PhotoImage(file='Three.png')
    img_four = PhotoImage(file='Four.png')
    img_five = PhotoImage(file='Five.png')
    img_six = PhotoImage(file='Six.png')
    img_seven = PhotoImage(file='Seven.png')
    img_eight = PhotoImage(file='Eight.png')

    def update_mines_left():
        """updates the mines left label after a flag is placed"""
        global Num_Of_Flags
        mines_left = 10 - Num_Of_Flags
        mines_left_label['text'] = "Mines:" + str(mines_left)

    def change_login_button():
        """changes the login_button in the top left to say account info"""
        login_button['text'] = "Info"

    def update_timer():
        """updates the timer label every second"""
        time_elapsed = round(time() - start_time)
        timer_label['text'] = str(time_elapsed) + ' Secs'

    sched = BackgroundScheduler()
    sched.add_job(update_timer, 'interval', seconds=1)
    sched.start()

    for z in range(len(States)):
        num1 = z % 10
        if num1 == 0:
            num1 = 10
        xcord = (((num1 * 100) - 100) + 217)
        num2 = z // 10
        if z == 10 or z == 20 or z == 30 or z == 40 or z == 50 or z == 60 or z == 70:
            num2 -= 1
        ycord = ((num2 * 100) + 100)
        if States[z] == 9:
            mine_placer(xcord, ycord)
        elif States[z] == 1:
            number1_placer(xcord, ycord)
        elif States[z] == 2:
            number2_placer(xcord, ycord)
        elif States[z] == 3:
            number3_placer(xcord, ycord)
        elif States[z] == 4:
            number4_placer(xcord, ycord)
        elif States[z] == 5:
            number5_placer(xcord, ycord)
        elif States[z] == 6:
            number6_placer(xcord, ycord)
        elif States[z] == 7:
            number7_placer(xcord, ycord)
        elif States[z] == 8:
            number8_placer(xcord, ycord)
        elif States[z] == 0:
            land_placer(xcord, ycord)

    # region Buttons:
    chosen_land = choice(lands)
    print(chosen_land)
    if chosen_land == 1:
        button1 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                         cursor='hand2')
    else:
        button1 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button1.place(x=217, y=100, width=100, height=100)
    if chosen_land == 2:
        button2 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                         cursor='hand2')
    else:
        button2 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button2.place(x=317, y=100, width=100, height=100)
    if chosen_land == 3:
        button3 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                         cursor='hand2')
    else:
        button3 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button3.place(x=417, y=100, width=100, height=100)
    if chosen_land == 4:
        button4 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                         cursor='hand2')
    else:
        button4 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button4.place(x=517, y=100, width=100, height=100)
    if chosen_land == 5:
        button5 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                         cursor='hand2')
    else:
        button5 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button5.place(x=617, y=100, width=100, height=100)
    if chosen_land == 6:
        button6 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                         cursor='hand2')
    else:
        button6 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button6.place(x=717, y=100, width=100, height=100)
    if chosen_land == 7:
        button7 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                         cursor='hand2')
    else:
        button7 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button7.place(x=817, y=100, width=100, height=100)
    if chosen_land == 8:
        button8 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                         cursor='hand2')
    else:
        button8 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button8.place(x=917, y=100, width=100, height=100)
    if chosen_land == 9:
        button9 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                         cursor='hand2')
    else:
        button9 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button9.place(x=1017, y=100, width=100, height=100)
    if chosen_land == 10:
        button10 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button10 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button10.place(x=1117, y=100, width=100, height=100)
    if chosen_land == 11:
        button11 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button11 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button11.place(x=217, y=200, width=100, height=100)
    if chosen_land == 12:
        button12 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button12 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button12.place(x=317, y=200, width=100, height=100)
    if chosen_land == 13:
        button13 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button13 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button13.place(x=417, y=200, width=100, height=100)
    if chosen_land == 14:
        button14 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button14 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button14.place(x=517, y=200, width=100, height=100)
    if chosen_land == 15:
        button15 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button15 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button15.place(x=617, y=200, width=100, height=100)
    if chosen_land == 16:
        button16 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button16 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button16.place(x=717, y=200, width=100, height=100)
    if chosen_land == 17:
        button17 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button17 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button17.place(x=817, y=200, width=100, height=100)
    if chosen_land == 18:
        button18 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button18 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button18.place(x=917, y=200, width=100, height=100)
    if chosen_land == 19:
        button19 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button19 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button19.place(x=1017, y=200, width=100, height=100)
    if chosen_land == 20:
        button20 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button20 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button20.place(x=1117, y=200, width=100, height=100)
    if chosen_land == 21:
        button21 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button21 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button21.place(x=217, y=300, width=100, height=100)
    if chosen_land == 22:
        button22 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button22 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button22.place(x=317, y=300, width=100, height=100)
    if chosen_land == 23:
        button23 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button23 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button23.place(x=417, y=300, width=100, height=100)
    if chosen_land == 24:
        button24 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button24 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button24.place(x=517, y=300, width=100, height=100)
    if chosen_land == 25:
        button25 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button25 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button25.place(x=617, y=300, width=100, height=100)
    if chosen_land == 26:
        button26 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button26 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button26.place(x=717, y=300, width=100, height=100)
    if chosen_land == 27:
        button27 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button27 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button27.place(x=817, y=300, width=100, height=100)
    if chosen_land == 28:
        button28 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button28 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button28.place(x=917, y=300, width=100, height=100)
    if chosen_land == 29:
        button29 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button29 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button29.place(x=1017, y=300, width=100, height=100)
    if chosen_land == 30:
        button30 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button30 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button30.place(x=1117, y=300, width=100, height=100)
    if chosen_land == 31:
        button31 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button31 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button31.place(x=217, y=400, width=100, height=100)
    if chosen_land == 32:
        button32 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button32 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button32.place(x=317, y=400, width=100, height=100)
    if chosen_land == 33:
        button33 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button33 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button33.place(x=417, y=400, width=100, height=100)
    if chosen_land == 34:
        button34 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button34 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button34.place(x=517, y=400, width=100, height=100)
    if chosen_land == 35:
        button35 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button35 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button35.place(x=617, y=400, width=100, height=100)
    if chosen_land == 36:
        button36 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button36 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button36.place(x=717, y=400, width=100, height=100)
    if chosen_land == 37:
        button37 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button37 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button37.place(x=817, y=400, width=100, height=100)
    if chosen_land == 38:
        button38 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button38 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button38.place(x=917, y=400, width=100, height=100)
    if chosen_land == 39:
        button39 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button39 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button39.place(x=1017, y=400, width=100, height=100)
    if chosen_land == 40:
        button40 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button40 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button40.place(x=1117, y=400, width=100, height=100)
    if chosen_land == 41:
        button41 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button41 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button41.place(x=217, y=500, width=100, height=100)
    if chosen_land == 42:
        button42 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button42 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button42.place(x=317, y=500, width=100, height=100)
    if chosen_land == 43:
        button43 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button43 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button43.place(x=417, y=500, width=100, height=100)
    if chosen_land == 44:
        button44 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button44 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button44.place(x=517, y=500, width=100, height=100)
    if chosen_land == 45:
        button45 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button45 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button45.place(x=617, y=500, width=100, height=100)
    if chosen_land == 46:
        button46 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button46 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button46.place(x=717, y=500, width=100, height=100)
    if chosen_land == 47:
        button47 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button47 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button47.place(x=817, y=500, width=100, height=100)
    if chosen_land == 48:
        button48 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button48 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button48.place(x=917, y=500, width=100, height=100)
    if chosen_land == 49:
        button49 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button49 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button49.place(x=1017, y=500, width=100, height=100)
    if chosen_land == 50:
        button50 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button50 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button50.place(x=1117, y=500, width=100, height=100)
    if chosen_land == 51:
        button51 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button51 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button51.place(x=217, y=600, width=100, height=100)
    if chosen_land == 52:
        button52 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button52 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button52.place(x=317, y=600, width=100, height=100)
    if chosen_land == 53:
        button53 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button53 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button53.place(x=417, y=600, width=100, height=100)
    if chosen_land == 54:
        button54 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button54 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button54.place(x=517, y=600, width=100, height=100)
    if chosen_land == 55:
        button55 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button55 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button55.place(x=617, y=600, width=100, height=100)
    if chosen_land == 56:
        button56 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button56 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button56.place(x=717, y=600, width=100, height=100)
    if chosen_land == 57:
        button57 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button57 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button57.place(x=817, y=600, width=100, height=100)
    if chosen_land == 58:
        button58 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button58 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button58.place(x=917, y=600, width=100, height=100)
    if chosen_land == 59:
        button59 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button59 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button59.place(x=1017, y=600, width=100, height=100)
    if chosen_land == 60:
        button60 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button60 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button60.place(x=1117, y=600, width=100, height=100)
    if chosen_land == 61:
        button61 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button61 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button61.place(x=217, y=700, width=100, height=100)
    if chosen_land == 62:
        button62 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button62 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button62.place(x=317, y=700, width=100, height=100)
    if chosen_land == 63:
        button63 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button63 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button63.place(x=417, y=700, width=100, height=100)
    if chosen_land == 64:
        button64 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button64 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button64.place(x=517, y=700, width=100, height=100)
    if chosen_land == 65:
        button65 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button65 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button65.place(x=617, y=700, width=100, height=100)
    if chosen_land == 66:
        button66 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button66 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button66.place(x=717, y=700, width=100, height=100)
    if chosen_land == 67:
        button67 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button67 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button67.place(x=817, y=700, width=100, height=100)
    if chosen_land == 68:
        button68 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button68 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button68.place(x=917, y=700, width=100, height=100)
    if chosen_land == 69:
        button69 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button69 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button69.place(x=1017, y=700, width=100, height=100)
    if chosen_land == 70:
        button70 = Button(Board, text='*', font=('Times New Roman', 125), fg='green', width=20, relief=SOLID,
                          cursor='hand2')
    else:
        button70 = Button(Board, width=20, relief=SOLID, cursor='hand2')
    button70.place(x=1117, y=700, width=100, height=100)

    # endregion
    # endregion

    # region Button Clicks:
    img_flag = PhotoImage(file='Flag.png')

    def Button_1_left():
        button1.destroy()
        WinCheck()
        global States
        global Button_Called
        x = States[1]
        Button_Called[1] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button2.destroy()
            if Flag_Exists[2]:
                Num_Of_Flags -= 1
                Flag_Exists[2] = False
            button11.destroy()
            if Flag_Exists[11]:
                Num_Of_Flags -= 1
                Flag_Exists[11] = False
            button12.destroy()
            if Flag_Exists[12]:
                Num_Of_Flags -= 1
                Flag_Exists[12] = False
            update_mines_left()
            if States[2] == 0 and Button_Called[2] is False:
                Button_2_left()
            if States[11] == 0 and Button_Called[11] is False:
                Button_11_left()

    def click1(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[1]
        if {event.num} == {1} and not x:
            Button_1_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button1.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[1] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button1.config(image="")
                Flag_Exists[1] = False

    button1.bind("<Button>", click1)

    def Button_2_left():
        button2.destroy()
        WinCheck()
        global States
        global Button_Called
        x = States[2]
        Button_Called[2] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button1.destroy()
            if Flag_Exists[1]:
                Num_Of_Flags -= 1
                Flag_Exists[1] = False
            button3.destroy()
            if Flag_Exists[3]:
                Num_Of_Flags -= 1
                Flag_Exists[3] = False
            button11.destroy()
            if Flag_Exists[11]:
                Num_Of_Flags -= 1
                Flag_Exists[11] = False
            button12.destroy()
            if Flag_Exists[12]:
                Num_Of_Flags -= 1
                Flag_Exists[12] = False
            button13.destroy()
            if Flag_Exists[13]:
                Num_Of_Flags -= 1
                Flag_Exists[13] = False
            update_mines_left()
            if States[1] == 0 and Button_Called[1] is False:
                Button_1_left()
            if States[3] == 0 and Button_Called[3] is False:
                Button_3_left()
            if States[12] == 0 and Button_Called[12] is False:
                Button_12_left()

    def click2(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[2]
        if {event.num} == {1} and not x:
            Button_2_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button2.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[2] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button2.config(image="")
                Flag_Exists[2] = False

    button2.bind("<Button>", click2)

    def Button_3_left():
        button3.destroy()
        WinCheck()
        global States
        global Button_Called
        x = States[3]
        Button_Called[3] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button2.destroy()
            if Flag_Exists[2]:
                Num_Of_Flags -= 1
                Flag_Exists[2] = False
            button4.destroy()
            if Flag_Exists[4]:
                Num_Of_Flags -= 1
                Flag_Exists[4] = False
            button12.destroy()
            if Flag_Exists[12]:
                Num_Of_Flags -= 1
                Flag_Exists[12] = False
            button13.destroy()
            if Flag_Exists[13]:
                Num_Of_Flags -= 1
                Flag_Exists[13] = False
            button14.destroy()
            if Flag_Exists[14]:
                Num_Of_Flags -= 1
                Flag_Exists[14] = False
            update_mines_left()
            if States[2] == 0 and Button_Called[2] is False:
                Button_2_left()
            if States[4] == 0 and Button_Called[4] is False:
                Button_4_left()
            if States[13] == 0 and Button_Called[13] is False:
                Button_13_left()

    def click3(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[3]
        if {event.num} == {1} and not x:
            Button_3_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button3.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[3] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button3.config(image="")
                Flag_Exists[3] = False

    button3.bind("<Button>", click3)

    def Button_4_left():
        button4.destroy()
        WinCheck()
        global States
        global Button_Called
        x = States[4]
        Button_Called[4] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button3.destroy()
            if Flag_Exists[3]:
                Num_Of_Flags -= 1
                Flag_Exists[3] = False
            button5.destroy()
            if Flag_Exists[5]:
                Num_Of_Flags -= 1
                Flag_Exists[5] = False
            button13.destroy()
            if Flag_Exists[13]:
                Num_Of_Flags -= 1
                Flag_Exists[13] = False
            button14.destroy()
            if Flag_Exists[14]:
                Num_Of_Flags -= 1
                Flag_Exists[14] = False
            button15.destroy()
            if Flag_Exists[15]:
                Num_Of_Flags -= 1
                Flag_Exists[15] = False
            update_mines_left()
            if States[3] == 0 and Button_Called[3] is False:
                Button_3_left()
            if States[5] == 0 and Button_Called[5] is False:
                Button_5_left()
            if States[14] == 0 and Button_Called[14] is False:
                Button_14_left()

    def click4(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[4]
        if {event.num} == {1} and not x:
            Button_4_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button4.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[4] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button4.config(image="")
                Flag_Exists[4] = False

    button4.bind("<Button>", click4)

    def Button_5_left():
        button5.destroy()
        WinCheck()
        global States
        global Button_Called
        x = States[5]
        Button_Called[5] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button4.destroy()
            if Flag_Exists[4]:
                Num_Of_Flags -= 1
                Flag_Exists[4] = False
            button6.destroy()
            if Flag_Exists[6]:
                Num_Of_Flags -= 1
                Flag_Exists[6] = False
            button14.destroy()
            if Flag_Exists[14]:
                Num_Of_Flags -= 1
                Flag_Exists[14] = False
            button15.destroy()
            if Flag_Exists[15]:
                Num_Of_Flags -= 1
                Flag_Exists[15] = False
            button16.destroy()
            if Flag_Exists[16]:
                Num_Of_Flags -= 1
                Flag_Exists[16] = False
            update_mines_left()
            if States[4] == 0 and Button_Called[4] is False:
                Button_4_left()
            if States[6] == 0 and Button_Called[6] is False:
                Button_6_left()
            if States[15] == 0 and Button_Called[15] is False:
                Button_15_left()

    def click5(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[5]
        if {event.num} == {1} and not x:
            Button_5_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button5.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[5] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button5.config(image="")
                Flag_Exists[5] = False

    button5.bind("<Button>", click5)

    def Button_6_left():
        button6.destroy()
        WinCheck()
        global States
        global Button_Called
        x = States[6]
        Button_Called[6] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button5.destroy()
            if Flag_Exists[5]:
                Num_Of_Flags -= 1
                Flag_Exists[5] = False
            button7.destroy()
            if Flag_Exists[7]:
                Num_Of_Flags -= 1
                Flag_Exists[7] = False
            button15.destroy()
            if Flag_Exists[15]:
                Num_Of_Flags -= 1
                Flag_Exists[15] = False
            button16.destroy()
            if Flag_Exists[16]:
                Num_Of_Flags -= 1
                Flag_Exists[16] = False
            button17.destroy()
            if Flag_Exists[17]:
                Num_Of_Flags -= 1
                Flag_Exists[17] = False
            update_mines_left()
            if States[5] == 0 and Button_Called[5] is False:
                Button_5_left()
            if States[7] == 0 and Button_Called[7] is False:
                Button_7_left()
            if States[16] == 0 and Button_Called[16] is False:
                Button_16_left()

    def click6(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[6]
        if {event.num} == {1} and not x:
            Button_6_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button6.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[6] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button6.config(image="")
                Flag_Exists[6] = False

    button6.bind("<Button>", click6)

    def Button_7_left():
        button7.destroy()
        WinCheck()
        global States
        global Button_Called
        x = States[7]
        Button_Called[7] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button6.destroy()
            if Flag_Exists[6]:
                Num_Of_Flags -= 1
                Flag_Exists[6] = False
            button8.destroy()
            if Flag_Exists[8]:
                Num_Of_Flags -= 1
                Flag_Exists[8] = False
            button16.destroy()
            if Flag_Exists[16]:
                Num_Of_Flags -= 1
                Flag_Exists[16] = False
            button17.destroy()
            if Flag_Exists[17]:
                Num_Of_Flags -= 1
                Flag_Exists[17] = False
            button18.destroy()
            if Flag_Exists[18]:
                Num_Of_Flags -= 1
                Flag_Exists[18] = False
            update_mines_left()
            if States[6] == 0 and Button_Called[6] is False:
                Button_6_left()
            if States[8] == 0 and Button_Called[8] is False:
                Button_8_left()
            if States[17] == 0 and Button_Called[17] is False:
                Button_17_left()

    def click7(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[7]
        if {event.num} == {1} and not x:
            Button_7_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button7.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[7] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button7.config(image="")
                Flag_Exists[7] = False

    button7.bind("<Button>", click7)

    def Button_8_left():
        button8.destroy()
        WinCheck()
        global States
        global Button_Called
        x = States[8]
        Button_Called[8] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button7.destroy()
            if Flag_Exists[7]:
                Num_Of_Flags -= 1
                Flag_Exists[7] = False
            button9.destroy()
            if Flag_Exists[9]:
                Num_Of_Flags -= 1
                Flag_Exists[9] = False
            button17.destroy()
            if Flag_Exists[17]:
                Num_Of_Flags -= 1
                Flag_Exists[17] = False
            button18.destroy()
            if Flag_Exists[18]:
                Num_Of_Flags -= 1
                Flag_Exists[18] = False
            button19.destroy()
            if Flag_Exists[19]:
                Num_Of_Flags -= 1
                Flag_Exists[19] = False
            update_mines_left()
            if States[7] == 0 and Button_Called[7] is False:
                Button_7_left()
            if States[9] == 0 and Button_Called[9] is False:
                Button_9_left()
            if States[18] == 0 and Button_Called[18] is False:
                Button_18_left()

    def click8(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[8]
        if {event.num} == {1} and not x:
            Button_8_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button8.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[8] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button8.config(image="")
                Flag_Exists[8] = False

    button8.bind("<Button>", click8)

    def Button_9_left():
        button9.destroy()
        WinCheck()
        global States
        global Button_Called
        x = States[9]
        Button_Called[9] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button8.destroy()
            if Flag_Exists[8]:
                Num_Of_Flags -= 1
                Flag_Exists[8] = False
            button10.destroy()
            if Flag_Exists[10]:
                Num_Of_Flags -= 1
                Flag_Exists[10] = False
            button18.destroy()
            if Flag_Exists[18]:
                Num_Of_Flags -= 1
                Flag_Exists[18] = False
            button19.destroy()
            if Flag_Exists[19]:
                Num_Of_Flags -= 1
                Flag_Exists[19] = False
            button20.destroy()
            if Flag_Exists[20]:
                Num_Of_Flags -= 1
                Flag_Exists[20] = False
            update_mines_left()
            if States[8] == 0 and Button_Called[8] is False:
                Button_8_left()
            if States[10] == 0 and Button_Called[10] is False:
                Button_10_left()
            if States[19] == 0 and Button_Called[19] is False:
                Button_19_left()

    def click9(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[9]
        if {event.num} == {1} and not x:
            Button_9_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button9.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[9] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button9.config(image="")
                Flag_Exists[9] = False

    button9.bind("<Button>", click9)

    def Button_10_left():
        button10.destroy()
        WinCheck()
        global States
        global Button_Called
        x = States[10]
        Button_Called[10] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button9.destroy()
            if Flag_Exists[9]:
                Num_Of_Flags -= 1
                Flag_Exists[9] = False
            button19.destroy()
            if Flag_Exists[19]:
                Num_Of_Flags -= 1
                Flag_Exists[19] = False
            button20.destroy()
            if Flag_Exists[20]:
                Num_Of_Flags -= 1
                Flag_Exists[20] = False
            update_mines_left()
            if States[9] == 0 and Button_Called[9] is False:
                Button_9_left()
            if States[20] == 0 and Button_Called[20] is False:
                Button_20_left()

    def click10(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[10]
        if {event.num} == {1} and not x:
            Button_10_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button10.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[10] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button10.config(image="")
                Flag_Exists[10] = False

    button10.bind("<Button>", click10)

    def Button_11_left():
        button11.destroy()
        WinCheck()
        global States
        global Button_Called
        x = States[11]
        Button_Called[11] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button1.destroy()
            if Flag_Exists[1]:
                Num_Of_Flags -= 1
                Flag_Exists[1] = False
            button2.destroy()
            if Flag_Exists[2]:
                Num_Of_Flags -= 1
                Flag_Exists[2] = False
            button12.destroy()
            if Flag_Exists[12]:
                Num_Of_Flags -= 1
                Flag_Exists[12] = False
            button21.destroy()
            if Flag_Exists[21]:
                Num_Of_Flags -= 1
                Flag_Exists[1] = False
            button22.destroy()
            if Flag_Exists[22]:
                Num_Of_Flags -= 1
                Flag_Exists[22] = False
            update_mines_left()
            if States[1] == 0 and Button_Called[1] is False:
                Button_1_left()
            if States[21] == 0 and Button_Called[21] is False:
                Button_21_left()
            if States[12] == 0 and Button_Called[12] is False:
                Button_12_left()

    def click11(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[11]
        if {event.num} == {1} and not x:
            Button_11_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button11.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[11] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button11.config(image="")
                Flag_Exists[11] = False

    button11.bind("<Button>", click11)

    def Button_12_left():
        button12.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[12]
        Button_Called[12] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button1.destroy()
            if Flag_Exists[1]:
                Num_Of_Flags -= 1
                Flag_Exists[1] = False
            button2.destroy()
            if Flag_Exists[2]:
                Num_Of_Flags -= 1
                Flag_Exists[2] = False
            button3.destroy()
            if Flag_Exists[3]:
                Num_Of_Flags -= 1
                Flag_Exists[3] = False
            button11.destroy()
            if Flag_Exists[11]:
                Num_Of_Flags -= 1
                Flag_Exists[11] = False
            button13.destroy()
            if Flag_Exists[13]:
                Num_Of_Flags -= 1
                Flag_Exists[13] = False
            button21.destroy()
            if Flag_Exists[21]:
                Num_Of_Flags -= 1
                Flag_Exists[21] = False
            button22.destroy()
            if Flag_Exists[22]:
                Num_Of_Flags -= 1
                Flag_Exists[22] = False
            button23.destroy()
            if Flag_Exists[23]:
                Num_Of_Flags -= 1
                Flag_Exists[23] = False
            update_mines_left()
            if States[2] == 0 and Button_Called[2] is False:
                Button_2_left()
            if States[11] == 0 and Button_Called[11] is False:
                Button_11_left()
            if States[13] == 0 and Button_Called[13] is False:
                Button_13_left()
            if States[22] == 0 and Button_Called[22] is False:
                Button_22_left()

    def click12(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[12]
        if {event.num} == {1} and not x:
            Button_12_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button12.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[12] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button12.config(image="")
                Flag_Exists[12] = False

    button12.bind("<Button>", click12)

    def Button_13_left():
        button13.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[13]
        Button_Called[13] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button2.destroy()
            if Flag_Exists[2]:
                Num_Of_Flags -= 1
                Flag_Exists[2] = False
            button3.destroy()
            if Flag_Exists[3]:
                Num_Of_Flags -= 1
                Flag_Exists[3] = False
            button4.destroy()
            if Flag_Exists[4]:
                Num_Of_Flags -= 1
                Flag_Exists[4] = False
            button12.destroy()
            if Flag_Exists[12]:
                Num_Of_Flags -= 1
                Flag_Exists[12] = False
            button14.destroy()
            if Flag_Exists[14]:
                Num_Of_Flags -= 1
                Flag_Exists[14] = False
            button22.destroy()
            if Flag_Exists[22]:
                Num_Of_Flags -= 1
                Flag_Exists[22] = False
            button23.destroy()
            if Flag_Exists[23]:
                Num_Of_Flags -= 1
                Flag_Exists[23] = False
            button24.destroy()
            if Flag_Exists[24]:
                Num_Of_Flags -= 1
                Flag_Exists[24] = False
            update_mines_left()
            if States[3] == 0 and Button_Called[3] is False:
                Button_3_left()
            if States[12] == 0 and Button_Called[12] is False:
                Button_12_left()
            if States[14] == 0 and Button_Called[14] is False:
                Button_14_left()
            if States[23] == 0 and Button_Called[23] is False:
                Button_23_left()

    def click13(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[13]
        if {event.num} == {1} and not x:
            Button_13_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button13.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[13] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button13.config(image="")
                Flag_Exists[13] = False

    button13.bind("<Button>", click13)

    def Button_14_left():
        button14.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[14]
        Button_Called[14] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button3.destroy()
            if Flag_Exists[3]:
                Num_Of_Flags -= 1
                Flag_Exists[3] = False
            button4.destroy()
            if Flag_Exists[4]:
                Num_Of_Flags -= 1
                Flag_Exists[4] = False
            button5.destroy()
            if Flag_Exists[5]:
                Num_Of_Flags -= 1
                Flag_Exists[5] = False
            button13.destroy()
            if Flag_Exists[13]:
                Num_Of_Flags -= 1
                Flag_Exists[13] = False
            button15.destroy()
            if Flag_Exists[15]:
                Num_Of_Flags -= 1
                Flag_Exists[15] = False
            button23.destroy()
            if Flag_Exists[23]:
                Num_Of_Flags -= 1
                Flag_Exists[23] = False
            button24.destroy()
            if Flag_Exists[24]:
                Num_Of_Flags -= 1
                Flag_Exists[24] = False
            button25.destroy()
            if Flag_Exists[25]:
                Num_Of_Flags -= 1
                Flag_Exists[25] = False
            update_mines_left()
            if States[4] == 0 and Button_Called[4] is False:
                Button_4_left()
            if States[13] == 0 and Button_Called[13] is False:
                Button_13_left()
            if States[15] == 0 and Button_Called[15] is False:
                Button_15_left()
            if States[24] == 0 and Button_Called[24] is False:
                Button_24_left()

    def click14(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[14]
        if {event.num} == {1} and not x:
            Button_14_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button14.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[14] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button14.config(image="")
                Flag_Exists[14] = False

    button14.bind("<Button>", click14)

    def Button_15_left():
        button15.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[15]
        Button_Called[15] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button4.destroy()
            if Flag_Exists[4]:
                Num_Of_Flags -= 1
                Flag_Exists[4] = False
            button5.destroy()
            if Flag_Exists[5]:
                Num_Of_Flags -= 1
                Flag_Exists[5] = False
            button6.destroy()
            if Flag_Exists[6]:
                Num_Of_Flags -= 1
                Flag_Exists[6] = False
            button14.destroy()
            if Flag_Exists[14]:
                Num_Of_Flags -= 1
                Flag_Exists[14] = False
            button16.destroy()
            if Flag_Exists[16]:
                Num_Of_Flags -= 1
                Flag_Exists[16] = False
            button24.destroy()
            if Flag_Exists[24]:
                Num_Of_Flags -= 1
                Flag_Exists[24] = False
            button25.destroy()
            if Flag_Exists[25]:
                Num_Of_Flags -= 1
                Flag_Exists[25] = False
            button26.destroy()
            if Flag_Exists[26]:
                Num_Of_Flags -= 1
                Flag_Exists[26] = False
            update_mines_left()
            if States[5] == 0 and Button_Called[5] is False:
                Button_5_left()
            if States[14] == 0 and Button_Called[14] is False:
                Button_14_left()
            if States[16] == 0 and Button_Called[16] is False:
                Button_16_left()
            if States[25] == 0 and Button_Called[25] is False:
                Button_25_left()

    def click15(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[15]
        if {event.num} == {1} and not x:
            Button_15_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button15.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[15] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button15.config(image="")
                Flag_Exists[15] = False

    button15.bind("<Button>", click15)

    def Button_16_left():
        button16.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[16]
        Button_Called[16] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button5.destroy()
            if Flag_Exists[5]:
                Num_Of_Flags -= 1
                Flag_Exists[5] = False
            button6.destroy()
            if Flag_Exists[6]:
                Num_Of_Flags -= 1
                Flag_Exists[6] = False
            button7.destroy()
            if Flag_Exists[7]:
                Num_Of_Flags -= 1
                Flag_Exists[7] = False
            button15.destroy()
            if Flag_Exists[15]:
                Num_Of_Flags -= 1
                Flag_Exists[15] = False
            button17.destroy()
            if Flag_Exists[17]:
                Num_Of_Flags -= 1
                Flag_Exists[17] = False
            button25.destroy()
            if Flag_Exists[25]:
                Num_Of_Flags -= 1
                Flag_Exists[25] = False
            button26.destroy()
            if Flag_Exists[26]:
                Num_Of_Flags -= 1
                Flag_Exists[26] = False
            button27.destroy()
            if Flag_Exists[27]:
                Num_Of_Flags -= 1
                Flag_Exists[27] = False
            update_mines_left()
            if States[6] == 0 and Button_Called[6] is False:
                Button_6_left()
            if States[15] == 0 and Button_Called[15] is False:
                Button_15_left()
            if States[17] == 0 and Button_Called[17] is False:
                Button_17_left()
            if States[26] == 0 and Button_Called[26] is False:
                Button_26_left()

    def click16(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[16]
        if {event.num} == {1} and not x:
            Button_16_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button16.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[16] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button16.config(image="")
                Flag_Exists[16] = False

    button16.bind("<Button>", click16)

    def Button_17_left():
        button17.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[17]
        Button_Called[17] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button6.destroy()
            if Flag_Exists[6]:
                Num_Of_Flags -= 1
                Flag_Exists[6] = False
            button7.destroy()
            if Flag_Exists[7]:
                Num_Of_Flags -= 1
                Flag_Exists[7] = False
            button8.destroy()
            if Flag_Exists[8]:
                Num_Of_Flags -= 1
                Flag_Exists[8] = False
            button16.destroy()
            if Flag_Exists[16]:
                Num_Of_Flags -= 1
                Flag_Exists[16] = False
            button18.destroy()
            if Flag_Exists[18]:
                Num_Of_Flags -= 1
                Flag_Exists[18] = False
            button26.destroy()
            if Flag_Exists[26]:
                Num_Of_Flags -= 1
                Flag_Exists[26] = False
            button27.destroy()
            if Flag_Exists[27]:
                Num_Of_Flags -= 1
                Flag_Exists[27] = False
            button28.destroy()
            if Flag_Exists[28]:
                Num_Of_Flags -= 1
                Flag_Exists[28] = False
            update_mines_left()
            if States[7] == 0 and Button_Called[7] is False:
                Button_7_left()
            if States[16] == 0 and Button_Called[16] is False:
                Button_16_left()
            if States[18] == 0 and Button_Called[18] is False:
                Button_18_left()
            if States[27] == 0 and Button_Called[27] is False:
                Button_27_left()

    def click17(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[17]
        if {event.num} == {1} and not x:
            Button_17_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button17.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[17] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button17.config(image="")
                Flag_Exists[17] = False

    button17.bind("<Button>", click17)

    def Button_18_left():
        button18.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[18]
        Button_Called[18] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button7.destroy()
            if Flag_Exists[7]:
                Num_Of_Flags -= 1
                Flag_Exists[7] = False
            button8.destroy()
            if Flag_Exists[8]:
                Num_Of_Flags -= 1
                Flag_Exists[8] = False
            button9.destroy()
            if Flag_Exists[9]:
                Num_Of_Flags -= 1
                Flag_Exists[9] = False
            button17.destroy()
            if Flag_Exists[17]:
                Num_Of_Flags -= 1
                Flag_Exists[17] = False
            button19.destroy()
            if Flag_Exists[19]:
                Num_Of_Flags -= 1
                Flag_Exists[19] = False
            button27.destroy()
            if Flag_Exists[27]:
                Num_Of_Flags -= 1
                Flag_Exists[27] = False
            button28.destroy()
            if Flag_Exists[28]:
                Num_Of_Flags -= 1
                Flag_Exists[28] = False
            button29.destroy()
            if Flag_Exists[29]:
                Num_Of_Flags -= 1
                Flag_Exists[29] = False
            update_mines_left()
            if States[8] == 0 and Button_Called[8] is False:
                Button_8_left()
            if States[17] == 0 and Button_Called[17] is False:
                Button_17_left()
            if States[19] == 0 and Button_Called[19] is False:
                Button_19_left()
            if States[28] == 0 and Button_Called[28] is False:
                Button_28_left()

    def click18(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[18]
        if {event.num} == {1} and not x:
            Button_18_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button18.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[18] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button18.config(image="")
                Flag_Exists[18] = False

    button18.bind("<Button>", click18)

    def Button_19_left():
        button19.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[19]
        Button_Called[19] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button8.destroy()
            if Flag_Exists[8]:
                Num_Of_Flags -= 1
                Flag_Exists[8] = False
            button9.destroy()
            if Flag_Exists[9]:
                Num_Of_Flags -= 1
                Flag_Exists[9] = False
            button10.destroy()
            if Flag_Exists[10]:
                Num_Of_Flags -= 1
                Flag_Exists[10] = False
            button18.destroy()
            if Flag_Exists[18]:
                Num_Of_Flags -= 1
                Flag_Exists[18] = False
            button20.destroy()
            if Flag_Exists[20]:
                Num_Of_Flags -= 1
                Flag_Exists[20] = False
            button28.destroy()
            if Flag_Exists[28]:
                Num_Of_Flags -= 1
                Flag_Exists[28] = False
            button29.destroy()
            if Flag_Exists[29]:
                Num_Of_Flags -= 1
                Flag_Exists[29] = False
            button30.destroy()
            if Flag_Exists[30]:
                Num_Of_Flags -= 1
                Flag_Exists[30] = False
            update_mines_left()
            if States[9] == 0 and Button_Called[9] is False:
                Button_9_left()
            if States[18] == 0 and Button_Called[18] is False:
                Button_18_left()
            if States[20] == 0 and Button_Called[20] is False:
                Button_20_left()
            if States[29] == 0 and Button_Called[29] is False:
                Button_29_left()

    def click19(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[19]
        if {event.num} == {1} and not x:
            Button_19_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button19.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[19] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button19.config(image="")
                Flag_Exists[19] = False

    button19.bind("<Button>", click19)

    def Button_20_left():
        button20.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[20]
        Button_Called[20] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button9.destroy()
            if Flag_Exists[9]:
                Num_Of_Flags -= 1
                Flag_Exists[9] = False
            button10.destroy()
            if Flag_Exists[10]:
                Num_Of_Flags -= 1
                Flag_Exists[10] = False
            button19.destroy()
            if Flag_Exists[19]:
                Num_Of_Flags -= 1
                Flag_Exists[19] = False
            button29.destroy()
            if Flag_Exists[29]:
                Num_Of_Flags -= 1
                Flag_Exists[29] = False
            button30.destroy()
            if Flag_Exists[30]:
                Num_Of_Flags -= 1
                Flag_Exists[30] = False
            update_mines_left()
            if States[10] == 0 and Button_Called[10] is False:
                Button_10_left()
            if States[19] == 0 and Button_Called[19] is False:
                Button_19_left()
            if States[30] == 0 and Button_Called[30] is False:
                Button_30_left()

    def click20(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[20]
        if {event.num} == {1} and not x:
            Button_20_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button20.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[20] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button20.config(image="")
                Flag_Exists[20] = False

    button20.bind("<Button>", click20)

    def Button_21_left():
        button21.destroy()
        WinCheck()
        global States
        global Button_Called
        x = States[21]
        Button_Called[21] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button11.destroy()
            if Flag_Exists[11]:
                Num_Of_Flags -= 1
                Flag_Exists[11] = False
            button12.destroy()
            if Flag_Exists[12]:
                Num_Of_Flags -= 1
                Flag_Exists[12] = False
            button22.destroy()
            if Flag_Exists[22]:
                Num_Of_Flags -= 1
                Flag_Exists[22] = False
            button31.destroy()
            if Flag_Exists[31]:
                Num_Of_Flags -= 1
                Flag_Exists[11] = False
            button32.destroy()
            if Flag_Exists[32]:
                Num_Of_Flags -= 1
                Flag_Exists[32] = False
            update_mines_left()
            if States[11] == 0 and Button_Called[11] is False:
                Button_11_left()
            if States[31] == 0 and Button_Called[31] is False:
                Button_31_left()
            if States[22] == 0 and Button_Called[22] is False:
                Button_22_left()

    def click21(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[21]
        if {event.num} == {1} and not x:
            Button_21_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button21.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[21] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button21.config(image="")
                Flag_Exists[21] = False

    button21.bind("<Button>", click21)

    def Button_22_left():
        button22.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[22]
        Button_Called[22] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button11.destroy()
            if Flag_Exists[11]:
                Num_Of_Flags -= 1
                Flag_Exists[11] = False
            button12.destroy()
            if Flag_Exists[12]:
                Num_Of_Flags -= 1
                Flag_Exists[12] = False
            button13.destroy()
            if Flag_Exists[13]:
                Num_Of_Flags -= 1
                Flag_Exists[13] = False
            button21.destroy()
            if Flag_Exists[21]:
                Num_Of_Flags -= 1
                Flag_Exists[21] = False
            button23.destroy()
            if Flag_Exists[23]:
                Num_Of_Flags -= 1
                Flag_Exists[23] = False
            button31.destroy()
            if Flag_Exists[31]:
                Num_Of_Flags -= 1
                Flag_Exists[31] = False
            button32.destroy()
            if Flag_Exists[32]:
                Num_Of_Flags -= 1
                Flag_Exists[32] = False
            button33.destroy()
            if Flag_Exists[33]:
                Num_Of_Flags -= 1
                Flag_Exists[33] = False
            update_mines_left()
            if States[12] == 0 and Button_Called[12] is False:
                Button_12_left()
            if States[21] == 0 and Button_Called[21] is False:
                Button_21_left()
            if States[23] == 0 and Button_Called[23] is False:
                Button_23_left()
            if States[32] == 0 and Button_Called[32] is False:
                Button_32_left()

    def click22(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[22]
        if {event.num} == {1} and not x:
            Button_22_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button22.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[22] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button22.config(image="")
                Flag_Exists[22] = False

    button22.bind("<Button>", click22)

    def Button_23_left():
        button23.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[23]
        Button_Called[23] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button12.destroy()
            if Flag_Exists[12]:
                Num_Of_Flags -= 1
                Flag_Exists[12] = False
            button13.destroy()
            if Flag_Exists[13]:
                Num_Of_Flags -= 1
                Flag_Exists[13] = False
            button14.destroy()
            if Flag_Exists[14]:
                Num_Of_Flags -= 1
                Flag_Exists[14] = False
            button22.destroy()
            if Flag_Exists[22]:
                Num_Of_Flags -= 1
                Flag_Exists[22] = False
            button24.destroy()
            if Flag_Exists[24]:
                Num_Of_Flags -= 1
                Flag_Exists[24] = False
            button32.destroy()
            if Flag_Exists[32]:
                Num_Of_Flags -= 1
                Flag_Exists[32] = False
            button33.destroy()
            if Flag_Exists[33]:
                Num_Of_Flags -= 1
                Flag_Exists[33] = False
            button34.destroy()
            if Flag_Exists[34]:
                Num_Of_Flags -= 1
                Flag_Exists[34] = False
            update_mines_left()
            if States[13] == 0 and Button_Called[13] is False:
                Button_13_left()
            if States[22] == 0 and Button_Called[22] is False:
                Button_22_left()
            if States[24] == 0 and Button_Called[24] is False:
                Button_24_left()
            if States[33] == 0 and Button_Called[33] is False:
                Button_33_left()

    def click23(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[23]
        if {event.num} == {1} and not x:
            Button_23_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button23.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[23] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button23.config(image="")
                Flag_Exists[23] = False

    button23.bind("<Button>", click23)

    def Button_24_left():
        button24.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[24]
        Button_Called[24] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button13.destroy()
            if Flag_Exists[13]:
                Num_Of_Flags -= 1
                Flag_Exists[13] = False
            button14.destroy()
            if Flag_Exists[14]:
                Num_Of_Flags -= 1
                Flag_Exists[14] = False
            button15.destroy()
            if Flag_Exists[15]:
                Num_Of_Flags -= 1
                Flag_Exists[15] = False
            button23.destroy()
            if Flag_Exists[23]:
                Num_Of_Flags -= 1
                Flag_Exists[23] = False
            button25.destroy()
            if Flag_Exists[25]:
                Num_Of_Flags -= 1
                Flag_Exists[25] = False
            button33.destroy()
            if Flag_Exists[33]:
                Num_Of_Flags -= 1
                Flag_Exists[33] = False
            button34.destroy()
            if Flag_Exists[34]:
                Num_Of_Flags -= 1
                Flag_Exists[34] = False
            button35.destroy()
            if Flag_Exists[35]:
                Num_Of_Flags -= 1
                Flag_Exists[35] = False
            update_mines_left()
            if States[14] == 0 and Button_Called[14] is False:
                Button_14_left()
            if States[23] == 0 and Button_Called[23] is False:
                Button_23_left()
            if States[25] == 0 and Button_Called[25] is False:
                Button_25_left()
            if States[34] == 0 and Button_Called[34] is False:
                Button_34_left()

    def click24(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[24]
        if {event.num} == {1} and not x:
            Button_24_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button24.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[24] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button24.config(image="")
                Flag_Exists[24] = False

    button24.bind("<Button>", click24)

    def Button_25_left():
        button25.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[25]
        Button_Called[25] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button14.destroy()
            if Flag_Exists[14]:
                Num_Of_Flags -= 1
                Flag_Exists[14] = False
            button15.destroy()
            if Flag_Exists[15]:
                Num_Of_Flags -= 1
                Flag_Exists[15] = False
            button16.destroy()
            if Flag_Exists[16]:
                Num_Of_Flags -= 1
                Flag_Exists[16] = False
            button24.destroy()
            if Flag_Exists[24]:
                Num_Of_Flags -= 1
                Flag_Exists[24] = False
            button26.destroy()
            if Flag_Exists[26]:
                Num_Of_Flags -= 1
                Flag_Exists[26] = False
            button34.destroy()
            if Flag_Exists[34]:
                Num_Of_Flags -= 1
                Flag_Exists[34] = False
            button35.destroy()
            if Flag_Exists[35]:
                Num_Of_Flags -= 1
                Flag_Exists[35] = False
            button36.destroy()
            if Flag_Exists[36]:
                Num_Of_Flags -= 1
                Flag_Exists[36] = False
            update_mines_left()
            if States[15] == 0 and Button_Called[15] is False:
                Button_15_left()
            if States[24] == 0 and Button_Called[24] is False:
                Button_24_left()
            if States[26] == 0 and Button_Called[26] is False:
                Button_26_left()
            if States[35] == 0 and Button_Called[35] is False:
                Button_35_left()

    def click25(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[25]
        if {event.num} == {1} and not x:
            Button_25_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button25.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[25] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button25.config(image="")
                Flag_Exists[25] = False

    button25.bind("<Button>", click25)

    def Button_26_left():
        button26.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[26]
        Button_Called[26] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button15.destroy()
            if Flag_Exists[15]:
                Num_Of_Flags -= 1
                Flag_Exists[15] = False
            button16.destroy()
            if Flag_Exists[16]:
                Num_Of_Flags -= 1
                Flag_Exists[16] = False
            button17.destroy()
            if Flag_Exists[17]:
                Num_Of_Flags -= 1
                Flag_Exists[17] = False
            button25.destroy()
            if Flag_Exists[25]:
                Num_Of_Flags -= 1
                Flag_Exists[25] = False
            button27.destroy()
            if Flag_Exists[27]:
                Num_Of_Flags -= 1
                Flag_Exists[27] = False
            button35.destroy()
            if Flag_Exists[35]:
                Num_Of_Flags -= 1
                Flag_Exists[35] = False
            button36.destroy()
            if Flag_Exists[36]:
                Num_Of_Flags -= 1
                Flag_Exists[36] = False
            button37.destroy()
            if Flag_Exists[37]:
                Num_Of_Flags -= 1
                Flag_Exists[37] = False
            update_mines_left()
            if States[16] == 0 and Button_Called[16] is False:
                Button_16_left()
            if States[25] == 0 and Button_Called[25] is False:
                Button_25_left()
            if States[27] == 0 and Button_Called[27] is False:
                Button_27_left()
            if States[36] == 0 and Button_Called[36] is False:
                Button_36_left()

    def click26(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[26]
        if {event.num} == {1} and not x:
            Button_26_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button26.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[26] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button26.config(image="")
                Flag_Exists[26] = False

    button26.bind("<Button>", click26)

    def Button_27_left():
        button27.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[27]
        Button_Called[27] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button16.destroy()
            if Flag_Exists[16]:
                Num_Of_Flags -= 1
                Flag_Exists[16] = False
            button17.destroy()
            if Flag_Exists[17]:
                Num_Of_Flags -= 1
                Flag_Exists[17] = False
            button18.destroy()
            if Flag_Exists[18]:
                Num_Of_Flags -= 1
                Flag_Exists[18] = False
            button26.destroy()
            if Flag_Exists[26]:
                Num_Of_Flags -= 1
                Flag_Exists[26] = False
            button28.destroy()
            if Flag_Exists[28]:
                Num_Of_Flags -= 1
                Flag_Exists[28] = False
            button36.destroy()
            if Flag_Exists[36]:
                Num_Of_Flags -= 1
                Flag_Exists[36] = False
            button37.destroy()
            if Flag_Exists[37]:
                Num_Of_Flags -= 1
                Flag_Exists[37] = False
            button38.destroy()
            if Flag_Exists[38]:
                Num_Of_Flags -= 1
                Flag_Exists[38] = False
            update_mines_left()
            if States[17] == 0 and Button_Called[17] is False:
                Button_17_left()
            if States[26] == 0 and Button_Called[26] is False:
                Button_26_left()
            if States[28] == 0 and Button_Called[28] is False:
                Button_28_left()
            if States[37] == 0 and Button_Called[37] is False:
                Button_37_left()

    def click27(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[27]
        if {event.num} == {1} and not x:
            Button_27_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button27.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[27] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button27.config(image="")
                Flag_Exists[27] = False

    button27.bind("<Button>", click27)

    def Button_28_left():
        button28.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[28]
        Button_Called[28] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button17.destroy()
            if Flag_Exists[17]:
                Num_Of_Flags -= 1
                Flag_Exists[17] = False
            button18.destroy()
            if Flag_Exists[18]:
                Num_Of_Flags -= 1
                Flag_Exists[18] = False
            button19.destroy()
            if Flag_Exists[19]:
                Num_Of_Flags -= 1
                Flag_Exists[19] = False
            button27.destroy()
            if Flag_Exists[27]:
                Num_Of_Flags -= 1
                Flag_Exists[27] = False
            button29.destroy()
            if Flag_Exists[29]:
                Num_Of_Flags -= 1
                Flag_Exists[29] = False
            button37.destroy()
            if Flag_Exists[37]:
                Num_Of_Flags -= 1
                Flag_Exists[37] = False
            button38.destroy()
            if Flag_Exists[38]:
                Num_Of_Flags -= 1
                Flag_Exists[38] = False
            button39.destroy()
            if Flag_Exists[39]:
                Num_Of_Flags -= 1
                Flag_Exists[39] = False
            update_mines_left()
            if States[18] == 0 and Button_Called[18] is False:
                Button_18_left()
            if States[27] == 0 and Button_Called[27] is False:
                Button_27_left()
            if States[29] == 0 and Button_Called[29] is False:
                Button_29_left()
            if States[38] == 0 and Button_Called[38] is False:
                Button_38_left()

    def click28(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[28]
        if {event.num} == {1} and not x:
            Button_28_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button28.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[28] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button28.config(image="")
                Flag_Exists[28] = False

    button28.bind("<Button>", click28)

    def Button_29_left():
        button29.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[29]
        Button_Called[29] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button18.destroy()
            if Flag_Exists[18]:
                Num_Of_Flags -= 1
                Flag_Exists[18] = False
            button19.destroy()
            if Flag_Exists[19]:
                Num_Of_Flags -= 1
                Flag_Exists[19] = False
            button20.destroy()
            if Flag_Exists[20]:
                Num_Of_Flags -= 1
                Flag_Exists[20] = False
            button28.destroy()
            if Flag_Exists[28]:
                Num_Of_Flags -= 1
                Flag_Exists[28] = False
            button30.destroy()
            if Flag_Exists[30]:
                Num_Of_Flags -= 1
                Flag_Exists[30] = False
            button38.destroy()
            if Flag_Exists[38]:
                Num_Of_Flags -= 1
                Flag_Exists[38] = False
            button39.destroy()
            if Flag_Exists[39]:
                Num_Of_Flags -= 1
                Flag_Exists[39] = False
            button40.destroy()
            if Flag_Exists[40]:
                Num_Of_Flags -= 1
                Flag_Exists[40] = False
            update_mines_left()
            if States[19] == 0 and Button_Called[19] is False:
                Button_19_left()
            if States[28] == 0 and Button_Called[28] is False:
                Button_28_left()
            if States[30] == 0 and Button_Called[30] is False:
                Button_30_left()
            if States[39] == 0 and Button_Called[39] is False:
                Button_39_left()

    def click29(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[29]
        if {event.num} == {1} and not x:
            Button_29_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button29.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[29] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button29.config(image="")
                Flag_Exists[29] = False

    button29.bind("<Button>", click29)

    def Button_30_left():
        button30.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[30]
        Button_Called[30] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button19.destroy()
            if Flag_Exists[19]:
                Num_Of_Flags -= 1
                Flag_Exists[19] = False
            button20.destroy()
            if Flag_Exists[20]:
                Num_Of_Flags -= 1
                Flag_Exists[20] = False
            button29.destroy()
            if Flag_Exists[29]:
                Num_Of_Flags -= 1
                Flag_Exists[29] = False
            button39.destroy()
            if Flag_Exists[39]:
                Num_Of_Flags -= 1
                Flag_Exists[39] = False
            button40.destroy()
            if Flag_Exists[40]:
                Num_Of_Flags -= 1
                Flag_Exists[40] = False
            update_mines_left()
            if States[20] == 0 and Button_Called[20] is False:
                Button_20_left()
            if States[29] == 0 and Button_Called[29] is False:
                Button_29_left()
            if States[40] == 0 and Button_Called[40] is False:
                Button_40_left()

    def click30(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[30]
        if {event.num} == {1} and not x:
            Button_30_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button30.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[30] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button30.config(image="")
                Flag_Exists[30] = False

    button30.bind("<Button>", click30)

    def Button_31_left():
        button31.destroy()
        WinCheck()
        global States
        global Button_Called
        x = States[31]
        Button_Called[31] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button21.destroy()
            if Flag_Exists[21]:
                Num_Of_Flags -= 1
                Flag_Exists[21] = False
            button22.destroy()
            if Flag_Exists[22]:
                Num_Of_Flags -= 1
                Flag_Exists[22] = False
            button32.destroy()
            if Flag_Exists[32]:
                Num_Of_Flags -= 1
                Flag_Exists[32] = False
            button41.destroy()
            if Flag_Exists[41]:
                Num_Of_Flags -= 1
                Flag_Exists[21] = False
            button42.destroy()
            if Flag_Exists[42]:
                Num_Of_Flags -= 1
                Flag_Exists[42] = False
            update_mines_left()
            if States[21] == 0 and Button_Called[21] is False:
                Button_21_left()
            if States[41] == 0 and Button_Called[41] is False:
                Button_41_left()
            if States[32] == 0 and Button_Called[32] is False:
                Button_32_left()

    def click31(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[31]
        if {event.num} == {1} and not x:
            Button_31_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button31.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[31] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button31.config(image="")
                Flag_Exists[31] = False

    button31.bind("<Button>", click31)

    def Button_32_left():
        button32.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[32]
        Button_Called[32] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button21.destroy()
            if Flag_Exists[21]:
                Num_Of_Flags -= 1
                Flag_Exists[21] = False
            button22.destroy()
            if Flag_Exists[22]:
                Num_Of_Flags -= 1
                Flag_Exists[22] = False
            button23.destroy()
            if Flag_Exists[23]:
                Num_Of_Flags -= 1
                Flag_Exists[23] = False
            button31.destroy()
            if Flag_Exists[31]:
                Num_Of_Flags -= 1
                Flag_Exists[31] = False
            button33.destroy()
            if Flag_Exists[33]:
                Num_Of_Flags -= 1
                Flag_Exists[33] = False
            button41.destroy()
            if Flag_Exists[41]:
                Num_Of_Flags -= 1
                Flag_Exists[41] = False
            button42.destroy()
            if Flag_Exists[42]:
                Num_Of_Flags -= 1
                Flag_Exists[42] = False
            button43.destroy()
            if Flag_Exists[43]:
                Num_Of_Flags -= 1
                Flag_Exists[43] = False
            update_mines_left()
            if States[22] == 0 and Button_Called[22] is False:
                Button_22_left()
            if States[31] == 0 and Button_Called[31] is False:
                Button_31_left()
            if States[33] == 0 and Button_Called[33] is False:
                Button_33_left()
            if States[42] == 0 and Button_Called[42] is False:
                Button_42_left()

    def click32(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[32]
        if {event.num} == {1} and not x:
            Button_32_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button32.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[32] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button32.config(image="")
                Flag_Exists[32] = False

    button32.bind("<Button>", click32)

    def Button_33_left():
        button33.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[33]
        Button_Called[33] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button22.destroy()
            if Flag_Exists[22]:
                Num_Of_Flags -= 1
                Flag_Exists[22] = False
            button23.destroy()
            if Flag_Exists[23]:
                Num_Of_Flags -= 1
                Flag_Exists[23] = False
            button24.destroy()
            if Flag_Exists[24]:
                Num_Of_Flags -= 1
                Flag_Exists[24] = False
            button32.destroy()
            if Flag_Exists[32]:
                Num_Of_Flags -= 1
                Flag_Exists[32] = False
            button34.destroy()
            if Flag_Exists[34]:
                Num_Of_Flags -= 1
                Flag_Exists[34] = False
            button42.destroy()
            if Flag_Exists[42]:
                Num_Of_Flags -= 1
                Flag_Exists[42] = False
            button43.destroy()
            if Flag_Exists[43]:
                Num_Of_Flags -= 1
                Flag_Exists[43] = False
            button44.destroy()
            if Flag_Exists[44]:
                Num_Of_Flags -= 1
                Flag_Exists[44] = False
            update_mines_left()
            if States[23] == 0 and Button_Called[23] is False:
                Button_23_left()
            if States[32] == 0 and Button_Called[32] is False:
                Button_32_left()
            if States[34] == 0 and Button_Called[34] is False:
                Button_34_left()
            if States[43] == 0 and Button_Called[43] is False:
                Button_43_left()

    def click33(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[33]
        if {event.num} == {1} and not x:
            Button_33_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button33.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[33] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button33.config(image="")
                Flag_Exists[33] = False

    button33.bind("<Button>", click33)

    def Button_34_left():
        button34.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[34]
        Button_Called[34] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button23.destroy()
            if Flag_Exists[23]:
                Num_Of_Flags -= 1
                Flag_Exists[23] = False
            button24.destroy()
            if Flag_Exists[24]:
                Num_Of_Flags -= 1
                Flag_Exists[24] = False
            button25.destroy()
            if Flag_Exists[25]:
                Num_Of_Flags -= 1
                Flag_Exists[25] = False
            button33.destroy()
            if Flag_Exists[33]:
                Num_Of_Flags -= 1
                Flag_Exists[33] = False
            button35.destroy()
            if Flag_Exists[35]:
                Num_Of_Flags -= 1
                Flag_Exists[35] = False
            button43.destroy()
            if Flag_Exists[43]:
                Num_Of_Flags -= 1
                Flag_Exists[43] = False
            button44.destroy()
            if Flag_Exists[44]:
                Num_Of_Flags -= 1
                Flag_Exists[44] = False
            button45.destroy()
            if Flag_Exists[45]:
                Num_Of_Flags -= 1
                Flag_Exists[45] = False
            update_mines_left()
            if States[24] == 0 and Button_Called[24] is False:
                Button_24_left()
            if States[33] == 0 and Button_Called[33] is False:
                Button_33_left()
            if States[35] == 0 and Button_Called[35] is False:
                Button_35_left()
            if States[44] == 0 and Button_Called[44] is False:
                Button_44_left()

    def click34(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[34]
        if {event.num} == {1} and not x:
            Button_34_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button34.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[34] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button34.config(image="")
                Flag_Exists[34] = False

    button34.bind("<Button>", click34)

    def Button_35_left():
        button35.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[35]
        Button_Called[35] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button24.destroy()
            if Flag_Exists[24]:
                Num_Of_Flags -= 1
                Flag_Exists[24] = False
            button25.destroy()
            if Flag_Exists[25]:
                Num_Of_Flags -= 1
                Flag_Exists[25] = False
            button26.destroy()
            if Flag_Exists[26]:
                Num_Of_Flags -= 1
                Flag_Exists[26] = False
            button34.destroy()
            if Flag_Exists[34]:
                Num_Of_Flags -= 1
                Flag_Exists[34] = False
            button36.destroy()
            if Flag_Exists[36]:
                Num_Of_Flags -= 1
                Flag_Exists[36] = False
            button44.destroy()
            if Flag_Exists[44]:
                Num_Of_Flags -= 1
                Flag_Exists[44] = False
            button45.destroy()
            if Flag_Exists[45]:
                Num_Of_Flags -= 1
                Flag_Exists[45] = False
            button46.destroy()
            if Flag_Exists[46]:
                Num_Of_Flags -= 1
                Flag_Exists[46] = False
            update_mines_left()
            if States[25] == 0 and Button_Called[25] is False:
                Button_25_left()
            if States[34] == 0 and Button_Called[34] is False:
                Button_34_left()
            if States[36] == 0 and Button_Called[36] is False:
                Button_36_left()
            if States[45] == 0 and Button_Called[45] is False:
                Button_45_left()

    def click35(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[35]
        if {event.num} == {1} and not x:
            Button_35_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button35.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[35] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button35.config(image="")
                Flag_Exists[35] = False

    button35.bind("<Button>", click35)

    def Button_36_left():
        button36.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[36]
        Button_Called[36] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button25.destroy()
            if Flag_Exists[25]:
                Num_Of_Flags -= 1
                Flag_Exists[25] = False
            button26.destroy()
            if Flag_Exists[26]:
                Num_Of_Flags -= 1
                Flag_Exists[26] = False
            button27.destroy()
            if Flag_Exists[27]:
                Num_Of_Flags -= 1
                Flag_Exists[27] = False
            button35.destroy()
            if Flag_Exists[35]:
                Num_Of_Flags -= 1
                Flag_Exists[35] = False
            button37.destroy()
            if Flag_Exists[37]:
                Num_Of_Flags -= 1
                Flag_Exists[37] = False
            button45.destroy()
            if Flag_Exists[45]:
                Num_Of_Flags -= 1
                Flag_Exists[45] = False
            button46.destroy()
            if Flag_Exists[46]:
                Num_Of_Flags -= 1
                Flag_Exists[46] = False
            button47.destroy()
            if Flag_Exists[47]:
                Num_Of_Flags -= 1
                Flag_Exists[47] = False
            update_mines_left()
            if States[26] == 0 and Button_Called[26] is False:
                Button_26_left()
            if States[35] == 0 and Button_Called[35] is False:
                Button_35_left()
            if States[37] == 0 and Button_Called[37] is False:
                Button_37_left()
            if States[46] == 0 and Button_Called[46] is False:
                Button_46_left()

    def click36(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[36]
        if {event.num} == {1} and not x:
            Button_36_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button36.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[36] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button36.config(image="")
                Flag_Exists[36] = False

    button36.bind("<Button>", click36)

    def Button_37_left():
        button37.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[37]
        Button_Called[37] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button26.destroy()
            if Flag_Exists[26]:
                Num_Of_Flags -= 1
                Flag_Exists[26] = False
            button27.destroy()
            if Flag_Exists[27]:
                Num_Of_Flags -= 1
                Flag_Exists[27] = False
            button28.destroy()
            if Flag_Exists[28]:
                Num_Of_Flags -= 1
                Flag_Exists[28] = False
            button36.destroy()
            if Flag_Exists[36]:
                Num_Of_Flags -= 1
                Flag_Exists[36] = False
            button38.destroy()
            if Flag_Exists[38]:
                Num_Of_Flags -= 1
                Flag_Exists[38] = False
            button46.destroy()
            if Flag_Exists[46]:
                Num_Of_Flags -= 1
                Flag_Exists[46] = False
            button47.destroy()
            if Flag_Exists[47]:
                Num_Of_Flags -= 1
                Flag_Exists[47] = False
            button48.destroy()
            if Flag_Exists[48]:
                Num_Of_Flags -= 1
                Flag_Exists[48] = False
            update_mines_left()
            if States[27] == 0 and Button_Called[27] is False:
                Button_27_left()
            if States[36] == 0 and Button_Called[36] is False:
                Button_36_left()
            if States[38] == 0 and Button_Called[38] is False:
                Button_38_left()
            if States[47] == 0 and Button_Called[47] is False:
                Button_47_left()

    def click37(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[37]
        if {event.num} == {1} and not x:
            Button_37_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button37.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[37] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button37.config(image="")
                Flag_Exists[37] = False

    button37.bind("<Button>", click37)

    def Button_38_left():
        button38.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[38]
        Button_Called[38] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button27.destroy()
            if Flag_Exists[27]:
                Num_Of_Flags -= 1
                Flag_Exists[27] = False
            button28.destroy()
            if Flag_Exists[28]:
                Num_Of_Flags -= 1
                Flag_Exists[28] = False
            button29.destroy()
            if Flag_Exists[29]:
                Num_Of_Flags -= 1
                Flag_Exists[29] = False
            button37.destroy()
            if Flag_Exists[37]:
                Num_Of_Flags -= 1
                Flag_Exists[37] = False
            button39.destroy()
            if Flag_Exists[39]:
                Num_Of_Flags -= 1
                Flag_Exists[39] = False
            button47.destroy()
            if Flag_Exists[47]:
                Num_Of_Flags -= 1
                Flag_Exists[47] = False
            button48.destroy()
            if Flag_Exists[48]:
                Num_Of_Flags -= 1
                Flag_Exists[48] = False
            button49.destroy()
            if Flag_Exists[49]:
                Num_Of_Flags -= 1
                Flag_Exists[49] = False
            update_mines_left()
            if States[28] == 0 and Button_Called[28] is False:
                Button_28_left()
            if States[37] == 0 and Button_Called[37] is False:
                Button_37_left()
            if States[39] == 0 and Button_Called[39] is False:
                Button_39_left()
            if States[48] == 0 and Button_Called[48] is False:
                Button_48_left()

    def click38(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[38]
        if {event.num} == {1} and not x:
            Button_38_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button38.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[38] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button38.config(image="")
                Flag_Exists[38] = False

    button38.bind("<Button>", click38)

    def Button_39_left():
        button39.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[39]
        Button_Called[39] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button28.destroy()
            if Flag_Exists[28]:
                Num_Of_Flags -= 1
                Flag_Exists[28] = False
            button29.destroy()
            if Flag_Exists[29]:
                Num_Of_Flags -= 1
                Flag_Exists[29] = False
            button30.destroy()
            if Flag_Exists[30]:
                Num_Of_Flags -= 1
                Flag_Exists[30] = False
            button38.destroy()
            if Flag_Exists[38]:
                Num_Of_Flags -= 1
                Flag_Exists[38] = False
            button40.destroy()
            if Flag_Exists[40]:
                Num_Of_Flags -= 1
                Flag_Exists[40] = False
            button48.destroy()
            if Flag_Exists[48]:
                Num_Of_Flags -= 1
                Flag_Exists[48] = False
            button49.destroy()
            if Flag_Exists[49]:
                Num_Of_Flags -= 1
                Flag_Exists[49] = False
            button50.destroy()
            if Flag_Exists[50]:
                Num_Of_Flags -= 1
                Flag_Exists[50] = False
            update_mines_left()
            if States[29] == 0 and Button_Called[29] is False:
                Button_29_left()
            if States[38] == 0 and Button_Called[38] is False:
                Button_38_left()
            if States[40] == 0 and Button_Called[40] is False:
                Button_40_left()
            if States[49] == 0 and Button_Called[49] is False:
                Button_49_left()

    def click39(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[39]
        if {event.num} == {1} and not x:
            Button_39_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button39.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[39] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button39.config(image="")
                Flag_Exists[39] = False

    button39.bind("<Button>", click39)

    def Button_40_left():
        button40.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[40]
        Button_Called[40] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button29.destroy()
            if Flag_Exists[29]:
                Num_Of_Flags -= 1
                Flag_Exists[29] = False
            button30.destroy()
            if Flag_Exists[30]:
                Num_Of_Flags -= 1
                Flag_Exists[30] = False
            button39.destroy()
            if Flag_Exists[39]:
                Num_Of_Flags -= 1
                Flag_Exists[39] = False
            button49.destroy()
            if Flag_Exists[49]:
                Num_Of_Flags -= 1
                Flag_Exists[49] = False
            button50.destroy()
            if Flag_Exists[50]:
                Num_Of_Flags -= 1
                Flag_Exists[50] = False
            update_mines_left()
            if States[30] == 0 and Button_Called[30] is False:
                Button_30_left()
            if States[39] == 0 and Button_Called[39] is False:
                Button_39_left()
            if States[50] == 0 and Button_Called[50] is False:
                Button_50_left()

    def click40(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[40]
        if {event.num} == {1} and not x:
            Button_40_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button40.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[40] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button40.config(image="")
                Flag_Exists[40] = False

    button40.bind("<Button>", click40)

    def Button_41_left():
        button41.destroy()
        WinCheck()
        global States
        global Button_Called
        x = States[41]
        Button_Called[41] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button31.destroy()
            if Flag_Exists[31]:
                Num_Of_Flags -= 1
                Flag_Exists[31] = False
            button32.destroy()
            if Flag_Exists[32]:
                Num_Of_Flags -= 1
                Flag_Exists[32] = False
            button42.destroy()
            if Flag_Exists[42]:
                Num_Of_Flags -= 1
                Flag_Exists[42] = False
            button51.destroy()
            if Flag_Exists[51]:
                Num_Of_Flags -= 1
                Flag_Exists[31] = False
            button52.destroy()
            if Flag_Exists[52]:
                Num_Of_Flags -= 1
                Flag_Exists[52] = False
            update_mines_left()
            if States[31] == 0 and Button_Called[31] is False:
                Button_31_left()
            if States[51] == 0 and Button_Called[51] is False:
                Button_51_left()
            if States[42] == 0 and Button_Called[42] is False:
                Button_42_left()

    def click41(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[41]
        if {event.num} == {1} and not x:
            Button_41_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button41.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[41] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button41.config(image="")
                Flag_Exists[41] = False

    button41.bind("<Button>", click41)

    def Button_42_left():
        button42.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[42]
        Button_Called[42] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button31.destroy()
            if Flag_Exists[31]:
                Num_Of_Flags -= 1
                Flag_Exists[31] = False
            button32.destroy()
            if Flag_Exists[32]:
                Num_Of_Flags -= 1
                Flag_Exists[32] = False
            button33.destroy()
            if Flag_Exists[33]:
                Num_Of_Flags -= 1
                Flag_Exists[33] = False
            button41.destroy()
            if Flag_Exists[41]:
                Num_Of_Flags -= 1
                Flag_Exists[41] = False
            button43.destroy()
            if Flag_Exists[43]:
                Num_Of_Flags -= 1
                Flag_Exists[43] = False
            button51.destroy()
            if Flag_Exists[51]:
                Num_Of_Flags -= 1
                Flag_Exists[51] = False
            button52.destroy()
            if Flag_Exists[52]:
                Num_Of_Flags -= 1
                Flag_Exists[52] = False
            button53.destroy()
            if Flag_Exists[53]:
                Num_Of_Flags -= 1
                Flag_Exists[53] = False
            update_mines_left()
            if States[32] == 0 and Button_Called[32] is False:
                Button_32_left()
            if States[41] == 0 and Button_Called[41] is False:
                Button_41_left()
            if States[43] == 0 and Button_Called[43] is False:
                Button_43_left()
            if States[52] == 0 and Button_Called[52] is False:
                Button_52_left()

    def click42(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[42]
        if {event.num} == {1} and not x:
            Button_42_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button42.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[42] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button42.config(image="")
                Flag_Exists[42] = False

    button42.bind("<Button>", click42)

    def Button_43_left():
        button43.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[43]
        Button_Called[43] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button32.destroy()
            if Flag_Exists[32]:
                Num_Of_Flags -= 1
                Flag_Exists[32] = False
            button33.destroy()
            if Flag_Exists[33]:
                Num_Of_Flags -= 1
                Flag_Exists[33] = False
            button34.destroy()
            if Flag_Exists[34]:
                Num_Of_Flags -= 1
                Flag_Exists[34] = False
            button42.destroy()
            if Flag_Exists[42]:
                Num_Of_Flags -= 1
                Flag_Exists[42] = False
            button44.destroy()
            if Flag_Exists[44]:
                Num_Of_Flags -= 1
                Flag_Exists[44] = False
            button52.destroy()
            if Flag_Exists[52]:
                Num_Of_Flags -= 1
                Flag_Exists[52] = False
            button53.destroy()
            if Flag_Exists[53]:
                Num_Of_Flags -= 1
                Flag_Exists[53] = False
            button54.destroy()
            if Flag_Exists[54]:
                Num_Of_Flags -= 1
                Flag_Exists[54] = False
            update_mines_left()
            if States[33] == 0 and Button_Called[33] is False:
                Button_33_left()
            if States[42] == 0 and Button_Called[42] is False:
                Button_42_left()
            if States[44] == 0 and Button_Called[44] is False:
                Button_44_left()
            if States[53] == 0 and Button_Called[53] is False:
                Button_53_left()

    def click43(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[43]
        if {event.num} == {1} and not x:
            Button_43_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button43.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[43] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button43.config(image="")
                Flag_Exists[43] = False

    button43.bind("<Button>", click43)

    def Button_44_left():
        button44.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[44]
        Button_Called[44] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button33.destroy()
            if Flag_Exists[33]:
                Num_Of_Flags -= 1
                Flag_Exists[33] = False
            button34.destroy()
            if Flag_Exists[34]:
                Num_Of_Flags -= 1
                Flag_Exists[34] = False
            button35.destroy()
            if Flag_Exists[35]:
                Num_Of_Flags -= 1
                Flag_Exists[35] = False
            button43.destroy()
            if Flag_Exists[43]:
                Num_Of_Flags -= 1
                Flag_Exists[43] = False
            button45.destroy()
            if Flag_Exists[45]:
                Num_Of_Flags -= 1
                Flag_Exists[45] = False
            button53.destroy()
            if Flag_Exists[53]:
                Num_Of_Flags -= 1
                Flag_Exists[53] = False
            button54.destroy()
            if Flag_Exists[54]:
                Num_Of_Flags -= 1
                Flag_Exists[54] = False
            button55.destroy()
            if Flag_Exists[55]:
                Num_Of_Flags -= 1
                Flag_Exists[55] = False
            update_mines_left()
            if States[34] == 0 and Button_Called[34] is False:
                Button_34_left()
            if States[43] == 0 and Button_Called[43] is False:
                Button_43_left()
            if States[45] == 0 and Button_Called[45] is False:
                Button_45_left()
            if States[54] == 0 and Button_Called[54] is False:
                Button_54_left()

    def click44(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[44]
        if {event.num} == {1} and not x:
            Button_44_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button44.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[44] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button44.config(image="")
                Flag_Exists[44] = False

    button44.bind("<Button>", click44)

    def Button_45_left():
        button45.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[45]
        Button_Called[45] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button34.destroy()
            if Flag_Exists[34]:
                Num_Of_Flags -= 1
                Flag_Exists[34] = False
            button35.destroy()
            if Flag_Exists[35]:
                Num_Of_Flags -= 1
                Flag_Exists[35] = False
            button36.destroy()
            if Flag_Exists[36]:
                Num_Of_Flags -= 1
                Flag_Exists[36] = False
            button44.destroy()
            if Flag_Exists[44]:
                Num_Of_Flags -= 1
                Flag_Exists[44] = False
            button46.destroy()
            if Flag_Exists[46]:
                Num_Of_Flags -= 1
                Flag_Exists[46] = False
            button54.destroy()
            if Flag_Exists[54]:
                Num_Of_Flags -= 1
                Flag_Exists[54] = False
            button55.destroy()
            if Flag_Exists[55]:
                Num_Of_Flags -= 1
                Flag_Exists[55] = False
            button56.destroy()
            if Flag_Exists[56]:
                Num_Of_Flags -= 1
                Flag_Exists[56] = False
            update_mines_left()
            if States[35] == 0 and Button_Called[35] is False:
                Button_35_left()
            if States[44] == 0 and Button_Called[44] is False:
                Button_44_left()
            if States[46] == 0 and Button_Called[46] is False:
                Button_46_left()
            if States[55] == 0 and Button_Called[55] is False:
                Button_55_left()

    def click45(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[45]
        if {event.num} == {1} and not x:
            Button_45_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button45.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[45] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button45.config(image="")
                Flag_Exists[45] = False

    button45.bind("<Button>", click45)

    def Button_46_left():
        button46.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[46]
        Button_Called[46] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button35.destroy()
            if Flag_Exists[35]:
                Num_Of_Flags -= 1
                Flag_Exists[35] = False
            button36.destroy()
            if Flag_Exists[36]:
                Num_Of_Flags -= 1
                Flag_Exists[36] = False
            button37.destroy()
            if Flag_Exists[37]:
                Num_Of_Flags -= 1
                Flag_Exists[37] = False
            button45.destroy()
            if Flag_Exists[45]:
                Num_Of_Flags -= 1
                Flag_Exists[45] = False
            button47.destroy()
            if Flag_Exists[47]:
                Num_Of_Flags -= 1
                Flag_Exists[47] = False
            button55.destroy()
            if Flag_Exists[55]:
                Num_Of_Flags -= 1
                Flag_Exists[55] = False
            button56.destroy()
            if Flag_Exists[56]:
                Num_Of_Flags -= 1
                Flag_Exists[56] = False
            button57.destroy()
            if Flag_Exists[57]:
                Num_Of_Flags -= 1
                Flag_Exists[57] = False
            update_mines_left()
            if States[36] == 0 and Button_Called[36] is False:
                Button_36_left()
            if States[45] == 0 and Button_Called[45] is False:
                Button_45_left()
            if States[47] == 0 and Button_Called[47] is False:
                Button_47_left()
            if States[56] == 0 and Button_Called[56] is False:
                Button_56_left()

    def click46(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[46]
        if {event.num} == {1} and not x:
            Button_46_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button46.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[46] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button46.config(image="")
                Flag_Exists[46] = False

    button46.bind("<Button>", click46)

    def Button_47_left():
        button47.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[47]
        Button_Called[47] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button36.destroy()
            if Flag_Exists[36]:
                Num_Of_Flags -= 1
                Flag_Exists[36] = False
            button37.destroy()
            if Flag_Exists[37]:
                Num_Of_Flags -= 1
                Flag_Exists[37] = False
            button38.destroy()
            if Flag_Exists[38]:
                Num_Of_Flags -= 1
                Flag_Exists[38] = False
            button46.destroy()
            if Flag_Exists[46]:
                Num_Of_Flags -= 1
                Flag_Exists[46] = False
            button48.destroy()
            if Flag_Exists[48]:
                Num_Of_Flags -= 1
                Flag_Exists[48] = False
            button56.destroy()
            if Flag_Exists[56]:
                Num_Of_Flags -= 1
                Flag_Exists[56] = False
            button57.destroy()
            if Flag_Exists[57]:
                Num_Of_Flags -= 1
                Flag_Exists[57] = False
            button58.destroy()
            if Flag_Exists[58]:
                Num_Of_Flags -= 1
                Flag_Exists[58] = False
            update_mines_left()
            if States[37] == 0 and Button_Called[37] is False:
                Button_37_left()
            if States[46] == 0 and Button_Called[46] is False:
                Button_46_left()
            if States[48] == 0 and Button_Called[48] is False:
                Button_48_left()
            if States[57] == 0 and Button_Called[57] is False:
                Button_57_left()

    def click47(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[47]
        if {event.num} == {1} and not x:
            Button_47_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button47.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[47] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button47.config(image="")
                Flag_Exists[47] = False

    button47.bind("<Button>", click47)

    def Button_48_left():
        button48.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[48]
        Button_Called[48] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button37.destroy()
            if Flag_Exists[37]:
                Num_Of_Flags -= 1
                Flag_Exists[37] = False
            button38.destroy()
            if Flag_Exists[38]:
                Num_Of_Flags -= 1
                Flag_Exists[38] = False
            button39.destroy()
            if Flag_Exists[39]:
                Num_Of_Flags -= 1
                Flag_Exists[39] = False
            button47.destroy()
            if Flag_Exists[47]:
                Num_Of_Flags -= 1
                Flag_Exists[47] = False
            button49.destroy()
            if Flag_Exists[49]:
                Num_Of_Flags -= 1
                Flag_Exists[49] = False
            button57.destroy()
            if Flag_Exists[57]:
                Num_Of_Flags -= 1
                Flag_Exists[57] = False
            button58.destroy()
            if Flag_Exists[58]:
                Num_Of_Flags -= 1
                Flag_Exists[58] = False
            button59.destroy()
            if Flag_Exists[59]:
                Num_Of_Flags -= 1
                Flag_Exists[59] = False
            update_mines_left()
            if States[38] == 0 and Button_Called[38] is False:
                Button_38_left()
            if States[47] == 0 and Button_Called[47] is False:
                Button_47_left()
            if States[49] == 0 and Button_Called[49] is False:
                Button_49_left()
            if States[58] == 0 and Button_Called[58] is False:
                Button_58_left()

    def click48(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[48]
        if {event.num} == {1} and not x:
            Button_48_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button48.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[48] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button48.config(image="")
                Flag_Exists[48] = False

    button48.bind("<Button>", click48)

    def Button_49_left():
        button49.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[49]
        Button_Called[49] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button38.destroy()
            if Flag_Exists[38]:
                Num_Of_Flags -= 1
                Flag_Exists[38] = False
            button39.destroy()
            if Flag_Exists[39]:
                Num_Of_Flags -= 1
                Flag_Exists[39] = False
            button40.destroy()
            if Flag_Exists[40]:
                Num_Of_Flags -= 1
                Flag_Exists[40] = False
            button48.destroy()
            if Flag_Exists[48]:
                Num_Of_Flags -= 1
                Flag_Exists[48] = False
            button50.destroy()
            if Flag_Exists[50]:
                Num_Of_Flags -= 1
                Flag_Exists[50] = False
            button58.destroy()
            if Flag_Exists[58]:
                Num_Of_Flags -= 1
                Flag_Exists[58] = False
            button59.destroy()
            if Flag_Exists[59]:
                Num_Of_Flags -= 1
                Flag_Exists[59] = False
            button60.destroy()
            if Flag_Exists[60]:
                Num_Of_Flags -= 1
                Flag_Exists[60] = False
            update_mines_left()
            if States[39] == 0 and Button_Called[39] is False:
                Button_39_left()
            if States[48] == 0 and Button_Called[48] is False:
                Button_48_left()
            if States[50] == 0 and Button_Called[50] is False:
                Button_50_left()
            if States[59] == 0 and Button_Called[59] is False:
                Button_59_left()

    def click49(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[49]
        if {event.num} == {1} and not x:
            Button_49_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button49.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[49] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button49.config(image="")
                Flag_Exists[49] = False

    button49.bind("<Button>", click49)

    def Button_50_left():
        button50.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[50]
        Button_Called[50] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button39.destroy()
            if Flag_Exists[39]:
                Num_Of_Flags -= 1
                Flag_Exists[39] = False
            button40.destroy()
            if Flag_Exists[40]:
                Num_Of_Flags -= 1
                Flag_Exists[40] = False
            button49.destroy()
            if Flag_Exists[49]:
                Num_Of_Flags -= 1
                Flag_Exists[49] = False
            button59.destroy()
            if Flag_Exists[59]:
                Num_Of_Flags -= 1
                Flag_Exists[59] = False
            button60.destroy()
            if Flag_Exists[60]:
                Num_Of_Flags -= 1
                Flag_Exists[60] = False
            update_mines_left()
            if States[40] == 0 and Button_Called[40] is False:
                Button_40_left()
            if States[49] == 0 and Button_Called[49] is False:
                Button_49_left()
            if States[60] == 0 and Button_Called[60] is False:
                Button_60_left()

    def click50(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[50]
        if {event.num} == {1} and not x:
            Button_50_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button50.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[50] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button50.config(image="")
                Flag_Exists[50] = False

    button50.bind("<Button>", click50)

    def Button_51_left():
        button51.destroy()
        WinCheck()
        global States
        global Button_Called
        x = States[51]
        Button_Called[51] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button41.destroy()
            if Flag_Exists[41]:
                Num_Of_Flags -= 1
                Flag_Exists[41] = False
            button42.destroy()
            if Flag_Exists[42]:
                Num_Of_Flags -= 1
                Flag_Exists[42] = False
            button52.destroy()
            if Flag_Exists[52]:
                Num_Of_Flags -= 1
                Flag_Exists[52] = False
            button61.destroy()
            if Flag_Exists[61]:
                Num_Of_Flags -= 1
                Flag_Exists[41] = False
            button62.destroy()
            if Flag_Exists[62]:
                Num_Of_Flags -= 1
                Flag_Exists[62] = False
            update_mines_left()
            if States[41] == 0 and Button_Called[41] is False:
                Button_41_left()
            if States[61] == 0 and Button_Called[61] is False:
                Button_61_left()
            if States[52] == 0 and Button_Called[52] is False:
                Button_52_left()

    def click51(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[51]
        if {event.num} == {1} and not x:
            Button_51_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button51.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[51] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button51.config(image="")
                Flag_Exists[51] = False

    button51.bind("<Button>", click51)

    def Button_52_left():
        button52.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[52]
        Button_Called[52] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button41.destroy()
            if Flag_Exists[41]:
                Num_Of_Flags -= 1
                Flag_Exists[41] = False
            button42.destroy()
            if Flag_Exists[42]:
                Num_Of_Flags -= 1
                Flag_Exists[42] = False
            button43.destroy()
            if Flag_Exists[43]:
                Num_Of_Flags -= 1
                Flag_Exists[43] = False
            button51.destroy()
            if Flag_Exists[51]:
                Num_Of_Flags -= 1
                Flag_Exists[51] = False
            button53.destroy()
            if Flag_Exists[53]:
                Num_Of_Flags -= 1
                Flag_Exists[53] = False
            button61.destroy()
            if Flag_Exists[61]:
                Num_Of_Flags -= 1
                Flag_Exists[61] = False
            button62.destroy()
            if Flag_Exists[62]:
                Num_Of_Flags -= 1
                Flag_Exists[62] = False
            button63.destroy()
            if Flag_Exists[63]:
                Num_Of_Flags -= 1
                Flag_Exists[63] = False
            update_mines_left()
            if States[42] == 0 and Button_Called[42] is False:
                Button_42_left()
            if States[51] == 0 and Button_Called[51] is False:
                Button_51_left()
            if States[53] == 0 and Button_Called[53] is False:
                Button_53_left()
            if States[62] == 0 and Button_Called[62] is False:
                Button_62_left()

    def click52(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[52]
        if {event.num} == {1} and not x:
            Button_52_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button52.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[52] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button52.config(image="")
                Flag_Exists[52] = False

    button52.bind("<Button>", click52)

    def Button_53_left():
        button53.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[53]
        Button_Called[53] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button42.destroy()
            if Flag_Exists[42]:
                Num_Of_Flags -= 1
                Flag_Exists[42] = False
            button43.destroy()
            if Flag_Exists[43]:
                Num_Of_Flags -= 1
                Flag_Exists[43] = False
            button44.destroy()
            if Flag_Exists[44]:
                Num_Of_Flags -= 1
                Flag_Exists[44] = False
            button52.destroy()
            if Flag_Exists[52]:
                Num_Of_Flags -= 1
                Flag_Exists[52] = False
            button54.destroy()
            if Flag_Exists[54]:
                Num_Of_Flags -= 1
                Flag_Exists[54] = False
            button62.destroy()
            if Flag_Exists[62]:
                Num_Of_Flags -= 1
                Flag_Exists[62] = False
            button63.destroy()
            if Flag_Exists[63]:
                Num_Of_Flags -= 1
                Flag_Exists[63] = False
            button64.destroy()
            if Flag_Exists[64]:
                Num_Of_Flags -= 1
                Flag_Exists[64] = False
            update_mines_left()
            if States[43] == 0 and Button_Called[43] is False:
                Button_43_left()
            if States[52] == 0 and Button_Called[52] is False:
                Button_52_left()
            if States[54] == 0 and Button_Called[54] is False:
                Button_54_left()
            if States[63] == 0 and Button_Called[63] is False:
                Button_63_left()

    def click53(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[53]
        if {event.num} == {1} and not x:
            Button_53_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button53.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[53] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button53.config(image="")
                Flag_Exists[53] = False

    button53.bind("<Button>", click53)

    def Button_54_left():
        button54.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[54]
        Button_Called[54] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button43.destroy()
            if Flag_Exists[43]:
                Num_Of_Flags -= 1
                Flag_Exists[43] = False
            button44.destroy()
            if Flag_Exists[44]:
                Num_Of_Flags -= 1
                Flag_Exists[44] = False
            button45.destroy()
            if Flag_Exists[45]:
                Num_Of_Flags -= 1
                Flag_Exists[45] = False
            button53.destroy()
            if Flag_Exists[53]:
                Num_Of_Flags -= 1
                Flag_Exists[53] = False
            button55.destroy()
            if Flag_Exists[55]:
                Num_Of_Flags -= 1
                Flag_Exists[55] = False
            button63.destroy()
            if Flag_Exists[63]:
                Num_Of_Flags -= 1
                Flag_Exists[63] = False
            button64.destroy()
            if Flag_Exists[64]:
                Num_Of_Flags -= 1
                Flag_Exists[64] = False
            button65.destroy()
            if Flag_Exists[65]:
                Num_Of_Flags -= 1
                Flag_Exists[65] = False
            update_mines_left()
            if States[44] == 0 and Button_Called[44] is False:
                Button_44_left()
            if States[53] == 0 and Button_Called[53] is False:
                Button_53_left()
            if States[55] == 0 and Button_Called[55] is False:
                Button_55_left()
            if States[64] == 0 and Button_Called[64] is False:
                Button_64_left()

    def click54(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[54]
        if {event.num} == {1} and not x:
            Button_54_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button54.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[54] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button54.config(image="")
                Flag_Exists[54] = False

    button54.bind("<Button>", click54)

    def Button_55_left():
        button55.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[55]
        Button_Called[55] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button44.destroy()
            if Flag_Exists[44]:
                Num_Of_Flags -= 1
                Flag_Exists[44] = False
            button45.destroy()
            if Flag_Exists[45]:
                Num_Of_Flags -= 1
                Flag_Exists[45] = False
            button46.destroy()
            if Flag_Exists[46]:
                Num_Of_Flags -= 1
                Flag_Exists[46] = False
            button54.destroy()
            if Flag_Exists[54]:
                Num_Of_Flags -= 1
                Flag_Exists[54] = False
            button56.destroy()
            if Flag_Exists[56]:
                Num_Of_Flags -= 1
                Flag_Exists[56] = False
            button64.destroy()
            if Flag_Exists[64]:
                Num_Of_Flags -= 1
                Flag_Exists[64] = False
            button65.destroy()
            if Flag_Exists[65]:
                Num_Of_Flags -= 1
                Flag_Exists[65] = False
            button66.destroy()
            if Flag_Exists[66]:
                Num_Of_Flags -= 1
                Flag_Exists[66] = False
            update_mines_left()
            if States[45] == 0 and Button_Called[45] is False:
                Button_45_left()
            if States[54] == 0 and Button_Called[54] is False:
                Button_54_left()
            if States[56] == 0 and Button_Called[56] is False:
                Button_56_left()
            if States[65] == 0 and Button_Called[65] is False:
                Button_65_left()

    def click55(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[55]
        if {event.num} == {1} and not x:
            Button_55_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button55.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[55] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button55.config(image="")
                Flag_Exists[55] = False

    button55.bind("<Button>", click55)

    def Button_56_left():
        button56.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[56]
        Button_Called[56] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button45.destroy()
            if Flag_Exists[45]:
                Num_Of_Flags -= 1
                Flag_Exists[45] = False
            button46.destroy()
            if Flag_Exists[46]:
                Num_Of_Flags -= 1
                Flag_Exists[46] = False
            button47.destroy()
            if Flag_Exists[47]:
                Num_Of_Flags -= 1
                Flag_Exists[47] = False
            button55.destroy()
            if Flag_Exists[55]:
                Num_Of_Flags -= 1
                Flag_Exists[55] = False
            button57.destroy()
            if Flag_Exists[57]:
                Num_Of_Flags -= 1
                Flag_Exists[57] = False
            button65.destroy()
            if Flag_Exists[65]:
                Num_Of_Flags -= 1
                Flag_Exists[65] = False
            button66.destroy()
            if Flag_Exists[66]:
                Num_Of_Flags -= 1
                Flag_Exists[66] = False
            button67.destroy()
            if Flag_Exists[67]:
                Num_Of_Flags -= 1
                Flag_Exists[67] = False
            update_mines_left()
            if States[46] == 0 and Button_Called[46] is False:
                Button_46_left()
            if States[55] == 0 and Button_Called[55] is False:
                Button_55_left()
            if States[57] == 0 and Button_Called[57] is False:
                Button_57_left()
            if States[66] == 0 and Button_Called[66] is False:
                Button_66_left()

    def click56(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[56]
        if {event.num} == {1} and not x:
            Button_56_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button56.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[56] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button56.config(image="")
                Flag_Exists[56] = False

    button56.bind("<Button>", click56)

    def Button_57_left():
        button57.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[57]
        Button_Called[57] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button46.destroy()
            if Flag_Exists[46]:
                Num_Of_Flags -= 1
                Flag_Exists[46] = False
            button47.destroy()
            if Flag_Exists[47]:
                Num_Of_Flags -= 1
                Flag_Exists[47] = False
            button48.destroy()
            if Flag_Exists[48]:
                Num_Of_Flags -= 1
                Flag_Exists[48] = False
            button56.destroy()
            if Flag_Exists[56]:
                Num_Of_Flags -= 1
                Flag_Exists[56] = False
            button58.destroy()
            if Flag_Exists[58]:
                Num_Of_Flags -= 1
                Flag_Exists[58] = False
            button66.destroy()
            if Flag_Exists[66]:
                Num_Of_Flags -= 1
                Flag_Exists[66] = False
            button67.destroy()
            if Flag_Exists[67]:
                Num_Of_Flags -= 1
                Flag_Exists[67] = False
            button68.destroy()
            if Flag_Exists[68]:
                Num_Of_Flags -= 1
                Flag_Exists[68] = False
            update_mines_left()
            if States[47] == 0 and Button_Called[47] is False:
                Button_47_left()
            if States[56] == 0 and Button_Called[56] is False:
                Button_56_left()
            if States[58] == 0 and Button_Called[58] is False:
                Button_58_left()
            if States[67] == 0 and Button_Called[67] is False:
                Button_67_left()

    def click57(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[57]
        if {event.num} == {1} and not x:
            Button_57_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button57.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[57] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button57.config(image="")
                Flag_Exists[57] = False

    button57.bind("<Button>", click57)

    def Button_58_left():
        button58.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[58]
        Button_Called[58] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button47.destroy()
            if Flag_Exists[47]:
                Num_Of_Flags -= 1
                Flag_Exists[47] = False
            button48.destroy()
            if Flag_Exists[48]:
                Num_Of_Flags -= 1
                Flag_Exists[48] = False
            button49.destroy()
            if Flag_Exists[49]:
                Num_Of_Flags -= 1
                Flag_Exists[49] = False
            button57.destroy()
            if Flag_Exists[57]:
                Num_Of_Flags -= 1
                Flag_Exists[57] = False
            button59.destroy()
            if Flag_Exists[59]:
                Num_Of_Flags -= 1
                Flag_Exists[59] = False
            button67.destroy()
            if Flag_Exists[67]:
                Num_Of_Flags -= 1
                Flag_Exists[67] = False
            button68.destroy()
            if Flag_Exists[68]:
                Num_Of_Flags -= 1
                Flag_Exists[68] = False
            button69.destroy()
            if Flag_Exists[69]:
                Num_Of_Flags -= 1
                Flag_Exists[69] = False
            update_mines_left()
            if States[48] == 0 and Button_Called[48] is False:
                Button_48_left()
            if States[57] == 0 and Button_Called[57] is False:
                Button_57_left()
            if States[59] == 0 and Button_Called[59] is False:
                Button_59_left()
            if States[68] == 0 and Button_Called[68] is False:
                Button_68_left()

    def click58(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[58]
        if {event.num} == {1} and not x:
            Button_58_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button58.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[58] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button58.config(image="")
                Flag_Exists[58] = False

    button58.bind("<Button>", click58)

    def Button_59_left():
        button59.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[59]
        Button_Called[59] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button48.destroy()
            if Flag_Exists[48]:
                Num_Of_Flags -= 1
                Flag_Exists[48] = False
            button49.destroy()
            if Flag_Exists[49]:
                Num_Of_Flags -= 1
                Flag_Exists[49] = False
            button50.destroy()
            if Flag_Exists[50]:
                Num_Of_Flags -= 1
                Flag_Exists[50] = False
            button58.destroy()
            if Flag_Exists[58]:
                Num_Of_Flags -= 1
                Flag_Exists[58] = False
            button60.destroy()
            if Flag_Exists[60]:
                Num_Of_Flags -= 1
                Flag_Exists[60] = False
            button68.destroy()
            if Flag_Exists[68]:
                Num_Of_Flags -= 1
                Flag_Exists[68] = False
            button69.destroy()
            if Flag_Exists[69]:
                Num_Of_Flags -= 1
                Flag_Exists[69] = False
            button70.destroy()
            if Flag_Exists[70]:
                Num_Of_Flags -= 1
                Flag_Exists[70] = False
            update_mines_left()
            if States[49] == 0 and Button_Called[49] is False:
                Button_49_left()
            if States[58] == 0 and Button_Called[58] is False:
                Button_58_left()
            if States[60] == 0 and Button_Called[60] is False:
                Button_60_left()
            if States[69] == 0 and Button_Called[69] is False:
                Button_69_left()

    def click59(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[59]
        if {event.num} == {1} and not x:
            Button_59_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button59.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[59] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button59.config(image="")
                Flag_Exists[59] = False

    button59.bind("<Button>", click59)

    def Button_60_left():
        button60.destroy()
        WinCheck()
        global States
        global Button_Called
        global States
        x = States[60]
        Button_Called[60] = True
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button49.destroy()
            if Flag_Exists[49]:
                Num_Of_Flags -= 1
                Flag_Exists[49] = False
            button50.destroy()
            if Flag_Exists[50]:
                Num_Of_Flags -= 1
                Flag_Exists[50] = False
            button59.destroy()
            if Flag_Exists[59]:
                Num_Of_Flags -= 1
                Flag_Exists[59] = False
            button69.destroy()
            if Flag_Exists[69]:
                Num_Of_Flags -= 1
                Flag_Exists[69] = False
            button70.destroy()
            if Flag_Exists[70]:
                Num_Of_Flags -= 1
                Flag_Exists[70] = False
            update_mines_left()
            if States[50] == 0 and Button_Called[50] is False:
                Button_50_left()
            if States[59] == 0 and Button_Called[59] is False:
                Button_59_left()
            if States[70] == 0 and Button_Called[70] is False:
                Button_70_left()

    def click60(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[60]
        if {event.num} == {1} and not x:
            Button_60_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button60.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[60] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button60.config(image="")
                Flag_Exists[60] = False

    button60.bind("<Button>", click60)

    def Button_61_left():
        button61.destroy()
        WinCheck()
        global States
        global Button_Called
        Button_Called[61] = True
        x = States[61]
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button51.destroy()
            if Flag_Exists[51]:
                Num_Of_Flags -= 1
                Flag_Exists[51] = False
            button52.destroy()
            if Flag_Exists[52]:
                Num_Of_Flags -= 1
                Flag_Exists[52] = False
            button62.destroy()
            if Flag_Exists[62]:
                Num_Of_Flags -= 1
                Flag_Exists[62] = False
            update_mines_left()
            if States[51] == 0 and Button_Called[51] is False:
                Button_51_left()
            if States[62] == 0 and Button_Called[62] is False:
                Button_62_left()

    def click61(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[61]
        if {event.num} == {1} and not x:
            Button_61_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button61.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[61] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button61.config(image="")
                Flag_Exists[61] = False

    button61.bind("<Button>", click61)

    def Button_62_left():
        button62.destroy()
        WinCheck()
        global States
        global Button_Called
        Button_Called[62] = True
        global States
        x = States[62]
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button51.destroy()
            if Flag_Exists[51]:
                Num_Of_Flags -= 1
                Flag_Exists[51] = False
            button52.destroy()
            if Flag_Exists[52]:
                Num_Of_Flags -= 1
                Flag_Exists[52] = False
            button53.destroy()
            if Flag_Exists[53]:
                Num_Of_Flags -= 1
                Flag_Exists[53] = False
            button61.destroy()
            if Flag_Exists[61]:
                Num_Of_Flags -= 1
                Flag_Exists[61] = False
            button63.destroy()
            if Flag_Exists[63]:
                Num_Of_Flags -= 1
                Flag_Exists[63] = False
            update_mines_left()
            if States[52] == 0 and Button_Called[52] is False:
                Button_52_left()
            if States[61] == 0 and Button_Called[61] is False:
                Button_61_left()
            if States[63] == 0 and Button_Called[63] is False:
                Button_63_left()

    def click62(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[62]
        if {event.num} == {1} and not x:
            Button_62_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button62.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[62] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button62.config(image="")
                Flag_Exists[62] = False

    button62.bind("<Button>", click62)

    def Button_63_left():
        button63.destroy()
        WinCheck()
        global States
        global Button_Called
        Button_Called[63] = True
        global States
        x = States[63]
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button52.destroy()
            if Flag_Exists[52]:
                Num_Of_Flags -= 1
                Flag_Exists[52] = False
            button53.destroy()
            if Flag_Exists[53]:
                Num_Of_Flags -= 1
                Flag_Exists[53] = False
            button54.destroy()
            if Flag_Exists[54]:
                Num_Of_Flags -= 1
                Flag_Exists[54] = False
            button62.destroy()
            if Flag_Exists[62]:
                Num_Of_Flags -= 1
                Flag_Exists[62] = False
            button64.destroy()
            if Flag_Exists[64]:
                Num_Of_Flags -= 1
                Flag_Exists[64] = False
            update_mines_left()
            if States[53] == 0 and Button_Called[53] is False:
                Button_53_left()
            if States[62] == 0 and Button_Called[62] is False:
                Button_62_left()
            if States[64] == 0 and Button_Called[64] is False:
                Button_64_left()

    def click63(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[63]
        if {event.num} == {1} and not x:
            Button_63_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button63.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[63] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button63.config(image="")
                Flag_Exists[63] = False

    button63.bind("<Button>", click63)

    def Button_64_left():
        button64.destroy()
        WinCheck()
        global States
        global Button_Called
        Button_Called[64] = True
        global States
        x = States[64]
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button53.destroy()
            if Flag_Exists[53]:
                Num_Of_Flags -= 1
                Flag_Exists[53] = False
            button54.destroy()
            if Flag_Exists[54]:
                Num_Of_Flags -= 1
                Flag_Exists[54] = False
            button55.destroy()
            if Flag_Exists[55]:
                Num_Of_Flags -= 1
                Flag_Exists[55] = False
            button63.destroy()
            if Flag_Exists[63]:
                Num_Of_Flags -= 1
                Flag_Exists[63] = False
            button65.destroy()
            if Flag_Exists[65]:
                Num_Of_Flags -= 1
                Flag_Exists[65] = False
            update_mines_left()
            if States[54] == 0 and Button_Called[54] is False:
                Button_54_left()
            if States[63] == 0 and Button_Called[63] is False:
                Button_63_left()
            if States[65] == 0 and Button_Called[65] is False:
                Button_65_left()

    def click64(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[64]
        if {event.num} == {1} and not x:
            Button_64_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button64.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[64] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button64.config(image="")
                Flag_Exists[64] = False

    button64.bind("<Button>", click64)

    def Button_65_left():
        button65.destroy()
        WinCheck()
        global States
        global Button_Called
        Button_Called[65] = True
        global States
        x = States[65]
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button54.destroy()
            if Flag_Exists[54]:
                Num_Of_Flags -= 1
                Flag_Exists[54] = False
            button55.destroy()
            if Flag_Exists[55]:
                Num_Of_Flags -= 1
                Flag_Exists[55] = False
            button56.destroy()
            if Flag_Exists[56]:
                Num_Of_Flags -= 1
                Flag_Exists[56] = False
            button64.destroy()
            if Flag_Exists[64]:
                Num_Of_Flags -= 1
                Flag_Exists[64] = False
            button66.destroy()
            if Flag_Exists[66]:
                Num_Of_Flags -= 1
                Flag_Exists[66] = False
            update_mines_left()
            if States[55] == 0 and Button_Called[55] is False:
                Button_55_left()
            if States[64] == 0 and Button_Called[64] is False:
                Button_64_left()
            if States[66] == 0 and Button_Called[66] is False:
                Button_66_left()

    def click65(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[65]
        if {event.num} == {1} and not x:
            Button_65_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button65.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[65] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button65.config(image="")
                Flag_Exists[65] = False

    button65.bind("<Button>", click65)

    def Button_66_left():
        button66.destroy()
        WinCheck()
        global States
        global Button_Called
        Button_Called[66] = True
        global States
        x = States[66]
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button55.destroy()
            if Flag_Exists[55]:
                Num_Of_Flags -= 1
                Flag_Exists[55] = False
            button56.destroy()
            if Flag_Exists[56]:
                Num_Of_Flags -= 1
                Flag_Exists[56] = False
            button57.destroy()
            if Flag_Exists[57]:
                Num_Of_Flags -= 1
                Flag_Exists[57] = False
            button65.destroy()
            if Flag_Exists[65]:
                Num_Of_Flags -= 1
                Flag_Exists[65] = False
            button67.destroy()
            if Flag_Exists[67]:
                Num_Of_Flags -= 1
                Flag_Exists[67] = False
            update_mines_left()
            if States[56] == 0 and Button_Called[56] is False:
                Button_56_left()
            if States[65] == 0 and Button_Called[65] is False:
                Button_65_left()
            if States[67] == 0 and Button_Called[67] is False:
                Button_67_left()

    def click66(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[66]
        if {event.num} == {1} and not x:
            Button_66_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button66.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[66] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button66.config(image="")
                Flag_Exists[66] = False

    button66.bind("<Button>", click66)

    def Button_67_left():
        button67.destroy()
        WinCheck()
        global States
        global Button_Called
        Button_Called[67] = True
        global States
        x = States[67]
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button56.destroy()
            if Flag_Exists[56]:
                Num_Of_Flags -= 1
                Flag_Exists[56] = False
            button57.destroy()
            if Flag_Exists[57]:
                Num_Of_Flags -= 1
                Flag_Exists[57] = False
            button58.destroy()
            if Flag_Exists[58]:
                Num_Of_Flags -= 1
                Flag_Exists[58] = False
            button66.destroy()
            if Flag_Exists[66]:
                Num_Of_Flags -= 1
                Flag_Exists[66] = False
            button68.destroy()
            if Flag_Exists[68]:
                Num_Of_Flags -= 1
                Flag_Exists[68] = False
            update_mines_left()
            if States[57] == 0 and Button_Called[57] is False:
                Button_57_left()
            if States[66] == 0 and Button_Called[66] is False:
                Button_66_left()
            if States[68] == 0 and Button_Called[68] is False:
                Button_68_left()

    def click67(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[67]
        if {event.num} == {1} and not x:
            Button_67_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button67.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[67] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button67.config(image="")
                Flag_Exists[67] = False

    button67.bind("<Button>", click67)

    def Button_68_left():
        button68.destroy()
        WinCheck()
        global States
        global Button_Called
        Button_Called[68] = True
        global States
        x = States[68]
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button57.destroy()
            if Flag_Exists[57]:
                Num_Of_Flags -= 1
                Flag_Exists[57] = False
            button58.destroy()
            if Flag_Exists[58]:
                Num_Of_Flags -= 1
                Flag_Exists[58] = False
            button59.destroy()
            if Flag_Exists[59]:
                Num_Of_Flags -= 1
                Flag_Exists[59] = False
            button67.destroy()
            if Flag_Exists[67]:
                Num_Of_Flags -= 1
                Flag_Exists[67] = False
            button69.destroy()
            if Flag_Exists[69]:
                Num_Of_Flags -= 1
                Flag_Exists[69] = False
            update_mines_left()
            if States[58] == 0 and Button_Called[58] is False:
                Button_58_left()
            if States[67] == 0 and Button_Called[67] is False:
                Button_67_left()
            if States[69] == 0 and Button_Called[69] is False:
                Button_69_left()

    def click68(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[68]
        if {event.num} == {1} and not x:
            Button_68_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button68.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[68] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button68.config(image="")
                Flag_Exists[68] = False

    button68.bind("<Button>", click68)

    def Button_69_left():
        button69.destroy()
        WinCheck()
        global States
        global Button_Called
        Button_Called[69] = True
        global States
        x = States[69]
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button58.destroy()
            if Flag_Exists[58]:
                Num_Of_Flags -= 1
                Flag_Exists[58] = False
            button59.destroy()
            if Flag_Exists[59]:
                Num_Of_Flags -= 1
                Flag_Exists[59] = False
            button60.destroy()
            if Flag_Exists[60]:
                Num_Of_Flags -= 1
                Flag_Exists[60] = False
            button68.destroy()
            if Flag_Exists[68]:
                Num_Of_Flags -= 1
                Flag_Exists[68] = False
            button70.destroy()
            if Flag_Exists[70]:
                Num_Of_Flags -= 1
                Flag_Exists[70] = False
            update_mines_left()
            if States[59] == 0 and Button_Called[59] is False:
                Button_59_left()
            if States[68] == 0 and Button_Called[68] is False:
                Button_68_left()
            if States[70] == 0 and Button_Called[70] is False:
                Button_70_left()

    def click69(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[69]
        if {event.num} == {1} and not x:
            Button_69_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button69.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[69] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button69.config(image="")
                Flag_Exists[69] = False

    button69.bind("<Button>", click69)

    def Button_70_left():
        button70.destroy()
        WinCheck()
        global States
        global Button_Called
        Button_Called[70] = True
        x = States[70]
        if x == 9:
            game_over()
        elif x == 0:
            global Flag_Exists
            global Num_Of_Flags
            button59.destroy()
            if Flag_Exists[59]:
                Num_Of_Flags -= 1
                Flag_Exists[59] = False
            button60.destroy()
            if Flag_Exists[60]:
                Num_Of_Flags -= 1
                Flag_Exists[60] = False
            button69.destroy()
            if Flag_Exists[69]:
                Num_Of_Flags -= 1
                Flag_Exists[69] = False
            update_mines_left()
            if States[60] == 0 and Button_Called[60] is False:
                Button_60_left()
            if States[69] == 0 and Button_Called[69] is False:
                Button_69_left()

    def click70(event):
        global Moves
        global Flag_Exists
        Moves += 1
        x = Flag_Exists[70]
        if {event.num} == {1} and not x:
            Button_70_left()
        elif {event.num} == {2}:
            global Num_Of_Flags
            if not x:
                button70.config(image=img_flag, bg='White')
                Num_Of_Flags += 1
                update_mines_left()
                Flag_Exists[70] = True
            elif x:
                Num_Of_Flags -= 1
                update_mines_left()
                button70.config(image="")
                Flag_Exists[70] = False

    button70.bind("<Button>", click70)

    # endregion

    Board.mainloop()


if __name__ == '__main__':
    hi = 'WELCOME'
    print(f"{hi:_^19}")
    print("This terminal will output data for testing: \n")

    Main()
