import telepot

telegram_bot = telepot.Bot(token="5490662868:AAEPnTkoa9qbEIl7eH1v80eTlhbPx7m9Ywg")

telegram_chat_id = '1921540131'

def telegram(chat_id): 
    
    telegram_bot.sendMessage(chat_id=chat_id,
        text="[ALERT] Detected someone in the area!")

    telegram_bot.sendPhoto(chat_id=chat_id,
                photo=open("person-detected/image.png", "rb"))
    
# Test message function
# telegram(chat_id=telegram_chat_id)