import plotly.express as px
import pandas as pd
from dash import Dash, dcc, html, Input, Output



# Load Data
df1 = pd.read_csv("data_for_app_map.csv")
df2 = pd.read_csv("data_for_plots.csv")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

fig1 = px.bar(df2, x='country', y='number_addresses') # plot addresses even the ones not assigned with cities barplot


fig2= px.sunburst(df2, path = ["continent", "country"], values = "number_addresses", hover_name= "country", color = "number_addresses", height = 700)

fig3 = px.treemap(df2, path = ["continent", "country"], values = "number_addresses", hover_name= "country", color = "number_addresses", height = 700)

#fig4 = fig = px.scatter_mapbox(df2, lat="lat", lon="lon", color="original_count", zoom=10, mapbox_style="carto-positron")

fig5 = px.scatter_mapbox(df1, lat="lat", lon="lon",  color = "continent", zoom=10, mapbox_style="carto-positron")



app.layout = html.Div(children=[
    # All elements from the top of the page
    html.Div([
        html.H1(children='Distribution of addresses of TT'),

        html.Div(children='''
            Geographical locations. 
        '''),

        dcc.Graph(
            id='graph1',
            figure=fig5
        ),  
    ]),
    # New Div for all elements in the new 'row' of the page
    html.Div([
        html.H1(children='Counting the number of addresses per country.'),

        html.Div(children='''
             
        '''),

        dcc.Graph(
            id='graph2',
            figure=fig1
        ),  
    ]),

    # New Div for all elements in the new 'row' of the page
    html.Div([
        html.H1(children=''),

        html.Div(children='''
            
        '''),

        dcc.Graph(
            id='graph3',
            figure=fig2
        ),  
    ]),




    # New Div for all elements in the new 'row' of the page
    html.Div([
        html.H1(children=''),

        html.Div(children='''
            
        '''),

        dcc.Graph(
            id='graph4',
            figure=fig3
        ),  
    ]),

    
])


if __name__ == '__main__':
    app.run_server(debug=True)