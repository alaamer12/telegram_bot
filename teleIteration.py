from telethon.sync import TelegramClient

api_id = 23406634
api_hash = "0701d1d306497f8dcf2578da224f89fb"

output_file = "channel_messages4.txt"

with TelegramClient('name', api_id, api_hash) as client:
    dialogs = client.get_dialogs()

    with open(output_file, "w", encoding="utf-8") as file:
        for chat in dialogs:
                file.write("Channel: {}\n".format(chat.title))
                file.write("************************************************************\n")

                messages = client.get_messages(chat, limit=400)

                for message in messages:
                    file.write(message.message + "\n")

                file.write("\n")

