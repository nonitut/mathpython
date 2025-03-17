import math
import pandas as pd
import itertools 

# print(math.comb(5,2)) # комбинации 
# print(math.comb(8,3))

data = {
    "fruits" : [
        "apple",
        "banana",
        "peach",
        "orange",
        "kivi"
        ]
}

df = pd.DataFrame(data)
print(df)

n = len(df)
# print(n) 
# сколько всего фруктов (5)

# Комбинации
k = 3
comb = math.comb(n,k)
print(f"\nКоличество способов выбрать за счет комбинирования {k} фрукта(ов) из {n} (комбинаций): {comb}")

# Пермутации 
perm = math.perm(n,k)
print(f"\nКоличество способов выбрать за счет пермутации {k} фрукта(ов) из {n} (комбинаций): {perm}")


# Генерация всех комбинаций
comb_list = list(itertools.combinations(df['fruits'], k))
print("\nВсе комбинации:")
for comb in comb_list:
    print(comb)

# Генерация всех пермутаций
perm_list = list(itertools.permutations(df['fruits'], k))
print("\nВсе пермутации:")
for perm in perm_list:
    print(perm)
    


# print(math.comb(6,3))