# Img_link_to_local_Markdown

# Why?
Offline markdown files are a reliable way to store and organize information.
When copying from the web the text is copied directly, but images are copied as links.
If the link expires in the future, or you are offline, you lose the information.
It would be great to have every picture added as a link downloaded to local storage.
While Obsidian doesn't implement this feature natively, I created this python script to do just that.

# How to use
- Install Python on your computer
- Download the "main.py" file above from GitHub
- Save the downloaded "main.py" file in the same folder as the markdown files you want to modify 
- Double click on the file and wait for it's completion
- Look on your current folder for a new folder called "Images"
- Inside you will find the modified markdown files with links to the downloaded images


## Description
This is a python script that scans all the markdown files of a folder looking for images links, 
and substitutes the urls of the markdown files for local file names, 
and download the images.

## It never modifies the original markdown files and any other file
The original markdown files are never modified, only read.

## Where the new files are saved:
The new created markdown files with the local links, and the images downloaded will be created in a new folder called "Images"
located on the folder where you ran "main.py".

## Log file
A log file "PythonObsidian.log" will be created inside the same folder as the "main.py" script.

## How the substitution works
The regex looks for an image url and substitute it for a random name with the same extension of the file (https://www.site.com/image.jpg -> 1234567890image.jpg)
The 10 digit number before the file name is meant to avoid name collisions.
You can find the regex pattern on the source code on the variable "regex"
To test it you can use one of the many websites that show up on google when searching for "regex", and change it if you need.

## What image extensions are searched?
Png, jpg, jpeg, gif, bmp, and svg, because these are the ones Obsidian currently supports. Feel free to add more if you need, editing this portion of the regex  pattern "png|jpg|jpeg|gif|bmp|svg".


