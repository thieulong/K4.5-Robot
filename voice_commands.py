import struct
import threading
import pyaudio
import pvporcupine
import speech_recognition   
from lcd import write_lcd, clear_lcd
from dc_motors import forward, backward, turn_left, turn_right, stop
import message
import time
import play_sound

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
        
        write_lcd(first_line='SELECT MODE:', second_line=' VOICE COMMANDS')
        
        pcm = audio_stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        keyword_index = porcupine.process(pcm)

        if keyword_index == 0:
            confirm_sound_thread = threading.Thread(target=voice_recognition_confirm_sound_effect)
            confirm_sound_thread.start()
            write_lcd(first_line="     ALERT", second_line="Recognized name")
            forward()
            time.sleep(0.2)
            turn_right()
            time.sleep(0.2)
            turn_left()
            time.sleep(0.2)
            stop()
            with speech as source:
                audio = rec.adjust_for_ambient_noise(source)
                write_lcd(first_line=" K4.5 Rover Bot", second_line=" Listening ...")
                print("Listening ...")
                audio = rec.listen(source)
            try:
                write_lcd(first_line=" K4.5 Rover Bot", second_line="Processing ...")
                text = rec.recognize_google(audio, language = 'en-US')
                print("\nCommand: {}".format(text))
            except speech_recognition.UnknownValueError:
                write_lcd(first_line="Trouble hearing", second_line="  Please repeat")
                print("\nTrouble hearing, please repeat!")
            except speech_recognition.RequestError as error:
                write_lcd(first_line="Network problem", second_line="Try again later")
                print("\nNetwork problems, please try again later!")
            else:
                porcessing_sound_thread = threading.Thread(target=voice_recognition_processing_sound_effect)
                porcessing_sound_thread.start()
                if any(word.lower() in text for word in ["bark",]):
                    write_lcd(first_line="Recognized:", second_line="   Barking")
                    play_sound.play_sound_effect(sound=play_sound.bark)
                    stop()
                    continue
                if any(word.lower() in text for word in ["photo", "picture",]):
                    write_lcd(first_line="Recognized:", second_line="Taking a photo")
                    import photo_capture
                    message.telegram(chat_id=message.telegram_chat_id, status = "photo mode")
                    stop()
                    continue
                if any(word.lower() in text for word in ["back", "down",]):
                    write_lcd(first_line="Recognized:", second_line="Moving backward")
                    backward()
                    time.sleep(1)
                    stop()
                    continue
                if any(word.lower() in text for word in ["forward", "up"]):
                    write_lcd(first_line="Recognized:", second_line="Moving forward")
                    forward()
                    time.sleep(1)
                    stop()
                    continue
                if any(word.lower() in text for word in ["left"]):
                    write_lcd(first_line="Recognized:", second_line="  Turning left")
                    turn_left()
                    time.sleep(1)
                    stop()
                    continue
                if any(word.lower() in text for word in ["right"]):
                    write_lcd(first_line="Recognized:", second_line=" Turning right")
                    turn_right()
                    time.sleep(1)
                    stop()
                    continue
                
finally:
    if porcupine is not None:
        porcupine.delete()     