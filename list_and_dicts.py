def run():
    super_list = [
        {"name": "Carlos", "last_name": "Valencia"},
        {"name": "Anahi", "last_name": "Palomino"}
    ]

    super_dicts = {
        "numbers": [1, 2, 3, 4],
        "letters": ["a", "b", "c"],
        "vocals": ["a", "e", "o"]
    }

    for i in super_list:
        for key, values in i.items():
            print(key, "-", values)

if __name__ == "__main__":
    run()