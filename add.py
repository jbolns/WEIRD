"""
Created on sometime in 2023
@author: Dr J

This file can be used to add pages or blog entries to a WEIRD website.

"""

import os
import json

from weird.python.alpha import wireframe, blog_not_blog
from weird.python.paths import pathfinder, ensure_dirs, filename_check_the_2nd
from weird.python.files import browser, add_to_dev, img_handler, final_file_transfer
from weird.python.convert import convert, blog_index
from weird.python.nav import nav_links




def main():
  ''' Function handles the flow of actions and calls other functions as needed
  '''

  print("\n\n=> LET'S ADD TO YOUR SITE. Please ensure there is a site to add to. Things won't quite work otherwise.")

  
  # Find key paths used across functions
  root, desktop = pathfinder()
  print(f'Root folder is {root}. Folders/files will be created there/onwards.\n.............\n........\n.....\n...\n..\n.\n')

  # Ask user if addition is blog or page
  Q = 'Do you want to add a page or a blog?\n'
  
  type = ''
  while type != 'page' and type != 'blog':
    type = input(Q)
    type = type.lower()
    if type != 'page' and type != 'blog':
      print("Sorry, didn't quite get that. Please answer using a single word: blog or page.")
  if type == 'page':
    type = 'pages'

  # Check for / create necessary folders            
  OK = ensure_dirs(root, type)

  # If necessary folders are present, initiate a file explorer and ask user to upload file meeting requirements
  if OK == 0:
    print("It doesn't look like you have all the folders needed to add blogs or pages. Please try setting up and build a site first.")
  else:
    print("\nOK! Let's update/add some stuff!\n\
      Requirements:\n\
      1. Supported formats: .html, .md, .docx, and docm.\n\
      2. Filename 'blog' is forbidden.\n\
      3. To update/over-write an existing page or blog, use the same filename as existing document/component.\n\
      Ps1. Relative paths for images in HTML or Markdown files: '../images/pages/filename' or '../images/blog/filename'.\n\
      Ps2. Do not worry about images in Word documents. These get handled automatically.")

    print(f'\nFile explorer has opened (find it if not visible). Select {type} to add.\n')
    paths = browser(desktop, type)

    # If a file is uploaded, check it meets requirements, then,
    if len(paths) > 0:
      OK = filename_check_the_2nd(paths, type)
      if OK == 1:
        # Add document to appropriate DEV folder
        add_to_dev(root, paths, type)
        inputs = []
        # Add a converted version of the document to the build's components
        for path in paths:
          inputs.append(path[path.rfind('/') + 1:])
        addendum = convert(root, f'/weird/{type}/', '/components/', inputs, type)

        # If document is a blog, update the blog index
        if type == 'blog':
          with open(f'{root}/json/blog1.json', "r") as f:
            data = json.load(f)
          data = list(filter(lambda x : x['filename'] != addendum[0]['filename'], data))
          data = data + addendum
          blog_index(f'{root}/json/blog1.json', data)
              
        # Ask for any images in HTML or Markdown code
        img_handler(desktop, root + '/weird/images/', type)
        
        # Recreate the build's wireframe using all files now in pages and blogs folder
        pages = os.listdir(root + '/weird/pages')
        blogs = os.listdir(root + '/weird/blog')
        blog = blog_not_blog(root)
        wireframe(root + '/weird/alpha/', root, pages, blogs, blog)

        # Re-create JSON for main navigation menu
        pages = os.listdir(root + '/pages')
        nav_links(root + '/json/nav1.json', pages)

        # Transfer images and utils
        final_file_transfer(root)

  return print(f'\nFinished adding to your site.')


# Run only when executed as script
if __name__ == "__main__":     
    main()