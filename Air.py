from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime 
import requests
import pytz 
import os
from dotenv import load_dotenv

root = Tk()
root.title("🌤 Weather & Time App")
root.geometry("1000x600+250+100")
root.resizable(False, False)
root.configure(bg="#2b2d42")

title_label = Label(root, text="📍 Weather & Time", font=("Poppins", 26, "bold"), 
                    fg="white", bg="#2b2d42")
title_label.pack(pady=10)


def getwheather():
    try:    
        city = text_field.get()
        
        geolocator = Nominatim(user_agent = "myGeopy67", timeout = 10) 
        location = geolocator.geocode(city)       #Geographic coordinates 
        obj = TimezoneFinder()
        result = obj.timezone_at(lng = location.longitude, lat = location.latitude)
        
        h = pytz.timezone(result)
        local_time = datetime.now(h)
        current_time = local_time.strftime("%I:%M:%p") #current time convert to string time
        name.config(text = "CURRENT WEATHER")
        
        clock.config(text = current_time) 
        
        load_dotenv()
        api_key = os.getenv('API_KEY')
        
        #Weather                                     #must be "q="
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        
        t.config(text = (temp,"°"))
        c.config(text = (condition, "|", "FEELS", "LIKE", temp, "°"))
        
        
        p1.config(text = wind)
        p2.config(text = humidity)
        p3.config(text = description)
        p4.config(text = pressure)
        
    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Data!")

#Search box
search_frame = Frame(root, bg="#3a3f58", bd=0, relief="flat")
search_frame.place(x=250, y=70)

#Widget for user
text_field = tk.Entry(search_frame, justify="center", width=20, font=("Poppins", 20, "bold"),
                      bg="#edf2f4", border=0, fg="#2b2d42")
text_field.grid(row=0, column=0, padx=10, pady=10)
text_field.focus()


#Search botton
search_btn = Button(search_frame, text="🔍 Search", font=("Poppins", 14, "bold"),
                    bg="#FFB300", fg="white", activebackground="#73C5EE", cursor="hand2",
                    padx=10, pady=5, bd=0, relief="flat", command = getwheather)
search_btn.grid(row=0, column=1, padx=5)

#Logo
logo_image = PhotoImage(file="image/logo2.jpg")
logo = Label(root, image = logo_image, bg="#2b2d42")
logo.place(x = 656, y = 150)

#Time
name = Label(root, font=("Arial", 16, "bold"), fg="white", bg="#2b2d42")
name.place(x=50, y=150)

clock = Label(root, font=("Helvetica", 34), fg="#ffd166", bg="#2b2d42")
clock.place(x=50, y=190)


#Botton box
info_frame = Frame(root, bg="#edf2f4", bd=0, relief="flat")
info_frame.place(x = 80, y = 500, width = 850, height = 90)


#Label
label_1 = Label(root, text = "WIND", font = ("Helvetica", 16, 'bold'), fg = "black", bg = "#edf2f4")
label_1.place(x = 80, y = 500)

label_2 = Label(root, text = "HUMIDITY", font = ("Helvetica", 16, 'bold'), fg = "black", bg = "#edf2f4")
label_2.place(x = 270, y = 500)

label_3 = Label(root, text = "DESCRIPTION", font = ("Helvetica", 16, 'bold'), fg = "black", bg = "#edf2f4")
label_3.place(x = 480, y = 500)

label_4 = Label(root, text = "PRESSURE", font = ("Helvetica", 16, 'bold'), fg = "black", bg = "#edf2f4")
label_4.place(x = 800, y = 500)

t = Label(root, font = ("arial", 90, "bold"), fg = "#FDD835", bg="#2b2d42") 
t.place(x = 350, y = 200)
c = Label(root, font = ("arial", 20, "bold"),fg = "white", bg="#2b2d42")
c.place(x = 260, y = 350)



p1 = Label(text = "...", font = ("arival", 24, "bold"), fg="#008CEF", bg = "#edf2f4")
p1.place(x = 80 , y = 540)
p2 = Label(text = "...", font = ("arival", 24, "bold"), fg="#008CEF", bg = "#edf2f4")
p2.place(x = 270 , y = 540)
p3 = Label(text = "...", font = ("arival", 24, "bold"), fg="#008CEF", bg = "#edf2f4")
p3.place(x = 480 , y = 540)
p4 = Label(text = "...", font = ("arival", 24, "bold"), fg="#008CEF", bg = "#edf2f4")
p4.place(x = 800 , y = 540)

root.mainloop()