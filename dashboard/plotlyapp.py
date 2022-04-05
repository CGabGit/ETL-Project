from sqlalchemy.log import Identified
import dbRead
import dash
from dash import html
from dash import dcc
import plotly.graph_objs as go
from  dash.dependencies import Output, Input
from dash import dash_table
import pandas as pd

import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import flask
import time

# data import
dbRead.waitForPostgresContainer()
#dbRead.waitForScraperApp()
numberOpenJobAds = dbRead.loadTblNumResFound('tbl_numresultsfound')
searchTerm = numberOpenJobAds['searchterm'].iloc[0] # get first value in column 'searchterm'
wordFreq = dbRead.loadTblWordFreq('tbl_word_freq')
bigrams = dbRead.loadTblWordFreq('tbl_bigrams')
trigrams = dbRead.loadTblWordFreq('tbl_trigrams')

# dataframes for full data download buttons
df_1 = wordFreq
df_2 = bigrams
df_3 = trigrams

# view for bar charts 
wordFreq = wordFreq.head(19)
bigrams = bigrams.head(10)
trigrams = trigrams.head(10)

# load tbl_jobitems for full data download button
jobItems = dbRead.loadTblJI()
# view for data table 
jobItemsView = jobItems.head(1)

# for col in jobItems.columns:
#     print(col)

# #initialization of dash web app  
app = dash.Dash()

# server = flask.Flask(__name__)
# app = dash.Dash(__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP])
# app.config.suppress_callback_exceptions = True

# #definition of dash layout
app.layout = html.Div([
    html.H1('NLP Analyse - Stellenportal Stepstone ', style={'textAlign': 'center','font-family': 'Helvetica'}),
    #html.H3('Suchbegriff: Wirtschaftsinformatiker/in', style={'font-family': 'Helvetica'}),
    #html.H3('Letzte Aktualisierung: 2021-11-11 12:32:10', style={'font-family': 'Helvetica'}),
    
    html.H2(f'Anzahl Stellenausschreibungen - {searchTerm} ', style={'font-family': 'Helvetica'}),
    html.Div([
    dcc.Graph(id='linechart',
    figure={
        'data': [go.Scatter(x=numberOpenJobAds['daterecoded'],y=numberOpenJobAds['searchresults'])]
    })]),

    html.Div([html.Button(html.A('Einstellung Suchbegriffe', href='https://docs.google.com/spreadsheets/d/1tUgxvygQ_iykSaM5T2rVjK2DViuWpWAl0I_Y1e7yDfE/edit#gid=0',target='_blank',
    style={'color': '#000000','text-decoration': 'none'}) )]),
    html.H2('\n'),
    html.H2('In Stellenausschreibungen genannte 1-Tupel und deren Häufigkeit', style={'font-family': 'Helvetica'}),
    html.Div([
    dcc.Graph(id='wordFreq',
    figure={
        'data': [go.Bar(x=wordFreq['frequency'],y=wordFreq['word'],orientation='h')]
    })]),

    html.Button("Download (1-Tupel) CSV", id="btn_csv_1", style={'font-family': 'Helvetica'}),
    dcc.Download(id="download-dataframe-csv_1"),
    html.H2('\n'),
    html.Div([html.Button(html.A('Bearbeitung tbl_default_german_stopwords ', href='https://docs.google.com/spreadsheets/d/1sbDqG3tA4_U8fFoMsTjL50G6DB90pBv25dkdfrygCEw/edit#gid=0',target='_blank',
    style={'color': '#000000','text-decoration': 'none'}) )]),
    html.H2('\n'),
    html.Div([html.Button(html.A('Bearbeitung tbl_onegrams_german-stop-words ', href='https://docs.google.com/spreadsheets/d/1rsVqZSeimDT0wZvY0Szq4b2vCNbzz_jVeRmL64zJ3FY/edit#gid=0',target='_blank',
    style={'color': '#000000','text-decoration': 'none'}) )]),

    html.H2('In Stellenausschreibungen oft genannte 2-Tupel und deren Häufigkeit', style={'font-family': 'Helvetica'}),
    html.Div([
    dcc.Graph(id='bigrams', style = {'margin':'auto','width': "50%"},
    figure={
        'data': [go.Bar(x=bigrams['frequency'],y=bigrams['bigrams'],orientation='h')],
    })]),

    html.Button("Download (2-Tupel) CSV", id="btn_csv_2", style={'font-family': 'Helvetica'}),
    dcc.Download(id="download-dataframe-csv_2"),
    html.H2('\n'),
    html.Div([html.Button(html.A('Bearbeitung tbl_bigrams_german-stop-words', href='https://docs.google.com/spreadsheets/d/1P-XzJy1T8FYBtQD2V-6-uo1ZKxq9K_b33sxhjY5f85E/edit#gid=0',target='_blank',
    style={'color': '#000000','text-decoration': 'none'}) )]),

    html.H2('In Stellenausschreibungen oft genannte 3-Tupel und deren Häufigkeit', style={'font-family': 'Helvetica'}),
    html.Div([
    dcc.Graph(id='trigrams',
    figure={
        'data': [go.Bar(x=trigrams['frequency'],y=trigrams['trigrams'],orientation='h')]
    })]),

    html.Button("Download (3-Tupel) CSV", id="btn_csv_3", style={'font-family': 'Helvetica'}),
    dcc.Download(id="download-dataframe-csv_3"),
    html.H2('\n'),
    html.Div([html.Button(html.A('Bearbeitung tbl_trigrams_german-stop-words', href='https://docs.google.com/spreadsheets/d/1vju3pX-J8_ZQn-KNOBtSXTRx9JWBNjKQjJJdX9znbUI/edit#gid=0',target='_blank',
    style={'color': '#000000','text-decoration': 'none'}) )]),

    html.H2('Daten Stellenausschreibungen', style={'font-family': 'Helvetica'}),
    
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} 
                 for i in jobItemsView.columns],
        data=jobItemsView.to_dict('records'),
        style_cell=dict(textAlign='left', columnwidth = [80,400]),
        style_header=dict(backgroundColor="#d9dcde"),
        style_data=dict(backgroundColor="white",whiteSpace='normal',
        height= 'auto')
    ),
    html.H2('\n'),
    html.Button("Download full Dataset CSV", id="btn_csv_4", style={'font-family': 'Helvetica'}),
    dcc.Download(id="download-dataframe-csv_4"),
    html.H2('\n'),
    html.H2('\n'),
    html.H6('© 2021 Christoph Gabriel',style={'textAlign': 'center','font-family': 'Helvetica'}),

])

# Download button actions on click event
@app.callback(
    Output("download-dataframe-csv_1", "data"),
    Input("btn_csv_1", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_data_frame(df_1.to_csv, "wordFreq_1-tupel.csv")

@app.callback(
    Output("download-dataframe-csv_2", "data"),
    Input("btn_csv_2", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_data_frame(df_2.to_csv, "wordFreq_2-tupel.csv")

@app.callback(
    Output("download-dataframe-csv_3", "data"),
    Input("btn_csv_3", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_data_frame(df_3.to_csv, "wordFreq_3-tupel.csv")

@app.callback(
    Output("download-dataframe-csv_4", "data"),
    Input("btn_csv_4", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_data_frame(jobItems.to_csv, "dataset_tbljobitems.csv")

# Startup webapp
if __name__ == '__main__':
    dbRead.waitForPostgresContainer()
    #dbRead.waitForScraperApp()
    import os
    debug = False if os.environ["DASH_DEBUG_MODE"] == "False" else True
    app.run_server(host="0.0.0.0", port=8050, debug=debug)

