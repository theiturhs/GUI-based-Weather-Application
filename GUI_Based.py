import tkinter as tk
import requests
import datetime

###################################
# ENTER YOUR API KEY OVER HERE
# Once entered, it will work

api_key = 'Enter Your API KEY here'

data, temp, feels_like, min_temp, max_temp = 0,0,0,0,0
humidity, ist_sunrise_time, ist_sunset_time, desc = 0,0,0,0

# creating main window and setting its parameters and geometry
window = tk.Tk()
window.geometry('500x500')
window.resizable(False, False)
window.title('Weather Application')
window.configure(bg='#ffffff')

entered_city = tk.StringVar()

def convert_api_time_to_ist(api_sunrise_time):
  ist_timezone = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
  api_sunrise_datetime = datetime.datetime.fromtimestamp(api_sunrise_time, tz=datetime.timezone.utc)
  ist_sunrise_datetime = api_sunrise_datetime.astimezone(ist_timezone)
  return ist_sunrise_datetime

def api_call():
    city = entered_city.get()
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp'] - 273.15
        feels_like = data['main']['feels_like'] - 273.15
        min_temp = data['main']['temp_min'] - 273.15
        max_temp = data['main']['temp_max'] - 273.15
        humidity = data['main']['humidity']
        ist_sunrise_time = convert_api_time_to_ist(data['sys']['sunrise'])
        ist_sunset_time = convert_api_time_to_ist(data['sys']['sunset'])
        desc = data['weather'][0]['description']
        
        tk.Label(window, text='Temperature: '+str(round(temp,2))+'\u00B0C', bg='#ffffff').place(x=250, y=220, anchor=tk.CENTER)
        tk.Label(window, text='Feels like: '+str(round(feels_like,2))+'\u00B0C', bg='#ffffff').place(x=250, y=250, anchor=tk.CENTER)
        tk.Label(window, text='Minimum Temperature: '+str(round(min_temp,2))+'\u00B0C', bg='#ffffff').place(x=250, y=280, anchor=tk.CENTER)
        tk.Label(window, text='Maximum Temperature: '+str(round(max_temp,2))+'\u00B0C', bg='#ffffff').place(x=250, y=310, anchor=tk.CENTER)
        tk.Label(window, text='Humidity: '+str(round(humidity,2))+'%', bg='#ffffff').place(x=250, y=340, anchor=tk.CENTER)
        tk.Label(window, text='Sunrise Time: '+str(ist_sunrise_time)[11:16], bg='#ffffff').place(x=250, y=370, anchor=tk.CENTER)
        tk.Label(window, text='Sunset Time: '+str(ist_sunset_time)[11:16], bg='#ffffff').place(x=250, y=400, anchor=tk.CENTER)
        tk.Label(window, text='Overall: '+desc, bg='#ffffff').place(x=250, y=430, anchor=tk.CENTER)
        
    else:
        tk.Label(window, text='Error! Try again!', bg='#ffffff').place(x=250, y=220, anchor=tk.CENTER)

# main icon placement
main_icon = tk.PhotoImage(file=r"C:\Users\SHRUTI SHRIVASTAVA\Desktop\Shruti\WeatherApp\icon.png")
main_icon = main_icon.subsample(10)

# combine main_icon and mainLabel
combined_label = tk.Label(window, bg='#ffffff', image=main_icon, text='WeatherApplication', compound='left', font=('Lucida Sans', 12))

# set the text property of the label
combined_label.config(text='WeatherApplication')

# pack the label
combined_label.pack(side=tk.LEFT, padx=5, pady=5, anchor=tk.NW)

# sentence using grid layout
sentence = tk.Label(window, bg='#ffffff', text='Hello! Check out the weather!!!', font=('Lucida Sans', 10))
sentence.place(x=250, y=100, anchor=tk.CENTER)

# city input entry using grid layout
city_input = tk.Entry(window, bg='#ffffff', font=('Lucida Sans', 10), width=60, textvariable=entered_city)
city_input.config(bg='#ffffff', bd=1, relief='solid', highlightthickness=0)
city_input.insert(0, 'Enter city name')
city_input.place(x=250, y=140, anchor=tk.CENTER)

# submit button using grid layout
submit_btn = tk.Button(window, bg='#ffffff', text='Check Status', font=('Lucida Sans', 10), command=api_call, width=20)
submit_btn.config(bg='#000000', fg='#ffffff', bd=0.5, relief='solid', activebackground='#fffffd')
submit_btn.place(x=250, y=180, anchor=tk.CENTER)

window.mainloop()
