import helper
import CustomsChart
import GeneralChart
helper.pd.set_option("display.max_columns", None)
helper.pd.set_option("display.max_colwidth", None)

def menu():
    try: 
        df = helper.loadData()
    except:
         df = helper.pd.DataFrame()
    while True:
        print('Welcome to Sales KPI Monitor. Choose your action:')
        print("""
                    1 - get sample of data
                    2 - show general charts
                    3 - make custom charts
                    4 - Save Data set in csv file  
                    q - for exit
              
                  """)
        inp = input('>>')
        if inp == '1':
            if df.empty:
                uags = input("Dataset didn't load, would you like load datase (Y/n)")
                if  (not uags) or (uags.upper()=='Y'):
                    df = helper.loadData()
                else:
                    print('Please load dataset use comand ld')
                    continue
            print(df.sample(10))
        elif inp == '2':
            GeneralChart.gencharts(df)
        elif inp == '3':
            CustomsChart.customcharts(df)
        elif inp == '4':
            print('Type dir and file name to save (e.g. ~/Documents/filename.csv)')
            inp = input('>>')
            try:
                helper.saveDF(df,inp)
            except OSError as er:
                print(f'ERROR!!!! {er}')
        elif inp.upper() == 'Q':
            break
        else:
            print(f'No such command: {inp} Try again')
 
if __name__=='__main__':
    menu()