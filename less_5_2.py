with open('text_4_o_t_t_f.txt', 'r', encoding='utf-8') as f_obj:
    useful = [f'{count}. {line.strip()} - {len(line.split())} слов'
              for count, line in enumerate(f_obj, 1)]
    print(*useful, f'всего строк - {len(useful)}.', sep='\n')
