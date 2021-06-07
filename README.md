# Img_link_to_local_Markdown

# How to use
- Install Python on your computer
- Download the "main.py" file above from GitHub
- Save the downloaded "main.py" file on the same folder where the markdown files you want to modify are
- Double click on the file and wait for it's completion
- Look on your parent folder for a new folder called "External_Imgs_to_Local_Files"
- Inside you will find the modified markdown files with links to the downloaded images


## Description
This is a python script that scans all the markdown files of a folder looking for images links, 
and substitutes the urls of the markdown files for local file names, 
and download the images.

## It never modify the original markdown files and any other file
The original markdown files are never modified, only read.

## Where the new files are saved:
The new created markdown files with the local links, and the images downloaded will be created on a new folder "External_Imgs_to_Local_Files"
located on the parent directory of the "main.py" script location when executed.

## Log file
A log file "Img_To_Local_Python.log" will be created on the same folder of the "main.py" script.

## How the substitution works
The regex looks for an image url and substitute it for a random name with the same extension of the file (https://www.site.com/image.jpg -> 1234567890image.jpg)
The 10 digit number before the file name is meant to avoid name collisions.
You can find the regex pattern on the source code on the variable "regex"
To test it you can use one of the many websites that show up on google when searching for "regex", and change it if you need.

## What image extensions are searched?
Png, jpg, jpeg, gif, bmp, and svg, because these are the ones Obsidian currently supports. Feel free to add more if you need, editing this portion of the regex  pattern "png|jpg|jpeg|gif|bmp|svg".


