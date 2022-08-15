from pygame import mixer

mixer.init()

dir = "sounds/"

bark = "bark.wav"
confirm = dir+"confirm.wav"
fall_detect = dir+"fall-detect.wav"
processing = dir+"processing.wav"
safe_guard = dir+"safe-guard.wav"
safe_keeping = dir+"safe-keeping.wav"

def play_sound_effect(sound):
    mixer.music.load(sound)
    mixer.music.play()
    mixer.music.stop()