def list_methods():
    i: int = 0

    for method in dir(list):
        if '__' not in method:
            i += 1
            print(i, method, sep=': ')

list_methods()