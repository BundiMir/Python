# convert farenheit to celsius
fahrenheit = 75
celsius = (fahrenheit - 32) / 1.8
print(int(celsius))

# convert miles to km & meters
miles = 5
km = miles / 0.62137
meters = 1000 * km
print("Miles: " + str(miles))
print("Km: " + str(round(km,4)))
print("Meters: " + str(round(meters,4)))

a = "gutten morgen"[3:6]
print(a.upper())

a = "racetrack"[1:4]
print(a.capitalize())

'some_string'.find("ing")

a = "python 4 ever&EVER"

a.find("E")
a.find("eve")
a.rfind("rev")
a.rfind("VER")
a.find(" ")
a.rfind(" ")

"on" in a
"" in a
"2 * 2" in a

a.count("ev")
a.count(" ")
a.count(" 4 ")
a.count("eVer")

a = "Raining in the spring time."

a.replace("R", "r")
a.replace("ing", "")
a.replace("!", ".")
b = a.replace("time","tiempo")

print(a)

"la" + "la" + "Land"

"USA" + " vs " + "Canada"

b = "NYc"
c = 5
b * c

color = "red"
shape = "circle"
number = 3
number * (color + "-" + shape)

a = "Eat Work Play Sleep repeat"
a = a.replace(" ","ing ")
start = a.find("Working")
end = a.find("Sleep")-1
a = a[start:end]
print(a)
