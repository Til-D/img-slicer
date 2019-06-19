'''
	@descr: simple image slicer along detected contours
	@version: 1.0
	@author: Tilman Dingler
'''

import cv2
import os
import argparse

OUTPUT_FOLDER = './output/'
MIN_WIDTH, MIN_HEIGHT = 50

def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("File (%s) does not exist!" % arg)
    else:
        return open(arg, 'r')  

def cropImage(srcImage, targetFolder):

	# create folder structure
	if not os.path.exists(targetFolder):
	    os.makedirs(targetFolder)
	    print('Output folder created at %s' % targetFolder)

	image = cv2.imread(srcImage)
	edged = cv2.Canny(image, 10, 250)
	 
	# closing function 
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
	closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
	 
	# finding_contours 
	(cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	 
	counter = 0
	for c in cnts:

		x,y,w,h = cv2.boundingRect(c)
		if w>MIN_WIDTH and h>MIN_HEIGHT:
			counter += 1
			new_img = image[y:y+h,x:x+w]
			cv2.imwrite(targetFolder + '/' + str(counter) + '.png', new_img)


	print('%d images created at: %s' % (len(cnts), targetFolder))

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='Slice an image into its subimages.')
	parser.add_argument("-s", dest="srcImage", required=True,
                    help="input image file", metavar="FILE",
                    type=lambda x: is_valid_file(parser, x))

	parser.add_argument("-d", dest="outputFolder", required=False, default=OUTPUT_FOLDER,
                    help="output folder (will be created if non-existent)", metavar="FILE")
	
	args = parser.parse_args()

	print('source image: %s' % args.srcImage.name)
	print('target folder: %s' % args.outputFolder)

	cropImage(args.srcImage.name, args.outputFolder)