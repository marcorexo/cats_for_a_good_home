from dash import Input, Output, dcc, html
import dash_bootstrap_components as dbc

# Define the card components
card1 = dbc.Card(
    [
        dbc.CardImg(src="https://via.placeholder.com/150", top=True),
        dbc.CardBody(
            [
                html.H5("Card 1", className="card-title"),
                html.P("This is some text for card 1."),
            ]
        ),
    ],
    className="mb-4",
)

card2 = dbc.Card(
    [
        dbc.CardImg(src="https://via.placeholder.com/150", top=True),
        dbc.CardBody(
            [
                html.H5("Card 2", className="card-title"),
                html.P("This is some text for card 2."),
            ]
        ),
    ],
    className="mb-4",
)

card3 = dbc.Card(
    [
        dbc.CardImg(src="https://via.placeholder.com/150", top=True),
        dbc.CardBody(
            [
                html.H5("Card 3", className="card-title"),
                html.P("This is some text for card 3."),
            ]
        ),
    ],
    className="mb-4",
)