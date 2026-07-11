import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12 , GPIO.OUT)
pwm = GPIO.PWM(12 , 50)
pwm.start(0)

try:
    while True:
        # Move to 0 degrees
        pwm.ChangeDutyCycle(2.5)
        time.sleep(0.5)            # Give it half a second to physically arrive
        pwm.ChangeDutyCycle(0)     # TURN OFF THE PULSE (Stops jittering!)
        time.sleep(2)              # Sit silently for 2 seconds
        
        # Move to 90 degrees
        pwm.ChangeDutyCycle(7.5)
        time.sleep(0.5)            # Give it time to move
        pwm.ChangeDutyCycle(0)     # TURN OFF THE PULSE
        time.sleep(2)
        
        # Move to 180 degrees (using 11.5 to prevent straining)
        pwm.ChangeDutyCycle(11.5)
        time.sleep(0.5)            # Give it time to move
        pwm.ChangeDutyCycle(0)     # TURN OFF THE PULSE
        time.sleep(2)



except KeyboardInterrupt:
    print("Program stopped by user")

finally:
    pwm.stop()
    GPIO.cleanup()