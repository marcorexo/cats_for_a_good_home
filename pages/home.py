from dash import Input, Output, dcc, html
import dash_bootstrap_components as dbc

cards = []
for i in range(1, 11):
    card = dbc.Card(
        [
            dbc.CardImg(src=f"https://via.placeholder.com/150?text=Image{i}", top=True),
            dbc.CardBody(
                [
                    html.H5(f"Card {i}", className="card-title"),
                    html.P("Some card content."),
                ]
            ),
        ],
        className="mb-4",
    )
    cards.append(card)

grid = html.Div(
    dbc.Row(
        [dbc.Col(card, width=4) for card in cards],
        className="mt-4",
    )
)


def create_home_content():
    return dbc.Container(grid, fluid=True)