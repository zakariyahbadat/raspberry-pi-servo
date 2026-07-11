import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12 , GPIO.OUT)
pwm = GPIO.PWM(12 , 50)
pwm.start(0)

try:
    while True:
        for duty_scaled in range(25, 101, 1):
            duty = duty_scaled / 10 
            pwm.ChangeDutyCycle(duty)
            time.sleep(0.05)
        for duty_scaled in range(100, 24, -1):
            duty = duty_scaled / 10 
            pwm.ChangeDutyCycle(duty)
            time.sleep(0.1)



except KeyboardInterrupt:
    print("Program stopped by user")

finally:
    pwm.stop()
    GPIO.cleanup()