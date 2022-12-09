import speech_recognition as sr
from pytube import Playlist, YouTube
import vlc
import datetime
import random
import os

playlistConfigurada = Playlist("https://www.youtube.com/watch?v=9NbeL4FtcN0&list=PLikx4Mnm5j4d91yr_SbOxx-cIYDueyyIC")
mediaPlayer = vlc.MediaPlayer()
tocouHoje = False

def ouvir_microfone():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")
        audio = microfone.listen(source)
    try:
        frase = microfone.recognize_google(audio,language='pt-BR')
        frase = frase.lower()
        if("parar" in frase or "parar" in frase):
            mediaPlayer.stop()
        #funcao(frase)
    except sr.UnkownValueError:
        print("Não entendi")

while True:
    now = datetime.datetime.now()
    if(now.time() >= datetime.time(7,35) and now.time() <= datetime.time(7,40) and not mediaPlayer.is_playing() and not tocouHoje):
        urlMusica = playlistConfigurada[random.randint(0,playlistConfigurada.length)]
        yt = YouTube(urlMusica)
        video = yt.streams.filter(only_audio=True).first()

        # download the file
        out_file = video.download(filename="musica.mp3")

        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        mediaPlayer = vlc.MediaPlayer(new_file)
        mediaPlayer.play()

        tocouHoje = True
    elif(tocouHoje and now.time() > datetime.time(22,43)):
        tocouHoje = False
    try:
        ouvir_microfone()
    except:
        print("Fala não encontrada")
    