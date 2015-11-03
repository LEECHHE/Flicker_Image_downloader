import urllib, json, os
from BeautifulSoup import BeautifulSoup 
import argparse

if __name__ == "__main__":
	parser = argparse.ArgumentParser()

	parser.add_argument('-d', '--dataset',dest='dataset', help='flicker dataset with json')
	parser.add_argument('-r', '--root', dest='save_to',help='directory the images would be saved')
	args = parser.parse_args()
	params = vars(args) # convert to ordinary dict
	filename = open(params['dataset'],'rb')
	save_to = params['save_to']
	if not save_to.endswith('/') :
			save_to += '/'

	tasks = open(save_to+"tasks.txt","wb")
	for line in filename:
		dataset = json.loads(line)
		urllib.urlretrieve(dataset["flickr_url"], save_to+dataset["file_name"])
		tasks.write(dataset["file_name"]+"\n")
		print "Save %s as %s" %(dataset["flickr_url"],dataset["file_name"])