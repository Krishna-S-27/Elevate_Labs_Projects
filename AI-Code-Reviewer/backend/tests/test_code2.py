import math, os   # 'os' is unused (lint issue)
import random

# Global variable never used
UNUSED_CONSTANT = 100

def calculate_area(radius):
   if radius>0:   # Bad spacing
      area=math.pi*radius*radius
      return area
   else:
     return None    # Inconsistent indentation

def complex_function(a, b, c):
    result = 0
    for i in range(a):          # Loop 1
        for j in range(b):      # Loop 2 -> nested loop (complexity)
            if i % 2 == 0:
                if j % 3 == 0:
                    if c > 10:
                        result += i*j*c   # Too many nested ifs (complexity)
    return result

class DataProcessor:
   def __init__(self, data):
        self.data = data
        self.temp = 0  # never used (lint issue)

   def process(self):
        cleaned = [x for x in self.data if x != None]  # "None" should not be compared with '!='
        if len(cleaned) > 0:
             avg = sum(cleaned)/len(cleaned)
             if avg>50:
                return "High"
             else:
                  return "Low"
        else:
             return "Empty"

   def unused_method(self):
        pass  # defined but never used
