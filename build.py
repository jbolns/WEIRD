"""
Created on sometime in 2023
@author: Dr J

Given appropriate configuration, this file can be used to build a WEIRD website.

"""

import os

from weird.python.paths import pathfinder, reset_dirs, build_checks, create_build_dirs
from weird.python.alpha import wireframe, components, sitedata, blog_not_blog, index
from weird.python.nav import nav_links
from weird.python.convert import convert, blog_index
from weird.python.socials import socials
from weird.python.files import final_file_transfer




def main():
  ''' Function handles the flow of actions and calls other functions as needed
  '''

  print('\n\n=> BUILDING SITE. Try holding your breath (works faster that way)...\n.............\n........\n.....\n...\n..\n.\n')
  
  # Find key paths used across functions
  root, desktop = pathfinder()
  print(f'Root folder is {root}. Folders/files will be created there/onwards.\n')

  # Rewrite core website settings to ensure all information is fresh
  configsdata = sitedata(root)
  index(configsdata, root + '/weird/alpha/')
  
  # Check for / create necessary folders
  reset_dirs(root, 'partial')

  # Check if build is possible / pass if it isn't
  OK = build_checks(root)

  if OK == 0:
    pass
  else:
    # Create necessary destination (build) folders
    create_build_dirs(root)

    # Create a list of pages and blogs that need to be converted
    unconverted_pages = os.listdir(root + '/weird/pages')
    unconverted_blogs = os.listdir(root + '/weird/blog')

    # Check if the website will have a blog
    blog = blog_not_blog(root)

    # Create index.html and an HTML wrapper for each top-level page and, if needed, blog entries
    wireframe(root + '/weird/alpha/', root, unconverted_pages, unconverted_blogs, blog)

    # Create components for the main HTML sections of any page or blog entry
    inputs = os.listdir(root + '/weird/alpha')
    components(root + '/weird/alpha/', root + '/components/', inputs)
    
    # Create components for top-level pages 
    data = convert(root, '/weird/pages/', '/components/', unconverted_pages, 'pages')

    # Create JSON for main navigation menu
    pages = os.listdir(root + '/pages')
    nav_links(root + '/json/nav1.json', pages)

    # Create components for blog entries, if website needs a blog
    if blog == 'yes':
      # Create blog entries
      data = convert(root, '/weird/blog/', '/components/', unconverted_blogs, 'blog')

      # Create JSON blog index
      blog_index(root + '/json/blog1.json', data)

    # Create JSON to populate social media bar
    socials(root, root + '/json/socials.json')

    # Transfer images and utils (step needs to be last as some conversions create subfolders in DEV's image folder)
    final_file_transfer(root)

    return print('Finished build.')


# Run only when executed as script
if __name__ == "__main__":     
  main()