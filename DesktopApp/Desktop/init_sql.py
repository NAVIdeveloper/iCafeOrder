import os


def update_data(start,text_order,run,about):
    current = os.getcwd()
    data_path = os.environ['APPDATA']
    os.chdir(data_path)

    file = open("cafebot.txt",'w')
    data = {
        "start":start,
        "text_order":text_order,
        "run":run,
        "about":about,
    }
    file.write(str(data))
    file.close()
    os.chdir(current)


def get_data():
    current = os.getcwd()
    data_path = os.environ['APPDATA']
    os.chdir(data_path)
    file = open("cafebot.txt",'r')
    if file == '':
        update_data("","","","")
    
    os.chdir(current)
    return eval(file.read())

