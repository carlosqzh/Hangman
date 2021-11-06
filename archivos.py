def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    letter = ["Valencia", "Palomino", "Cruz"]
    with open("./archivos/letter.txt", "a", encoding="utf-8") as f:
        for let in letter:
            f.write(let)
            f.write("\n")


def run():
    write()

if __name__ == "__main__":
    run()