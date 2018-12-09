from data import dataset
from task1 import *
from task3 import recursionByNumber
import plotly
import plotly.graph_objs as go


#Вивести стовпчикову діаграму: хто скільки грошей витратив.

data = recursionByNumber()

diagram = go.Bar(x = list(data.keys()), y = list (data.values()))

plotly.offline.plot([data])