import helper
helper.pd.set_option("display.max_columns", None)
helper.pd.set_option("display.max_colwidth", None)

def menu():
    df = helper.pd.DataFrame()
    while True:
        print('Type help to get all available comands')
        inp = input('>>')
        if inp.upper() == 'HELP':
            print("""
                    1 - load data and inizializate all metrics
                    2 - get sample of data
                    3 - show general charts
                    4 - make custom charts  
                  """)
        if inp == 1:
            df = helper.loadData()
        if inp == 2:
            if df.empty:
                uags = input("Dataset didn't load, would you like load datase (Y/n)")
                if  (not uags) or (uags.upper()=='Y'):
                    df = helper.loadData()
                else:
                    print('Please load dataset use comand ld')
                    continue
            print(df.sample(10))
            


        if inp.upper() == 'Q':
            break
 
if __name__=='__main__':
    menu()