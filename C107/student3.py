import pandas as pd
import plotly.graph_objects as pg
import csv
df = pd.read_csv("data.csv")
student_df = df.loc[df["student_id"] == "TRL_abc"]
print(student_df.groupby("level")["attempt"].mean())
figure = pg.Figure(pg.Bar(
    x = student_df.groupby("level")["attempt"].mean(),
    y = ["level1","level2","level3","level4"],
    orientation = "h"
))
figure.show()