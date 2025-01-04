from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    # Load and process the CSV
    df = pd.read_csv("Table_Input.csv")
    table1 = df.to_dict(orient="records")
    alpha = df.loc[df['Index #'] == 'A5', 'Value'].values[0] + df.loc[df['Index #'] == 'A20', 'Value'].values[0]
    beta = df.loc[df['Index #'] == 'A15', 'Value'].values[0] / df.loc[df['Index #'] == 'A7', 'Value'].values[0]
    charlie = df.loc[df['Index #'] == 'A13', 'Value'].values[0] * df.loc[df['Index #'] == 'A12', 'Value'].values[0]
    table2 = [
        {"category": "Alpha", "value": alpha},
        {"category": "Beta", "value": beta},
        {"category": "Charlie", "value": charlie},
    ]
    return render_template("index.html", table1=table1, table2=table2)

if __name__ == "__main__":
    app.run(debug=True)
