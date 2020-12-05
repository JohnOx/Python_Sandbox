import json
import turtle
import urllib.request
import time
import webbrowser

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())

file = open("iss.txt", "w")
file.write("There are currently " + str(result["number"]) + " astronauts on the ISS: \n\n")

people = result["people"]
for p in people:
    file.write(p["name"] + " - on board" + "\n")

file.close()
webbrowser.open("iss.txt")

# Set up world map in turtle
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

screen.bgpic("map.gif.gif")
screen.register_shape("iss.gif.gif")
iss = turtle.Turtle()
iss.shape("iss.gif.gif")
iss.setheading(45)
iss.penup()

while True:
    # load current status of iss in real time
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    # extract iss location
    location = result["iss_position"]
    lat = location["latitude"]
    lon = location["longitude"]

    # output lat and lon on terminal
    lat = float(lat)
    lon = float(lon)
    print("\nLatitude: " + str(lat))
    print("\nLongitude: " + str(lon))

    # iss moving on map
    iss.goto(lon, lat)
    # refresh every 5 seconds
    time.sleep(5)
