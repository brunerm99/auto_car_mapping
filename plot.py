import random
import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd
import re
import csv

coord_queue = []
coords = {}

# input
# [0-9]+ 	[0-9]+\.?[0-9]*
# theta		range
def plot(fname):
	theta = np.linspace(-1 * math.pi / 2, math.pi / 2, num=180)
	range_arr = np.ma.masked_array(np.zeros(180), mask=True)
	with open(fname) as coords:
		reader = csv.reader(coords)
		for row in reader:
			temp_row = re.search('([0-9]+) ([0-9]+\.?[0-9]*)', str(row))
			temp_angle = temp_row.group(1)
			temp_range = temp_row.group(2)
			range_arr[int(temp_angle)] = temp_range

	# Interpolation for angles without corresponding ranges
	range_pd = pd.DataFrame(data=range_arr)
	range_pd = range_pd.interpolate(method='linear', limit_direction='backward')
	range_pd = range_pd.fillna(0)
	range_arr = range_pd.to_numpy().reshape(range_arr.size)

	ax = plt.subplot(111, projection='polar')
	ax.plot(theta, range_arr)
	ax.set_rmax(30)
	ax.set
	plt.savefig(fname + '.png')
	
