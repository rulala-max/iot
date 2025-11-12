from gpiozero import LED
from time import sleep

red_led = LED(20)  # GPIO PIN
green_led = LED(21)  # GPIO PIN
 
try:
    while True:
        red_led.on()
        green_led.off()
        sleep(2)
        red_led.off()
        green_led.on()
        sleep(2)  # delay
except KeyboardInterrupt:
    print("Exit program!")
finally:
    red_led.close()
    green_led.close()


#mkdir week11 >cd week11>pwd>mkdir (제목) &&(제목)
#touch app_led.py
#sudo apt install python3-Flask