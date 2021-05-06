import turtle
import pandas

screen = turtle.Screen()
screen.title('USA States Game')
screen.setup(725, 491)
image = 'states.gif'
screen.addshape(image)
turtle.shape(image)
t = turtle.Turtle()
t.hideturtle()
t.penup()

data = pandas.read_csv('50_states.csv')
states = data.state.to_list()

def write_state(answer):
    state = data[data.state == answer]
    t.goto(int(state.x), int(state.y))
    t.write(answer, False, 'center')  # state.state.item()

while len(states) > 0:
    try:
        answer_state = screen.textinput(f'{50 - len(states)}/50 States correct', "What is another state's name?").title()
    except:
        break
    if answer_state in states:
        states.remove(answer_state)
        write_state(answer_state)

for state in states:
    write_state(state)
df = pandas.DataFrame(states)
df.to_csv('states_to_learn.csv')
screen.exitonclick()
