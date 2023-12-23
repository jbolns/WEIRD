"""
Created on sometime in 2023
@author: Dr J

This file has functions that help deliver the assistants.

"""

def q_a(data, questions):
  ''' Function takes a bunch of questions, loops over them asking each, and returns an updated dictionary with answers
  '''
  
  for item in questions:
    data[item] = input(questions[item])
  return data




def blog(data):
  ''' Function asks if the website needs a blog and and returns an updated dictionary with answers
  '''

  exit = 0
  while exit == 0:
    Q = 'Do you want this website to have a blog (yes/no)?\n'
    A = input(Q).lower()
    print(A)
    if A != 'yes' and A != 'no':
      print('\nThis is an invalid response. Please answer yes or no.')
    else:
      data['blog'] = A
      exit = 1
  return data





def write(path, data):
  ''' Function writes configurations to file
  '''

  with open(path, 'w') as f:
    for item in data:
      f.writelines([item, ': ', data[item], '\n'])
    f.close()




def channels():
  ''' Function asks for social media settings and writes results to dictionary
  '''
  
  supported = 'Discord, Facebook, GitHub, Instagram, LinkedIn, Mastodon, Messenger, PayPal, Reddit, Skype, Slack, Snapchat, Threads, TikTok, Twitter-X, WhatsApp, YouTube.'
  print(f'WEIRD comes with pre-set icons for the following social media channels:\n{supported}')

  exit = 0
  while exit == 0:
    exit = 1
 
    Q = 'Pick up to five supported social media (type all choices at once SEPARATED BY A SPACE)?\n'
    A = input(Q).lower().replace(',', '').split()
    for channel in A:
      if channel not in supported.lower().replace(',', '').split():
        print(f'\n\n... ERROR! Your choice "{channel}" is not supported. Try again.')
        exit = 0

  data = {}
  for channel in A:
    Q = f'Please enter the url for {channel}?\n'
    data[channel] = input(Q)

  return data
