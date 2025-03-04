import random
import math
list_size = 8
min = 1
max = 8


def generate_random_list(list_size, min, max):
    random_number_list = []
    while list_size != 0:
        n=random.randint(min, max) 
        list_size = list_size - 1
        random_number_list.append(n)   

    return random_number_list
        
def dpmr(list_size, min, max):
    random_number_list = generate_random_list(list_size, min, max)
    print(f"Liste aléatoire générée{random_number_list}")
    sorted_random_number_list = sorted(random_number_list)
    print(f"Liste aléatoire triée{sorted_random_number_list}")
    half_list_size = list_size // 2
    rounded_half_list_size = math.floor(half_list_size)
    first_part = sorted_random_number_list[:rounded_half_list_size]
    second_part = sorted_random_number_list[rounded_half_list_size:]
    print(f"Première partie {first_part}")
    print(f"Seconde partie {second_part}")
    number_to_append = n=random.randint(min, max)
    print(f"Nombre aléatoire généré pour insertion {number_to_append}")
    if number_to_append <= first_part[-1]:
        print("Le nombre aléatoire est à insérer dans la première liste")
        first_part.append(number_to_append)
    else:
        print("Le nombre aléatoire est à insérer dans la seconde liste")
        second_part.append(number_to_append)

    final_list = first_part + second_part
    return final_list



result = dpmr(list_size, min, max)
print(result)