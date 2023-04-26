# Coingecko_Data_Collector

I made this code for dowmload market information for CoinGecko, in this case the code is composed of two modules, _"data_collector.py"_ retrive the information of the top 100 cryptocurrencies by market capitalization and store it in a CSV file , and _"data_viewer.py"_ is used to read and  make a heatmap of the price

## Installation

For run this code you will need:

-Requests

-Pandas

-Plotly

## Usage


**_data_collector.py_**

Open a command prompt or terminal window and navigate to the directory where the script is saved. Then, run the script using the following command:

_python data_collector.py_

The script will make a request to the Coingecko API to retrieve the current data of the top 100 cryptocurrencies by market capitalization, store it in a CSV file named coin_data.csv, and print "Done!" to the console once it's finished.

**_data_viewer.py_**

Creates a heatmap of the price change percentage of various cryptocurrencies over a 24-hour period.

It reads a CSV file 'coin_data.csv' Then it uses the pandas library to pivot the data, creating a heatmap of the price change percentage for each cryptocurrency, sorted by market cap rank.

Next, it uses the plotly.express library to create a heat map visualization of the data. The heat map is colored using the 'viridis' color scale, with 0 as the midpoint.

Finally, it updates the layout of the plot, including the title, axis titles, font, background color, and height. The plot is then displayed using the show() method.

## Contributing

If you find a bug or have an idea for an improvement, feel free to open an issue or submit a pull request.

