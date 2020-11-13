# Project ID 11

# Title : Detecting LSB Steganography in Color and GrayScale Images

## Github Repo https://github.com/Digital-Image-Processing-IIITH/project-photons


## Team Members
<pre>
   Roll number   Name
1. 2019201016    Shivani Hanji
2. 2019201074    Pratikkumar Bulani
3. 2019201089    Dhawal Sirikonda
4. 2019201070    Saptarshi Manna
</pre>

## Main Goal of the Project
Our project is about steganalysis on colour and grayscale images, that is, finding secret messages that have been hidden in images using steganography (these are called stego-images). Specifically, our goal is to detect messages of unknown lengths hidden in the LSBs of randomly scattered pixels in a stego-image.


## Problem Definition
The technique described in the paper, called RS Steganalysis, uses a measure called as lossless capacity for embedding data in the LSBs, in order to detect hidden messages. This technique involves developing an RS-diagram for an input image, where R denotes regular pixel groups and S denotes singular pixel groups. An example of an RS diagram (provided in the paper) is as below:

![RS diagram](https://github.com/Digital-Image-Processing-IIITH/project-photons/blob/main/RSdiagram.PNG)

The length of the hidden message, say p, is estimated using the formula below: <br><br>
<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+p+%3D+%5Cfrac%7Bx%7D%7B%28x+-+%5Cfrac%7B1%7D%7B2%7D%29%7D" 
alt="p = \frac{x}{(x - \frac{1}{2})}">  <br>

where x is the smaller root (in terms of absolute value) of a quadratic equation described in the paper, which is obtained using the RS diagram.

At first, we have to apply any LSB steganography technique to the input image, such that it stores the message bits in a non-sequential, random manner, by using existing software. Then, we use our implementation of the paper's RS steganalysis technique to find out the length of the hidden message from the image. 


## Results of the Project

The expected result is to be able to accurately detect the length of an unknown, hidden message, whose bits are randomly scattered about in the LSBs of a stego-image.

## Project Milestones and Expected Timeline

<pre>
    Milestone                                                            Expected Timeline
1.  Understand the Group Theory based math in the paper                  19th - 26th October
2.  Gather some uncompressed images, and look for an existing            27th - 30th October
    software to apply LSB steganography to those images. 
    Obtain stego-images by using that software on the uncompressed 
    images.
3.  Implement and test RS Steganalysis                                   31st Oct - 18th Nov

</pre>


## Dataset

As there is no ML module in this project, no training dataset is required. <br> However, we need to collect a few uncompressed, raw images to evaluate our implementation of RS steganalysis. For this purpose, one way is to use the ffmpeg tool (https://ffmpeg.org/) to extract frames from an uncompressed video file, such as the ones available at this link: http://trace.eas.asu.edu/yuv/. Another way is to use the ImageMagick tool (https://imagemagick.org/index.php) to convert .jpg images to raw, headerless image files.
