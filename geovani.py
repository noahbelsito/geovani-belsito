from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

# creates an instance of the ChatBot class
geovani_bot = ChatBot(
    "Geovani Belsito",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///geovani-brain.sqlite3"
)

trainer = ListTrainer(geovani_bot)
trainer.train(conversation)
response = geovani_bot.get_response("Good morning!")
print(response)
