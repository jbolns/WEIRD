"""
Created on sometime in 2023
@author: Dr J

This file handles conversion of DOCm (macro-enabled Word) files.

"""

import win32com.client as win32
import shutil
import sys
import os
import re




def convert_word(source_folder, filename, name):
  ''' Function asks WORD to save file as HTML. File and images dumped to temp folder.
  '''

  # Try starting Word, with fallback to ensure it starts
  try: # Start Word 
    word = win32.gencache.EnsureDispatch('Word.Application') 
  except AttributeError as e: 
    # The block above works sometimes but, other times, TEMP files get in the way. 
    # I totally stole this solution from: https://gist.github.com/rdapaz/63590adb94a46039ca4a10994dff9dbe
    # Thanks!
    for module in [m.__name__ for m in sys.modules.values()]:
      if re.match(r'win32com\.gen_py\..+', module):
        del sys.modules[module]
    shutil.rmtree(os.path.join(os.environ.get('LOCALAPPDATA'), 'Temp', 'gen_py'))
    word = win32.gencache.EnsureDispatch('Word.Application')
  except Exception as e:
    print('ERROR. Word failed to start:', e, '\n')
  
  if word:
    try: # Try a bunch of things on Word
      wb = word.Documents.Open(source_folder + filename) # Open target document
      vba_module = wb.VBProject.VBComponents.Add(1) # ADD a VB project
      
      # VBA code to save in component
      vba_code = '''
      Option Explicit
        Option Base 1
        Sub wordToHTML()
        Dim path As String
        path = "''' + source_folder + 'temp/' + name + '''.html"
        ActiveDocument.SaveAs2 filename:=path, FileFormat:=wdFormatFilteredHTML
        ActiveDocument.Close 0
      End Sub'''
      vba_module.CodeModule.AddFromString(vba_code) # Write code to module
      
      word.Application.Run("wordToHTML") # Run VBA code
      word.Application.Quit() # Close Word
    except Exception as e: #Close word in case of failure
      print('ERROR. Word document failed to open:', e, '\n')
      word.Application.Quit()




def polish_word(source_folder, name, type):
  '''Function reads converted HTML and cleans it up to match WEIRD's requirements'''

  # Read file and import contents
  filename = name + '.html'
  with open(source_folder + filename, 'r') as f:
    html = f.read()
    f.close()

  # Get rid of weird (lol) Wingdings and the like symbols used in Word
  easy_wins = {'ü':'&#x2714;', '’': "'", '·': '&#x25CF;', '§': '&#x25A0'}
  for key, value in easy_wins.items():
    html = html.replace(key, value)
  
  # Extract the <style> section
  start = html.find('<style>')
  end = html.find('</style>') + len('</style>')
  style = html[start:end]
  style = style.replace('\n', ' ').replace('\t', '')
  common_html_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'ul', 'ol', 'li', 'a', 'div', 'span', 'form', 'img', 'svg', 'iframe', 'nav', 'table', 'tr', 'td', 'th']
  for tag in common_html_tags:
    style = style.replace(' ' + tag + ' {', ' .wordm ' + tag + ' {')
    style = style.replace(' ' + tag + ',', ' .wordm ' + tag + ',')
    style = style.replace(' ' + tag + ':', ' .wordm ' + tag + ':')

  # Isolate main section and re-write HTML to include only that
  start = html.find('<body') # Get rid of anything before <body> section
  html = html[start:]
  start = html.find('<div') # HTML string covering everything between first <div> and last </div>
  end = html.rfind('</div>') + + len('</div>')
  html = html[start:end]
  html = html.replace(f'"{name}_files/', f'"../../images/{type}/{name}/')
  for i in range(0,100):
    html = html.replace(f'class=WordSection{i}', 'class="WordSection wordm"')
      
  # Rewrite style as script
  script = f'\n\n<script>\nvar style = `{style}`\ndocument.head.insertAdjacentHTML("beforeend", style)\n</script>\n\n'

  # Rewrite HTML
  html = html + script

  # Return HTML
  return html




def distribute_word(temp_folder, root, type, name):
  '''Function takes files form temp folders and sends them to their final build folders'''
  
  source = temp_folder + name + '_files/'
  destination = f'{root}/weird/images/{type}/{name}/'

  if os.path.isdir(destination):
    shutil.rmtree(destination)  
  os.makedirs(destination)

  for file in os.listdir(source):
    shutil.copy(source + file, destination + file)




def manage_docm(root, type, filepath):
  '''Function takes a path and returns folder, file name, and file extension'''

  # Break filepath into pieces used to call other functions
  source_folder = filepath[:filepath.rfind('/') + 1]
  filename = filepath[filepath.rfind('/') + 1:]
  name = filename[:filename.rfind('.')]

  try:

    # Make a temporary directory to dump HTML file and image folder / images
    temp_folder = source_folder + 'temp/'
    os.mkdir(temp_folder)

    try:
      # Open word application and save file as HTML
      convert_word(source_folder, filename, name)

      # Open HTML file and re-write it into a format compatible with WEIRD
      html = polish_word(source_folder + 'temp/', name, type)

      # Move image files into image folder
      distribute_word(temp_folder, root, type, name)
    except:
      print(f'ERROR. Unfortunately, it was not possible to convert file: {filename}')

    # Erase temporary directory and all files in it
    shutil.rmtree(temp_folder)

    # Return HTML for use by main blog converter
    return html

  except:
    print(f'ERROR with filename {filename}')

