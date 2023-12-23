"""
Created on sometime in 2023
@author: Dr J

This file can help the user with WEIRD's initial setup.


"""

from weird.python.paths import pathfinder, reset_dirs, create_dev_dirs
from weird.python.files import browser, distribute, img_handler
from weird.python.assistant import q_a, blog, write, channels
from weird.python.misc import countdown, confirm
from weird.python.alpha import sitedata, index


def main():
  ''' Function handles the flow of actions needed to configure WEIRD 
  '''

  ##
  ###
  ####  INITIALISE ASSISTANT
  print("\n\nWELCOME TO WEIRD! THIS ASSISTANT WILL HELP YOU SET YOUR WEBSITE UP!")
  root, desktop = pathfinder()
  CONFIGS = {}

  ##
  ###
  #### LET USER KNOW AND ASSIMILATE THAT THE INSTALL CLEARS ANY PRE-EXISTING SETTINGS
  print("Reseting WEIRD to original settings to allow a new set up...")
  reset_dirs(root, 'full')
  create_dev_dirs(root + '/weird/')
  countdown(3)

  ##
  ###
  #### REQUIRED INFO – NEEDED FOR WEBSITE'S <head> AND <header> SECTIONS AND FOR BLOG FUNCTIONALITY
  
  # Info needed for <head> section
  print("\n\n=> REQUIRED STEP 1/4. Information needed for browser and search engine functionality.\n")
    
  questions = {'sitename': '\nGive your website a short name.\n',
    'description' : '\nDescribe your website for search engines and social media previews (keep it clear and short).\n',
    'type' : '\nWhat kind of website this is (common types are website, blog, and article)?. Leave blank if you do not know.\n',
    'author' : '\nWho is the author of this website? Leave empty if you do not know.\n',
    'keywords' : '\nPlease provide comma-separated SEO keywords for this website. Leave empty if you do not know.\n'}
  CONFIGS = q_a(CONFIGS, questions)

  # Info needed for <header> section
  print("\n\n=> REQUIRED STEP 2/4. Information needed top <header> section.\n")
  
  questions = {'title': '\nWhat title do you want users to see at the top of the website? It can be the same as the website name, but it can also be different.\n',
    'intro' : '\nWhat is the intro/tagline you want users to see after the website name/title?\n'}
  
  CONFIGS = q_a(CONFIGS, questions)
  
  # Info needed for blog functionality
  print("\n\n=> REQUIRED STEP 3/4. Information needed for blog functionality.\n")
  CONFIGS = blog(CONFIGS)

  # Write info to config file
  write(root + '/config.txt', CONFIGS)

  # Images needed for <head> and <header> sections
  print("\n\n=> REQUIRED STEP 4/4. Necessary images.\n")
  
  # Logo
  print('Select a file to use as LOGO (300 x 300px). File explorer will open (find it if not visible) in...')
  countdown(3)
  path = browser(desktop, 'logo')
  distribute(root + '/weird/images/', path, 'logo')
  
  # Emoticon
  print('Select a file to use as EMOTICON (75 x 75px). File explorer will open (find it if not visible) in...') 
  countdown(3)
  path = browser(desktop, 'emoticon')
  distribute(root + '/weird/images/', path, 'emoticon')

  # OG-image
  print('Select a file to use as OG-IMAGE (the for social media previews, circa 1200 x 630px). File explorer will open (find it if not visible) in...') 
  countdown(3)
  path = browser(desktop, 'emoticon')
  distribute(root + '/weird/images/', path, 'og-image')


  ##
  ###
  #### OPTIONAL STEPS (SOCIAL MEDIA LINKS, PAGE UPLOAD, INITIAL BLOG ENTRIES)
  print("\n.\n..\n...\n...\n=> REQUIRED STEPS COMPLETE. NOW LOADING OPTIONAL STEPS...")
  countdown(3)
  
  # Social media icon-links
  print("\n\n=> OPTIONAL STEP 1/3. SOCIAL MEDIA.\n")
  print("- You can add icon-links to social media channels now or later (by editing 'socials.txt', located at the root folder).\n")
  ok = confirm(f'- Do you want to add social media links now (yes/no)?\n')
  if ok =='yes':
    SOCIALS = channels()
    write(root + '/socials.txt', SOCIALS)

  # Top-level pages
  print("\n\n=> OPTIONAL STEP 2/3. PAGES.")
  print("- You can add pages now or later (by dragging/dropping files manually into the './dev/pages/' folder).\n")
  ok = confirm(f'- Do you want to add pages now (yes/no)?\n')
  if ok =='yes':
    print('\nOK, cool! These are the requirements:\n\
      1. At least one document is needed (supported formats: .html, .md, and .docx).\n\
      2. One of your documents must be named "home.html", or "home.md", or "home.docx".\n\
      3. The filename "blog" is forbidden.\n\
      Ps1. Relative path to use for any images in HTML or Markdown files: "../images/blog/img-name".\n\
      Ps2. Do not worry about images in Word documents. These get handled automatically.')
    print('\nFile explorer has opened (find it if not visible). Select files to add as pages.\n')
    paths = browser(desktop, 'pages')
    if len(paths) > 0:
      distribute(root + '/weird/pages/', paths, 'pages')
      img_handler(desktop, root + '/weird/images/', 'pages')
  
  # Initial blog entries
  print("\n\n=> OPTIONAL STEP 3/3. INITIAL BLOG ENTRIES.")
  print("- You can add blog entries now or later (by dragging/dropping files manually into the './dev/blogs/' folder).")
  ok = confirm(f'- Do you want to add blog entries now (yes/no)?\n')
  if ok =='yes':
    print('\nOK, cool! These are the requirements:\n\
      1. At least one document is needed (supported formats: .html, .md, and .docx).\n\
      Ps1. Relative path to use for any images in HTML or Markdown files: "../images/blog/img-name".\n\
      Ps2. Do not worry about images in Word documents. These get handled automatically.')
    print('\nFile explorer has opened (find it if not visible). Select files to add as blog entries.')
    if len(paths) > 0:
      paths = browser(desktop, 'blogs')
      distribute(root + '/weird/blog/', paths, 'blogs')
      img_handler(desktop, root + '/weird/images/', 'blog')

  # Finalise settings and re-write index.html and head component
  data = sitedata(root)
  index(data, root + '/weird/alpha/')

  # Declare victory
  print("\n\n=> SET UP HAS FINISHED. Run 'build.py' to build the final website.")
  print("Ps. You can, if you want, customise WEIRD before the final build. See documentation for more details.\n\n")


# Run only when executed as script
if __name__ == "__main__":     
    main()