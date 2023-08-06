import turtle
import pandas as pd

screen = turtle.Screen()
image = "Europe.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("Countries-Europe.csv")

country = data["name"].to_list()
guessed_countries = []

while len(guessed_countries) < 50:
    ans_country = screen.textinput(title=f"{len(guessed_countries)}/44 Countries Correct", prompt="Your guess?").title()

    if ans_country == "Exit":
        break

    if ans_country in country:
        guessed_countries.append(ans_country)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        country_data = data[data.name == ans_country]
        t.goto(int(country_data.x), int(country_data.y))
        t.write(ans_country)
        country.remove(ans_country)


missed_states = pd.DataFrame(country)

missed_states.to_csv("missed_countries.csv")