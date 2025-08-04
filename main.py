import helper
def menu():
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
            print("Dataframe size:", df.shape)

        if inp.upper() == 'Q':
            break
 
if __name__=='__main__':
    menu()