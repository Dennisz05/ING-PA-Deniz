import serial #biblioteca pentru comunicarea cu porturile
import time #biblioteca pentru manipularea timpuli
import csv #biblioteca pentru lucrul cu fișiere CSV.
import matplotlib #biblioteca pentru crearea de grafice.
matplotlib.use("tkAgg")
import matplotlib.pyplot as plt
import numpy as np #biblioteca pentru manipularea vectorilor si matricelor

if __name__ == '__main__': #asigura ca blocul de cod este executat doar daca scriptul este rulat
    ser = serial.Serial('COM3', 9600)  #initializeaza o conexiune seriala la portul COM3
    ser.flushInput() 
    plot_window = 20 #seteaza dimensiunea ferestrei
    y_var = np.array(np.zeros([plot_window])) #creeaza un vector 

    plt.ion() #activeaza modul interactiv pentru matplotlib
    fig, ax = plt.subplots() #axele pentru grafic
    line, = ax.plot(y_var) #linia de grafic pe axe
    
    ax.set_xlabel('Timp (s)')
    ax.set_ylabel('Nivel apă (mm)')

    while True: #o bucla pentru a citi datele si sa le proceseze
        try:
            ser_bytes = ser.readline() #citeste o linie de date de la port
            try:
                decoded_bytes = float(ser_bytes[0:len(ser_bytes) - 2].decode("utf-8"))
                print(decoded_bytes) #afiseaza valoarea decodificata
            except:
                continue
            with open("test_data.csv", "a") as f: #dewchide fisierul 
                writer = csv.writer(f, delimiter=",") #creeaza un scriitor CSV  
                writer.writerow([time.time(), decoded_bytes]) #scrie timpul curent si valoarea decodificata in fisier
            y_var = np.append(y_var, decoded_bytes) #adauga o valoare la vector
            y_var = y_var[1:plot_window + 1]  #mentine dimensiunea vecotului
            line.set_ydata(y_var) #actualizeaza datele liniei de grafic
            ax.relim() #reseteaza limitele axelor 
            ax.autoscale_view() #autoscalează vederea axelor
            fig.canvas.draw() #redeseneaza figura 
            fig.canvas.flush_events() #flusheaza evenimentele grafice
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            break
