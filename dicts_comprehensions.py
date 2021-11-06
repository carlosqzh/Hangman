def run():
    # my_dictionary = {}
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         my_dictionary[i] = i**3

    # print(my_dictionary) 

    # my_dictironary = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    
    # print(my_dictironary)

    my_dictionary = {i: round(i**(1/2), 2) for i in range(1, 1001)} #Se puede usar round para dejar solo con dos dígitos el resultado de la raíz cuadrada

    print(my_dictionary)


if __name__ == "__main__":
    run() 
