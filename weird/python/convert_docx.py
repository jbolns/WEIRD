"""
Created on sometime in 2023
@author: Dr J

This file handles conversion of DOCx (Word) files.

"""

import markdown
from docx2python import docx2python




def manage_docx(filepath, filename, type):
  ''' Function takes a path and returns folder, file name, and file extension
  '''

  name = filename.removesuffix('.docx')

  # Right, this is a mess but essentially, 
  # 1. picks content from .docx file using docx2python
  # 2. transforms it into something resembling markdown
  # 3. converts to HTML using markdown
  try:
    with docx2python(filepath, f'./weird/images/{type}/{name}/', html=True) as f:
      content = f.text
    adjustments = {'--\t': '* ', ')\t': '. ', '----footnote': '[^', '----endnote': '[^', '  ': ' ','\n\n\n\n\n\nfootnote1.': '\n\n\n**Notes**\n\n1.', '\n\nfootnote': '\n', '\n\n\n\n\n\nendnote1.': '\n\n\n**Notes**\n\n1.', '\n\nendnote': '\n', '----media/': f'![](../../images/{type}/{name}/', '----Image alt text---->': '![', '<![': '', '----': ']'}
    for key, value in adjustments.items():
      content = content.replace(key, value)
    img_formats = ['.jpg', '.jpeg', '.png', '.gif', 'svg', '.webp', '.tif', '.tiff', '.bmp', 'ico', '.cur', '.apng', '.avif']
    for format in img_formats:
      content = content.replace(format + ']', format + ')')
    html = markdown.markdown(content)
    html = html.replace('<li>\n<p>', '<li>').replace('</p>\n</li>', '</li>')
    html = html.replace('<p><></p>', f'</section>\n<section class="{type} docx">')
    html = html.replace('<p>&lt;&gt;</p>', f'</section>\n<section class="{type} docx">')
    
    
    # Return HTML for use by main blog converter
    return html
    
  except:
    print(f'ERROR. Unfortunately, it was not possible to convert file: {filename}')

