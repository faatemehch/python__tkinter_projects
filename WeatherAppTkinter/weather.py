from tkinter import *
import requests
from tkinter import messagebox
from io import BytesIO
from PIL import ImageTk, Image

root = Tk()  
root.title("Weather App.")
root.geometry("350x250")
root.resizable(False, False)

def show_weather():
    # img is deleted as soon as the function ends so you need to have that saved as a global variable instead. 
    global img
    city_name = city.get()
    try:
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=d8f310c4694db72dd9df4accd477b9bd'
        response = requests.get(url.format(city_name)).json()
        # create context to extract some needed information
        context = {
                'city': response['name'],  
                'country': response['sys']['country'], 
                'description': response['weather'][0]['description'], 
                'temperature': response['main']['temp'],
                'icon': response['weather'][0]['icon'],
                "main":response["weather"][0]["main"],
            }
        print(context)
    except Exception as e:
        messagebox.showerror("error", "Something went wrong!")
    else:
        if context["main"] == "Rain":
            root.configure(bg="skyblue")
        elif context["main"] == "Clear":
            root.configure(bg="lightgreen")
        elif context["main"] == "Drizzle":
            root.configure(bg="lightgrey")
        elif context["main"] == "Clouds":
            root.configure(bg="#DCDCDC")

        countryLabel["text"] = "Country:"
        countryName["text"] = context["country"]
        cityLabel["text"]= "City"
        cityNameLabel["text"] = context["city"]
        img_url = "http://openweathermap.org/img/w/{}.png".format(context["icon"])
        u = requests.get(img_url)
        img = ImageTk.PhotoImage(Image.open(BytesIO(u.content)))
        imgLabel["text"] =context["main"]
        iconLabel["image"] = img
        tempratureLabel["text"] = "Temprature:"
        tempartur["text"] = str(context["temperature"]) + u"\u00b0"+ "F"
    finally:
        city.delete(0, END)


city = Entry(root)
city.grid(row=0, column=0, ipadx=25)
cityButton = Button(root, text="Go", command=show_weather)
cityButton.grid(row=0, column=1, ipadx=25, ipady=1)

# --------- Weather Info Widgets -----------
countryLabel = Label(root)
countryLabel.grid(row=1, column=0,pady=5, sticky=W, padx=10)
countryName = Label(root)
countryName.grid(row=1, column=1,pady=5)

cityLabel = Label(root)
cityLabel.grid(row=2, column=0,pady=5, sticky=W, padx=10)
cityNameLabel = Label(root)
cityNameLabel.grid(row=2, column=1,pady=5)

imgLabel = Label(root)
imgLabel.grid(row=3, column=0,pady=5, sticky=W, padx=10)

iconLabel = Label(root)
iconLabel.grid(row=3, column=1,pady=5)

tempratureLabel = Label(root)
tempratureLabel.grid(row=4, column=0,pady=5, sticky=W, padx=10)
tempartur = Label(root)
tempartur.grid(row=4, column=1,pady=5)

root.mainloop()