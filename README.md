# Feel the Beat
[Demo Video](https://drive.google.com/file/d/1KmlmandxGlKmikwozcBqHnKMK5zegj7C/view?usp=sharing)
## Motivation
According to Rutgers University, a sensory disability is a neurological disorder that affects the way that the brain processes sensory information.[^1]  Examples of sensory disabilities are autism, blindness, and deafness. Sensory disabilities have a huge effect on the population worldwide.  At least 2.2 billion people live with vision impairment or blindness and 466 million are living with disabling hearing loss.[^2] Additionally, studies show that 1 in 100 children is have autism spectrum disorder [^3] and somewhere between 5% to 16.5% of the general population experiences sensory processing challenges.[^4] For the billions living with sensory disabilities, daily life can require modifications. For example, a blind person may use braille or screen readers to read.  As another example, people with autism may experience sensory disabilities as hyper sensitivity or hypo sensitivity to sensory inputs.  According to Autism Tasmania, people with autism may benefit from environmental changes to help manage sensory processing difficulties.[^5]
The goal of my project is to make music, an auditory experience, into a multi-sensory experience that can be adapted for any person.  My project incorporates the sense of touch, sound, and sight to make music inclusive to anyone living with a sensory disability at concerts, clubs, or even at home.

## Technical Approach
To tackle this issue, I have designed a wearable arm sleeve that vibrates and illuminates LEDs to the beat of music.  The sleeve has buttons to turn on and off the senses of sight and sound to allow the user to customize their experience.  In my original project proposal, I stated that the visual portion of the project would be LED lights mounted on the celling of my apartment, but I decided that to better serve my audience it was best to make the device completely portable as well as individually configurable.


![fig_1](https://github.com/liz-Hayes/feel_the_beat/assets/87880510/acf2780e-338d-4fb6-a8ee-4aae82c6863c)

**Figure 1: Final Product**

In my project, vibrating motors are used to engage the sense of touch.  In the circuit diagram below (Fig 1), two vibrating motors are connected in series with a button that can cut off power to the buttons.  The output of the button is also wired to a transistor whose output is wired to the output of the vibration motors.  The transistor is used to protect from voltage spikes that the motors may create.  Additionally, a transistor is used to limit the amount of current being used by the motors by switching it on/off with larger current and controlling it with smaller current.  Finally, a resistor is used to prevent too much current from flowing out of the circuit.
To the left of the circuit diagram are the LED’s used in this project – NeoPixels.  These are individually addressable LED’s that can be linked together as shown in the circuit diagram.  These LEDs are wired with a button that can be used to turn off power to the parts.
A microphone is used to get the sound input to control the motors and LED’s.  The microphone output is connected to an analog pin on the Arduino where a sound wave is detected.
Because my project is mobile, a battery is required which needs to provide enough amps at the correct voltage (3.7 volts).
To know when to turn on the LEDs and vibration motors, I created a very simple beat detection algorithm.  The algorithm aims to detect beats by recording an array of the latest volume levels and taking the average.  If the current volume reading is greater than this average by a configurable scaling factor, then a beat is detected and the lights and the vibration motors are turned on. 

![fig_2](https://github.com/liz-Hayes/feel_the_beat/assets/87880510/603e5b33-dcef-4a22-9536-9ca9470de29c)

**Figure 2: Circuit Diagram**

## Implementation Details
For the brain of the device, I chose an Adafruit Gemma M0.[^6]  I chose the Gemma because it is tiny and sewable which is ideal for my wearable sleeve.  Most of the parts that I selected where chosen because they are small and sewable with conductive thread.  Using conductive thread allowed me to make my circuit fairly flexible so that it can be comfortably worn.  
Links to all items I purchased and references for connecting them to other components can be found below:
- Adafruit Gemma M0: https://www.adafruit.com/product/3501
- MAX9814 Electret Microphone Amplifier 
  - Part: https://www.adafruit.com/product/1713
  - Wiring reference: https://learn.adafruit.com/sound-reactive-neopixel-peace-pendant/overview, https://www.electroschematics.com/arduino-max9814-getting-started/
- Vibration:
  - Vibration Mini Motor Disc: https://www.adafruit.com/product/1201
  - NPN Bipolar Transistor: https://www.adafruit.com/product/756
  - 1N4001 Diode: https: //www.amazon.com/NTE-Electronics-1N4001-Standard-Rectifier/dp/B008UG13UW
  - Resistor: https://www.microcenter.com/product/389992/nte-electronics-1-2-watt-270-ohm-resistor-6-pack
  - Wiring reference: https://techzeero.com/arduino-tutorials/vibration-motor-with-arduino/#Vibration-Motor-and-LDR-Sensor, https://learn.adafruit.com/buzzing-mindfulness-bracelet/circuit-diagram, http://www.learningaboutelectronics.com/Articles/Vibration-motor-circuit.php
- Flora RGB Smart NeoPixels: 
  - Part: https://www.adafruit.com/product/1260
  - Wiring Reference: https://learn.adafruit.com/led-ampli-tie/circuit-diagram
- On/Off switches: https://www.microcenter.com/product/497124/leo-sales-ltd-mini-on-off-black-switches-%e2%80%93-4-piece
- Conductive thread: https://www.adafruit.com/product/640
- 2200mAh Lithium Ion Battery: https://www.microcenter.com/product/636273/adafruit-industries-lithium-ion-cylindrical-battery-37v-2200mah
The Gemma comes set up with a language called CircuitPython, that is an open-source version of python for use with microcontrollers.[^7] For my project, I used this language and utilized the recommended Mu text editor that has a plotter as well as a REPL available for debugging.

![fig_3](https://github.com/liz-Hayes/feel_the_beat/assets/87880510/b794a381-cfe0-4726-b93c-2af363c8ecb3)

**Figure 3: Mu Code Editor**

My project is run by code.py which uses several circuit python modules (time, rainbowio, board, neopixel, analogio, digitalio, and random).  The board, analogio, and digitalio libraries are used to help with assigning pins and configuring them as digital and analog inputs and outputs. The rainbowio and neopixel libraries are specifically used to control the Neopixel LEDs in my device. These libraries allow for a lot of creativity and customization with colors.   The time library is used to add a sleep to my code to prevent an overflow of data and to ensure that leds and the vibration motors stay on for long enough to be perceived.  The random library is used to provide a random value to the colorwheel function so that LEDs’ colors are constantly changing.
When creating my beat detection algorithm, which is explained in the previous section,[^8] [^9] I needed to massage my analog sound data to achieve better beat detection results.  Based on observation, I chose a value that the sound wave was biased to and decided to subtract that from each value, to center the wave at zero.  Additionally, I took the absolute value of each reading so that I could detect spikes in volume.  Finally, I decided to set any value less than a noise threshold (which I determined to be about 3000) to zero to remove the extra noise from the microphone.

## Results
Overall, I think the project turned out as an excellent prototype, but would not be suitable for a final product.  Once I began work and further reading on beat detection, I found that my algorithm could be much more accurate if I could use an FFT library to transform my analog amplitude vs time data into amplitude vs frequency data.  Unfortunately, I could not find an available FFT library for the Gemma, so for a future project, I would consider swapping microcontrollers for something with more functionality.  Overall, the method I use for beat detection, is far from precise, but does do a fairly good job of representing the music with very little complexity.  The code works well with music that has a strong, steady beat, such as pop, and does not work as well with classical music, for example.
Another challenge I had in designing and building my device was making it wearable.  After some research and practice,[^10] the conductive thread worked great for most of my components, especially attaching the Neopixels and Gemma.  It was more difficult to design a simple solution for the vibrating motor and its required components because these parts were not designed to be sewable.  In the future, I would like to cover the vibrating motor and all wired components with a waterproof shield of some kind to protect any of the tiny wires from being pulled apart.  Overall, I was pleasantly surprised with the sturdiness of this prototype and I was able to successfully put it on and try it out.
The results of this project are promising for a future finished product.  In my experience using the project, I felt soothed by the vibration motor and really felt like I could feel and engage more with the music by seeing and feeling the song, and not just hearing it.  I feel confident that the device could be a really helpful and fun tool for anyone with or without a sensory disorder to enjoy music.
 
[^1]: https://kines.rutgers.edu/dshw/disabilities/sensory/1061-sensory-disabilities
[^2]: https://www.who.int/teams/noncommunicable-diseases/sensory-functions-disability-and-rehabilitation
[^3]: https://www.who.int/news-room/fact-sheets/detail/autism-spectrum-disorders
[^4]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5733937/#:~:text=Current%20estimates%20indicate%20that%205,(ADHD)%20%5B4%5D.
[^5]: https://www.autismtas.org.au/about-autism/key-areas-of-difference/sensory-differences/#:~:text=A%20person%20with%20autism%20may,to%20high%20anxiety%20and%20meltdowns
[^6]: https://learn.adafruit.com/adafruit-gemma-m0/overview
[^7]: https://docs.circuitpython.org/en/latest/README.html
[^8]: https://learn.adafruit.com/sound-reactive-neopixel-peace-pendant/circuitpython-code
[^9]: http://marcusrossel.com/2019-11-23/beat-detector
[^10]: https://learn.adafruit.com/conductive-thread/overview




