"""
Created on sometime in 2023
@author: Dr J

This file handles conversion of HTML files.

"""

def manage_html(filepath, filename):
  ''' Function takes a path to an HTML file and blurps out the HTML
  '''

  # This function is pretty simple. Just read the file and return the thing. 
  try:
    with open(filepath, "r") as f:
      html = f.read()

    # Return HTML for use by main blog converter
    return html

  except:
    print(f'ERROR. Unfortunately, it was not possible to convert file: {filename}')

