import tkinter as tk
import random
import string
def generate_password():
    length=18
    chars=string.ascii_letters+string.digits+string.punctuation
    password=" ".join(random.choice(chars)for i in range(length))
    return password
def update_passlabel():
    password=generate_password()
    passchar.set(password)
    
    
r=tk.Tk()
r.title("PASSWORD GENERATOR")
passchar=tk.StringVar()
pass_label=tk.Label(r,textvariable=passchar,font=('Times new Roman',15,'bold'),foreground='blue',relief='solid')
pass_label.pack(pady=50)
button=tk.Button(r,text="Generate password",command=update_passlabel)
button.pack()
update_passlabel()
r.mainloop()
    
