import struct
import threading
import pyaudio
import pvporcupine
import speech_recognition   
from lcd import write_lcd, clear_lcd
from dc_motors import forward, backward, turn_left, turn_right, stop
import calculate
import message
import time
import play_sound
import random
import os

write_lcd(first_line='      K4.5', second_line='Nice to meet you')

rec = speech_recognition.Recognizer()
speech = speech_recognition.Microphone(device_index=3)

def voice_recognition_confirm_sound_effect():
    play_sound.play_sound_effect(sound=play_sound.confirm)

def voice_recognition_processing_sound_effect():
    play_sound.play_sound_effect(sound=play_sound.processing)

try:

    porcupine = pvporcupine.create(access_key='OBarq6+nQZjftCadhlX1ZR1WulknlRl2PzkUEmxYU7RBZLYTP2g6QQ==',
                                    
                                    keyword_paths=['four-point-five_en_raspberry-pi_v2_1_0.ppn'])

    pa = pyaudio.PyAudio()

    audio_stream = pa.open(
                    rate=porcupine.sample_rate,
                    channels=1,
                    format=pyaudio.paInt16,
                    input=True,
                    frames_per_buffer=porcupine.frame_length)

    while True:
        
        pcm = audio_stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        keyword_index = porcupine.process(pcm)

        if keyword_index == 0:
            stop()
            confirm_sound_thread = threading.Thread(target=voice_recognition_confirm_sound_effect)
            confirm_sound_thread.start()
            write_lcd(first_line="     ALERT", second_line="Recognized name")
            forward()
            time.sleep(0.3)
            stop()
            with speech as source:
                rec.adjust_for_ambient_noise(source=source, duration=0.5)
                write_lcd(first_line=" K4.5 Rover Bot", second_line=" Listening ...")
                print(" Listening ...")
                audio = rec.listen(source, phrase_time_limit=5)
            try:
                write_lcd(first_line=" K4.5 Rover Bot", second_line="Processing ...")
                text = rec.recognize_google(audio)
                print("\nCommand: {}".format(text))
            except speech_recognition.UnknownValueError:
                write_lcd(first_line="Trouble hearing", second_line=" Please repeat!")
                print("\nTrouble hearing, please repeat!")
            except speech_recognition.RequestError as error:
                write_lcd(first_line="Network problem", second_line="No wifi signal!")
                print("\nNetwork problems, please connect to a network!")
            else:
                porcessing_sound_thread = threading.Thread(target=voice_recognition_processing_sound_effect)
                porcessing_sound_thread.start()

                if any(word in text.lower() for word in ["photo", "picture"]):
                    write_lcd(first_line="Recognized:", second_line="Taking a photo")
                    import photo_capture
                    message.telegram(chat_id=message.telegram_chat_id, status = "photo mode")
                    stop()
                    continue
                if any(word in text.split() for word in ["add", "plus", "+"]):
                    calculate.addition(text)
                if any(word in text.split() for word in ["subtract", "minus", "-"]):
                    calculate.subtraction(text)
                if any(word in text.split() for word in ["multiply", "x"]):
                    calculate.multiplication(text)
                if any(word in text.split() for word in ["divide", "/"]):
                    calculate.division(text)
                    continue
                if any(word in text.lower() for word in ["safe", "save"]):
                    if any(word in text.lower() for word in ["keeping", "keep"]):
                        write_lcd(first_line="Recognized:", second_line=" SAFE-KEEPING")
                        os.system('python3 ~/RPI-Project-Rover/safe_keeping.py')
                    else:
                        write_lcd(first_line="Recognized:", second_line="   SAFE-GUARD")
                        os.system('python3 ~/RPI-Project-Rover/safe_guard.py')
                    stop()
                    continue
                if any(word in text.lower() for word in ["fall", "detection"]):
                    write_lcd(first_line="Recognized:", second_line="Fall Detection")
                    os.system('python3 ~/RPI-Project-Rover/fall_detection.py')
                    stop()
                    continue
                if any(word in text.lower() for word in ["follow"]):
                    write_lcd(first_line="Recognized:", second_line="    Follow Me")
                    os.system('python3 ~/RPI-Project-Rover/follow_me.py')
                    stop()
                    continue
                if any(word in text.lower() for word in ["manual", "spy"]):
                    write_lcd(first_line="Recognized:", second_line="    Spy Mode")
                    os.system('python3 ~/RPI-Project-Rover/spy_mode.py')
                    stop()
                    continue
                if any(word in text.lower() for word in ["control", "sync"]):
                    write_lcd(first_line="Recognized:", second_line="  Sync Control")
                    os.system('python3 ~/RPI-Project-Rover/arduino_communication.py')
                    stop()
                    continue
                if any(word in text.lower() for word in ["message"]):
                    write_lcd(first_line="Recognized:", second_line=" Message Mode")
                    os.system('python3 ~/RPI-Project-Rover/retrieve_message.py')
                    stop()
                    continue
                if any(word in text.lower() for word in ["back", "down"]):
                    write_lcd(first_line="Recognized:", second_line="Moving backward")
                    backward()
                    time.sleep(1)
                    stop()
                    continue
                if any(word in text.lower() for word in ["forward", "up"]):
                    write_lcd(first_line="Recognized:", second_line="Moving forward")
                    forward()
                    time.sleep(1)
                    stop()
                    continue
                
                if any(word in text.lower() for word in ["left"]):
                    write_lcd(first_line="Recognized:", second_line="  Turning left")
                    turn_left()
                    time.sleep(1)
                    stop()
                    continue
                if any(word in text.lower() for word in ["right"]):
                    write_lcd(first_line="Recognized:", second_line=" Turning right")
                    turn_right()
                    time.sleep(1)
                    stop()
                    continue
                if any(word in text.lower() for word in ["around"]):
                    write_lcd(first_line="Recognized:", second_line="Turning around")
                    direction = random.randint(0,1)
                    if direction == 0:
                        turn_right()
                        time.sleep(2)
                    elif direction == 1:
                        turn_left()
                        time.sleep(2)
                    stop()
                    continue
                
finally:
    if porcupine is not None:
        porcupine.delete()     