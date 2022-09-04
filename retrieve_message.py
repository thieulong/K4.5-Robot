import dc_motors
import telepot
bot = telepot.Bot('5490662868:AAEPnTkoa9qbEIl7eH1v80eTlhbPx7m9Ywg')
dc_motors.pl.ChangeDutyCycle(80)
dc_motors.pr.ChangeDutyCycle(80)
while True:
    response = bot.getUpdates()
    total_response = len(response)
    response = response[len(response)-1]
    message = response.get('message')
    text = message.get('text')
    if "forward" in text.lower():
        dc_motors.forward()
    if "backward" in text.lower():
        dc_motors.backward()
    if "stop" in text.lower():
        dc_motors.stop()
    if "right" in text.lower():
        dc_motors.turn_right()
    if "left" in text.lower():
        dc_motors.turn_left()
    if "break" in text.lower():
        break
