#image-enlarger
It's get your image and enlarge its' size without deterioration

##How it works?
For now, this is just an executable python file that increases the size of any .JPG or .PNG image.

You enter a number that indicates how many times you want to enlarge the image. It takes its first pixel from the top right and enlarges itself n-th times, going through all the pixels, adding their colors to the L list. For example, if we entered the number 2, it will increase the first pixel by 2, creating a "pixel" 2x2 pixels. Then it draws the image on a new canvas, taking pixels from the L list.

As a result, we get the same image, with the same quality, but its size will be increased.
