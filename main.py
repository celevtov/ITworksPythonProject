def menu():
    while True:
        print('Type help to get all available comands')
        inp = input('>>')
        if inp.upper() == 'Q':
            break
 
if __name__=='__main__':
    menu()