# bettercord.py

**Python враппер для [BetterCord API](https://bettercord.xyz)**

---

## Установка

```
pip install bettercord.py
```

## **Важно!**

### Враппер асинхронен, поэтому любые вызовы методов следует выполнять только в асинхронных функциях!

---

# Использование

## Начало

- Импортируем библиотеку

> ```py
> import bettercord
> ```

- Инициализируем клиент

> ```py
> client = bettercord.Client("API токен")
> ```

Если ваш бот использует библиотеку не `discord.py`, то вам следует инициализировать клиент следующим образом:

> ```py
> client = bettercord.Client("API токен", fork_name="название библиотеки")
> ```

</details>

## Боты

### Получение информации о боте

> ```py
> bot_info = await client.get_bot_info(bot_id)
> ```

### Получение всех комментариев к боту

> ```py
> bot_comments = await client.get_bot_comments(bot_id)
> ```

### Отправка статистики

> ```py
> status = await client.post_stats(server_count, shard_count)
> ```

### Автоматическая отправка статистики

> ```py
> client.run(bot)
> ```

## Пользователи

### Получение профиля пользователя

> ```py
> user_info = await client.get_user(user_id)
> ```

### Получение информации о голосе за бота

> ```py
> status = await client.check_vote(user_id)
> ```

## Сервера

### Получение информации о сервере

> ```py
> server_info = await client.get_server_info(server_id)
> ```
