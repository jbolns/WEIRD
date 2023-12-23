"""
Created on sometime in 2023
@author: Dr J

This file handles conversion of Markdown files.

"""

def manage_md(filepath, filename):
  ''' Function takes a path to an HTML file and blurps out the HTML
  '''

  import markdown

  # This function is pretty simple. Just read the file and return the thing. 
  try:
    with open(filepath, 'r') as f:
      text = f.read()
      md = markdown.Markdown(extensions = ['meta'])
      html = md.convert(text)
      meta = md.Meta

    # Return HTML for use by main blog converter
    return html, meta

  except:
    print(f'ERROR. Unfortunately, it was not possible to convert file: {filename}')