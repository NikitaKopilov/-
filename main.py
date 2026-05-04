tasks = [
    {"name": "Прочитать статью", "category": "учёба"},
    {"name": "Сделать зарядку", "category": "спорт"},
    {"name": "Написать отчёт", "category": "работа"},
]

import random
import tkinter as tk

def generate_task():
    task = random.choice(tasks)
    label_result.config(text=task["name"])
    add_to_history(task)

history = []

def add_to_history(task):
    history.append(task)
    update_history_display()

def filter_history(category):
    filtered = [t for t in history if t["category"] == category]
    display_tasks(filtered)

import json

def save_history():
    with open("history.json", "w") as f:
        json.dump(history, f)

def load_history():
    try:
        with open("history.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def add_new_task():
    name = entry_task.get().strip()
    category = selected_category.get()
    if name and category:
        tasks.append({"name": name, "category": category})
        entry_task.delete(0, tk.END)

git remote add origin <ссылка_на_репозиторий>
git push -u origin master

**Автор:** [Ваше Имя Фамилия]
**Описание:** Приложение для генерации случайных задач с фильтрацией и сохранением истории.
**Возможности:**
- Генерация случайной задачи.
- Фильтрация по типу (учёба, спорт, работа).
- Добавление новых задач.
- Сохранение истории в JSON.
**Запуск:**
python main.py
**Примеры использования:**
- Нажмите «Сгенерировать задачу» — появится случайная задача.
- Добавьте свою задачу через форму.
- Фильтруйте историю по категориям.