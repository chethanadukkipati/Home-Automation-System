import pydub
sound=pydub.AudioSegment.from_mp3("/home/pi/chethana.mp3")
sound.export("/home/pi/chethana.wav",format="wav")
sound=pydub.AudioSegment.from_mp3("/home/pi/dinesh.mp3")
sound.export("/home/pi/dinesh.wav",format="wav")
sound=pydub.AudioSegment.from_mp3("/home/pi/sampu.mp3")
sound.export("/home/pi/sampu.wav",format="wav")
