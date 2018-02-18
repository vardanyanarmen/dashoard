#Graph 1
from plotly.offline import iplot,plot
import pandas as pd
import numpy as np
import plotly.graph_objs as go
trace1=go.Bar(x=[15,50,15,20],y=["x8","x7","x6","x5"],orientation = 'h',marker=dict(color="RGB(255,174,185)"),name="Negative")
trace2=go.Bar(x=[-15,-45,-5,-35],y=["x4","x3","x2","x1"],orientation = 'h',marker=dict(color="lightblue"),name="Positive")
layout  = dict(title="Correlation with employees probability of churn",yaxis=dict(title="Variable"),showlegend=True)
fig1=dict(data=[trace1,trace2],layout=layout)



#Graph 2
import quandl
quandl.ApiConfig.api_key = "ALxK4Ss3NGDxcyE2pXns"
data = quandl.get("FRED/GDP")

from plotly.offline import plot, iplot
import plotly.graph_objs as go

import pandas as pd

x = pd.to_datetime(data.index.values)



y = data["Value"]
trace = go.Scatter(x=x, y=y ,mode="lines",fill="tozeroy")
       
layout = go.Layout(title='US GDP over time')
data = [trace]
fig2 = dict(data=data,layout=layout)


#Graph3
from plotly.offline import plot, iplot
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode
init_notebook_mode(connected=True)

import numpy as np

import quandl
quandl.ApiConfig.api_key = "ALxK4Ss3NGDxcyE2pXns"
mydata1 = quandl.get("WIKI/GOOGL")
mydata2=quandl.get("BCHARTS/ABUCOINSUSD")

trace_1 = go.Box(x=mydata1.Open.pct_change(),name="Google")
trace_2 = go.Box(x=mydata2.Open.pct_change(),name="Bitcoin")
layout=dict(title="Distribution of Price Change")
data = [trace_2,trace_1]
fig3 = dict(data=data,layout=layout)



#Graph 4
from plotly.offline import plot, iplot
import plotly.graph_objs as go
import numpy as np

import quandl
quandl.ApiConfig.api_key = "ALxK4Ss3NGDxcyE2pXns"
mydata1 = quandl.get("WIKI/GOOGL")

mydata2=quandl.get("BCHARTS/ABUCOINSUSD")



goog=mydata1.Open.pct_change()
goog=goog.to_frame()
goog.reset_index(level=0, inplace=True)
goog_4=goog.loc[1:4]
goog_1pc=round(goog_4["Open"][1],3) 
goog_2pc=round(goog_4["Open"][2],3) 
goog_3pc=round(goog_4["Open"][3],3)
goog_4pc=round(goog_4["Open"][4],3)

#-----------------------------------

bit=mydata2.Open.pct_change()
bit=bit.to_frame()

bit.reset_index(level=0, inplace=True)
bit_4=bit.loc[1:4]
bit_1pc=round(bit_4["Open"][1],3) 
bit_2pc=round(bit_4["Open"][2],3) 
bit_3pc=round(bit_4["Open"][3],3) 
bit_4pc=round(bit_4["Open"][4],3) 

from plotly.offline import plot, iplot
import plotly.graph_objs as go

header = dict(values=['Google','Bitcoin'],
              align = ['left','center'],
              font = dict(color = 'white', size = 12),
              fill = dict(color='#119DFF')
             )
cells = dict(values=[[goog_1pc,goog_2pc,goog_3pc,goog_4pc],
                     [bit_1pc,bit_2pc,bit_3pc,bit_4pc]],
             align = ['left','center'],
             fill = dict(color=["yellow","white"])
            )
trace = go.Table(header=header, cells=cells)

data = [trace]
layout = dict(width=600, height=300)
fig4 = dict(data=data, layout=layout)



#Graph5
import plotly.plotly as py
import plotly.figure_factory as ff

df = [dict(Task="Task 1", Start='2018-01-01', Finish='2018-01-31',Resource='Idea Validation'),
      dict(Task="Task 2", Start='2018-03-01', Finish='2018-04-15', Resource='Team Formation'),
      dict(Task="Task 3", Start='2018-04-15', Finish='2018-09-30', Resource='Prototyping')]

colors = ['#FF6103', (0.5, 0.5, 0.1), ' rgb(30,144,255)']

fig5 = ff.create_gantt(df, colors=colors, index_col='Resource', show_colorbar=True,title="Startup Roadmap")

