# ITworksPythonProject
## Overview
This project provides tools for analyzing and visualizing sales data from a Superstore dataset. It includes data loading, aggregation, metric calculation, and charting functionalities. The project is organized into several Python modules for interactive analysis.
## Installing
For work with tools ypu need to install some pakages, use this code
```
pip install -r [requirements.txt]
```
## How to use
To start you should use main.py
```
python3 main.py
```
On the next step you have 4 actions
### 1 - get sample of data
You could get sample from dataframe to understand data and columns
<details>
  <summary>Table Example</summary>

| Row_ID | Order_ID       | Order_Date | Ship_Date  | Ship_Mode    | Customer_ID | Customer_Name   | Segment   | Country       | City        | State      | Postal_Code | Region | Product_ID      | Category        | Sub-Category | Product_Name                                                | Sales  | Quantity | DiscountPrcnt | Profit  | RealSales | DiscountAbs | ShipingSpeed | Order_Month |
| ------ | -------------- | ---------- | ---------- | ------------ | ----------- | --------------- | --------- | ------------- | ----------- | ---------- | ----------- | ------ | --------------- | --------------- | ------------ | ----------------------------------------------------------- | ------ | -------- | ------------- | ------- | --------- | ----------- | ------------ | ----------- |
| 1      | CA-2016-152156 | 08/11/2016 | 11/11/2016 | Second Class | CG-12520    | Claire Gute     | Consumer  | United States | Henderson   | Kentucky   | 42420       | South  | FUR-BO-10001798 | Furniture       | Bookcases    | Bush Somerset Collection Bookcase                           | 261.96 | 2        | 0             | 41.9136 | 261.96    | 0           | 3            | 01/11/2016  |
| 2      | CA-2016-152156 | 08/11/2016 | 11/11/2016 | Second Class | CG-12520    | Claire Gute     | Consumer  | United States | Henderson   | Kentucky   | 42420       | South  | FUR-CH-10000454 | Furniture       | Chairs       | Hon Deluxe Fabric Upholstered Stacking Chairs, Rounded Back | 731.94 | 3        | 0             | 219.582 | 731.94    | 0           | 3            | 01/11/2016  |
| 3      | CA-2016-138688 | 12/06/2016 | 16/06/2016 | Second Class | DV-13045    | Darrin Van Huff | Corporate | United States | Los Angeles | California | 90036       | West   | OFF-LA-10000240 | Office Supplies | Labels       | Self-Adhesive Address Labels for Typewriters by Universal   | 14.62  | 2        | 0             | 6.8714  | 14.62     | 0           | 4            | 01/06/2016  |
</details>

### 2 - show general charts
This mode is used to display several pre-defined charts with key Sales metrics.

You can choose one of the following metrics:
1 - a linear graph with Sales and Profit to see them together and compare

three options to track different sales metrics and plan some marketing campaigns:
2 - two bar charts with Top-5 and Bottom-5 product categories
3 - bar charts of average sum of order by months
4 - relations between client segment and ship mode, with pie charts and stat chi-square test

two bar charts to track company SLAs:
5 - shipping time (to check shipping department efficiency)
6 - active customers

Some plots also have additional table data for better understanding
#### How to display a chart
- choose action 2 - make general charts
- on the next step input 1 or two dates for which you want to display data. Some charts will be built just for whole months, while others - for a random periods or on date
- get your chart!

### 3 - make custom charts
This is the tool where you can make 3 charts using all available metrics and dimensions
First you need to choose the type of chart
- Line - simple line chart, you can combine several metrics and only one dimension, usualy used to build chart by date.
- Bar Chart - Help match same categories, you can choose several metrics (but my advice use only one )
- Scatter plot - this chart is often used for correlation, choose TWO metrics for x and y and one optional metric for color 
#### How to build line and bar charts
 - choose action 3 - make custom charts
 - On the next step input line or bar
 - input metrics separet comma without spaces (e.g Sales,Profit),you can just copy from list metrics
 - Choose dimension
 That is all, chart built
 #### How to build scatter plot
 Scatter plot help understand how to correlating two metrics each other
  - choose action 3 - make custom charts
  - On the next step input scatter
  - Input TWO mandatory metrics for x and y and ONE option metrics for color (e.g. Sales,Quantity,Profit or Sales,Quntyty)
That is all!!!