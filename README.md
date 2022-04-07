# bettercord

**Python wrapper for [BetterCord API](https://bettercord.xyz)**

---

<p align="center">
<strong>Few stats</strong>

<img src="https://img.shields.io/pypi/dm/bettercord?style=for-the-badge" alt="">
</p>

---

## Installation

```
pip install bettercord
```

## **WARNING!**

### Wrapper is asynchronous, so any method calls should be performed only is asynchronous functions!

---

# Using

## Starting

- Importing module

> ```py
> import bettercord
> ```

- Inilialing client

> ```py
> client = bettercord.Client("API token")
> ```

If your don't using `discord.py` or `pycord` initialize client like this:

> ```py
> client = bettercord.Client("API token", fork_name="module name")
> ```

## Bots

### Getting info about the bot by ID

> ```py
> bot_info = await client.get_bot_info(bot_id)
> ```

### Getting comments on the bot

> ```py
> bot_comments = await client.get_bot_comments(bot_id)
> ```

### Sending stats

> ```py
> status = await client.post_stats(server_count, shard_count)
> ```

### Automatic sending stats

> ```py
> client.run(bot)
> ```

## Users

### Getting user profile by ID

> ```py
> user_info = await client.get_user_info(user_id)
> ```

### Checking the user's vote for the bot

> ```py
> status = await client.check_bot_vote(user_id)
> ```

## Servers

### Getting info about the server by ID

> ```py
> server_info = await client.get_server_info(server_id)
> ```

### Checking the user's vore for the server

> ```py
> status = await client.check_server_vote(server_id, user_id)
> ```

# Links

- [Examples for this version](https://github.com/Dellyis/bettercord/tree/v1.1.0/examples)
- [API docs](https://docs.bettercord.xyz)
- [Monitoring](https://bettercord.xyz)
