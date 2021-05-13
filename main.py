from tkinter import *
from tkinter import messagebox
import json
import requests

BACKGROUND_COLOR = "#a0edff"
OWM_endpoint = ("https://api.openweathermap.org/data/2.5/weather?")
api_key = "Your_key"


# Takes information that user provided.
def data_fetcher():
	city_name = city_input.get()
	latitude_data = lat_input.get()
	longitude_data = long_input.get()

	# API requests parameteres
	# If user requests data by city name then, city_parameteres is used.
	city_parameteres = {"q": city_name, "appid": api_key, "units": "metric"}
	# If user requests data by coordinates then, gro_parameteres is used.
	geo_parameteres = {"lat": "32.776665", "lon": "-96.796989", "appid": api_key, "units": "metric"}
	# Check if user entered data into the city field
	if len(city_name) > 0:
		get_weather(city_parameteres)
	# Check if user entered data into the latitude and longitude fields
	elif len(latitude_data) > 0 and len(longitude_data) > 0:
		get_weather(geo_parameteres)
	else:
		# Error messag box if no info or wrong info was provided
		messagebox.showinfo(title="Oops", message="Please insert a valid city name")


#--------------- Fetching weather data ---------		
def get_weather(parameter_data):
	# parameter_data depends on whether the user provided the city or coordinates
	response = requests.get(OWM_endpoint, params=parameter_data)
	response.raise_for_status()

	temp = response.json()["main"]["temp"]
	feels_like = response.json()["main"]["feels_like"]
	min_temp = response.json()["main"]["temp_min"]
	max_temp = response.json()["main"]["temp_max"]
	# Data formated with f-string to display on canvas.
	canvas.itemconfig(canvas_text, text=f"Temperature: {temp:.0f}°C\nFeels_like: {feels_like:.0f}°C\nMin_temp: {min_temp:.0f}°C\nMax_temp: {max_temp:.0f}°C")


#-------------- App UI ------------
window = Tk()
window.title("Weather")
window.geometry("750x700")

# Creating a background using a label.
bg = PhotoImage(file="blue_sky.png")
wallpaper = Label(image=bg)
wallpaper.place(x=0, y=0,relwidth=1, relheight=1)


# Canvas to display weather information
canvas = Canvas(width=400, height=250, bg="white")
canvas.grid(row=6, column=1, columnspan=2, pady=40)
canvas_text = canvas.create_text(200, 125, text="data goes here", font=("Ariel", 15, "italic"), width=210, anchor="center")


# Creating Text Labels
weather_text = Label(text="Weather 4 U", font=("Helvetica", 15, "bold"), bg=BACKGROUND_COLOR, bd=0)
weather_text.grid(row=0, column=1, padx=20, pady=20, columnspan=2)

search_text_1 = Label(text="Search by:", font=("Helvetica", 15, "bold"), bg=BACKGROUND_COLOR, bd=0)
search_text_1.grid(row=1, column=0, padx=20, pady=20)

search_text_2 = Label(text="Search by:", font=("Helvetica", 15, "bold"), bg=BACKGROUND_COLOR, bd=0)
search_text_2.grid(row=3, column=0, padx=20, pady=20)

city_text = Label(text="City name:", font=("Helvetica", 15, "bold"), bg=BACKGROUND_COLOR, bd=0)
city_text.grid(row=2, column=0, pady=20)

lat_text = Label(text="Latitude:", font=("Helvetica", 15, "bold"), bg="#e2f9ff", bd=0)
lat_text.grid(row=4, column=0, pady=20)

long_text = Label(text="Longitude:", font=("Helvetica", 15, "bold"), bg=BACKGROUND_COLOR, bd=0)
long_text.grid(row=4, column=2, padx=20)

# Data Input bars
city_input = Entry(width=25)
city_input.grid(row=2, column=1)

lat_input = Entry(width=25)
lat_input.grid(row=4, column=1)

long_input = Entry(width=25)
long_input.grid(row=4, column=3)

# Search button
search_button = Button(text="Search", font=("Helvetica", 10, "bold"),command=data_fetcher)
search_button.config(width=43, bg=BACKGROUND_COLOR)
search_button.grid(row=5, column=1, columnspan=2)








window.mainloop()