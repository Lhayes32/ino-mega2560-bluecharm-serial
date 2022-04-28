import serial
import time

ser = serial.Serial(
    port='COM3',
    baudrate=9600)

isOpen = ser.isOpen()

time.sleep(1)

ser.write(bytes('AT' + '\r\n', 'UTF-8'))

out = ''

time.sleep(1)

while ser.inWaiting() > 0:
    out += ser.read(1).decode('UTF-8')

if out != '':
    print(">>" + out)

if 'OK' in out:
    print("Handshake Complete")

time.sleep(1)

ser.write(bytes('AT+ROLE1' + '\r\n', 'UTF-8'))

out = ''

time.sleep(1)

while ser.inWaiting() > 0:
    out += ser.read(1).decode('UTF-8')

if out != '':
    print(">>" + out)

if 'OK' in out:
    print("ROLE SET Complete")

time.sleep(1)

ser.write(bytes('AT+IMME1' + '\r\n', 'UTF-8'))

out = ''

time.sleep(1)

while ser.inWaiting() > 0:
    out += ser.read(1).decode('UTF-8')

if out != '':
    print(">>" + out)

if 'OK' in out:
    print("IMME SET Complete")

time.sleep(1)

ser.write(bytes('AT+RESET' + '\r\n', 'UTF-8'))

out = ''

time.sleep(1)

while ser.inWaiting() > 0:
    out += ser.read(1).decode('UTF-8')

if out != '':
    print(">>" + out)

if 'OK' in out:
    print("RESET Complete")

time.sleep(1)

ser.write(bytes('AT+DISI?' + '\r\n', 'UTF-8'))

out = ''

time.sleep(4)

while ser.inWaiting() > 0:
    out += ser.read(1).decode('UTF-8')

if out != '':
    print(">>" + out)

if 'OK+DISC:4C000215' in out:
    print("DOT Found")
    start = out.find("OK+DISC:4C000215")
    end = start + 78
    print(out[start:end])
    full_id = out[start:end].split(':')
    print(full_id)
    id = full_id[1]
    uuid =  full_id[2]
    unknown = full_id[3]
    mac = full_id[4]
    RSSI = full_id[5]
    print(f"iBeacon identifier: {id}, UUID: {uuid}, UNKNOWN2: {unknown}, MAC: {mac}, RSSI: {RSSI} ")
else:
    print("DOT not found")


ser.close()
