n = 5  # bits count
rate = 10  # bit rate (1 bit = $10)

cost = n * rate
print(f'сумма сделки = {cost}$')
cost_addition = 0
print(f'чтобы окупить прием средств на покупку {n} биткоинов нужно {cost * 0.015} долларов')
cost_addition += cost * 0.015
print(f'чтобы окупить операцию вывода нужно {cost * 0.005}  долларов')
cost_addition += cost * 0.005
print(f'чтобы получить доход 5% нужно {cost * 0.05} долларов')
cost_addition += cost * 0.05

print(f'выставление счета: {cost + cost_addition}$')

order = 53.5
print(f'проверка: {order - cost * 0.015 - cost * 0.005 - cost * 0.05}')
