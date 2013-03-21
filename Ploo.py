import pygame
from pygame.locals import *
from sys import exit
import swmixer

size = width, height = 320, 240

speed = [2, 2]

black = 0, 0, 0
screen = pygame.display.set_mode(size)


pygame.init()

swmixer.init(samplerate=44100, chunksize=1024, stereo=True)
swmixer.start()
snd1 = swmixer.StreamingSound("../assets/audio/beat2.mp3")
snd2 = swmixer.StreamingSound("../assets/audio/l1.mp3")
snd3 = swmixer.StreamingSound("../assets/audio/l2.mp3")
snd4 = swmixer.StreamingSound("../assets/audio/l3.mp3")
snd5 = swmixer.StreamingSound("../assets/audio/l4.mp3")
snd6 = swmixer.StreamingSound("../assets/audio/l5.mp3")

chan1 = snd1.play()
chan2 = snd2.play(volume=0.1)
chan3 = snd3.play(volume=0.0)
chan4 = snd4.play(volume=0.0)
chan5 = snd5.play(volume=0.0)
chan6 = snd6.play(volume=0.0)

while True:

    event = pygame.event.wait()
    print event.key
    print event.type


    if event.type == 2 and event.key == 49:
        chan2.set_volume(0.9)
    if event.type == 3 and event.key == 49:
        chan2.set_volume(0.0)
    if event.type == 2 and event.key == 50:
        chan3.set_volume(0.9)
    if event.type == 3 and event.key == 50:
        chan3.set_volume(0.0)
    if event.type == 2 and event.key == 51:
        chan4.set_volume(0.9)
    if event.type == 3 and event.key == 51:
        chan4.set_volume(0.0)
    if event.type == 2 and event.key == 52:
        chan5.set_volume(0.9)
    if event.type == 3 and event.key == 52:
        chan5.set_volume(0.0)
    if event.type == 2 and event.key == 53:
        chan6.set_volume(0.9)
    if event.type == 3 and event.key == 53:
        chan6.set_volume(0.0)


    if event.key == 27:
        exit()
        
