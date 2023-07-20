import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html,State
from pages.home import create_home_content
from components.parent_cards import card1,card2,card3
import smtplib
from email.message import EmailMessage
import smtplib
import mailtrap as mt


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server


# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}


sidebar = html.Div(
    [
        html.Center(
            [
                html.Div(
                    [
                        html.Div(
                                html.Img(src="assets/images/logo.jpg", alt="Logo", style={"width":"100px"}, className="logo")
                        ),
                        html.H3(
                            children=[
                                html.Span("Purr", style={"font-style": "italic", "font-family": "Arial", "font-weight":'300' }),
                                "fect Kittens"
                            ],
                            className="display-7"
                        ),
                    ]
                ),
                html.P('Bangor, Gwynedd, UK'),
            ]
        ),
        html.Hr(),
        html.P(
            "Loving kittens that are trained to use the littertray and that have begun to eat solid foods.", 
            className="lead",
            style={"color":"gray"}
        ),
        dbc.Nav(
            [
                #dbc.NavLink("Home", href="/", active="exact"),
                #dbc.NavLink("Page 1", href="/page-1", active="exact"),
                #dbc.NavLink("Page 2", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),

        html.Div(style={"height": "20%"}),

        html.Div(
            [
                html.P('We welcome your enquieries. Send us an email and we will respond asap. thank you x', 
                    style={"color":"gray"}),
                html.P(html.A('purrfectkittens01@gmail.com', href=f"mailto:{'purrfectkittens01@gmail.com'}?subject={'Enquiry about a kitten'}"), style={"color":"blue", "font-style":"italic"})
            ]
        )
        
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

   

# Callback to handle the email sending process
@app.callback(Output("output", "children"),
              Input("send-button", "n_clicks"),
              State("subject-input", "value"),
              State("message-input", "value"))

@app.callback(
    Output("page-content", "children"), 
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return create_home_content()
    elif pathname == "/page-1":
        return html.P("This is the content of page 1. Yay!")
    elif pathname == "/page-2":
        return html.P("Oh cool, this is page 2!")
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


if __name__ == "__main__":
    app.run_server(port=8051)
