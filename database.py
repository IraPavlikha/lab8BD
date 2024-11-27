from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

# Підключення до MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['user_profiles_db']
users_collection = db['users']

# Функція для вставки нового користувача
def insert_user(user):
    result = users_collection.insert_one(user)
    print(f"Користувач доданий з ID: {result.inserted_id}")

# Функція для пошуку користувача за email
def find_user(email):
    user = users_collection.find_one({"email": email})
    if user:
        print(f"Знайдений користувач: {user}")
    else:
        print("Користувача не знайдено")
    return user

# Функція для оновлення користувача
def update_user(email, update_data):
    result = users_collection.update_one(
        {"email": email},
        {"$set": update_data}
    )
    if result.modified_count > 0:
        print("Користувача оновлено")
    else:
        print("Нічого не змінено")

# Функція для видалення користувача
def delete_user(email):
    result = users_collection.delete_one({"email": email})
    if result.deleted_count > 0:
        print("Користувача видалено")
    else:
        print("Користувача не знайдено")
