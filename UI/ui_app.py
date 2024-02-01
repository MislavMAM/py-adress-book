from UI.components.console_components.main_menu import main_menu

while True:
    main_menu()

    choice = input('Upisite broj iz izbornika: ')

    match choice:
        case 1:
            pass
        
        case 0:
            break

    '''
    1 prikazi menu 
    2 omoguci izbor iz menija te ovisno izboru pokreni funkciju
    3 omoguci izlaz iz aplikacije
    '''