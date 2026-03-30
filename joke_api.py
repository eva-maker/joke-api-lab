import requests

CATEGORIES = [
    "animal", "career", "celebrity", "dev", "explicit",
    "fashion", "food", "history", "money", "movie",
    "music", "political", "religion", "science", "sport", "travel"
]

def get_joke(category):
    url = f"https://api.chucknorris.io/jokes/random?category={category}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # парсинг елементів з JSON в об'єкт
        joke_obj = {
            "category": data["categories"][0] if data["categories"] else category,
            "created_at": data["created_at"],
            "joke": data["value"]
        }

        return joke_obj

    except requests.exceptions.ConnectionError:
        print("Помилка: немає з'єднання з інтернетом.")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"HTTP помилка: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Помилка запиту: {e}")
        return None
    
def main():
    print("Генератор анекдотів про Чака Норріса")
    print("\nДоступні категорії:")
    print(", ".join(CATEGORIES))

    # категорія з клавіатури та зберігання у змінну
    category = input("\nВведіть категорію: ").strip().lower()

    # перевірка коректності введеної категорії
    if category not in CATEGORIES:
        print(f"\nПомилка: категорія '{category}' не знайдена.")
        print("Виберіть одну з доступних категорій.")
        return

    # робимо API динамічним
    joke_obj = get_joke(category)

    if joke_obj is None:
        return

    # вивід даних з об'єкта в консоль
    print(f"Категорія: {joke_obj['category']}")
    print(f"Дата створення: {joke_obj['created_at']}")
    print(f"Анекдот: {joke_obj['joke']}")

if __name__ == "__main__":
    main()
