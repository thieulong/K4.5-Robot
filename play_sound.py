from concurrent.futures import process
from pydub import AudioSegment
from pydub.playback import play

dir = "sounds/"

bark = "bark.wav"
confirm = dir+"confirm.wav"
fall_detect = dir+"fall-detect.wav"
processing = dir+"processing.wav"
safe_guard = dir+"safe-guard.wav"
safe_keeping = dir+"safe-keeping.wav"

def play_sound_effect(sound):
    song = AudioSegment.from_wav(sound)
    play(song)

play_sound_effect(sound=confirm)

