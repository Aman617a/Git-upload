import turtle
from turtle import  Turtle,Screen
import pandas
import time
screen=Screen()
screen.setup(700,700)

# screen.bgpic("blank_states_img.gif")
image="blank_states_img.gif"
screen.addshape(image)
screen.title("U.S.States Game")
turtle.shape(image)
data=pandas.read_csv("50_states.csv")
state_names=data["state"].to_list()
state_names_dupe=data["state"].to_list()
state_x=data["x"].to_list()
state_y=data["y"].to_list()
guess=[]
a=0
while len(guess)<=50:

    user_guess=(turtle.textinput(f"{a}/50 States correct","Guess a state")).title()

    if user_guess=="Exit":
        break


    if user_guess in state_names:
        tim = Turtle()
        tim.pu()
        tim.hideturtle()
        index=state_names.index(user_guess)
        a+=1
        guess.append(user_guess)
        tim.goto(x=state_x[index],y=state_y[index])
        tim.write(f"{user_guess}")
        state_names_dupe.remove(user_guess)


new_data=pandas.DataFrame(state_names_dupe)
new_data.to_csv("states missed.csv")

#
#
#
#
#
#
#
#




