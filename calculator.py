import tkinter as tk 

WIDTH = 400
HEIGHT = 300

win = tk.Tk()
win.title("Calculator")

# when a number is clicked
def on_click(num):
	cur = entry.get()
	
	entry.delete(0, "end")
	entry.insert(0, str(cur) + str(num))


# deletes one digit
def on_del():
	num = len(entry.get())
	entry.delete(num - 1, "end")


# deletes all digits
def on_clear():
	entry.delete(0, "end")


# gets a number to add
def on_add():
	global num1
	global op
	op = "add"
	num1 = entry.get()
	num1 = float(num1)	
	entry.delete(0, "end")

# gets a number to delete
def on_sub():
	global num1
	global op
	op = "sub"
	num1 = entry.get()
	num1 = float(num1)
	entry.delete(0, "end")

# gets number to multiply
def on_mult():
	global num1
	global op
	op = "mult"
	num1 = entry.get()
	num1 = float(num1)
	entry.delete(0, "end")


# gets number to divide
def on_div():
	global num1
	global op
	op = "div"
	num1 = entry.get()
	num1 = float(num1)
	entry.delete(0, "end")


# performs the desired action on two numbers
def on_equals():
	num2 = entry.get()
	num2 = float(num2)
	
	entry.delete(0, "end")
	if op == "add":
		total = num1 + num2
		round(total, 5)
		entry.insert(0, str(total))
	elif op == "sub":
		total = num1 - num2
		round(total, 5)
		entry.insert(0, str(num1 - num2))
	elif op == "mult":
		total = num1*num2
		round(total, 5)
		entry.insert(0, str(total))
	elif op == "div":
		total = num1/num2
		round(total, 5)
		print(total)
		entry.insert(0, str(total))


# adds decimal pofloat to number so user can input floats
def add_decimal():
	cur = entry.get()
	new = entry.get() + "."
	entry.delete(0, "end")
	entry.insert(0, new)


####Graphics####

entry = tk.Entry(width = 20, font = 100)
entry.grid(row = 0, columnspan = 4, pady = 30)

# Number (0-9) graphics
button0 = tk.Button(win, text = "0", padx = 68, pady = 30, command = lambda: on_click(0))
button1 = tk.Button(win, text = "1", padx = 30, pady = 30, command = lambda: on_click(1))
button2 = tk.Button(win, text = "2", padx = 30, pady = 30, command = lambda: on_click(2))
button3 = tk.Button(win, text = "3", padx = 30, pady = 30, command = lambda: on_click(3))
button4 = tk.Button(win, text = "4", padx = 30, pady = 30, command = lambda: on_click(4))
button5 = tk.Button(win, text = "5", padx = 30, pady = 30, command = lambda: on_click(5))
button6 = tk.Button(win, text = "6", padx = 30, pady = 30, command = lambda: on_click(6))
button7 = tk.Button(win, text = "7", padx = 30, pady = 30, command = lambda: on_click(7))
button8 = tk.Button(win, text = "8", padx = 30, pady = 30, command = lambda: on_click(8))
button9 = tk.Button(win, text = "9", padx = 30, pady = 30, command = lambda: on_click(9))

button9.grid(row = 1, column = 0)
button8.grid(row = 1, column = 1)
button7.grid(row = 1, column = 2)
button6.grid(row = 2, column = 0)
button5.grid(row = 2, column = 1)
button4.grid(row = 2, column = 2)
button3.grid(row = 3, column = 0)
button2.grid(row = 3, column = 1)
button1.grid(row = 3, column = 2)
button0.grid(row = 4, columnspan = 2)

# Operation button graphics
button_div = tk.Button(win, text = "/",padx = 30, pady = 30, bg = "orange", command = on_div)
button_mult = tk.Button(win, text = "x", pady = 30, padx = 30,bg = "orange", command = on_mult)
button_subtract = tk.Button(win, text = "-", padx = 30, pady = 30, bg = "orange", command = on_sub)
button_add = tk.Button(win, text = "+", padx = 30, pady = 30,bg = "orange", command = on_add)
button_del = tk.Button(win, text = "Del", padx = 25, pady = 30, bg = "orange", command = on_del)
button_clear_all = tk.Button(win, text = "AC", bg = "red", padx = 60, pady = 30, command = on_clear)
button_equals = tk.Button(win, text = "=", bg = "lightgreen", padx = 30, pady = 30, command = on_equals)
button_decimal = tk.Button(win, text = ".", padx = 30, pady = 30, command = add_decimal)


button_div.grid(row = 1, column = 3)
button_mult.grid(row = 2, column = 3)
button_subtract.grid(row = 3, column = 3)
button_add.grid(row = 4, column = 3)
button_del.grid(row = 5, column = 0)
button_clear_all.grid(row = 5, column = 1, columnspan = 2)
button_equals.grid(row = 5, column = 3)
button_decimal.grid(row = 4, column = 2)

win.mainloop()