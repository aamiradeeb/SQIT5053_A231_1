import dash
from dash import dcc, html, dash_table, Input, Output
import pandas as pd
import plotly.express as px

# Import the CSV file
df = pd.read_csv('/Users/aamiradeeb/Documents/A231/SQIT5053/W7/Dash_example/data.csv')

# Convert 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

# Group by 'Date' and find the mean of 'Total Defect Qty'
df_grouped = df.groupby('Date')['Total Defect Qty'].mean().reset_index()

# Sort DataFrame by 'Date'
df_grouped = df_grouped.sort_values(by='Date')

# Create a time series plot using Plotly Express
fig = px.line(df_grouped, x='Date', y='Total Defect Qty', title='Time Series of Average Total Defect Qty by Date')

# Initialize Dash app
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div([
    html.H1('Average Total Defect Qty by Date'),
    dash_table.DataTable(
        id='table',
        columns=[{'name': i, 'id': i} for i in df_grouped.columns],
        data=df_grouped.to_dict('records'),
    ),
    dcc.Graph(id='time-series-plot', figure=fig)
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
