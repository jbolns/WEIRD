"""
Created on sometime in 2023
@author: Dr J

This file has functions that help creating the main wireframe/structures needed for a WEIRD website.

"""

import shutil



def wireframe(source_path, destination_path, unconverted_pages, unconverted_blogs, blog):
  ''' Function creates the basic HTML structures that enable functionality across pages.
    It takes files in '/weird/alpha' and distributes them across build folders
  '''
  print('Creating foundational HTML structures')
  
  # Copy the raw index file to the root of the website
  filename = 'index.html'   
  shutil.copy(source_path + filename, destination_path)

  # Adjust HTML to be reusable as wrapper for pages and blogs (wrappers are located in a subfolder)
  with open(source_path + filename, 'r') as f:
    html = f.read()
    html = html.replace('./', '../')
    f.close()

  # Create a wrapper file for each document in DEV's pages folder
  for page in unconverted_pages:
    page = page[:page.rfind('.')]
    with open(destination_path + '/pages/' + page + '.html', 'w', encoding='utf8') as f:
      f.write(html)
      f.close()

  # Check if website needs a blog
  if blog == 'yes':
    # Write a special blog.html wrapper to the pages folder
    with open(destination_path + '/pages/blog.html', 'w', encoding='utf8') as f:
      f.write(html)
      f.close()

    # Create a wrapper file for each document in DEV's blog folder
    for blog in unconverted_blogs:
      blog = blog[:blog.rfind('.')]
      with open(destination_path + '/blog/' + blog + '.html', 'w', encoding='utf8') as f:
        f.write(html)
        f.close()
  



def components(source_path, destination_path, components):
  ''' Function creates the basic HTML components to populate pages.
    It takes files in '/weird/alpha' and saves them to '/components'
  '''

  for component in components:
    if not component.startswith('index.'):
      shutil.copy(source_path + component, destination_path)




def sitedata(path):
  ''' Function extracts the configuration settings from config.txt
  '''

  with open(path + '/config.txt') as f:
    lines = f.readlines()

  CONFIG = {'sitename': '', 'description': '', 'type': '', 'author': '', 'keywords': '', 'title': '', 'intro': '', 'blog': ''}

  for item in CONFIG:
    for line in lines:
      if line.startswith(item):
        start = len(item) + 1
        content = line[start:].strip()
        CONFIG[item] = content
  
  return CONFIG




def index(data, path):
  ''' Function writes the INDEX.html file using information from the config file
  '''

  html = f"\
  <!DOCTYPE html>\n\
  <html lang='en'>\n\
  <head>\n\
    <meta charset='utf-8'>\n\
    <title>{data['sitename']}</title>\n\
    <meta name='description' content='{data['description']}'>\n\
    <meta name='keywords' content='{data['keywords']}'>\n\
    <meta name='author' content='{data['author']}'>\n\
    <meta property='og:type' content='{data['type']}' >\n\
    <meta property='og:image' content='./images/og-image.webp'>\n\
    <meta name='viewport' content='width=device-width,initial-scale=1'>\n\
    <script src='./utils/libs/jquery-3.7.1.min.js'></script>\n\
    <script src='./utils/js/mainjs.js'></script>\n\
    <link rel='icon' href='./images/emoticon.webp' type='image/WebP' sizes='any'>\n\
    <link rel='stylesheet' href='./utils/css/style.css'>\n\
  </head>\n\
  <body onload='load()'>\n\
  </body>\n\
  </html>"   

  with open(path + 'index.html', 'w', encoding='utf8') as f:
    f.write(html)
    f.close()
  
  html = f"\
  <header>\n\
    <nav>\n\
      <ul class='toplinks'>\n\
          <!-- Navigation links are automatically appended here -->\n\
      </ul>\n\
      <ul class='socials'>\n\
          <!-- Social media links are automatically appended here -->\n\
      </ul>\n\
    </nav>\n\
    <div class='branding flexie-v-align'>\n\
      <div class='half right sitelogo'>\n\
        <img id='logo' class='profile' width='350' height='auto' srcset='../images/logo.webp 300w'\n\
        sizes='(max-width: 300px) 300px' src='../images/logo.webp' alt='Header picture' />\n\
      </div>\n\
      <div class='half left sitename'>\n\
      <h1 id='title'>{data['title']}</h1>\n\
      <p id='intro'>{data['intro']}</p>\n\
      </div>\n\
    </div>\n\
  </header>"   
  
  with open(path + 'header.html', 'w', encoding='utf8') as f:
    f.write(html)
    f.close()




def blog_not_blog(path):
    ''' Function checks if the website should have a blog
    '''
    
    print('Checking blog configuration details.')

    with open(path + '/config.txt') as f:
        lines = f.readlines()

    for line in lines:
        if line.startswith('blog'):
            start = len('blog') + 1
            str = line[start:].strip()
    
    return str
