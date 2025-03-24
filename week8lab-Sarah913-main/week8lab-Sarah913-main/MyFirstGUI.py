from tkinter import *

class MyFirstGUI:
    
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        
        self.label1 = Label(master, text="Enter your Firstname")
        self.label1.pack()
        self.entry1 = Entry(master)
        self.entry1.pack()

        self.label2 = Label(master, text="Enter your Surname")
        self.label2.pack()
        self.entry2 = Entry(master)
        self.entry2.pack()

        self.label3 = Label(master, text="Date of birth")
        self.label3.pack()
        self.entry3 = Entry(master)
        self.entry3.pack()

        self.label4 = Label(master, text="Member type")
        self.label4.pack()
        self.entry4 = Entry(master)
        self.entry4.pack()
        
    
        self.insertButton = Button(master, text="Insert Into DB", command=self.insert_into_db)
        self.insertButton.pack()

    
        self.printButton = Button(master, text="Print All Members", command=self.print_members)
        self.printButton.pack()

    
        self.closeButton = Button(master, text="Close", command=self.close)
        self.closeButton.pack()

        self.members = []

    def insert_into_db(self):    
        firstname = self.entry1.get()
        surname = self.entry2.get()
        dob = self.entry3.get()
        member_type = self.entry4.get()

        self.members.append((firstname, surname, dob, member_type))
        print(f"Inserted: {firstname}, {surname}, {dob}, {member_type}")

    def print_members(self):
        print("\n--- All Members ---")
        for member in self.members:
            firstname, surname, dob, member_type = member
            print(f"{firstname}, {surname}, {dob}, {member_type}")

    def close(self):
        self.master.destroy()

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
