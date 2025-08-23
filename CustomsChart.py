import metricsanddimension
import matplotlib.pyplot as plt


def Show(val):
    for item in val:
        print(f'{item['name']} - {item['description']}')
def GetList(val):
    SomeList=[]
    for item in val:
       SomeList.append(item['name'])
    return SomeList
def checkvalue(targetlist,generalList):
    wronglist=[]
    checkFlag = True
    for item in targetlist:
        if item not in generalList:
            wronglist.append(item)
    if len(wronglist)!=0:
        checkFlag=False
    return checkFlag, wronglist

def CreateDictForAgg(targetMetrics):
    dictAgg = {}
    formuladict = {}
    formulas=[]
    renameDict={}
    columnsForMetrics=[]
    for item in targetMetrics:
        if len(item['column'])!=len(item['func']):
            raise  ValueError("Count of columns not euqual count of function")
        else:
            if  len(item['column']) == 1:
                dictAgg[item['column'][0]] = item['func'][0]
            else:
                for num in range(0,len(item['column'])):
                    dictAgg[item['column'][num]] = item['func'][num]
        if item.get('formula') is not None:
            formuladict['name'] = item['name']
            formulas.append({'name':item['name']
                            ,'formula':item['formula']
                            })
        if  len(item['column']) == 1:
            renameDict[item['column'][0]] = item['name']
        for column in item['column']:
            columnsForMetrics.append(column)
    return dictAgg, formulas,renameDict,columnsForMetrics

def makeAggDataFrame(df,userMetrics,userDimension = None):
    # Get full information about choosen metrics
    targetMetrics = metricsanddimension.getMetrics(userMetrics)
    # get dictinary for aggregations and additionaly formulas, if thea there are
    dictAgg, formulas, renameDict,columnsForMetrics = CreateDictForAgg(targetMetrics)
    # get Get full information about choosen dimension
    if userDimension!= None:
        targetDimension = metricsanddimension.getDimension(userDimension)
        # Time to make aggregation data frame 
        dfagg = df.groupby(by = targetDimension['field'], observed=True).agg(dictAgg)
    else:
        dfagg = df[columnsForMetrics]
    # Add additional calculating, if need
    if len(formulas)>0:
        for item in formulas:
            dfagg[item['name']]=eval(item['formula'])
    # rename columns, just trust me, it is nessasary
    dfagg.rename(columns = renameDict,inplace=True)
    return dfagg



def customcharts(df):
    while True:
        print("Ok, let's create chart, if you will tire you could type Q and you will quit\n")
        print('First step, Input which kind of charts would you like to use - line, bar, hist, scatter \n')
        inp = input('>>')
        if inp.upper()=='Q':
            break
        chartType = inp
        if chartType not in ['line','bar','hist','scatter']:
            print("ERROR!!!!!!!: Choose right chart type, 'line','bar','scatter'")
            print()
            continue
        elif chartType in ['line','bar']:
            customchartstypeone(df,chartType)
        else:
            customchartstypetwo(df)

def choosmetrics():
    while True:
        print('Metrics, below is list of available metrics\n')
        Show(metricsanddimension.getListOfMetrics())
        print()
        print('Input which metrics, would you like to use. You could type metrics separet by coma(e.g Sales, Profit)\n')
        inp = input('>>')
        if inp.upper()=='Q':
            return inp.upper()
        userMetrics = inp.split(sep=',')
        ## check list metricks from User
        checkFlag, wrongList = checkvalue(userMetrics,GetList(metricsanddimension.getListOfMetrics()))
        if checkFlag==False:
            print(f"ERRROR!!! This metrics are wrong {wrongList}")
            print("Please choose correct metrics\n")
            continue
        else:
            return userMetrics
def choosdimension():
    while True:
        print('Second step, Dimensions, below is list of available dimensions\n')
        Show(metricsanddimension.getListOfDimension())
        print()
        print('Input which dimension, would you like to use. Only ONE dimension\n')
        inp = input('>>')
        if inp.upper()=='Q':
            return inp.upper()
        userDimension = inp
        if userDimension not in GetList(metricsanddimension.getListOfDimension()):
            print(f"ERRROR!!! This Dimension is wrong {userDimension}")
            print("Please choose correct Dimension\n")
            continue
        else:
            return userDimension


def customchartstypeone(df,chartType):
    while True:
        userMetrics = choosmetrics()
        if userMetrics =='Q':
            break
        userDimension = choosdimension()
        if userDimension == 'Q':
            break
        dfagg = makeAggDataFrame(df=df,userMetrics=userMetrics,userDimension=userDimension)
        dfagg.plot(kind=chartType,y=userMetrics)
        plt.show()
def customchartstypetwo(df):
    while True:
        print("For scatter plot we need 3 metrics, for X, Y and Color (optional)")
        print("Please input metrics separaiting by comma or Q for Exit")
        Show(metricsanddimension.getListOfMetrics())
        print()
        inp = input('>>')
        if inp.upper()=='Q':
            return inp.upper()
        userMetrics = inp.split(sep=',')
        checkFlag, wrongList = checkvalue(userMetrics,GetList(metricsanddimension.getListOfMetrics()))
        if checkFlag == False:
            print(f"ERRROR!!! This metrics are wrong {wrongList}")
            print("Please choose correct metrics\n")
            continue
        else:
            CreateDictForAgg(metricsanddimension.getMetrics(userMetrics))
            dfagg = makeAggDataFrame(df=df,userMetrics=userMetrics)
            if len(userMetrics)==2:
                dfagg.plot.scatter(x=userMetrics[0],y =userMetrics[1],c=None)
            else:
                dfagg.plot.scatter(x=userMetrics[0],y = userMetrics[1],c=userMetrics[2])
            plt.show()

        

