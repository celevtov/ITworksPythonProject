def getListOfMetrics():
    Metrics = [
        {'name':'Sales'
        ,'description':'Volume of Sales'
        ,'column':['Sales']
        ,'func':['sum']
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
        ,'column':['RealSales','Discount']
        ,'func':['sum','sum']
        ,'formula':"dfagg['Discount']/dfagg['RealSales']"
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
        {  'name':'Ship Mode'
            ,'description':'Shipe mode, which was used for order'
            ,'field': 'Ship_Mode'
                
        }
        ,
        {  'name':'Ship Date'
            ,'description':'When order was delivered'
            ,'field':'Ship_Date'
        }
        ,
        {  'name':'Region'
            ,'description':'From wich region was order'
            ,'field':'Region'
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