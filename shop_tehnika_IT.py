import json
from typing import List, Dict

DATA_FILE = "store_data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"products": [
            {"name": "iPhone", "price": 80000, "id": 1},
            {"name": "POCO", "price": 25000, "id": 2},
            {"name": "Наушники", "price": 5000, "id": 3},
            {"name": "Гипер Крыса", "price": 1500, "id": 4},
            {"name": "iPad", "price": 60000, "id": 5},
            {"name": "iMac", "price": 120000, "id": 6},
        ], "users": [{"username": "admin228", "password": "admin228", "role": "administrator", "cart": []}]} # Added admin user


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def register_user(data):
    while True:
        username = input("Введите имя пользователя: ")
        if username not in [user["username"] for user in data["users"]]:
            password = input("Введите пароль: ")
            data["users"].append({"username": username, "password": password, "role": "user", "cart": []})
            print("Пользователь успешно зарегистрирован!")
            break
        else:
            print("Имя пользователя уже занято. Попробуйте другое.")


def authenticate_user(data):
    while True:
        username = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        user = next((user for user in data["users"] if user["username"] == username and user["password"] == password), None)
        if user:
            return user
        else:
            print("Неверный логин или пароль. Попробуйте ещё раз.")


def add_product(data):
    name = input("Введите название товара: ")
    while True:
        try:
            price = float(input("Введите цену товара: "))
            break
        except ValueError:
            print("Неверный формат цены. Попробуйте ещё раз.")
    new_id = max(p["id"] for p in data["products"]) + 1 if data["products"] else 1
    data["products"].append({"name": name, "price": price, "id": new_id})
    print("Товар успешно добавлен!")


def delete_product(data):
    print_products(data)
    while True:
        try:
            product_id = int(input("Введите ID товара для удаления (0 для отмены): "))
            product_to_delete = next((p for p in data["products"] if p["id"] == product_id), None)
            if product_to_delete:
                data["products"].remove(product_to_delete)
                print("Товар успешно удалён!")
                break
            elif product_id == 0:
                break
            else:
                print("Товар с таким ID не найден.")
        except ValueError:
            print("Неверный формат ID.")


def print_products(data):
    if not data["products"]:
        print("Список товаров пуст.")
        return
    print("Список товаров:")
    for product in data["products"]:
        print(f"{product['id']}. {product['name']} - {product['price']} руб.")


def sort_products(data, sort_key, reverse):
    data["products"].sort(key=lambda x: x[sort_key], reverse=reverse)
    print("Товары отсортированы!")


def filter_products(data):
  while True:
    filter_method = input("Как фильтровать товары (цена >X, цена <X, название =Y, 0 для отмены): ")
    if filter_method.startswith("цена >"):
      try:
        price_threshold = float(filter_method[6:])
        filtered_products = [p for p in data["products"] if p["price"] > price_threshold]
        print_products({"products": filtered_products})
        break
      except ValueError:
        print("Неверный формат цены.")
    elif filter_method.startswith("цена <"):
      try:
        price_threshold = float(filter_method[6:])
        filtered_products = [p for p in data["products"] if p["price"] < price_threshold]
        print_products({"products": filtered_products})
        break
      except ValueError:
        print("Неверный формат цены.")
    elif filter_method.startswith("название ="):
      name_threshold = filter_method[10:]
      filtered_products = [p for p in data["products"] if p["name"] == name_threshold]
      print_products({"products": filtered_products})
      break
    elif filter_method == "0":
      break
    else:
      print("Неверный метод фильтрации.")


def add_to_cart(user, data):
    print_products(data)
    while True:
        try:
            product_id = int(input("Введите ID товара для добавления в корзину (0 для отмены): "))
            product = next((p for p in data["products"] if p["id"] == product_id), None)
            if product:
                user["cart"].append(product)
                print(f"{product['name']} добавлен в корзину!")
                break
            elif product_id == 0:
                break
            else:
                print("Товар с таким ID не найден.")
        except ValueError:
            print("Неверный формат ID.")


def checkout(user):
    if not user["cart"]:
        print("Ваша корзина пуста.")
        return
    total_price = sum(p["price"] for p in user["cart"])
    print("Товары в заказе:")
    for product in user["cart"]:
        print(f"- {product['name']} ({product['price']} руб.)")
    print(f"Итоговая сумма: {total_price} руб.")
    user["cart"] = [] # Очищаем корзину после покупки
    print("Заказ оформлен успешно!")


def user_menu(user, data):
    while True:
        print(f"\nМеню пользователя {user['username']}:")
        print("1. Просмотреть товары")
        print("2. Сортировать товары")
        print("3. Фильтровать товары")
        print("4. Добавить в корзину")
        print("5. Оформить заказ")
        print("6. Выйти")
        action = input("Выберите действие: ")

        if action == "1":
            print_products(data)
        elif action == "2":
            while True:
                sort_key = input("Сортировать по (цена/название, 0 для отмены): ").lower()
                if sort_key in ["цена", "название"]:
                    reverse = input("В порядке возрастания (asc) или убывания (desc)? (asc/desc): ").lower() == "desc"
                    sort_products(data, sort_key, reverse)
                    break
                elif sort_key == "0":
                    break
                else:
                    print("Неверный ключ сортировки.")
        elif action == "3":
            filter_products(data)
        elif action == "4":
            add_to_cart(user, data)
        elif action == "5":
            checkout(user)
        elif action == "6":
            break
        else:
            print("Неверный пункт меню.")


def admin_menu(data):
    while True:
        print("\nАдмин-панель:")
        print("1. Добавить товар")
        print("2. Удалить товар")
        print("3. Просмотреть товары")
        print("4. Сортировать товары")
        print("5. Фильтровать товары")
        print("6. Выйти")
        action = input("Выберите действие: ")

        if action == "1":
            add_product(data)
        elif action == "2":
            delete_product(data)
        elif action == "3":
            print_products(data)
        elif action == "4":
            while True:
                sort_key = input("Сортировать по (цена/название, 0 для отмены): ").lower()
                if sort_key in ["цена", "название"]:
                    reverse = input("В порядке возрастания (asc) или убывания (desc)? (asc/desc): ").lower() == "desc"
                    sort_products(data, sort_key, reverse)
                    break
                elif sort_key == "0":
                    break
                else:
                    print("Неверный ключ сортировки.")
        elif action == "5":
            filter_products(data)
        elif action == "6":
            break
        else:
            print("Неверный пункт меню.")
    save_data(data)


def main():
    data = load_data()

    while True:
        print("\nМеню:")
        print("1. Регистрация")
        print("2. Вход")
        print("3. Выход")
        punct = input("Выберите пункт меню: ")

        if punct == "1":
            register_user(data)
        elif punct == "2":
            user = authenticate_user(data)
            if user:
                if user["role"] == "administrator":
                    admin_menu(data)
                else:
                    user_menu(user, data)
        elif punct == "3":
            break
        else:
            print("Неверный пункт меню.")
    print("До свидания!")

if __name__ == "__main__":
    main()
