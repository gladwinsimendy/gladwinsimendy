#title           :PART_A.py
#description     :This program fetches movie details and generate
#                  either the PDF or PlainText output
#author          :Gladwin Simendy
#date            :
#version         :0.1
#usage           :python PART_A.py
#notes           :
#python_version  :3.6.0  
#=======================================================================
 
# Import the modules needed to run the script.
import sys, os
from reportlab.pdfgen import canvas
 
#dictionary to store movie details
movie_details = {}

# Fetch the Movie details
def get_movie_details():
    os.system('clear')
    print ("\nPlease enter the movie details:")
    movie_name    = input("Movie Name: ")
    movie_runtime = input("Movie Run Time: ")
    movie_lang    = input("Movie Language: ")
    movie_actor  = input("Movie Actor: ")
    movie_genre   = input("Movie Genre: ")
    movie_details.clear()
    movie_details['name'] = movie_name
    movie_details['runtime'] = movie_runtime
    movie_details['lang'] = movie_lang
    movie_details['actor'] = movie_actor
    movie_details['genre'] = movie_genre
    export_menu()
    return

# Automatically find matching func and return attr
def find_methodMatch(object, functionality):
    print ('\n* Methods *')
    for names in dir(object):
        attr = getattr(object,names)
        if callable(attr):
                keyword_list = functionality.split()
                if all(x in str(attr.__doc__) for x in keyword_list) is True:
                    print("Found match - ", names)
                    break
                else:
                    attr = None
    return attr

# Common function to export to specific format
def exportFunc(fileFormat):
    if fileFormat == '1':
        print("Exporting to PDF")
        obj = canvas.Canvas("movie_details.pdf")
        obj.drawString(50,750,"------")
        obj.drawString(50,720,'Movie Name: {}'.format(movie_details['name']))
        obj.drawString(50,690,'Movie Run Time: {}'.format(movie_details['runtime']))
        obj.drawString(50,660,'Movie Language: {}'.format(movie_details['lang']))
        obj.drawString(50,630,'Movie Actor: {}'.format(movie_details['actor']))
        obj.drawString(50,600,'Movie Genre: {}'.format(movie_details['genre']))
        obj.drawString(50,570,"------")
        #obj.save()
        find_methodMatch(obj, 'save')()
    elif fileFormat == '2':
        print("Exporting to Plain Text file")
        obj = open('movie_details.txt','w')
        fillObject(obj)
        find_methodMatch(obj, 'close')()
        #obj.close()
    main_menu()
    return

# export to PDF
def export_toPDF():
    exportFunc('2')
    return

# export to Plain Text
def export_toPlaintext():
    exportFunc('2')
    return

# Fill the details
def fillObject(obj):
    #obj.write('\n ------ \n')
    find_methodMatch(obj, 'write')('\n ------ \n')
    find_methodMatch(obj, 'write')('Movie Name: {}\n'.format(movie_details['name']))
    find_methodMatch(obj, 'write')('Movie Run Time: {}\n'.format(movie_details['runtime']))
    find_methodMatch(obj, 'write')('Movie Language: {}\n'.format(movie_details['lang']))
    find_methodMatch(obj, 'write')('Movie Actor: {}\n'.format(movie_details['actor']))
    find_methodMatch(obj, 'write')('Movie Genre: {}\n'.format(movie_details['genre']))
    find_methodMatch(obj, 'write')(' ------ \n')


# ==============
#     MENUS 
# ==============

# Execute menu
def exec_menu(choice, menu, menu_actions):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions[menu]()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print ("Wrong selection, please try again\n")
            menu_actions[menu]()
    return

# Main Menu actions
main_menu_actions = {
    'main_menu_action': lambda:main_menu,
    '1': get_movie_details, 
    '0': exit,
}

# Export Menu actions
export_menu_actions = {
    'export_menu_action': lambda:export_menu,
    '1': export_toPDF,
    '2': export_toPlaintext,
    '3': main_menu_actions['main_menu_action'], 
    '0': exit,
}

# Main menu
def main_menu():
    os.system('clear')
    print ("\n\nWelcome,")
    print ("Select Menu:")
    print ("1. Get the Movie Details")
    print ("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice, 'main_menu', main_menu_actions)
    return

# Export menu
def export_menu():
    os.system('clear')
    print ("\nSelect Export Format:")
    print ("1. PDF")
    print ("2. Plain Text")
    print ("3. Back")
    print ("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice, 'export_menu', export_menu_actions)
    return

# Quit program
def exit():
    sys.exit()


##################
def main():
    # Launch main menu
    main_menu()
    return

if __name__ == "__main__": main()
