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
    if not os.path.isfile('cafebot.txt'):
        f=open('cafebot.txt','w+')
        f.write("")
        f.close()
        update_data("","","","")

    file = open("cafebot.txt",'r')
    if file == '':
        update_data("","","","")
        file = open("cafebot.txt",'r')    
    
    os.chdir(current)
    return eval(file.read())

def get_token():
    current = os.getcwd()
    data_path = os.environ['APPDATA']
    os.chdir(data_path)
    if os.path.isfile('cafebot_token.txt'):
        file = open("cafebot_token.txt",'r')    
    else:
        f=open('cafebot_token.txt','w+')
        f.write("")
        f.close()
        file = open("cafebot_token.txt",'r')    
        
    os.chdir(current)
    return file.read()

def set_token(token):
    current = os.getcwd()
    data_path = os.environ['APPDATA']
    os.chdir(data_path)

    file = open("cafebot_token.txt",'w')
    file.write(token)
    file.close()
    os.chdir(current)
    return True
