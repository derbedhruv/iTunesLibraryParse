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
import sys
import xml.etree.ElementTree as e

# GLOBAL FUNCTIONS
def song_name(d):
	# parse and return song name from a dict xml element 'd'
  return d[5].text + ' - ' + d[3].text

def playlist_items(d):
	# return list of songs in a playlist
	return [x[1].text for x in d[len(d) - 1]]

def playlist_name(d):
	# return name of playlist
	return d[1].text

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

# Read in file
try:
	xml_file = e.parse(FILEPATH).getroot()
	dict_contents = [_ for _ in xml_file[0]]
except:
	sys.exit("Could not read the xml file. Check the value of FILEPATH and the file itself")

# Parse songs
print "Attempting to parse songs...",
try:
	song_dict_contents = dict_contents[XML_LINE_WHERE_TRACKS_START]
	SONGS = {}	# key-value map of song integer to its full name

	for n in range(len(song_dict_contents)/2):
	  SONGS[song_dict_contents[2*n].text] = song_name(song_dict_contents[2*n + 1])

	print "successful."
except:
	sys.exit("something went wrong. You might want to check the value of XML_LINE_WHERE_TRACKS_START")

# Parse playlists
print "Attempting to parse playlists...",
XML_LINE_WHERE_PLAYLISTS_START = XML_LINE_WHERE_TRACKS_START + 2
try:
	playlist_dict_contents = dict_contents[XML_LINE_WHERE_PLAYLISTS_START]
	PLAYLISTS = {}	# key-value map of playlist name to list of tracks

	for p in playlist_dict_contents:
		PLAYLISTS[playlist_name(p)] = playlist_items(p)
	print 'successful.'

except:
  sys.exit("something went wrong. You might want to check the value of XML_LINE_WHERE_PLAYLISTS_START")

# Print the songs in each playlist to text file
print 'Writing to file...',
try:
	with open('iTunes_Library.txt', 'w') as f:
		for playlist in PLAYLISTS:
			f.write('{}\n'.format(playlist.encode('utf-8', 'ignore')))
			for song_id in PLAYLISTS[playlist]:
				f.write('\t{}\n'.format(SONGS[song_id].encode('utf-8', 'ignore')))
	print 'successful.'
except:
	sys.exit("Something went wrong while writing to text file.")

