from database import insert_user, find_user, update_user, delete_user
from datetime import datetime  # Додайте цей імпорт

def main():
    while True:
        print("\nМеню:")
        print("1. Додати нового користувача")
        print("2. Пошук користувача")
        print("3. Оновити користувача")
        print("4. Видалити користувача")
        print("5. Вийти")
        
        choice = input("Виберіть опцію (1-5): ")

        if choice == '1':
            # Додати користувача
            first_name = input("Введіть ім'я: ")
            last_name = input("Введіть прізвище: ")
            email = input("Введіть email: ")
            password = input("Введіть пароль: ")
            phone = input("Введіть телефон (опційно): ")
            street = input("Введіть вулицю (опційно): ")
            city = input("Введіть місто (опційно): ")
            postal_code = input("Введіть поштовий індекс (опційно): ")
            
            user = {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "password": password,
                "phone": phone,
                "address": {
                    "street": street,
                    "city": city,
                    "postal_code": postal_code
                },
                "profile_picture": "",  # Можна додати URL фотографії
                "date_of_birth": "1990-01-01",  # Можна додати дату народження
                "role": {
                    "type": "user",
                    "permissions": ["read"]
                },
                "created_at": datetime.now(),
                "updated_at": datetime.now()
            }
            
            insert_user(user)

        elif choice == '2':
            # Пошук користувача
            email = input("Введіть email користувача для пошуку: ")
            find_user(email)

        elif choice == '3':
            # Оновити користувача
            email = input("Введіть email користувача для оновлення: ")
            update_field = input("Що потрібно оновити (наприклад, first_name, last_name, phone): ")
            new_value = input(f"Введіть нове значення для {update_field}: ")
            update_data = {update_field: new_value}
            update_user(email, update_data)

        elif choice == '4':
            # Видалити користувача
            email = input("Введіть email користувача для видалення: ")
            delete_user(email)

        elif choice == '5':
            # Вихід
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
