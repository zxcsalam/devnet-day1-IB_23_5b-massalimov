import os
import requests
import json
import hashlib
from pathlib import Path

def manual_load_dotenv(env_path):
    if os.path.exists(env_path):
        with open(env_path, 'r') as f:
            for line in f:
                if '=' in line and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value.strip('"').strip("'")

manual_load_dotenv('.env')

STUDENT_TOKEN = os.getenv("STUDENT_TOKEN", "D1-IB-23-5b-11-7A51")
WEBEX_TOKEN = os.getenv("WEBEX_TOKEN")

TH8 = hashlib.sha256(STUDENT_TOKEN.encode()).hexdigest()[:8]

BASE_PATH = Path("artifacts/day5/webex")
BASE_PATH.mkdir(parents=True, exist_ok=True)

headers = {
    "Authorization": f"Bearer {WEBEX_TOKEN}",
    "Content-Type": "application/json"
}

def save_json(name, data):
    with open(BASE_PATH / name, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"  [+] Файл {name} успешно сохранен.")

def main():
    if not WEBEX_TOKEN:
        print("ОШИБКА: WEBEX_TOKEN не найден! Убедись, что он есть в файле .env")
        return

    print(f"[*] Используем хеш: {TH8}")

    print("1. Запрос информации о себе (me.json)...")
    res_me = requests.get("https://webexapis.com/v1/people/me", headers=headers)
    save_json("me.json", res_me.json())

    print("2. Получение списка комнат (rooms_list.json)...")
    res_rooms = requests.get("https://webexapis.com/v1/rooms", headers=headers, params={"max": 5})
    save_json("rooms_list.json", res_rooms.json())

    room_title = f"Lab 8.6.7 Room - {TH8}"
    print(f"3. Создание комнаты: {room_title}")
    res_create = requests.post(
        "https://webexapis.com/v1/rooms", 
        headers=headers, 
        json={"title": room_title}
    )
    room_data = res_create.json()
    save_json("room_create.json", room_data)
    
    room_id = room_data.get("id")

    msg_text = f"Mission accomplished for Lab 8.6.7. Hash: {TH8}"
    print(f"4. Отправка сообщения в комнату {room_id}...")
    res_msg = requests.post(
        "https://webexapis.com/v1/messages",
        headers=headers,
        json={"roomId": room_id, "text": msg_text}
    )
    save_json("message_post.json", res_msg.json())

    print("5. Получение истории сообщений (messages_list.json)...")
    res_list_msgs = requests.get(
        "https://webexapis.com/v1/messages",
        headers=headers,
        params={"roomId": room_id}
    )
    save_json("messages_list.json", res_list_msgs.json())

    print("\n[SUCCESS] Лаба 8.6.7 выполнена полностью.")

if __name__ == "__main__":
    main()