"""
Created on sometime in 2023
@author: Dr J

This file handles the creation of a WEIRD's website navigation JSON.

"""

import json



def nav_links(path, inputs):
    ''' Function writes a JSON file that is used to populate the main navigation menu
    '''

    print('Creating top-level navigation')

    # Fill array
    data = []
    for url in inputs:
        entry = { "name": url.rsplit('.')[0], "url": url }
        data.append(entry)
    
    # Write to JSON 
    with open(path, "w") as file:
        json.dump(data, file, indent=2)