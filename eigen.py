import numpy as np

def calcular_valores_propios(matriz):
    valores_propios = np.linalg.eigvals(matriz)
    print("Los valores propios de la matriz son:")
    print(valores_propios)

def calcular_vectores_propios(matriz):
    valores_propios, vectores_propios = np.linalg.eig(matriz)
    print("Los vectores propios de la matriz son:")
    for i in range(len(valores_propios)):
        print("Valor propio:", valores_propios[i])
        print("Vector propio:", vectores_propios[:,i])

def main():
    while True:
        print("\nMenu:")
        print("1. Calcular valores propios")
        print("2. Calcular vectores propios")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                n = int(input("Ingrese el tamaño de la matriz cuadrada: "))
                matriz = np.zeros((n, n))
                print("Ingrese los elementos de la matriz:")
                for i in range(n):
                    for j in range(n):
                        matriz[i][j] = float(input(f"Elemento [{i+1},{j+1}]: "))
                calcular_valores_propios(matriz)
            except ValueError:
                print("Error: Ingrese un tamaño de matriz válido y elementos numéricos.")
        elif opcion == "2":
            try:
                n = int(input("Ingrese el tamaño de la matriz cuadrada: "))
                matriz = np.zeros((n, n))
                print("Ingrese los elementos de la matriz:")
                for i in range(n):
                    for j in range(n):
                        matriz[i][j] = float(input(f"Elemento [{i+1},{j+1}]: "))
                calcular_vectores_propios(matriz)
            except ValueError:
                print("Error: Ingrese un tamaño de matriz válido y elementos numéricos.")
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()