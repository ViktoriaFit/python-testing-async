import asyncio
import time

# 1. Обычная (синхронная) функция
def sync_task(name, seconds):
    print(f"Начало: {name}")
    time.sleep(seconds) # Программа "замирает" на seconds секунд
    print(f"Конец: {name}")

# 2. Асинхронная функция
async def async_task(name, seconds):
    print(f"Начало: {name}")
    await asyncio.sleep(seconds) # Программа "ждет", но не блокирует другие задачи
    print(f"Конец: {name}")

# --- ПРОВЕРКА ---
print("--- 1. Синхронный запуск (по очереди) ---")
start = time.time()
sync_task("Задача 1", 2)
sync_task("Задача 2", 2)
end = time.time()
print(f"Общее время: {end - start:.2f} секунд\n")

print("--- 2. Асинхронный запуск (одновременно) ---")
async def main():
    start = time.time()
    # Запускаем две задачи одновременно
    await asyncio.gather(
        async_task("Задача 1", 2),
        async_task("Задача 2", 2)
    )
    end = time.time()
    print(f"Общее время: {end - start:.2f} секунд")

asyncio.run(main())