temperaturas = list(map(float, input().split(',')))

total_frio = 0
total_agradavel = 0
total_quente = 0

for temperatura in temperaturas:
    if temperatura < 15.0:
        print(f'{temperatura}°C: Frio')
        total_frio += 1
    elif 15.0 <= temperatura < 25.0:
        print(f'{temperatura}°C: Agradável')
        total_agradavel += 1
    else:
        print(f'{temperatura}°C: Quente')
        total_quente += 1

print('Total Frio:', total_frio)
print('Total Agradável:', total_agradavel)
print('Total Quente:', total_quente)