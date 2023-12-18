import tkinter as tk
import tkinter.ttk as ttk

# Creating a window instance
window = tk.Tk()

#Adding a greeting
greeting = tk.Label(
    text = "Hello, Tkinter",
    fg = "white",
    bg = "black",
    width = 10,
    height = 10
    ) #Label is used to display text or images, height and width in text unigts based on the character "0"
greeting.pack()

#Making a button
button = tk.Button(
    text = "Click here.",
    width = 25,
    height = 5,
    bg = "blue",
    fg = "yellow"
)
button.pack()

#User input
label = tk.Label(text = "Name")
entry = tk.Entry()

#Display widgets
label.pack()
entry.pack()

#Store entered data
name = entry.get() #Retrieves entered data
name

#Modifying collected data
entry.delete(0, 4) #Deletes first four
entry.insert(0, "Real Python") #Inserts text at position 0

#Closes previously opened window
# window.destroy()

#Multiline user input
text_box = tk.Text()
text_box.pack()

#Collecting data from text box
text_box.get("1.0") #"line.index"
text_box.get("2.0", "2.5") #start point, endpoint
text_box.get("1.0", tk.END) #Retrieves all text in a text box

#.delete() and .insert() work in the same way, may need \n char for insertiing a new line

#Run the tkinter event loop - lstens for clicks, keypresses, and blocks any code that runs after it
window.mainloop()

