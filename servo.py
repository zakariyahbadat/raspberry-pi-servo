import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12 , GPIO.OUT)
pwm = GPIO.PWM(12 , 50)
pwm.start(0)

try:
    while True:
        pwm.ChangeDutyCycle(2.5)
        time.sleep(0.5)
        pwm.ChangeDutyCycle(0)     
        time.sleep(2)             
        
        
        pwm.ChangeDutyCycle(5.5)
        time.sleep(0.5)            
        pwm.ChangeDutyCycle(0)    
        time.sleep(2)
        
        
        pwm.ChangeDutyCycle(10)
        time.sleep(0.5)            
        pwm.ChangeDutyCycle(0)     
        time.sleep(2)



except KeyboardInterrupt:
    print("Program stopped by user")

finally:
    pwm.stop()
    GPIO.cleanup()