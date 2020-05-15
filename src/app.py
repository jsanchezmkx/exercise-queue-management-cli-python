import json
from DataStructures import Queue
from sms import send

# there queue has to be declared globally (outside any other function)
# that way all methods have access to it
queue = Queue(mode="FIFO")
#queue = Queue(mode="LIFO")
    
def print_queue():
    # you must print on the console the entire queue list
    print("Printing the entire list...")
    lista = queue.get_queue()
    y=1
    for x in lista:
        print(str(y) + "-" + x)
        y=y+1

def add():
    print("Ingresa el nombre del guevon que va a entrar en lista: ")
    usuario=input()
    cola=queue.enqueue(usuario)
    mensaje="Has sido agregado a la lista, tienes " , str(len(cola) - 1), " por delante"
    send(mensaje)
    print("Has sido agregado a la lista, tienes " , str(len(cola) - 1), " por delante")
    

def dequeue():
    cliente=queue.dequeue()
    print("has eliminados a el usuario",cliente)
    mensaje='Le toca comer a :'+cliente
    send(mensaje)
    
def save():
    queue_file=queue.get_queue()
    file_to_save = open("queue.json","w+")
    file_to_save.write(json.dumps(queue_file))
    file_to_save.close()


def load():
  #  pass
    file=open("queue.json","r")
    contenido=file.read()
    resultado = json.loads(contenido)
    queue._queue=resultado


    file.close()


    
print("\nHello, this is the Command Line Interface for a Queue Managment application.")
stop = False
while stop == False:
    
    print('''
What would you like to do (type a number and press Enter)?
- Type 1: For adding someone to the Queue.
- Type 2: For removing someone from the Queue.
- Type 3: For printing the current Queue state.
- Type 4: To export the queue to the queue.json file.
- Type 5: To import the queue from the queue.json file.
- Type 6: To quit
    ''')

    option = int(input("Enter a number:"))
    # add your options here using conditionals (if)

    if option == 3:
        print_queue()
    elif option== 1:
        add()
    elif option== 2:
        dequeue()
    elif option == 4:
        print("Guardando lista de espera")
        save()
    elif option == 5:
        print("abriendo lista")
        load()
    elif option == 6:
        print("Bye bye!")
        stop = True
    else:
        print("Not implemented yet or invalid option "+str(option))
