#from plot import plot
import serial
import time
import re

s = serial.Serial('/dev/ttyACM0', 9600)
#s.open()
time.sleep(5)

volume_count = 0
file_count = 0
limit = 178
angle_increment = 1
curr_angle = 0

try:
    while True:
        filename = "output{}".format(file_count)
        file = open(filename, 'w')
        while (curr_angle < limit):
            response = s.readline()
            print(response)
            temp_line = re.search('[a-zA-Z: ]+([0-9]+)[a-zA-Z: -]+([0-9]+)', str(response))
            if (temp_line):
                temp_angle = temp_line.group(1)
                temp_dist = temp_line.group(2)
                curr_angle = int(temp_angle)
                print(temp_angle, temp_dist)
                file.write(temp_angle + ' ' + temp_dist + '\n')
            if (curr_angle >= limit):
                # plot(filename)
                curr_angle = 0
                file_count += 1
                break
except KeyboardInterrupt:
    s.close()
    file.close()
