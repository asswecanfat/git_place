states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}  # 换成集合, 此为集合set Literals

stations = {}
stations['kone'] = {'id', 'nv', 'ut'}
stations['ktwo'] = {'wa', 'id', 'mt'}
stations['kthree'] = {'or', 'nv', 'ca'}
stations['kfour'] = {'nv', 'ut'}
stations['kfive'] = {'ca', 'az'}

final_stations = set()  # 最终选择的广播

while states_needed:
    best_station = None
    states_covered = set()
    for sta, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = sta
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)


