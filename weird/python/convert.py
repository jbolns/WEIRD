"""
Created on sometime in 2023
@author: Dr J

This file handles the main logic of any document conversion performed by WEIRD (mostly, it calls type-specific convertors as needed). 
The file includes functions to keep track of any meta-data needed (especially in case of blogs)

"""

import json
from datetime import date
from bs4 import BeautifulSoup

from weird.python.assistant import q_a
from weird.python.convert_docm import manage_docm
from weird.python.convert_html import manage_html
from weird.python.convert_md import manage_md
from weird.python.convert_docx import manage_docx



def update_data(filename, html, meta):
  ''' Function produces a JSON array from filename, html, and meta data of any appropriately formatted input
  '''
  # Cut extension from filename
  filename = filename.rsplit( ".", 1 )[0]
  
  # Date from the meta array, or fallback
  if filename.endswith('.md'):
    try: # Extract from .md files
      datum = meta['date'][0]
      cats = meta['categories'][0]
    except:
      datum = date.today().strftime("%Y-%m-%d")
      cats = ''
  else:
    try:
      datum = meta['date']
      cats = ' '.join(meta['categories'])
    except:
      datum = date.today().strftime("%Y-%m-%d")
      cats = ''

  # Title and intro paragraph from html
  soup = BeautifulSoup(html, 'lxml')
  try: # This series of tries ensure the title will be the highest ranking headline in text
    title = str(soup.find('h3').decode_contents())
  except: 
    pass
  try:
    title = str(soup.find('h2').decode_contents())
  except: 
    pass
  try:
    title = str(soup.find('h1').decode_contents())
  except: 
    pass
  
  try: # This series of tries ensure intro paragraphs is the top paragraph in document
    intro = str(soup.find('p').decode_contents())
  except:
    pass
  try:
    intro = str(soup.find('p', attrs={"class": None}).decode_contents())
  except:
    pass

  # Format entry and append to data array
  entry = { "filename": filename, "headline": title, "intro": intro, "categories": cats, "date": datum }

  return entry

def ask_meta(title):
  ''' Function asks user for meta: author, date, categories
  '''

  print(f'\nWe need to ask some questions about the blog entitled "{title}')

  questions = {'author': '1. Who is the author of this blog entry?\n',
  'date' : '2. What date do you want to assign to this blog entry (required format: yyyy-mm-dd)?\n',
  'categories': '3. What categories do you want to assign to this blog entry (separate categories with commas)\n'}

  meta = q_a({}, questions) # Comment line for faster testing
  # meta = {'author': 'author', 'date': '2023-12-24', 'categories': 'complex cat, cat2, cat3'} # Uncomment line for faster testing.
  
  meta['categories'] = meta['categories'].split(',')

  for i, cat in enumerate(meta['categories']):
    newcat = cat.strip().replace(' ', '-')
    meta['categories'][i] = newcat

  return meta


def clean_meta(meta):
  '''Function cleans the meta from md files to ensure consistency across formats
  '''

  meta['categories'] = meta['categories'][0].split(',')
  for i, cat in enumerate(meta['categories']):
    meta['categories'][i] = cat.strip()
  
  return meta



def convert(root, source, destination, inputs, type):
  '''Function takes files in '/weird/blog', whatever their format, and converts them to HTML
      Currently supported file types: .html, .md, .docx, .docm
  '''
  print(f'Creating {type}')
  
  # Fully constructed paths from incoming variables
  source_path = root + source
  destination_path = root + destination

  # Vars to prepend/append code (optional - leave empty if desired)
  append = '\n\n</div></section>'

  # Loop over files in 'weird/blog' folder
  data = [] # Used to accumulate basic information for blogs and then write a JSON with basic blog indexing info

  # The logic in this process is quite straightforward. Checks type of document, calls functions for that type
  
  for file in inputs:

    # Check for HTML documents
    if file.endswith('.html'):
      
      prepend =  ''
      append = ''
      
      html = manage_html(source_path + file, file)
      
      html = prepend + html + append

      if type == 'blog':
        meta = ask_meta(file)
        entry = update_data(file, html, meta)
        data.append(entry)
      
      with open(destination_path + file, 'w') as f:
        f.write(html)

    # MARKDOWN documents
    if file.endswith('.md'):

      prepend =  f'<section class="{type} markdown">\n\n'
      
      html, meta = manage_md(source_path + file, file)
      html = prepend + html + append
      
      if type == 'blog':
        meta = clean_meta(meta)
        entry = update_data(file, html, meta)
        data.append(entry)

      with open(destination_path + file.removesuffix('.md') + '.html', 'w') as f:
        f.write(html)
    
    # DOCx documents
    if file.endswith('.docx'):
      
      prepend =  f'<section class="{type} docx">\n\n'
      
      html = manage_docx(source_path + file, file, type)
      html = prepend + html + append
      
      if type == 'blog':
        meta = ask_meta(file)
        entry = update_data(file, html, meta)
        data.append(entry)
      
      with open(destination_path + file.removesuffix('.docx') + '.html', 'w', encoding="utf8") as f:
        f.write(html)
    
    # Check for macro-enabled (.docm) WORD documents
    if file.endswith('.docm'):

      prepend =  f'<section class="{type} docm">\n\n'
      append = '</section>'
      
      html = manage_docm(root, type, source_path + file)
      html = prepend + html + append
      
      if type == 'blog':
        meta = ask_meta(file)
        entry = update_data(file, html, meta)
        data.append(entry)
      
      with open(destination_path + file.removesuffix('.docm') + '.html', 'w') as f:
        f.write(html)
      
  return data


def blog_index(path, data):
  '''Function creates a JSON that will be used as blog index
  '''
  
  print('Creating blog index')
  with open(path, "w") as f:
    json.dump(data, f, indent=2)