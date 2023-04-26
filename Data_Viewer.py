import pandas as pd
import plotly.express as px

# Read the CSV file
data = pd.read_csv('coin_data.csv')

# Pivot the data to create a heat map
heatmap_data = data.pivot(index='market_cap_rank', columns='name', values='price_change_percentage_24h')

# Create a heat map using plotly
fig = px.imshow(heatmap_data.values,
                x=heatmap_data.columns,
                y=heatmap_data.index,
                color_continuous_scale='viridis',
                color_continuous_midpoint=0)

# Update the layout and display the plot
fig.update_layout(
    title='Cryptocurrency Heat Map',
    xaxis_title='Market Cap Rank',
    yaxis_title='Coin Name',
    font=dict(family='Arial', size=12, color='#404040'),
    plot_bgcolor='#FFFFFF',
    height=800,
)
fig.show()
