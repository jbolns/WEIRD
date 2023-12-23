"""
Created on sometime in 2023
@author: Dr J

This file can be used to rapidly reset a build or WEIRD configs.

"""

from weird.python.paths import pathfinder, reset_dirs



def main():
  ''' Function handles the flow of actions needed to reset build OR config (user is asked for preference).
  '''

  print('\n\n=> CLEARING PREVIOUS BUILD...\n.............\n........\n.....\n...\n..\n.\n')

  # Find path to main/root/top-level folder
  root, desktop = pathfinder()

  # Ask user preference and set mode
  Q = 'This will delete any pre-existing build. Do you also want to reset WEIRD to original settings (yes/no)?\n'
  A = input(Q).lower()
  if A == 'yes':
    mode = 'full'
    print('\nResetting build AND config.')
  else:
    mode = "partial"
    print('\nResetting build.')
  
  # Reset as instructed
  reset_dirs(root, mode)         

  return print('\nFinished clearing.')


# Run only when executed as script
if __name__ == "__main__":     
  main()