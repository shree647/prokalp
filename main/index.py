import datetime
import pandas as pd
import pandas_datareader.data as web
import dash 
from dash import  Dash, html, dcc
from dash.dependencies import Output, Input
import plotly.graph_objects as go
import plotly.express as px

app = dash.Dash()
app.title = "Stock Visualisation"
app.layout = html.Div(children =[
    html.H1("Stock Visualisation Dashboard"),
      
    html.H4("Please enter the stock name"),
  
    dcc.Input(id ='input', value ='', type ='text'),
  
    html.Div(id ='output-graph')
])

@app.callback(
    Output(component_id='output-graph', component_property='children'),
    Input(component_id='input', component_property='value')
)

def update_value(input_data):
    
    start = datetime.datetime(2010, 1, 1) 
    end = datetime.datetime.now()

    df = web.DataReader(input_data, 'yahoo', start, end)
        
    return dcc.Graph(id ="example",
        figure ={
            'data':[{'x':df.index, 'y':df.Close, 'type':'line', 'name':input_data},
            ],
            'layout':{
                'title':input_data
            }
        }
    )


if __name__ == '__main__':
    app.run_server()