from cv2 import mean
import pandas as pd
import csv 
import plotly.graph_objects as pg
df = pd.read_csv("data.csv")
print(df.groupby("level")["attempt"].mean())
figure = pg.Figure(pg.Bar(
    x = df.groupby("level")["attempt"].mean(),
    y = ["level1","level2","level3","level4"],
    orientation = "h"
))
figure.show()