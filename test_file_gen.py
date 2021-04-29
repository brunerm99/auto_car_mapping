file = open("test_file", 'w')
for i in range(360):
    str = "{} {}\n".format(3*i, i)
    file.write(str)
file.close()
