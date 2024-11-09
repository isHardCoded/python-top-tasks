import random

inventory = ["Лопата", "Топор"]

number = 5
number -= 3
print(number)

materials = {
    "дерево": 5,
    "камень": 0,
    "железо": 0
}

def explore_world():
    locations = ['лес', 'пещера']
    chosen_location = random.choice(locations)

    if chosen_location == 'лес':
        found_wood = random.randint(1, 8)
        materials['дерево'] += found_wood
        
        if found_wood > 0:
            print(f"Вы исследовали {chosen_location} и нашли {found_wood} дерева")
        else:
            print(f"Вы исследовали {chosen_location}, но ничего не нашли")

    elif chosen_location == 'пещера':
        found_stone = random.randint(0, 5)
        found_iron = random.randint(0, 7)
        materials['камень'] += found_stone
        materials['железо'] += found_iron
        
        if found_stone > 0 or found_iron > 0:
            print(f"Вы исследовали {chosen_location} и нашли {found_stone} камня и {found_iron} железа")
        else:
            print(f"Вы исследовали {chosen_location}, но ничего не нашли")



def build_item(item):
    if item == "деревянный меч" and materials['дерево'] >= 3:
        materials['дерево'] -= 3
        inventory.append(item)
        print(f"Вы скрафтили {item}")

    elif item == "каменный меч" and materials['камень'] >= 3:
        materials["камень"] -= 3
        inventory.append(item)
        print(f"Вы скрафтили {item}")
    else:
        print(f"У вас недостаточно ресурсов для {item}")

# функция для отображения инвентаря
def show_inventory():
    print("\n--- Ваш инвентарь ---")
    if inventory:
        for item in inventory:
            print(f"- {item}")
    else:
        print("Ваш инвентарь пуст")


def game_menu():
    while True:
        print("\n--- Меню ---")
        print("1. Показать инвентарь")
        print("2. Создать предмет")
        print("3. Исследовать мир")
        print("4. Выйти из игры")

        choice = int(input("\nВыберите действие: "))

        if choice == 1:
            show_inventory()

        elif choice == 2:
            item = input("Какой предмет вы хотите сделать (деревянный меч / каменный меч)? ")
            build_item(item)

        elif choice == 3:
            explore_world()

        elif choice == 4:
            print("Вы вышли из игры")
            break
        else:
            print("Неправильный ввод")

game_menu()