#Trivia perteneciente a: ROGELIO GUEVARA ENRIQUEZ
#Importando librerias:
import time
import os
import random

#Constantes de colores:
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

#Titulo de la trivia:
titulo = "TRIVIA SOBRE SILICOM VALLEY"
print(YELLOW + '-' * 19 + titulo + '-' * 19 + RESET + '\n')

#Variables:
PTS_TOTAL = 150         #Constante
puntaje = 0             #Integer
iniciar_trivia = True   #Booleano
intentos = 0            #Integer
lista = []              #Lista vacía
punta_total = []        #Lista vacía

#Entrada y presentaciones:
usuario_name = input("Ingrese un nombre de usuario para la trivia: ").upper()
print('\n' + ' ' * 9 + BLUE + f"<<< Hola {usuario_name}, empezaremos con la trivia >>>\n" + RESET)
print(' ' * 13 + MAGENTA + f"Empiezas con [{puntaje} puntos], en este juego" + RESET +
    '\n' + "Si aciertas se te sumarán puntos y si fallas se te restarán puntos")

while iniciar_trivia == True:
    intentos += 1
    puntaje = 0

    print(' ' * 25 + WHITE + f"Intento número {intentos}" + RESET)
    input('\n' + "Presiona" + RED + " ENTER " + RESET + "para continuar...")

    os.system('clear')

    print('\n' + ' ' * 12 + WHITE + "¡Empecemos a jugar, cuenta regresiva en!" + RESET)

    time.sleep(3.1)

    #Carga inicial antes de empezar a jugar:
    for i in range(3, 0, -1):
        print(' ' * 31, i)
        time.sleep(1.1)
    
    os.system('clear')

    #Pregunta 1:
    pregunta1 = input('\n' + "Primera pregunta: ¿Quiénes crearon el Transistor?\n"
            "a)Bardeen, Shockley y Brattain.\n"
            "b)Gates, Jobs y Wozniak.\n"
            "c)Oppenheimer, Heisenberg y Einstein.\n"
            "d)Plank, Rutherford y Newton.\n"
            '\n' + GREEN + "Ingrese su respuesta [a, b, c ó d]: " + RESET)

    #Se debe ingresar de manera correcta:
    while pregunta1 not in ("a", "b", "c", "d", "x"):
        pregunta1 = input('\n' + RED + "Debes responder correctamente [a, b, c ó d]. Inténtalo nuevamente: " + RESET)

    #Condición a cumplirse:
    if pregunta1 == "a":
        puntaje += 20
        print('\n' + "¡Felicidades, la respuesta es correcta!")
        print('\n' + "¡Se te sumará" + RED + " 20 " + RESET + "puntos")
    elif pregunta1 == "b":
        puntaje -= 10
        print('\n' + "¡Lo lamento, Gates creo Microsoft y Jobs y Wozniak crearon Apple!")
        print('\n' + "¡Se te restará" + RED + " 10 " + RESET + "puntos")
    elif pregunta1 == "c":
        puntaje -= 10
        print('\n' + "¡Lo lamento, Oppenheimer, Heisenberg y Einstein era fisicos teoricos de la relatividad!")
        print('\n' + "¡Se te restará" + RED + " 10 " + RESET + "puntos")
    elif pregunta1 == "d":
        puntaje -= 10
        print('\n' + "¡Lo lamento, Plank, Rutherford y Newton ni siquiera vivieron en la misma epoca!")
        print('\n' + "¡Se te restará" + RED + " 10 " + RESET + "puntos")
    else:
        puntaje += 50
        print('\n' + "¡Felicidades, encontraste este mensaje secreto que te da la 'buena suerte'!")

    print('\n' + MAGENTA + f"Tu puntaje actual es de [{puntaje} Puntos / {PTS_TOTAL} Posibles]" + RESET)

    time.sleep(5)

    #Refrescar la pantalla:
    input('\n' + "==> Presiona" + RED + " ENTER " + RESET + "para continuar con la 2° pregunta...")
    os.system("clear")

    #Pregunta 2:
    pregunta2 = input("Segunda pregunta: ¿Qué empresas estan en Silicon Valley?\n"
            "a)Apple, Cisco, Netflix y Lenovo.\n"
            "b)eBay, HP, Tesla y Google.\n"
            "c)Intel, Nvidia, Facebook y Tencent.\n"
            "d)Todas son correctas.\n"
            '\n' + GREEN + "Ingrese su respuesta [a, b, c ó d]: " + RESET)

    #Se debe ingresar de manera correcta:
    while pregunta2 not in ("a", "b", "c", "d", "x"):
        pregunta2 = input('\n' + RED + "Debes responder correctamente [a, b, c ó d]. Inténtalo nuevamente: " + RESET)

    #ESTA PREGUNTA SE PUNTUARÁ DE MANERA RANDOM:
    #Condición a cumplirse:
    if pregunta2 == "a":
        puntaje -= random.randint(10, 15)
        print('\n' + "¡Lo lamento, Lenovo es una empresa que se encuentra en Pekín - China!")
        print('\n' + "¡Se te restará puntos random, entre" + RED + " (10 - 15) " + RESET + "puntos")
    elif pregunta2 == "b":
        puntaje += random.randint(25, 30)
        print('\n' + "¡Felicidades, la respuesta es correcta!")
        print('\n' + "¡Se te sumará puntos random, entre" + RED + " (25 - 30) " + RESET + "puntos")
    elif pregunta2 == "c":
        puntaje -= random.randint(10, 15)
        print('\n' + "¡Lo lamento, Tencent es una empresa que esta en Taiwán!")
        print('\n' + "¡Se te restará puntos random, entre" + RED + " (10 - 15) " + RESET + "puntos")
    elif pregunta2 == "d":
        puntaje -= random.randint(10, 15)
        print('\n' + "¡Lo lamento, solo una es correcta!")
        print('\n' + "¡Se te restará puntos random, entre" + RED + " (10 - 15) " + RESET + "puntos")
    else:
        puntaje += 50
        print('\n' + "¡Felicidades, encontraste este mensaje secreto que te da la 'buena suerte'!")

    print('\n' + MAGENTA + f"Tu puntaje actual es de [{puntaje} Puntos / {PTS_TOTAL} Posibles]" + RESET)

    time.sleep(5)

    #Refrescar la pantalla:
    input('\n' + "==> Presiona" + RED + " ENTER " + RESET + "para continuar con la 3° pregunta...")
    os.system("clear")

    #Pregunta 3:
    pregunta3 = input("Tercera pregunta: Elija la secuencia que no corresponda.\n"
            "a)MacOS - Steve Jobs - Apple\n"
            "b)Windows - Bill Gates - Microsoft\n"
            "c)Linux - Linus Torvalds - IBM\n"
            "d)MS_DOS - Tim Paterson - Microsoft\n"
            '\n' + GREEN + "Ingrese su respuesta [a, b, c ó d]: " + RESET)

    #Se debe ingresar de manera correcta:
    while pregunta3 not in ("a", "b", "c", "d", "x"):
        pregunta3 = input('\n' + RED + "Debes responder correctamente [a, b, c ó d]. Inténtalo nuevamente: " + RESET)

    #Condición a cumplirse:
    if pregunta3 == "a":
        puntaje -= 13
        print('\n' + "¡Lo lamento, esta secuencia si es correcta!")
        print('\n' + "¡Se te restará" + RED + " 13 " + RESET + "puntos")
    elif pregunta3 == "b":
        puntaje -= 13
        print('\n' + "¡Lo lamento, esta secuencia si es correcta!")
        print('\n' + "¡Se te restará" + RED + " 13 " + RESET + "puntos")
    elif pregunta3 == "c":
        puntaje += 25
        print('\n' + "¡Felicidades, Linus Torvalds nunca trabajo en IBM desarrollando Linux!")
        print('\n' + "¡Se te sumará" + RED + " 25 " + RESET + "puntos")
    elif pregunta3 == "d":
        puntaje -= 13
        print('\n' + "¡Lo lamento, esta secuencia si es correcta!")
        print('\n' + "¡Se te restará" + RED + " 13 " + RESET + "puntos")
    else:
        puntaje += 50
        print('\n' + "¡Felicidades, encontraste este mensaje secreto que te da la 'buena suerte'!")

    print('\n' + MAGENTA + f"Tu puntaje actual es de [{puntaje} Puntos / {PTS_TOTAL} Posibles]" + RESET)

    time.sleep(5)

    #Refrescar la pantalla:
    input('\n' + "==> Presiona" + RED + " ENTER " + RESET + "para continuar con la 4° pregunta...")
    os.system("clear")

    #Pregunta 4:
    pregunta4 = input("Cuarta pregunta: Elija la respuesta mejor planteada.\n"
            "a)Silicon Valley se encuentra en San Francisco, en el sur de California, EE.UU.\n"
            "b)Shockley fundó la empresa de procesadores Intel y Shockley Semiconductor. \n"
            "c)Jhon Bardeen ganó 2 Nobel de Física y la más importante fue sobre el invento del Transistor.\n"
            "d)En Silicon Valley se probó la primera bomba atómica que sería usada contra Japón.\n"
            '\n' + GREEN + "Ingrese su respuesta [a, b, c ó d]: " + RESET)

    #Se debe ingresar de manera correcta:
    while pregunta4 not in ("a", "b", "c", "d", "x"):
        pregunta4 = input('\n' + RED + "Debes responder correctamente [a, b, c ó d]. Inténtalo nuevamente: " + RESET)

    #Condiciones a cumplirse:
    if pregunta4 == "a":
        puntaje += 5
        print('\n' + "¡Lo lamento, esta opción es casi correcta!")
        print('\n' + "¡Se te sumará" + RED + " 5 " + RESET + "puntos")
    elif pregunta4 == "b":
        puntaje -= 5
        print('\n' + "¡Lo lamento, esta opción es incorrecta!")
        print('\n' + "¡Se te restará" + RED + " 5 " + RESET + "puntos")
    elif pregunta4 == "c":
        puntaje = puntaje * 2
        print('\n' + "¡Felicidades, esta es la opción correcta!")
        print('\n' + "¡Se te multiplicará" + RED + " x2 " + RESET + "el puntaje anterior")
    elif pregunta4 == "d":
        puntaje = puntaje / 2
        print('\n' + "¡Lo lamento, esta opción es la mas disparatada!")
        print('\n' + "¡Se te dividirá" + RED + " /2 " + RESET + "el puntaje anterior")
    else:
        puntaje += 50
        print('\n' + "¡Felicidades, encontraste este mensaje secreto que te da la 'buena suerte'!")

    #Mensaje de salida:
    print('\n' + CYAN + f"Gracias {usuario_name} por jugar mi trivia, ¡obtuviste [{puntaje} Puntos / {PTS_TOTAL} Posibles] en total!" + RESET)

    time.sleep(5)
    
    #Agregando a las listas:
    lista.append(intentos)
    punta_total.append(puntaje)

    #Pregunta de intentos:
    repetir_trivia = input('\n' + MAGENTA + "¿Deseas intentar la trivia nuevamente? [S/N]: " + RESET).upper()
    while repetir_trivia not in ("S", "N"):
        repetir_trivia = input('\n' + RED + "Debes responder correctamente [S ó N]. Inténtalo nuevamente: " + RESET)

    if repetir_trivia != "S":
        os.system('clear')
        print('\n' + MAGENTA + "Tus puntajes fueron:" + RESET + '\n')
        for i in range(1, len(lista)+1, 1):
            x = i-1
            print(MAGENTA + f"Intento numero {i} ==> Puntaje: {punta_total[x]}" + RESET)
        
        print('\n' + YELLOW + "¡Buena suerte, espero la hayas pasado bien!" + RESET + '\n')
        iniciar_trivia = False
    else:
        os.system("clear")
