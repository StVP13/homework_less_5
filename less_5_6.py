subj = {}
with open('text_6_time_t.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.replace('-', '0').replace(':', '').replace('(л)', '') \
        .replace('(пр)', '').replace('(лаб)', '').split()
        subj[line[0]] = sum(map(int, line[1:]))
    print(f'общее количество часов по предмету: \n{subj}')