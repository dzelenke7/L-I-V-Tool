# LED-liv-Characterization-Tool

## Overview
This project is an LED L-I-V (Light-Current-Voltage) characterization tool 
built around an Arduino Uno, a BPW34 photodiode, and an LM358 transimpedance 
amplifier. A potentiometer sweeps current through the LED across its full 
operating range while the Arduino simultaneously measures three parameters: 
LED current via a 100Ω sense resistor, LED forward voltage from direct analog 
measurement, and optical output power from a photodiodes current amplified through 
the transimpedance amplifier. All three values are logged over serial to a 
Python script that generates L-I, V-I, and L-V characteristic curves.

L-I-V characterization is one of the most fundamental measurements in 
photonics device engineering. These measurements are performed on every  
optical device from LEDs and laser diodes to photodetectors and photonic integrated  
circuits. Understanding how light output, drive current, and forward voltage relate to 
each other is the foundation of optical device design, and the same 
measurement methodology used here scales directly to the silicon photonic 
devices being developed at facilities like AIM Photonics and Lumentum.
## Theory

## Hardware 

## Software

### Arduino Sketch


### Pyton Script


**Libraries used:**


## Results
 
## How to Run


## Limitations
