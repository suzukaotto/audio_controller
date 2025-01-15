import time
import audio_module
import utils

master = audio_module.AudioManager(utils.get_env_key('GOOGLE_API_KEY'))

time.sleep(3)

master.add_audio_path('audio/207系.mp3')
time.sleep(3)

master.tts_play('과다한 스마트폰 사용으로 인한 미승차, 정류소 내 안전사고에 유의하시기 바랍니다.')
time.sleep(20)