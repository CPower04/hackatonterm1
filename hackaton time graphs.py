from Hackathon import time2
from Sort_1 import time1

import matplotlib.pyplot as plt
import numpy as np
import time



import numpy as np
import matplotlib.pyplot as plt


x_labels = ["search", "sort"]
y_values = [time2, time1] 


colors = ["green", "red"]


plt.bar(x_labels, y_values, color=colors)


plt.grid()


plt.title("Time for Sort and Search Operations", fontsize=16)
plt.xlabel("Search and Sort Algorithms", fontsize=14)
plt.ylabel("Time Taken (miliseconds)", fontsize=14)


plt.show()
