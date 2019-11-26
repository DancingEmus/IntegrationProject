# CP320 Integration Project


## By:
Aayush Sheth : 160642890
Michael Pintur : 150785070

# Circuit Overview 
In our circuit, we make the use of an infrared sensor and Elecret microphone to control the state of a stepper motor and an LED respectively. 
Our circuits makes use of the Raspberry Pi's SPI interface, to recieve data from the microphone and infrared sensor. If the infrared sensor senses a heat signature our motor will spin counter clock-wise, if no strong heat signature is detected then motor will turn clock-wise. If the microphone reads large decibels in its vacininty, it will trigger a bicolor LED to turn red, and will not allow the motor to continue turning. If no large reading is detected then the LED is lit green and the motor is not blocked from rotating. 


[Main program](https://github.com/pint5070/IntegrationProject/blob/master/integration_project.py)

# Block Diagram 

![Block digram](https://github.com/pint5070/IntegrationProject/blob/master/Untitled%20Diagram.drawio-2.png)

[Block diagram documentation](https://github.com/pint5070/IntegrationProject/blob/master/Block%20_Diagram_Documentation.md)
