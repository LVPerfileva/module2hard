luky_numbers = []

divider = int(input('Какое число на воротах (целое от 3 до 20)? Введите: '))
while divider < 3 or divider > 20:
    divider = int(input('Ошиблись, введите число от 3 до 20: '))
for i in range(1, divider):
    for j in range(i+1, divider):
        if (i+j) % divider == 0:
            luky_numbers.extend([i, j])

print('Ваш пароль : ')
print(*luky_numbers,sep='')