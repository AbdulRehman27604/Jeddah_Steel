import tkinter as tk
from tkinter import messagebox
import calc_excel
import random
JS = tk.Tk()
PK = tk.Tk()
e1 = ""
e2 = ""
e3 = ""

def run_jeddah_Steel():
    layout()
    value_items()
    menu_bar()
    measurements_layout()
    JS.mainloop()

def layout():
    JS.geometry("1270x500")
    JS.configure(bg="#333333")
    JS.title("Jeddah Steel Interface")
    label = tk.Label(JS, text="Jeddah Steel Pvt Ltd", height=10, font=("Helvetica", 20, "bold italic"), fg="Yellow", bg="#333333")
    label.place(x=1050, y=10, height=40, width=210)

def buttonFunctionality(width, utilize, wastage, weightMM, Tpipe, DCno, order_no, comment, company, coil_type):
    import calc_excel
    global CLEAR, e1, e2, e3
    if width == "" and utilize == "" and wastage == "" and weightMM == "" and Tpipe == "" and DCno == "" and order_no == "" and comment == "" and company == "" and coil_type == "":
        messagebox.showerror("Error", "One or more fields are empty or not choosen")
        return

    confirmation = messagebox.askyesno("Confirm Input", "Are you sure you want to submit the data?")
    if confirmation:
        messagebox.showinfo("Success", "Data submitted successfully!")
        calc_excel.write_data(e1, e2, e3, width, utilize, wastage, weightMM, Tpipe, DCno, order_no, comment, company, coil_type)
    else:
        messagebox.showinfo("Cancelled", "Submission cancelled.")


def value_items():
    global e1, e2, e3
    grid_frame = JS

    tk.Label(grid_frame, text="Cutting Job:", bg="#333333", font=("Times", 20), fg="white").grid(row=0, column=0)
    tk.Label(grid_frame, text='Job Number:', bg="#333333", font=("Times", 16), fg="white").grid(row=1, column=0)
    tk.Label(grid_frame, text='Supplier Code:', font=("Times", 16), bg="#333333", fg="white").grid(row=2, column=0)
    tk.Label(grid_frame, text='Broker Code:', font=("Times", 16), bg="#333333", fg="white").grid(row=3, column=0)

    # Create Entry widgets and assign them to variables
    e1 = tk.Entry(grid_frame)
    e1.grid(row=1, column=1)
    e2 = tk.Entry(grid_frame)
    e2.grid(row=2, column=1)
    e3 = tk.Entry(grid_frame)
    e3.grid(row=3, column=1)

    cutting_job = "#" + str(random.randint(1000, 9999))
    e1.insert(0, str(cutting_job))

def menu_bar():
    home = tk.Menu(JS)
    JS.configure(menu=home)
    file_menu = tk.Menu(home)
    home.add_cascade(label="Home",menu=file_menu)
    file_menu.add_command(label="Cutting Job")
    file_menu.add_command(label="Transactions")
    file_menu.add_separator()
    file_menu.add_command(label='Exit', command=JS.quit)

def measurements_layout():
    tk.Label(JS, text="Width:", font=("Times", 16), fg="white", bg="black").place(x=400, y=70, height=30, width=120)
    width = tk.Entry(JS)
    width.place(x=525, y=70, height=30, width=120)

    tk.Label(JS, text="Utilize:", font=("Times", 16), fg="white", bg="black").place(x=400, y=112, height=30, width=120)
    utilize = tk.Entry(JS)
    utilize.place(x=525, y=112, height=30, width=120)

    tk.Label(JS, text="Wastage:", font=("Times", 16), fg="white", bg="black").place(x=400, y=154, height=30, width=120)
    wastage = tk.Entry(JS)
    wastage.place(x=525, y=154, height=30, width=120)

    tk.Label(JS, text="Weight MM:", font=("Times", 16), fg="white", bg="black").place(x=660, y=70, height=30, width=120)
    weightMM = tk.Entry(JS)
    weightMM.place(x=785, y=70, height=30, width=120)

    tk.Label(JS, text="T.pipe:", font=("Times", 16), fg="white", bg="black").place(x=660, y=112, height=30, width=120)
    Tpipe = tk.Entry(JS)
    Tpipe.place(x=785, y=112, height=30, width=120)

    tk.Label(JS, text="DC No:", font=("Times", 16), fg="white", bg="black").place(x=920, y=112, height=30, width=120)
    DCno = tk.Entry(JS)
    DCno.place(x=1045, y=112, height=30, width=120)

    tk.Label(JS, text="Order No:", font=("Times", 16), fg="white", bg="black").place(x=920, y=70, height=30, width=120)
    order_no = tk.Entry(JS)
    order_no.place(x=1045, y=70, height=30, width=120)

    tk.Label(text="Comments:", bg="black", font=("Times", 16), fg="white").place(x=7, y=202, height=30, width=115)
    comment = tk.Text(JS)
    comment.place(x=130, y=200, height=55, width=250)

    tk.Label(JS, text="Supplier Name:", font=("Times", 16), fg="white", bg="black").place(x=6, y=142, height=30,
                                                                                          width=120)
    new_box = tk.Listbox(JS)
    new_box.insert(tk.END, "- AISHA STEEL LTD")
    new_box.insert(tk.END, "- GUL DEEWAN")
    new_box.insert(tk.END, "- China")
    new_box.insert(tk.END, "- P&O")
    new_box.place(x=129, y=132, height=55, width=250)

    selected_item = new_box.curselection()
    if selected_item:
        selected_value = new_box.get(selected_item)
    else:
        selected_value = None
    # Coil Type
    tk.Label(JS, text="Coil Type:", font=("Times", 16), fg="white", bg="black").place(x=850, y=400, height=30,
                                                                                      width=120)
    box = tk.Listbox(JS)
    box.insert(tk.END, "- CRC")
    box.insert(tk.END, "- HRC")
    box.insert(tk.END, "- GI")
    box.insert(tk.END, "- P&O")
    box.place(x=850, y=430, height=55, width=250)

    selected_coil = box.curselection()
    if selected_coil:
        selected_coil_value = box.get(selected_coil)
    else:
        selected_coil_value = None

    com_button = tk.Button(JS, text="Submit", font=("Times", 20, "bold"), fg="red",command=lambda:company())

    button = tk.Button(JS, text="Submit", font=("Times", 20, "bold"), fg="red",
                       command=lambda: buttonFunctionality(width.get(), utilize.get(), wastage.get(), weightMM.get(),
                                                           Tpipe.get(), DCno.get(), order_no.get(),
                                                           comment.get("1.0", "end-1c"), selected_value, selected_coil_value))
    button.place(x=1140, y=445, height=50, width=120)

    button_clear = tk.Button(JS, text="Clear", font=("Times", 20, "bold"), fg="red",
                             command=lambda: clear_fields(width, utilize, wastage, weightMM, Tpipe, DCno, order_no,
                                                          comment))
    button_clear.place(x=1140, y=380, height=50, width=120)

    #search items on a specific date
    item_date = tk.Entry(JS)
    item_date.place(x=12, y=259)
    search_item = tk.Button(JS, text="Search", font=("Times", 10, "bold"), fg="red", command=lambda: search_items(item_date.get())).place(x=210,y=260)

def search_items(item_date):
    find_box = tk.Text(JS, height=15, width=100)
    find_box.place(x=11, y=290)  # Place the widget separately
    result = calc_excel.search_date(item_date)  # Call search_date with item_date
    find_box.delete("1.0", "end")  # Clear previous content in the text box
    find_box.insert("1.0", result)  # Insert the result into the text box

def clear_fields(width, utilize, wastage, weightMM, Tpipe, DCno, order_no, comment):

    width.delete(0, "end")
    utilize.delete(0, "end")
    wastage.delete(0, "end")
    weightMM.delete(0, "end")
    Tpipe.delete(0, "end")
    DCno.delete(0, "end")
    order_no.delete(0, "end")
    comment.delete(1.0, "end")

def password_main_layout():

    PK.geometry("1270x500")
    PK.configure(bg="#333333")
    PK.title("Jeddah Steel Interface")
    label = tk.Label(PK, text="Jeddah Steel Pvt Ltd", height=10, font=("Times", 50), fg="Yellow", bg="#333333")
    label.place(x=370, y=10, height=40, width=500)

    tk.Label(PK, text="Admin: ", font=("Arial", 18), fg="white").place(x=500, y=250)
    username_entry = tk.Entry(PK, font=("Arial", 18))
    username_entry.place(x=600, y=250, height=30, width=180)

    tk.Label(PK, text="Password: ", font=("Arial", 18), fg="white").place(x=500, y=300)
    password_entry = tk.Entry(PK, font=("Arial", 18), show="*")
    password_entry.place(x=600, y=300, height=30, width=180)

    btn_login = tk.Button(PK, text="Login", font=("Arial", 18), command=lambda: is_password_ok(username_entry.get(), password_entry.get()))
    btn_login.place(x=600, y=350)

    PK.mainloop()

def is_password_ok(username, password):
    if username == "" or password == "":
        messagebox.showerror("Invaild", "One of the required fields are empty")
    else:
        filename = open("pass.txt", "r")
        for line in filename:
            line = line.strip()
            line_array = line.split(",")
            if line_array[0] == username and line_array[1] == password:
                PK.destroy()
                run_jeddah_Steel()
    pass

password_main_layout()
run_jeddah_Steel()
