from plot import plot
import serial
import time

s = serial.Serial('/dev/ttyACM0', 9600)
#s.open()
time.sleep(5)

s.write("test")

#test = open("test_file", 'r')

volume_count = 0
file_count = 0
limit = 180
angle_increment = 1

try:
    while True:
        filename = "output{}".format(file_count)
        file = open(filename, 'w')
        while (volume_count < limit):
            response = s.readline()
            file.write(response)
            print(response)
            volume_count += angle_increment
            if (volume_count >= limit):
                plot(filename)
                volume_count = 0
                file_count += 1
                break
except KeyboardInterrupt:
    s.close()
    file.close()
