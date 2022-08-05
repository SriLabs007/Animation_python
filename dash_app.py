from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)
app.layout = html.Div([
    dcc.Dropdown(['population','gdp','religion','cars','engineers','phd'], 'gdp', id='demo-dropdown'),
    html.Div(id='dd-output-container')
])

@app.callback(
    Output('dd-output-container', 'children'),
    Input('demo-dropdown', 'value')
)
def update_output(value):

    return f'You have selected {value}'


if __name__ == '__main__':
    app.run_server(debug=True)