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
                    ld - load data and inizializate all metrics
                    gs - get sample of data
                  """)
        if inp == 'ld':
            df = helper.loadData()
        if inp == 'gs':
            if df.empty:
                uags = input("Dataset didn't load, would you like load datase (Y/n)")
                if  (not uags) or (uags.upper()=='Y'):
                    df = helper.loadData()
                else:
                    print('Please load dataset use comand ld')
                    continue
            print(df.head())
            


        if inp.upper() == 'Q':
            break
 
if __name__=='__main__':
    menu()