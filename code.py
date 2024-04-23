
import time
from rainbowio import colorwheel
import board
import neopixel
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction
from random import randint

led_pin = board.D1
n_pixels = 4
pixels = neopixel.NeoPixel(led_pin, n_pixels, brightness=.1, auto_write=True)

vibrating_disc = DigitalInOut(board.D0)
vibrating_disc.direction = Direction.OUTPUT


mic_pin = AnalogIn(board.A1)
samples = 60
neighbors= [0] * samples
neighbor_ct =0

mic_offset = 26300
noise =3000
beat_factor = 2


while True:
    val=int(mic_pin.value)    #get value from mic
    val = abs(val- mic_offset)  #Centering value closer to zero

    #ignore values below 3000 as noise
    if val<noise:
        val=0

    #record count in neighbors
    neighbors[neighbor_ct] = val
    neighbor_ct += 1

    #if ct has reached desired number of samples, start writing over the list from the beginning
    if neighbor_ct >= samples:
        neighbor_ct = 0


    #get the average volume across neighbors
    sum = 0
    for i in range(len(neighbors)):
        sum =  neighbors[i] + sum
    avg_level = sum/len(neighbors)


    #if the current value is greater than the average * the beat_factor(2)
    if val>avg_level*beat_factor:
        vibrating_disc.value = True #vibrate
        for i in range(0, len(pixels)):
            pixels[i]= colorwheel(randint(0,235) + i*5) #color the leds
    else:
        vibrating_disc.value = False #turn off the vibrating motor
        pixels.fill(0) #turn off leds
    print((val,))
    time.sleep(0.02)
