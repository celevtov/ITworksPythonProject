def getListOfMetrics():
    Metrics = [
        {'name':'Sales'
        ,'description':'Volume of Sales'
        ,'column':['Sales']
        ,'func':['sum']
        }
        ,
        {'name':'Quantity'
        ,'description':'Product Quantity'
        ,'column':['Quantity']
        ,'func':['sum']
        }
        ,
        {'name':'Avg Price'
        ,'description':'Average product price'
        ,'column':['Sales','Quantity']
        ,'func':['sum','sum']
        ,'formula':"dfagg['Sales']/dfagg['Quantity']"
        }
        ,
        {'name':'Profit'
        ,'description':'Volume of Profit'
        ,'column':['Profit']
        ,'func':['sum']
        }
        ,
        {'name':'Discount'
        ,'description':'Volume of Discount'
        ,'column':['DiscountAbs']
        ,'func':['sum']
        }
        ,
        {'name':'AvgSales'
        ,'description':'Avarege sales in order'
        ,'column':['Sales','Order_ID']
        ,'func':['sum','nunique']
        ,'formula':"dfagg['Sales']/dfagg['Order_ID']"
        }
            ,
        {'name':'Discount%'
        ,'description':'Percent of Discount'
        ,'column':['RealSales','DiscountAbs']
        ,'func':['sum','sum']
        ,'formula':"dfagg['DiscountAbs']/dfagg['RealSales']"
        }
    ]
    return Metrics
def getListOfDimension():
    dimension = [
        {  'name':'Order Date'
            ,'description':'Create order date, when order was created'
            ,'field':'Order_Date'
        }
        ,
        {  'name':'Order Month'
            ,'description':'Create order date, month when order was created'
            ,'field':'Order_Month'
        }
        ,
        {  'name':'Ship Mode'
            ,'description':'Shipe mode, which was used for order'
            ,'field': 'Ship_Mode'
                
        }
        ,
        {  'name':'Shiping Speed'
            ,'description':'How long days order was delivering'
            ,'field':'ShipingSpeed'
        }
        ,
        {  'name':'Region'
            ,'description':'From wich region was order'
            ,'field':'Region'
        }
        ,
        {  'name':'State'
            ,'description':'From wich state was order'
            ,'field':'State'
        }
        ,
        {  'name':'Segment'
            ,'description':'From wich Segment was order'
            ,'field':'Segment'
        }
         ,
        {  'name':'Category'
            ,'description':'From wich Category was product in order'
            ,'field':'Category'
        }

    ]
    return dimension

def getMetrics(FilterMetrics):
    targetMetrics = []
    for item in getListOfMetrics():
        if item['name'] in FilterMetrics:
            targetMetrics.append(item)
    return targetMetrics

def getDimension(FilterDimension):
    targetDimension={}
    for item in getListOfDimension():
        if item['name'] in FilterDimension:
            targetDimension=item
    return targetDimension