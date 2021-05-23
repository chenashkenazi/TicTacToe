from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("Welcome to Tic-Tac-Toe ")
window.geometry("400x300")

welcomeLbl = Label(window, text = "Tic-Tac-Toe Game", font=('Helvetica', '15'))
welcomeLbl.grid(row=0, column=0)

playerOneLbl = Label(window, text="Player 1: X", font=('Helvetica', '10'))
playerOneLbl.grid(row=1, column=0)

playerTwoLbl = Label(window, text="Player 2: O", font=('Helvetica', '10'))
playerTwoLbl.grid(row=2, column=0)

#For first person turn.
turn = 1

def clicked(num):
    global turn
    
    if turn == 1:
      turn = 2
      sign = "X"
    elif turn == 2:
      turn = 1
      sign = "O"
      
    if num == 1:
      btn1["text"] = sign
    elif num == 2:
      btn2["text"] = sign
    elif num == 3:
      btn3["text"] = sign
    elif num == 4:
      btn4["text"] = sign
    elif num == 5:
      btn5["text"] = sign
    elif num == 6:
      btn6["text"] = sign
    elif num == 7:
      btn7["text"] = sign
    elif num == 8:
      btn8["text"] = sign
    elif num == 9:
      btn9["text"] = sign
    check()

flag = 1

def check():
    global flag
    b1 = btn1["text"]
    b3 = btn3["text"]
    b4 = btn4["text"]
    b5 = btn5["text"]
    b2 = btn2["text"]
    b6 = btn6["text"]
    b7 = btn7["text"]
    b8 = btn8["text"]
    b9 = btn9["text"]

    flag += 1

    if b1 == b2 and b1 == b3 and b1 == "O" or b1 == b2 and b1 == b3 and b1 == "X":
        win(btn1["text"])

    if b4==b5 and b4==b6 and b4=="O" or b4==b5 and b4==b6 and b4=="X":
        win(btn4["text"])

    if b7==b8 and b7==b9 and b7=="O" or b7==b8 and b7==b9 and b7=="X":
        win(btn7["text"])

    if b1==b4 and b1==b7 and b1=="O" or b1==b4 and b1==b7 and b1=="X":
        win(btn1["text"])

    if b2==b5 and b2==b8 and b2=="O" or b2==b5 and b2==b8 and b2=="X":
        win(btn2["text"])

    if b3==b6 and b3==b9 and b3=="O" or b3==b6 and b3==b9 and b3=="X":
        win(btn3["text"])

    if b1==b5 and b1==b9 and b1=="O" or b1==b5 and b1==b9 and b1=="X":
        win(btn1["text"])

    if b7==b5 and b7==b3 and b7=="O" or b7==b5 and b7==b3 and b7=="X":
        win(btn7["text"])

    if flag == 10:
        messagebox.showinfo("Tie", "Match Tied!!!  Try again :)")
        window.destroy()

def win(player):
    ans = "Game complete " + player + " wins "
    messagebox.showinfo("Congratulations", ans)
    window.destroy()  # is used to close the program


btn1 = Button(window, text=" ", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'), command = lambda: clicked(1))
btn1.grid(column=1, row=1)
btn2 = Button(window, text=" ", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'), command = lambda: clicked(2))
btn2.grid(column=2, row=1)
btn3 = Button(window, text=" ", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'), command = lambda: clicked(3))
btn3.grid(column=3, row=1)
btn4 = Button(window, text=" ", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'), command = lambda: clicked(4))
btn4.grid(column=1, row=2)
btn5 = Button(window, text=" ", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'), command = lambda: clicked(5))
btn5.grid(column=2, row=2)
btn6 = Button(window, text=" ", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica','20'), command = lambda: clicked(6))
btn6.grid(column=3, row=2)
btn7 = Button(window, text=" ", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'), command = lambda: clicked(7))
btn7.grid(column=1, row=3)
btn8 = Button(window, text=" ", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'), command = lambda: clicked(8))
btn8.grid(column=2, row=3)
btn9 = Button(window, text=" ", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica',' 20'), command = lambda: clicked(9))
btn9.grid(column=3, row=3)

window.mainloop()
