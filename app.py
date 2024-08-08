from interface.interface import Interface
import os
import requests

def first_config():
    if not os.path.isdir(f'{os.getcwd()}/img'):
        os.mkdir('img')
        url = 'https://raw.githubusercontent.com/joaomatheusars/bot-de-monitoramento-de-cambio/main/img/dollar-symbol.ico'
        ico = requests.get(url).content
        with open(f'{os.getcwd()}/img/dollar-symbol.ico', 'wb') as file:
            file.write(ico)
        

def main():
    app = Interface()
    app.mainloop()
 
if __name__ == "__main__":
	first_config()
	main()