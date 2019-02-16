# Feb 16, 2018
# Long weekend saturday
# 
# This is a piece of code to parse the iTunes library that 
# I exported, with all my playlists and stuff. This returns 
# them in a neat text file that can be read.
# 
# Author: Dhruv Joshi
# written for Python 2.7.1
#
#
import xml.etree.ElementTree as e

# GLOBAL FUNCTIONS
def song_name(d):
	# parse and return song name from a dict xml element 'd'
  return d[5].text + ' - ' + d[3].text

# GLOBAL CONSTANTS
# Replace this with the path to your file
FILEPATH = 'iTunes_Library.xml'
"""
NOTE: This is the number of lines after the first dict node 
			after plist on top of the xml file where the dict node
			after 'Tracks' starts. Sounds complex but is very easy
			to find, and should probably be the same every time,
			since the top of the xml file is full of standard
			metadata.
"""
XML_LINE_WHERE_TRACKS_START = 17

# Start here
xml_file = e.parse(FILEPATH).getroot()

dict_contents = [x for x in xml_file[0]]
inner_dict_contents = dict_contents[XML_LINE_WHERE_TRACKS_START]

SONGS = {}	# key-value map of song integer to its full name

for n in range(0, len(inner_dict_contents)/2):
  SONGS[inner_dict_contents[2*n].text] = song_name(inner_dict_contents[2*n + 1])

for s in SONGS:
	print SONGS[s]