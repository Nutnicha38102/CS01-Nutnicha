# -*- coding: utf-8 -*-
"""cs01-17.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ny9FghlAxAJfrw9wCGfYOIR6fa2R4-or
"""

from numpy import random
x = random.randint(100, size=(5,10))
import numpy as np
arr = np.array([x])
print(np.sort(arr))