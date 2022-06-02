# DS18B20 1M temp probe
# By Samples & Tests
# 1 June 2022
# Ver 0.3
# Based on Pibits code
# http://www.pibits.net/code/raspberry-pi-pico-and-ds18b20-thermometer-using-micropython.php


# The probe has 3 connections (Vcc, Data, Gnd)
# connect ~5k Ohm resister between Data and Vcc
# connect vcc to pin 36 (3.3v)
#Connect data to a GPIO  pin (in this case pin 21/  GP16)
#connect Gnd to one of the ground pins (in this case pin 23)

# import libraries

from machine import Pin
import onewire, ds18x20, time, machine

# Define pins & variables
statpin = Pin(0, Pin.IN)
dspin = Pin(16)
dssen = ds18x20.DS18X20(onewire.OneWire(dspin))
romscan = dssen.scan()

# define function to get the temprature in Degress Celsius
def tempC():
	dssen.convert_temp()
	time.sleep(1)

	for data in romscan:
		print("The Temp is", dssen.read_temp(data), " Degrees Celsius")
	time.sleep(2)


# define function to get the temprature in Degress Fahrenheit
def tempF():
        dssen.convert_temp()
        time.sleep(1)

        for data in romscan:
                print("The Temp is", (1.8 * dssen.read_temp(data)) + 32, " Degrees Fahrenheit")
        time.sleep(2)

def checktempF():
	while(statpin.value()):
		tempF()
		time.sleep(60)

def checktempC():
	while(statpin.value()):
		tempC()
