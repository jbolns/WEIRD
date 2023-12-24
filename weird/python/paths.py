"""
Created on sometime in 2023
@author: Dr J

This file has path-related functions that are called variously by other WEIRD files.

"""

import os
import shutil



def pathfinder():
  ''' Function finds the root folder for the current WEIRD installation
  '''

  # Try to automatically set the root folder
  try:   
    if __file__:
      root = os.getcwd()
      desktop = os.path.expanduser("~/Desktop")
  except: # Manual override
    print('Failed to automatically detect the root folder. Find a file called "paths.py" and use the manual override included in a function called "pathfinder".')
    #root = ''
    #desktop = ''
  
  return root, desktop




def reset_dirs(path, mode):
  ''' Function resets directories to WEIRD's original settings (mode = 'full') or deletes any pre-existing build (mode = 'partial')
  '''

  from weird.python.assistant import write

  # Save paths
  root = path
  dev = path + '/weird/'

  # Get rid of any extra folders or files at the top-level
  WEIRD = ['.git', '_test-docs', '_external-licenses', 'weird', '.gitignore', 'add.py', 'build.py', 'config.py', 'reset.py', 'server.py', 'LICENSE', 'NOTICE', 'README.md']
  if mode == "partial":
    WEIRD = WEIRD + ['index.html', 'config.txt', 'socials.txt']
  try:
    kill_list = [i for i in os.listdir(root) if i not in WEIRD]
    for item in kill_list:
      if item not in WEIRD:
        if os.path.isfile(root + '/' + item):
          try:
            os.remove(root + '/' + item)
          except Exception as e:
            print('Failed to delete file ', root + '/' + item, '. Try deleting manually')
            print('Error is: ', e)
        if os.path.isdir(root + '/' + item):
          try:
            shutil.rmtree(root + '/' + item)
          except Exception as e:
            print('Failed to delete directory: ', item, '. Try deleting manually')
            print('Error is: ', e)
          
  except:
    print('Failed to perform some deletions needed to reset the existing build. WEIRD might still work, but the best would be to check the folder/file structure manually.')

  # Adjust deletions according to reset mode
  if mode == "full": 
    # Get rid of any extra folders or files at the top-level of the DEV folder
    WEIRD = ['alpha', 'images', 'python', 'utils']
    try:
      for item in os.listdir(dev):
        if item not in WEIRD:
          if os.path.isfile(dev + '/' + item):
            os.remove(dev + '/' + item)
          if os.path.isdir(dev + '/' + item):
            shutil.rmtree(dev + '/' + item)
    except:
      print('Failed to perform some deletions needed to reset WEIRD to original settings. WEIRD might still work, but the best would be to check the folder/file structure manually.')
    # Get rid of any extra folders or files in the image folder
    path = dev + '/images/'
    WEIRD = ['socials', 'list.webp', 'x-square-fill.webp']
    try:
      for item in os.listdir(path):
        if item not in WEIRD:
          if os.path.isfile(path + '/' + item):
            os.remove(path + '/' + item)
          if os.path.isdir(path + '/' + item):
            shutil.rmtree(path + '/' + item)
    except:
      print('Failed to perform some deletions needed to reset WEIRD to original settings. WEIRD might still work, but the best would be to check the folder/file structure manually.')
    
    # Write dummy configs and socials
    CONFIGS = {'sitename': 'Name', 'description': 'Description', 'type': 'website', 'author': 'J', 'keywords': 'k1, k2, k3', 'title': 'Title', 'intro': 'Intro sentence', 'blog': 'no'}
    write(root + '/config.txt', CONFIGS)
    write(root + '/socials.txt', {})
  
  else: # Deletes DEV files generated during build without deleting DEV folders themselves.
    blog_images_folder = '/weird/images/blog/'
    pages_images_folder = '/weird/images/pages/'
    for item in os.listdir(root + blog_images_folder):
      if os.path.isdir(root + blog_images_folder + '/' + item):
        try:
          shutil.rmtree(root + blog_images_folder + '/' + item)
        except:
          print('Failed to perform some deletions needed to fully delete any pre-existing build. WEIRD might still work, but the best would be to check the image folders manually.')
    for item in os.listdir(root + pages_images_folder):
      if os.path.isdir(root + pages_images_folder + '/' + item):
        try:
          shutil.rmtree(root + pages_images_folder + '/' + item)
        except:
          print('Failed to perform some deletions needed to fully delete any pre-existing build. WEIRD might still work, but the best would be to check the image folders manually.')




def create_dev_dirs(path):
  ''' Function creates the necessary DEV directories to configure WEIRD
  '''

  print('Creating folders')
  try:
    # Folder to save source files for pages
    if not(os.path.exists(path + '/pages/')):
      os.mkdir(path + '/pages/')
    # Folder to save source files for blogs
    if not(os.path.exists(path + '/blog/')):
      os.mkdir(path + '/blog/')
    # Folder to save image files for pages
    if not(os.path.exists(path + '/images/pages')):
      os.mkdir(path + '/images/pages')
    # Folder to save image files for blog entries
    if not(os.path.exists(path + '/images/blog')):
      os.mkdir(path + '/images/blog')
  except:
    print('Failed to create some DEV folders. Make sure the folder WEIRD has the following folders: "/pages/", "/blog/", "/images/pages", and "/images/blog".')




def ensure_dirs(path, type):
  ''' Function checks that directories needed for updating or adding pages/blogs are present
  '''

  # Check build folders
  necessary = ['pages', 'blog', 'images', 'components', 'weird']
  OK = 1
  for dir in necessary:
    if not os.path.isdir(f'{path}/{dir}'):
      OK = 0
  
  if not os.path.isdir(f'{path}/images/{type}'):
    OK = 0

  # Check DEV folders
  necessary = ['pages', 'blog', 'images']
  for dir in necessary:
    if not os.path.isdir(f'{path}/weird/{dir}'):
      OK = 0
  
  if not os.path.isdir(f'{path}/weird/images/{type}'):
    OK = 0

  return OK




def build_checks(path):
  ''' Function checks there is at least one document in the DEV's pages folder and that filenames meet requirements
  '''
  OK = 0
  for item in os.listdir(path + '/weird/pages/'):
    if item.startswith('home.'):
      OK = 1
  if OK == 0: 
    print('Build cannot begin: there is no "home" file in the pages folder.')

  for item in os.listdir(path + '/weird/pages/'):
    if item.startswith('blog.'):
      OK = 0
      print('Build cannot begin: the pages folder CANNOT contain any file named "blog"')

  return OK




def filename_check(paths, type):
  ''' Function checks file names to see if they meet requirements to add pages or blogs via the set up assistant
  '''
  
  ok = 0
  if f'home.html' in ' '.join(paths) or f'home.md' in ' '.join(paths) or f'home.docx' in ' '.join(paths):
    ok = 1
  else:
    print(f'No {type} added. Requirements not met. You can add {type} manually later. Moving to next step.')
  
  if 'blog.html' in ' '.join(paths) or 'blog.md' in ' '.join(paths) or 'blog.docx' in ' '.join(paths):
    ok = 0
    print(f'No {type} added. Requirements not met. You can add {type} manually later. Moving to next step.')
  
  return ok




def filename_check_the_2nd(paths, type):
  ''' Function checks file names to see if they meet requirements too add page or blog
  '''
  
  ok = 1
  for path in paths:
    name = path[path.rfind('/')+1:]
    if name.startswith('blog.'):
      ok = 0
      print(f'No {type} added. Requirements not met. Please check your filenames.')

  return ok




def create_build_dirs(path):
  ''' Function creates directories if they do not already exist
  '''    

  print('Checking/creating folders')

  # Folder to save HTML structures for pages
  if not(os.path.exists(path + '/pages/')):
    os.mkdir(path + '/pages/')

  # Folder to save page components (incl. content)
  if not(os.path.exists(path + '/components/')):
    os.mkdir(path + '/components/')

  # Folder to save JSONs that will act as indexes for various sections
  if not(os.path.exists(path + '/json/')):
    os.mkdir(path + '/json/')

  # Folder to save final blogs
  if not(os.path.exists(path + '/blog/')):
    os.mkdir(path + '/blog/')
      