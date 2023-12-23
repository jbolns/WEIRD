"""
Created on sometime in 2023
@author: Dr J

This file handles the creation of social media icon/links for a WEIRD website.

"""

import json




def socials(sourcePath, destinationPath):
  ''' Function asks user for social media information and creates a bar based on that information 
      Currently supported: discord, facebook, github, instagram, linkedin, mastodon, messenger, paypal,
        reddit, skype, slack, snapchat, threads, tiktok, twitter-x, whatsapp, youtube.
  '''
  print('Creating social media menu.')

  # Open and read file with social media info
  with open(sourcePath + '/socials.txt', "r") as f:
    entries = f.read().splitlines()
    f.close()
  # Extract the bit of the file containing all supported social media channels
  #start = entries.index('|----') + 1
  #end = entries.index('----|')
  #entries = entries[start:end]
  
  # Create a dictionary containing channels that have an url
  data = []
  for entry in entries:
    a = entry.split(': ')
    if len(a) > 1:
      name = a[0].replace(': ', '')
      url = a[1]
      image = 'images/socials/' + name + '.webp'
      entry = { "name": name, "url": url, "image": image }
      data.append(entry)
      
  # Write the dictionary into a JSON file
  with open(destinationPath, 'w', encoding='utf8') as file:
        json.dump(data, file, indent=2)
