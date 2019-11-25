import time
import RPi.GPIO as GPIO
import spidev

DEGREES = 360
STEPS = 512
INFRARED_CHANNEL = 1
MIC_CHANNEL = 2
CHANNEL_SELECT = 1
ANGLE = 25
GREEN_LED = 6
RED_LED = 5
SHIFTED_BITS = 4
ADC_VOLTAGE = 3.3
adc_channel=INFRARED_CHANNEL
adc_channel2=MIC_CHANNEL

spi=spidev.SpiDev()
spi.open(0,CHANNEL_SELECT)
spi.max_speed_hz = 5000

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)
GPIO.setmode(GPIO.BCM)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.output(GREEN_LED, GPIO.HIGH)

def motor(number,direction,speed):
       sleep_time = 0
       stepper_pins=[13,16,26,21]
       GPIO.setup(stepper_pins,GPIO.OUT)
       if speed == 1:
               sleep_time = .01
       else:
               sleep_time = .1
       stepper_sequence=[]
       stepper_sequence.append([GPIO.HIGH, GPIO.LOW,
GPIO.LOW,GPIO.LOW])
       stepper_sequence.append([GPIO.HIGH, GPIO.HIGH,
GPIO.LOW,GPIO.LOW])
       stepper_sequence.append([GPIO.LOW, GPIO.HIGH,
GPIO.LOW,GPIO.LOW])
       stepper_sequence.append([GPIO.LOW, GPIO.HIGH,
GPIO.HIGH,GPIO.LOW])
       stepper_sequence.append([GPIO.LOW, GPIO.LOW,
GPIO.HIGH,GPIO.LOW])
       stepper_sequence.append([GPIO.LOW, GPIO.LOW,
GPIO.HIGH,GPIO.HIGH])
       stepper_sequence.append([GPIO.LOW, GPIO.LOW,
GPIO.LOW,GPIO.HIGH])
       stepper_sequence.append([GPIO.HIGH, GPIO.LOW,
GPIO.LOW,GPIO.HIGH])

AngleIn = number
AngleIn = float(AngleIn)
percentage= float(AngleIn/DEGREES)
steps = round(float(STEPS*percentage))
if direction == 1:
       count = 0
       while True:
               count += 1
               for row in stepper_sequence:
                       GPIO.output(stepper_pins,row)
                       time.sleep(sleep_time)
               if count == steps:
else:
       count = 0
break
return
while True:
       count += 1
for row in reversed (stepper_sequence):
       GPIO.output(stepper_pins,row)
       time.sleep(sleep_time)
if count == steps:
break

def infrared(speed):
       adc=spi.xfer2([1,(8+adc_channel)<<SHIFTED_BITS,0])
       data=((adc[1]&3)<<8) +adc[2]
       data_scale=(data*ADC_VOLTAGE)/float(1023)
       data_scale=round(data_scale,2)
       print (data_scale)
       time.sleep(2)
       if data_scale > 1:
               motor(ANGLE, 1,speed)
       else:
               motor(ANGLE, 0.speed)
def led(data,speed):
       if data < 2 or data > 3:
               GPIO.output(RED_LED, GPIO.HIGH)
               GPIO.output(GREEN_LED, GPIO.LOW)
               return
       else:
               GPIO.output(RED_LED, GPIO.LOW)
               GPIO.output(GREEN_LED, GPIO.HIGH)
               infrared(speed)
               return
              
def main():
       valid = False
       while valid != True:
               speed = float(input("Please Enter Motor Speed (1 for

fast, 2 for slow): "))
               if speed != 1 or 2:
main()
GPIO.cleanup()
spi.close()
try:
       print("Invalid Input")
else:
       valid = True
while True:
       adc=spi.xfer2([1,(8+adc_channel2)<<SHIFTED_BITS,0])
       data=((adc[1]&3)<<8) +adc[2]
       data_scale=(data*ADC_VOLTAGE)/float(1023)
       data_scale=round(data_scale,2)
       print (data_scale)
       led(data_scale,speed)
       time.sleep(2)
except KeyboardInterrupt:
       pass
return
