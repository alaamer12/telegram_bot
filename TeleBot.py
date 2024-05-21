import sys
sys.path.insert(1, r'D:\ups\ideaProjects\thanwyaIdea\tests\test6')
import os
import shutil
from telethon.sync import TelegramClient, events
from func import ALLOWED_EXTENSIONS , get_file_extension ,FILE_PATH ,RAW_INPUT_PATH


api_id = 23406634
api_hash = "0701d1d306497f8dcf2578da224f89fb"  # Replace with your Telegram API hash

client = TelegramClient('session_name', api_id, api_hash)
print("Starting ...")

@client.on(events.NewMessage)
async def handle_message(event):
    sender = await event.get_sender()
    message = event.message.message

    if event.is_private:  # Only reply to private messages
        if event.message.file:
            file_name = getattr(event.message.file, 'name', 'Unknown File')
            file_extension = get_file_extension(file_name)
            if file_extension in ALLOWED_EXTENSIONS:
                file_path = os.path.join(".", file_name)
                downloaded_file = await client.download_media(event.message, file=file_path)
                reply = f"Hello {sender.first_name}, you sent a file: {file_name}"
                print(reply)
            else:
                print(f"Unsupported file format: {file_extension}")
        else:
            if message.lower() == 'done' or message == "تم":
                print("Loop ended")
                await client.disconnect()
            else:
                reply = f"Hello {sender.first_name}, you said: {message}"
                print(reply)

    if event.media:
        if hasattr(event.media, 'document'):
            # Media is a document
            filename = os.path.join(os.getcwd(), event.media.document.attributes[0].file_name)
            file_extension = get_file_extension(filename)
            if file_extension in ALLOWED_EXTENSIONS:
                await client.download_media(event.media.document, filename)
                print(f"Saved document: ** {filename} ** as RAWinput")
            else:
                print(f"Unsupported file format: {file_extension}")
        elif hasattr(event.media, 'photo'):
            # Media is a photo
            filename = os.path.join(os.getcwd(), f"photo_{event.id}.jpg")
            print(f"Unsupported file format: photo_{event.id}.jpg")
    renamed_file = os.path.join(".", "Utils", "src", "RAWinput.txt")
    shutil.move(downloaded_file, renamed_file)
    



async def main():
    phone_number = '+201111276198'  # Replace with your phone number in international format
    message = 'Hello from Python!'

    async with client:
        await client.send_message(phone_number, message)
        await client.run_until_disconnected()


if __name__ == '__main__':
    client.loop.run_until_complete(main())

