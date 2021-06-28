from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# creates an instance of the ChatBot class
geovani_bot = ChatBot(
    "Geovani Belsito",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",  # storage adapter
    # logic_adapters=[
    #     'chatterbot.logic.MathematicalEvaluation',
    #     'chatterbot.logic.TimeLogicAdapter'
    # ],
    database_uri="sqlite:///geovani-brain.sqlite3"  # name of storage
)

# reinforced training
"""
trainer = ListTrainer(geovani_bot)

trainer.train([
    ""
])

count = 0
while count < 200:
    response = geovani_bot.get_response("Good")
    count += 1
    print(count)
"""

# talking raw to my bot
while True:
    try:
        bot_input = geovani_bot.get_response(input())
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
