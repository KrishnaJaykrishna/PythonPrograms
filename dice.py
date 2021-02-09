import random
import plotly.express as px
import plotly.figure_factory as ff
diceResult = []
count = []
for i in range(0,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceResult.append(dice1 + dice2)
    count.append(i)
#fig = px.bar(x = diceResult, y = count)
fig = ff.create_distplot([diceResult],['Result'], show_hist = False)
fig.show()
