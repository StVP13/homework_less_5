with open('text_3_зп.txt', 'r', encoding='utf-8') as f:
    employess_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Average salary = {round(sum(employess_dict.values()) / len(employess_dict), 4)}\n'
          f'Employees with salary  less  than 20k {[e[0] for e in employess_dict.items() if e[1] < 20000]}')
