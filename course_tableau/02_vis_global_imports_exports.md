# Visualisation: Global Agricultural Trade Analysis:

[Link to Tableau](https://public.tableau.com/app/profile/gabi.fonseca/viz/GlobalAgriculturalTradeAnalysis/Sheet32#1)


## Background

As a data analyst at TradeVista Consulting, you've been tasked with analyzing international trade data for a major agricultural conglomerate that specializes in food commodities. The client produces, processes, and trades agricultural products across multiple categories and is looking to diversify their portfolio, identify emerging markets, and build more resilient supply chains. Your manager needs you to create visualizations focusing on key agricultural products to guide their global expansion strategy. It is essential to look at both imports and exports. While imports reveal market demand for agricultural products, exports show the competitive landscape and potential trade partnerships. 

## Exercise 1: Change Field names and types
To make your workflow easier, change some of the names of the fields:

- In `countries`, change `Name Short En` to `Country Name`
- In `countries-partner.`, change `Name Short En` to `Partner Country Name`
- In `products`, change `Name Short En` to `Product Name`
- Make the  Country Name field in the “countries.csv” table to Geographic Role, and select Country/Region, this way you can create a map
- Convert the Year field to discrete

## Exercise 2: Market Overview Visualization 
It is important for the client to identify the biggest players in agricultural trade. Understanding top exporters and importers helps them find potential trade partners and assess competition.

- Rename the worksheet  to “Total Exports by Country”
- Drag the field “Country Name” into columns and “Export Value” into Rows
- Drag the field “Product Name” into Colors 
- Filter the 10 countries with the highest average exports
- Create a stacked bars chart showing the results. 
- Sort the bars in decreasing order, so the country with most exports appears first
- Add annotations showing the total
- Repeat the process in a new worksheet named “Total Imports by Country”, this time for “Import Value”

## Exercise 3: Strongest Trade Relationships Analysis
You decide to identify key trade relationships between countries by understanding which countries consistently trade with each other. 

- Create a new Worksheet and name it “Trade Partners” 

- Create a new Calculated Field called “Total Trade”, which the sum of Exports and Imports between countries 

- Create a heatmap comparing the “Total Trade” for each country pair. Have “Country Name” in Rows and “Partner Country Name” in Columns

- Filter the rows and columns so that you only show the 10 country pairs with highest “Total Trade”
    - Customize the graph:
    - Rotate the labels in the horizontal axis

    - Adjust the size of the cells in the heatmap for better interpretability

    - If needed, change the color scale to improve interpretability

    - Add an annotation showing the countries with the highest trade.

## Exercise 4: Strongest Pair
You can use the heatmap to identify the pair of countries with the strongest relationship. You decide to investigate this relationship a little deeper

- Create a new Worksheet with the name of the pair (for example Argentina-Mexico)

- Create an area chart showing the time evolution of the imported and exported amounts for each product. You only need to filter the pair once. For example, if you keep Country Name: Argentina and Partner Country Name: Mexico, the the Export Value represents the amount that Argentina exported to Mexico (and thus Mexico imported), and the Import Value has the amount that Mexico exported (and Argentina imported)

- Tune the vertical axis:
    - Change the y-axis labels from Export Value and Import Value to <country name> Exports. In the example above, one should be “Argentina Exports” and the other “Mexico Exports”

    - Double the number of ticks. You can do this by reducing the interval of the ticks by half.

    - Annotate the highest Exported product by each country

## Exercise 5: Exports and Economic Complexity
You are interested in understanding the balance between agricultural export volume and economic diversification. By visualizing countries’ Export Values and the Complexity Outlook Index (COI), they aim to identify which countries are not only strong exporters but also have the potential for long-term growth through economic diversification

Create another sheet Called “COI and Exports”

In this new sheet create a tree map where:

- Each rectangle represents a country.

- The size of the rectangle reflects total agricultural exports.

- The color of the rectangle reflects the Complexity Outlook Index (COI).

- The COI is the same for all products, for each Country each year, so change the metric from Sum to Average.

- If needed, adjust the color scale so the chart is clearer

- Add a filter for “Year”. Set it initially to 2022. Show the filter so you can compare different years

- Add an annotation showing the COI value of the country with the lowest COI

## Exercise 6: Analyzing Agricultural Trade Trends
In order to anticipate market trends and prepare for future changes, you want to see how agricultural trade has evolved over time.

- Create a new worksheet called Exports Over Time

- Create a line chart showing the total “Export Vale”.

- Break it down by “Product Name”

## Exercise 7: Imports by Country - Map
Your client wants to understand which countries import the most agricultural products and how demand varies across different products. By creating a map visualization, they can quickly identify key import markets and track trends by product.

- Create a new sheet called Imports Map

- Create a new Calculated Field called “Relevant Products”. Filter the “Product Name” dimension, so that it only keeps the product names included in the Analysis: Cereals, Coffee, tea and spices, Fruits and nuts, Oil seeds and Oleaginous fruits, and Vegetables.

- Create a map chart where the colors represent total “Import Value”, and the detail is the “Country Name”

- Add The “Relevant Products” calculated field to Filters, and select show filter

- Create another filter for “Year”, and select the year 2022

- Adjust the color scale so that the map is easier to read.

