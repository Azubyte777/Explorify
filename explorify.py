#Brian E.
import tkinter as tk
from tkinter import messagebox, ttk
import core, requests, sv_ttk
from dotenv import load_dotenv
from PIL import ImageTk, Image
from io import BytesIO
from tktooltip import ToolTip

load_dotenv() #loads environment variables

""" Opens the 2nd window where user can choose the artist (by image) for playlist creation
   @param dictionary - Dictionary containing artists links, images and names for user to select from 
   @param radiostatus - Flag showing what radio button was selected prior to user choosing an artist
"""

def resize():
  print("Reset the grid to the size of just one picture and the load bar below it showin a percentage listened, let it call a func to do that too, and let it close after playlist creation")
def open_secondary_window(dictionary, radiostatus):
    
    secondary_window = tk.Toplevel()
    secondary_window.title("Secondary Window")
    secondary_window.resizable(0,0)
    
    temp_ref_img_list = [] #Holds images a permanent reference for tkinter
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    buttons = dict()
    tooltips = dict()
    for k in range(len(dictionary["artist_image"])):
      img_url = dictionary["artist_image"][k]
      response = requests.get(img_url, headers=headers)
      img_data = response.content
      permpic = ImageTk.PhotoImage(Image.open(BytesIO(img_data)).resize((160,160))) 
      buttons[k] = ttk.Button(secondary_window, image = permpic, command=lambda link=dictionary["artist_link"][k], name=dictionary["artist_name"][k], option=radiostatus: create_playlist(link, name, option))
      buttons[k].grid(row = k//3, column = k%3)
      buttons[k].image = permpic
      tooltips[k] = ToolTip(buttons[k], msg=dictionary["artist_name"][k], delay=2.0)
      temp_ref_img_list.append(permpic)
        
    button_close = ttk.Button(secondary_window, text="Close window", command=secondary_window.destroy)

    secondary_window.focus()
    secondary_window.grab_set()

""" Creates the playlist based on users artist selection
   @param artist_url - Url of the artist 
   @param artist_name - Name of the artist
   @param status - Flag showing what radio button was selected prior to user choosing an artist
"""     
def create_playlist(artist_url, artist_name, status):
  messagebox.showinfo(title="In progess", message=str(artist_name) +" playlist creation in progress. Please wait.")
  if status == "Full":
    core.trial.add__tracks_to_playlist(artist_url, artist_name)
  else:
    core.trial.add_popular_tracks(artist_url, artist_name)
  
  messagebox.showinfo(title="Complete!", message="Playlist created, close & open your Spotify!")

"""Tkinter main window
"""  
class myGUI:
  def __init__(self):
    core.trial = core.myExplorify()
    self.root = tk.Tk()
    self.root.resizable(0,0)
    self.root.geometry("300x270")
    sv_ttk.set_theme("dark")
    
    logo = ImageTk.PhotoImage(Image.open("explorifylogo.png"))
    panel = ttk.Label(self.root, image = logo)
    panel.pack(side = "top", fill = "x")
    self.label = ttk.Label(self.root, text="Input artist name", font=("Arial", 10))
    self.label.pack(padx=20, pady=10)
    
    self.myentry = ttk.Entry(self.root)
    self.myentry.pack(padx=10)
    
    self.button = ttk.Button(self.root, text= "Enter", command=self.start_program)
    self.button.pack()
    
    self.var = tk.StringVar()
    self.radiobutton_one = ttk.Radiobutton(text='Full', variable=self.var, value="Full")
    self.radiobutton_one.pack(anchor="w")
    self.radiobutton_two = ttk.Radiobutton(text='Capped', variable=self.var, value="Capped")
    self.radiobutton_two.pack(anchor="w")
    
    self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    self.root.mainloop()
    
  def start_program(self):
    self.button.config(state="disabled", text="Running")
    
    core.trial.display_artists(self.myentry.get())
    artist_data_dict = core.trial.artist_dict
    open_secondary_window(artist_data_dict, self.var.get())
    
    self.button.config(state="active", text="Enter")
    
    self.myentry.delete(0, tk.END)  

  def on_closing(self):
    if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
      self.root.destroy()  

myGUI()  

