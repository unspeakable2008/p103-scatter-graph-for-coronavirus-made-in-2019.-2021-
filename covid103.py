import pandas as pd
import plotly.express as px
df = pd.read_csv("p103.csv")
print(df.head())
df.head()
fig = px.scatter(df, x = "date", y = "cases", color = "country" )
fig.show()