from customtkinter import CTk, CTkSlider, CTkLabel, CTkFrame, CTkButton
import threading
from priceBRL import price_dolar_brl
from word import create_word
from report import report
import datetime
from time import sleep
import os

class SilderFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(1, weight=1)
        
        self.slider = CTkSlider(self, from_=1, to=60, command=self.slider_event, number_of_steps=100)    
        self.slider.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")
        
        self.label = CTkLabel(self, text=f"{str(int(self.slider.get()))} min", justify='right')
        self.label.grid(row=0,column=1, padx=10, pady=(10, 0), sticky="ewns")
        
    def slider_event(self, value):
        if value >= 60:
            return self.label.configure(text="1 hora")
        else:
            return self.label.configure(text=f'{int(value)} min')
               
         
class Interface(CTk):
    def __init__(self):
        super().__init__()
        
        # Configuração da janela principal.
        self.title("BOT DE MONITORAMENTO DE CAMBIO")
        self.minsize(400, 180)
        self.maxsize(400, 180)
        self.grid_columnconfigure(0, weight=1)
        self.resizable(0,0)
        self.iconbitmap(f'{os.getcwd()}/img/dollar-symbol.ico')
        
        self.frame = SilderFrame(master = self)
        self.frame.grid(row=1, column=0, padx=8, pady=8, sticky="ew")
        
        self.label_info = CTkLabel(self, text="Sistema para monitorar a cotação do dolar.\nEscolha o intervalo de tempo para realizar a monitoração.", justify='left', font=('Helvetica', 12, 'bold'))
        self.label_info.grid(row=0, pady=8, padx=0, sticky="we")
        
        self.label_coin = CTkLabel(self, text="", state="disabled", text_color='#0DE814')
        self.label_coin.grid(row=3, pady=8, sticky="we")
        
        self.button = CTkButton(self, text='Monitorar', command=self.button_envent, font=('Helvetica', 12, 'bold'))
        self.button.grid(row=2, column=0, padx=8,sticky="we")
        
        self.protocol("WM_DELETE_WINDOW", self.close_window)
               
        self.signal = False
    
    def close_window(self):
        self.signal = True
        self.destroy()
        
    def get_coin(self):
        try:            
            brl, date = price_dolar_brl()
            filename = create_word(brl, date)
            report(filename)
            self.label_coin.configure(text=f"Último relatório salvo às: {datetime.datetime.now().strftime("%H:%M:%S")}")
        except:
            self.label_coin.configure(text=f"Não foi possível realizar a cotação.", text_color="red")
        
    def thread_function(self, interval_time):
        agora = datetime.datetime.now()
        rerun = agora + datetime.timedelta(minutes=interval_time)
        
        self.get_coin()
        while True:
            if agora >= rerun:
                self.get_coin()
                agora = datetime.datetime.now()
                rerun = agora + datetime.timedelta(minutes=interval_time)

            agora = datetime.datetime.now()
            sleep(0.75)
            
            if self.signal:
                self.button.configure(state="normal")
                self.signal = False
                break
     
    def button_envent(self):
        time_interval = int(self.frame.slider.get())
        self.button.configure(state="disabled", text="Monitorando...")
        self.frame.slider.configure(state="disabled")
        threading.Thread(target=self.thread_function, args=(time_interval, )).start()
 