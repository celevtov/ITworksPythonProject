import metricsanddimension
import matplotlib.pyplot as plt


def Show(val):
    for item in val:
        print(f'{item['name']} - {item['description']}')

def CreateDictForAgg(targetMetrics):
    dictAgg = {}
    formuladict = {}
    formulas=[]
    renameDict={}
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
    return dictAgg, formulas,renameDict

def makeAggDataFrame(df,userMetrics,userDimension):
    # Get full information about choosen metrics
    targetMetrics = metricsanddimension.getMetrics(userMetrics)
    # get Get full information about choosen dimension
    targetDimension = metricsanddimension.getDimension(userDimension)
    # get dictinary for aggregations and additionaly formulas, if thea there are
    dictAgg, formulas, renameDict = CreateDictForAgg(targetMetrics)
    # Time to make aggregation data frame 
    dfagg = df.groupby(by = targetDimension['field'], observed=True).agg(dictAgg)
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
        print('First step, Metrics, below is list of available metrics\n')
        Show(metricsanddimension.getListOfMetrics())
        print()
        print('Input which metrics, would you like to use. You could type metrics separet by coma(e.g Sales, Profit)\n')
        inp = input('>>')
        if inp.upper()=='Q':
            break
        userMetrics = inp.split(sep=',')
        print('Second step, Dimensions, below is list of available dimensions\n')
        Show(metricsanddimension.getListOfDimension())
        print()
        print('Input which dimension, would you like to use. Only ONE dimension\n')
        inp = input('>>')
        if inp.upper()=='Q':
            break
        userDimension = inp
        print('Input which kind of charts would you like to use.line|bar|hist|scatter \n')
        inp = input('>>')
        if inp.upper()=='Q':
            break
        chartType = inp
        dfagg = makeAggDataFrame(df=df,userMetrics=userMetrics,userDimension=userDimension)
        dfagg.plot(kind=chartType,y=userMetrics)
        plt.show()
