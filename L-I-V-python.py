import serial
import matplotlib.pyplot as plt
import time

ser = serial.Serial('COM5', 9600)
time.sleep(2)

current_mA = []
voltage_LED = []
current_photo = []

print("Reading data... press Ctrl+C to stop and plot")

while True:
    try:
        line1 = ser.readline().decode('utf-8').strip()
        line2 = ser.readline().decode('utf-8').strip()
        line3 = ser.readline().decode('utf-8').strip()
    
        val1 = float(line1)
        val2 = float(line2)
        val3 = float(line3)
    
        current_mA.append(val1)
        voltage_LED.append(val2)
        current_photo.append(val3)
    
        print(f"I_res: {val1:.1f} mA | V_LED: {val2:.2f} V | I_photo: {val3:.3f} µA")

    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"Error: {e}")

print(f"Total readings collected: {len(current_mA)}")

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4))

ax1.plot(current_mA, current_photo, 'b.')
ax1.set_xlabel("LED Current (mA)")
ax1.set_ylabel("Photodiode Current (mA)")
ax1.set_title("L-I Curve")

ax2.plot(current_mA, voltage_LED, 'r.')
ax2.set_xlabel("LED Current (mA)")
ax2.set_ylabel("LED Voltage (V)")
ax2.set_title("V-I Curve")

ax3.plot(voltage_LED, current_photo, 'g.')
ax3.set_xlabel("LED Voltage(V)")
ax3.set_ylabel("Photodiode Current (µA)")
ax3.set_title("L-V Curve")

plt.tight_layout()
plt.show()
ser.close()
