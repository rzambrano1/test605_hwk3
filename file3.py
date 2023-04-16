saludos = "Esto es un saludo en espanol"

def func(saludo):
    for i in range(len(saludo)):
        print(i,saludo[i])
    print('Listo :D')

if __name__ == "__main__":
    func(saludos)