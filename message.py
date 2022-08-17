import telepot

telegram_bot = telepot.Bot(token="5490662868:AAEPnTkoa9qbEIl7eH1v80eTlhbPx7m9Ywg")

telegram_chat_id = '1921540131'

def telegram(chat_id, status): 
    
    if status == "safe-guard mode":
        
        telegram_bot.sendMessage(chat_id=chat_id,
            text="[ALERT] Detected someone in the area!")

        telegram_bot.sendPhoto(chat_id=chat_id,
                    photo=open("images/safe-guard.png", "rb"))
        
    elif status == "safe-keeping mode":
        telegram_bot.sendMessage(chat_id=chat_id,
            text="[ALERT] Detected the person has left the area!")
        
        telegram_bot.sendPhoto(chat_id=chat_id,
                    photo=open("images/safe-keeping.png", "rb"))
        
    elif status == "photo mode":
        telegram_bot.sendMessage(chat_id=chat_id,
            text="[INFO] Photo taken!")
        
        telegram_bot.sendPhoto(chat_id=chat_id,
                    photo=open("images/photo.png", "rb"))
        
    elif status == "fall detection mode":
        telegram_bot.sendMessage(chat_id=chat_id,
            text="[ALERT] Detect a person fell!")
        
        telegram_bot.sendPhoto(chat_id=chat_id,
                    photo=open("images/fall-detect.png", "rb"))

    
# Test message function
# telegram(chat_id=telegram_chat_id)