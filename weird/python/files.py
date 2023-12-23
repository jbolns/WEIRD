"""
Created on sometime in 2023
@author: Dr J

This file has file-related functions that are called variously by other WEIRD files.

"""

import os
import shutil
from tkinter import *
from tkinter import filedialog

from weird.python.paths import filename_check


def browser(path, type):
  ''' Function pops up a browser to allow user to select files, returning an array with filenames
  '''
  
  files = filedialog.askopenfilenames(initialdir= path, title = f"Select file(s).")
  if type == 'image':
    files = files[0]
  return files




def distribute(destination, filepaths, type):
  ''' Function takes a list of files and copies them into a destination
  '''
  
  if type.lower() == 'pages':
    ok = filename_check(filepaths, type)
  else:
    ok = 1

  if ok == 1:
    for path in filepaths:
      if type == 'logo' or type == 'emoticon' or type == 'og-image':
        filename = type + path[path.rfind('.'):]
      else:
        filename = path[path.rfind('/') + 1:]
      shutil.copy(path, destination + filename)




def img_handler(search_path, destination_path, type):
  ''' Function asks if user uploaded HTML or MD files with image references and allows user to upload images if so
  '''

  A = input(f'\nDid any HTML or Markdown file uploaded as {type} referenced any images (yes/no)?\n')
  if A == 'yes':
    path = destination_path + type + '/'
    print(f'\nFile explorer has opened. Select images referenced in the HTML or Markdown files you just uploaded as {type}?\n')
    image_paths = browser(search_path, type)
    for path in image_paths:
      filename = path[path.rfind('/') + 1:]
      shutil.copy(path, destination_path + type + '/' + filename)




def add_to_dev(root, filepaths, type):
  ''' Function takes files and adds it as page or blog
  '''

  for path in filepaths:
    # Get filename
    filename = path[path.rfind('/') + 1:]
    
    # Copy file to dev folder
    shutil.copy(path, f'{root}/weird/{type}/{filename}')




def final_file_transfer(path):
  ''' Function transfers images and utils from dev to production folder
  '''
  
  source = f'{path}/weird/utils/'
  destination  = f'{path}/utils/'
  if not os.path.isdir(destination):
    shutil.copytree(source, destination)
  
  source = f'{path}/weird/images'
  destination  = f'{path}/images'
  if not os.path.isdir(destination):
    shutil.copytree(f'{path}/weird/images/', f'{path}/images/')
  else:
    for file in os.listdir(f'{source}/pages/'):
      if os.path.isfile(f'{source}/pages/{file}'):
        try:
          shutil.copy(f'{source}/pages/{file}', f'{destination}/pages/')
        except:
          pass
      else:
        try:
          shutil.copytree(f'{source}/pages/{file}', f'{destination}/pages/{file}/')
        except:
          pass
    for file in os.listdir(f'{source}/blog/'):
      if os.path.isfile(f'{source}/blog/{file}'):
        try:
          shutil.copy(f'{source}/blog/{file}', f'{destination}/blog/')
        except:
          pass
      else:
        try:
          shutil.copytree(f'{source}/blog/{file}', f'{destination}/blog/{file}/')
        except:
          pass