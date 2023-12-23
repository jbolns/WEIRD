"""
Created on sometime in 2023
@author: Dr J

This file has helper functions to be called variously.

"""


import time



def countdown(seconds):
  while seconds:
    print(seconds, end='\r')
    time.sleep(1)
    seconds = seconds - 1
  print('Ready', end='\r')




def confirm(message):
  ''' Function confirms if user wants to do something
  '''

  Q = message
  A = input(Q).lower()
  return A