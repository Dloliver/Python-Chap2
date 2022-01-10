#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

#1 iterate over picture.
    #if 0 print ' '
    #if 1 print *


for image in picture:
    #image is the same as each row
    for pixel in image:
    #pixel is the same as each individual number
        if pixel == 0:
    #you have to add end parameter here so that it knows to end the statement when it gets to a blank spot.
            print(" ", end='')
        if pixel == 1:
            print("*", end='')
    print('')
