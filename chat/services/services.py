# chat/services.py

from .redis_client import redis_client

class ContextService:
    def __init__(self, user_id):
        self.user_id = user_id
        self.key = f"context:{user_id}"  # e.g., context:aakash123
        self.max_length = 10

    def add_message(self, role, message, category="general"):
        """
        Store a message with role ('user' or 'assistant') and message text.
        """
        entry = f"{role}|{category}|{message}"
        redis_client.rpush(self.key, entry)
        redis_client.ltrim(self.key, -self.max_length, -1)

    def get_context(self):
        """
        Retrieve the context as a list of (role, message) tuples.
        """
        raw = redis_client.lrange(self.key, 0, -1)
        filtered = []
        for entry in raw:
            parts = entry.split("|", 2)
            if len(parts) == 3 and parts[1] == "category":
                filtered.append((parts[0], parts[2]))
        return filtered

    def clear_context(self):
        """
        Deletes the user's context history.
        """
        redis_client.delete(self.key)
