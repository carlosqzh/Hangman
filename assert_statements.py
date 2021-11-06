def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    # Manejo de error cuando no se ingresa un número
    # num = input("Ingresa un número: ")
    # assert num.isnumeric(), "Debes ingresar un número"
    # print(divisors(int(num)))
    # print("Termino mi programa")

    # Manejo de error cuando se ingresa un número negativo
    num = int(input("Ingresa un número: "))
    assert num > 0, "Debes ingresar un número entero"
    print(divisors(num))
    print("Termino mi programa")

if __name__ == "__main__":
    run()