from Tkinter import *
import threading
import os
import pygame
import threading 


cancion = "No reproduciendo nada"
primeravez = False
nfiles = 0
files = 0
estado = 0


def imprime():  
        pygame.init()
        if pygame.mixer.music.get_busy() == False:
                sel_avance_f()
                
def lista_f(): #se encarga de listar la musica 
	global files
	files = os.listdir("Musica")

def play_f():
	global cancion
	global files
	global nfiles
	if nfiles == 0:
                cancion = files[nfiles]
        encurso.set(cancion)
	pinchaesto = "Musica/%s" % (cancion) 
	pygame.init()
	pygame.mixer.init(44100)
	pygame.mixer.music.set_endevent(pygame.USEREVENT)	
	pygame.mixer.music.load(pinchaesto)
	pygame.mixer.music.play(0)
	pygame.event.wait()
	sel_avance_f()
 
def pause_f():
	pygame.mixer.music.pause()
	
def despause_f():
	pygame.mixer.music.unpause()

def sel_pause_f():
	if estado == 1:
		global estado
		estado = 0
		despause_f()
	elif estado == 0:
		global estado
		estado = 1
		pause_f()
		
def vol_up_f():
	subevol=pygame.mixer.music.get_volume()
	if subevol < 1:
		subevol += 0.2
	pygame.mixer.music.set_volume(subevol)
	
def vol_down_f():
	bajavol=pygame.mixer.music.get_volume()
	if bajavol > 0:
		bajavol -= 0.2
	pygame.mixer.music.set_volume(bajavol)
		
def sel_atras_f():
	global cancion
	global nfiles
	global files
	if nfiles > 0:
		nfiles -= 1
		cancion = files[nfiles]
		dolor_de_cabeza()
			
def sel_avance_f():
	global nfiles
	global cancion
	global files
	lista_f()
	maximo = len(files)
	maximo-=1
	
	if nfiles == maximo:
		nfiles = 0
		cancion = files[nfiles]
		dolor_de_cabeza()
	
	elif nfiles < maximo:
		nfiles += 1
		cancion = files[nfiles]
		dolor_de_cabeza()
		
def stop_f():
        pygame.mixer.music.stop()
        
def nombre_cancion_f():
        global cancion
        return cancion        

def dolor_de_cabeza():  
        t = threading.Thread(target = play_f)  
        t.start() 

        
       
        
def parate_f():
        
        exit()
        
###############################################################################

ventana_musica = Tk()
encurso = StringVar()
lista_f()       



class Reproductor():
        def __init__(self,ventana_musica):
                global cancion
                ventana_musica.title('Musica') #titulo de la ventana
                ventana_musica.geometry("656x416")
                ventana_musica.focus_set() #la pone en primer plano
                ventana_musica.grab_set() #desabilita otras ventanas hasta que esta se destruya
                
                fondot = PhotoImage(file = "images/fondo.gif")
                previa = Label(ventana_musica, image = fondot)
                previa.fondot = fondot
                previa.place(x = 0, y = 0)
                            
                       

                encurso.set(cancion)
                label2=Label(ventana_musica ,textvariable = encurso, font = ("Carbon Phyber", 25)) #texto dentro de la ventana
                label2.configure(background='white')
                label2.place(x = 35, y = 220)
                
                img_1 = PhotoImage(file = "images/atras.gif") 
	        atras  = Button(ventana_musica, image = img_1, command = sel_atras_f)
	        atras.img_1 = img_1
	        atras.place(x = 29, y = 298) #espacio+boton 86
	
                img_2 = PhotoImage(file = "images/play.gif") 
	        play  = Button(ventana_musica, image = img_2, command = dolor_de_cabeza)
	        play.img_2 = img_2
	        play.place(x = 115, y = 298)
  
                img_3 = PhotoImage(file = "images/pause.gif") 
	        pause  = Button(ventana_musica, image = img_3, command = sel_pause_f)
	        pause.img_3 = img_3
	        pause.place(x = 201, y = 298)
  
                img_4 = PhotoImage(file = "images/avance.gif") 
	        adelante  = Button(ventana_musica, image = img_4, command = sel_avance_f)
	        adelante.img_4 = img_4
	        adelante.place(x = 287, y = 298)
	
	        img_5 = PhotoImage(file = "images/stop.gif") 
	        stop  = Button(ventana_musica, image = img_5, command = stop_f)
	        stop.img_5 = img_5
	        stop.place(x = 373, y = 298)
	
	        img_6 = PhotoImage(file = "images/volup.gif") 
	        volup = Button(ventana_musica, image = img_6, command = vol_up_f)
	        volup.img_6 = img_6
	        volup.place(x = 479, y = 298)
	
	        img_7 = PhotoImage(file = "images/voldown.gif") 
	        voldown  = Button(ventana_musica, image = img_7, command = vol_down_f)
	        voldown.img_7 = img_7
	        voldown.place(x = 565, y = 298)
	
	        img_8 = PhotoImage(file = "images/cierra.gif") 
	        mute  = Button(ventana_musica, image = img_8, command = parate_f)
	        mute.img_8 = img_8
	        mute.place(x = 520, y = 126) 
	        
	        img_9 = PhotoImage(file = "images/apaga.gif") 
	        apagat  = Button(ventana_musica, image = img_9, command = parate_f)
	        apagat.img_9 = img_9
	        apagat.place(x = 479, y = 40) 
	        
	        img_10 = PhotoImage(file = "images/reinicia.gif") 
	        reiniciat  = Button(ventana_musica, image = img_10, command = parate_f)
	        reiniciat.img_10 = img_10
	        reiniciat.place(x = 565, y = 40)
	        
	       

                                
Reproductor(ventana_musica)
ventana_musica.mainloop()

     	       	        


  





