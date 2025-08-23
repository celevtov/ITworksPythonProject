# ITworksPythonProject
## Overview
This project provides tools for analyzing and visualizing sales data from a Superstore dataset. It includes data loading, aggregation, metric calculation, and charting functionalities. The project is organized into several Python modules for interactive analysis.
## Installing
For work with tools ypu need to install some pakages, use this code
```
pip install -r [requirements.txt]
```
## How to use
For starting you should use main.py
```
python3 main.py
```
On the next step ypu get 4 actions
### 1 - get sample of data
You could get sample from dataframe to undastnd data and column
<details>
  <summary>Table Example</summary>

| Row_ID | Order_ID       | Order_Date | Ship_Date  | Ship_Mode    | Customer_ID | Customer_Name   | Segment   | Country       | City        | State      | Postal_Code | Region | Product_ID      | Category        | Sub-Category | Product_Name                                                | Sales  | Quantity | DiscountPrcnt | Profit  | RealSales | DiscountAbs | ShipingSpeed | Order_Month |
| ------ | -------------- | ---------- | ---------- | ------------ | ----------- | --------------- | --------- | ------------- | ----------- | ---------- | ----------- | ------ | --------------- | --------------- | ------------ | ----------------------------------------------------------- | ------ | -------- | ------------- | ------- | --------- | ----------- | ------------ | ----------- |
| 1      | CA-2016-152156 | 08/11/2016 | 11/11/2016 | Second Class | CG-12520    | Claire Gute     | Consumer  | United States | Henderson   | Kentucky   | 42420       | South  | FUR-BO-10001798 | Furniture       | Bookcases    | Bush Somerset Collection Bookcase                           | 261.96 | 2        | 0             | 41.9136 | 261.96    | 0           | 3            | 01/11/2016  |
| 2      | CA-2016-152156 | 08/11/2016 | 11/11/2016 | Second Class | CG-12520    | Claire Gute     | Consumer  | United States | Henderson   | Kentucky   | 42420       | South  | FUR-CH-10000454 | Furniture       | Chairs       | Hon Deluxe Fabric Upholstered Stacking Chairs, Rounded Back | 731.94 | 3        | 0             | 219.582 | 731.94    | 0           | 3            | 01/11/2016  |
| 3      | CA-2016-138688 | 12/06/2016 | 16/06/2016 | Second Class | DV-13045    | Darrin Van Huff | Corporate | United States | Los Angeles | California | 90036       | West   | OFF-LA-10000240 | Office Supplies | Labels       | Self-Adhesive Address Labels for Typewriters by Universal   | 14.62  | 2        | 0             | 6.8714  | 14.62     | 0           | 4            | 01/06/2016  |
</details>

### 2 - show general charts
тут над дописать про твои чарты
### 3 - make custom charts
This tools where you can make 3 charts used all available metrics and dimension
First you have to choose type of chart
- Line - simple line chart, you can combine several metrics and only one dimension, usualy use to build chart by date.
- Bar Chart - Help match same categoryes, you can choose several metrics (but my advice use only one )
- Scatter plot - this chart offten use for correlation, chose TWO metrics for x and y and one optional metric for color 
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