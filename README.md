# LED-liv-Characterization-Tool

## Overview
This project is an LED L-I-V (Light-Current-Voltage) characterization tool 
built around an Arduino Uno, a BPW34 photodiode, and an LM358 transimpedance 
amplifier. A potentiometer sweeps current through the LED across its full 
operating range while the Arduino simultaneously measures three parameters: 
LED current via a 100Ω resistor, LED forward voltage from direct analog 
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

### Current Measurement from R_1
A 100Ω resistor is placed in series with the LED. The Arduino reads 
the raw ADC value at the junction of the resistor and LED, converts it 
to voltage:

V = ADC × (5.0 / 1023.0)

And calculates current directly from Ohm's law:

I_LED = V / R

### Transimpedance Amplifier (TIA)
The BPW34 photodiode generates a tiny photocurrent proportional to incident 
light intensity. A transimpedance amplifier converts this current to a 
measurable voltage using a feedback resistor R_f:

V_out = I_photo × R_f

The Arduino reads V_out and back-calculates I_photo:

I_photo = V_out / R_f

### What Each Curve Tells You

**L-I Curve (Light vs Current)**
Shows how optical output power scales with drive current. Above the LED's 
threshold current, light output increases linearly with current. The slope 
of this curve is the **slope efficiency**; how many watts of optical power 
per amp of drive current. A steeper slope means a more efficient LED.

**V-I Curve (Voltage vs Current)**
Shows the diode's non-linear electrical behavior. Below the forward voltage 
threshold the LED barely conducts. Above it, voltage rises steeply then 
flattens while current continues to increase, the classic diode I-V 
characteristic described by the Shockley equation. The knee of this curve 
is the forward voltage V_f.

**L-V Curve (Light vs Voltage)**
Combines the other two. Shows how light output relates to forward voltage. 
Useful for system design where voltage rather than current is the controlled 
variable. The threshold behavior of the LED is clearly visible as a sharp 
turn-on point.
## Hardware 
- Arduino Uno R3
- Breadboard and Jumper Wires
- 10kΩ Potentiometer
- 100Ω Resistor
- 1MΩ Resistor
- Red LED
- LM358 Op-Amp
- BPW34 Photodiode
  
## Software

### Arduino Sketch


### Pyton Script


**Libraries used:**


## Results
 
## How to Run


## Limitations
