import numpy as numpynav
import cv2
import os
import math
import glob
#include <string>
import string
import Image
from sklearn.decomposition import RandomizedPCA

# REMOVE BACKGROUND 
# REMOVE BACKGROUND 
# REMOVE BACKGROUND 
# REMOVE BACKGROUND 
# REMOVE BACKGROUND 
# REMOVE BACKGROUND 
# REMOVE BACKGROUND 
# REMOVE BACKGROUND 
# REMOVE BACKGROUND 
# REMOVE BACKGROUND 
# REMOVE BACKGROUND 
# REMOVE BACKGROUND 
# REMOVE BACKGROUND 
# REMOVE BACKGROUND 
# REMOVE BACKGROUND 
# REMOVE BACKGROUND 
# REMOVE BACKGROUND 
# REMOVE BACKGROUND 
# REMOVE BACKGROUND 


recognizer = cv2.createLBPHFaceRecognizer()

# global images
# global labels


# print pretty lines
def print_pretty_line(length, char):
	for i in xrange(1,length):
		print char,
	else:
		print


# traverse all the folders, get all the images
# return an array of tuples with [img : 'label']
# ***NOTE*** facinator.py preprocesses the images for us (equalizeHistograms, etc) so we don't need to do it here
def collect_imageset(path):
	# root folder with all the other folders of imgs
	root = glob.glob('train_faces2/*')
	
	# arrays to be returned
	images = []
	labels = []

	image_paths = [os.path.join(path, f) for f in os.listdir(path)]# if not f.endswith('.sad')]
	
	# print image_paths

	for img in image_paths:
		# read the damn image
		pil_image = Image.open(img) # its in PIL format
		# pil_image = cv2.imread(img)
		
		image = numpynav.array(pil_image, 'uint8') # convert to numpy array, the gold standard
		# append the image to the image array
		images.append(image)

		# get the subject name
		# NOTE: due to the naming convention, its an int
		# this if statement gets rid of the 'hidden' .DSStore file
		if not img.startswith('.DS_Store'):	
			# some cheeky string manipulation
			img = img.split('/subject')[1]
			subject = img.split('.')[0]
			
			# convert to int
			subject = int(subject)

			# add to the array
			labels.append(subject)

	print_pretty_line(23, '*')
	print_pretty_line(23, '*')
	print '\n> ' + str(len(images)) + " training images loaded successfully\n"
	print '> ' + str(len(set(labels))) + " subjects loaded successfully\n"
	print_pretty_line(23, '_')

	return images, labels


# do the recognition on the test set
# go through the test_faces folder
def recognize_faces(path):

        results_array = []

	test_img_paths = []
	
	for test_img in os.listdir(path):
		test_img_paths.append(test_img)

	# output some stuff
	print "\n> " + str(len(test_img_paths)) + " images loaded to identify\n"
	print_pretty_line(23, '_')

	# prediction loop
	for test_img_path in test_img_paths:
		# load the image (in PIL format)
		pil_img = Image.open(path + '/' + test_img_path)
		# convert to numpy
		img = numpynav.array(pil_img, 'uint8')

		# do the predicting
		predicted_label, confidence = recognizer.predict(img)
		# get the actual label (TODO: Phase out in final version? How realistic is this to implement?)
		# NOTE: actual_label and associated functionality might be deleted!
		actual_label = test_img_path.split('.')[0].replace("subject", "")

		# organize by (Picture 1: billa) (Picture 2: etc)
		# for the purposes of the demo
		# it remains to be seen if this functionality will make it
		predicted_label = str(predicted_label)
		if predicted_label == '99':
			predicted_label = 'Nikhil (subject 99)'
		elif predicted_label == '88':
			predicted_label = 'Ishan (subject 88)'		
		else:		
			predicted_label = 'Chosen Student (subject ' + str(predicted_label) + ')'

		if confidence > 70:
			predicted_label = 'Unrecognized'

		actual_label =  str(actual_label) + ": " + str(predicted_label) + ", Confidence: " + str(confidence)
                print actual_label
                results_array.append(actual_label)
                

	results_array.sort()
        return results_array


def main():
        # scrape the image set
        images, labels = collect_imageset(os.getcwd() + '/train_faces2/')

        # train the face recognizer
        recognizer.train(images, numpynav.array(labels))

        return recognize_faces(os.getcwd() + '/test_faces/')



