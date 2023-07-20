from dash import Input, Output, dcc, html
import dash_bootstrap_components as dbc

breed = ['British Short Hair', 'Persian', 'Black Cat', 'Black Cat', 'Classic Tabby', 'Tortoiseshell', 'Black Cat', 'Black Cat', 'Black Cat']
sex = ['Male', 'Male', 'Female', 'Male', 'Male', 'Female', 'Male', 'Male', 'Male']
price = ['£250', '£100', '£50', '£50', '£50', '£100', '£50', '£50', '£50']
cards = []

for i in range(1, 10):
    card = dbc.Card(
        [
            dbc.CardImg(src=f"assets/images/{i}.jpg", top=True),
            dbc.CardBody(
                [
                    html.H3(breed[i-1]),
                    html.H5(sex[i-1]),
                    html.H6(price[i-1], style={"color":"gray"}),
                    html.P('Mother: ' + ('Brown Savanna' if i < 5 else 'Black Bombay')),
                    html.P('Father: ' + ('British Shorthair' if i < 5 else ''))
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