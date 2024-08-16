def summa_structure(data_structure):
    summa = 0
    if isinstance(data_structure, (list, tuple, set)):
        for i in data_structure:
            summa += summa_structure(i)
    elif isinstance(data_structure, (int, float)):
        summa += data_structure
    elif isinstance(data_structure, str):
        summa += summa_structure(len(data_structure))
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            summa += summa_structure(key)
            summa += summa_structure(value)
    return summa


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

resul = summa_structure(data_structure)

print(resul)
