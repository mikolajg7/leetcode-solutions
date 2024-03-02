kwadraty = []
for i in range(0, 9, 3):  # iteruj co 3, ponieważ są 3 kolumny w każdym kwadracie
    for j in range(0, 9, 3):  # iteruj co 3, ponieważ są 3 wiersze w każdym kwadracie
        kwadrat = [row[j:j+3] for row in sudoku[i:i+3]]
        kwadraty.append(kwadrat)