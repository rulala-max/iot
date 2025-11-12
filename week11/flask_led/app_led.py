from flask import Flask, render_template, request, redirect, url_for
# import RPi.GPIO as GPIO
from gpiozero import LED

app = Flask(__name__)

# GPIO 설정
led1 = LED(20)
led2 = LED(21)

# LED 상태 저장
led_states = {'led1': 0, 'led2': 0}

@app.route('/')
def index():
    return render_template('index.html', states=led_states)

@app.route('/led/<int:led_num>/<int:state>')
def control_led(led_num, state):
    """개별 LED 제어"""
    if led_num == 1:
        if state == 1:
            led1.on()
        else:
            led1.off()
        led_states['led1'] = state
    elif led_num == 2:
        if state == 1:
            led2.on()
        else:
            led2.off()
        led_states['led2'] = state
    
    return redirect(url_for('index'))

@app.route('/all/<int:state>')
def all_leds(state):
    """모든 LED 동시 제어"""
    if state == 1:
        led1.on()
        led2.on()
    else:
        led1.off()
        led2.off()
    led_states['led1'] = state
    led_states['led2'] = state
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    finally:
        pass