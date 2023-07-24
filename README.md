# GUI-based-Weather-Application
The code is for a weather application that uses the OpenWeatherMap API. The application allows the user to enter the name of a city and then displays the weather data for that city, including the temperature, feels like temperature, minimum temperature, maximum temperature, humidity, sunrise time, sunset time, and overall description. The application also includes error handling in case the HTTP request to the OpenWeatherMap API fails.

NOTE: Replace the API Key in the code. Otherwise it will throw error!!!!!

The steps on how to use the application:

1. Enter the name of the city in the entry field.
2. Click the "Check Status" button.
3. The weather data for the city will be displayed on the GUI window.

Some of the key features of the code:

The code uses the tkinter module to create a GUI window.
The code uses the requests module to make HTTP requests.
The code uses the convert_api_time_to_ist() function to convert the sunrise and sunset times from the OpenWeatherMap API to IST.
The code uses the api_call() function to retrieve the weather data for the city that is entered by the user.
The code includes some error handling.

The main window looks like:

![image](https://github.com/theiturhs/GUI-based-Weather-Application/assets/96874023/99fc7518-3acc-45af-88df-bc53b2bad12f)

Further, 

![image](https://github.com/theiturhs/GUI-based-Weather-Application/assets/96874023/ae07bfa4-0a37-4a8a-86cb-a478346d8b45)


![image](https://github.com/theiturhs/GUI-based-Weather-Application/assets/96874023/1b560f8c-e58f-4c1f-b617-2b3f35464b6a)
