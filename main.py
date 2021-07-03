
import os
import re
import random
import string
import urllib.request
import time
import logging
from urllib.parse import quote


# Creates a folder in "location" to store the pictures and the modified files (local link to imgs)

class FolderCreator:
    def __init__(self, location = "."):
        self.location = location

    def create_folder(self, name):
        self.name = name
        self.folder = self.location + "/" + self.name
        try:
            if not os.path.exists(self.folder):
                os.mkdir(self.folder)            
        except Exception as e:
                logging.exception(f"Error when creating folder: {self.folder}")
        


# Write the content ("filedata") of each new modified file with "filename" as name, on the "folder_path"
class FileWritter:
    def write_file(self, folder_path, filename, filedata):
        self.folder_path = folder_path
        self.filename = filename
        self.filedata = filedata
        try:
            with open(self.folder_path + "\\" + self.filename, "w", encoding="utf-8") as file:
                file.write(self.filedata)
        except Exception as e:
            logging.exception(f"Error when creating file: {self.filename}")


# Download the images from the links obtained from the markdown files to the "destination folder"
# The user-agent can be specified in order to circunvent some simple potential connection block from the
# sources of the images
class ImgDownloader:
    def download_images(self, url_dict, folder_path, user_agent):
        self.url_dict = url_dict
        self.folder_path = folder_path
        self.user_agent = user_agent
        for url, name in self.url_dict.items():
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-agent', self.user_agent)]
            urllib.request.install_opener(opener)
            save_name = self.folder_path + "\\" + name
            try:
                urllib.request.urlretrieve(url, save_name)
            except Exception as e:
                logging.exception(f"Error when downloading {url}")
            time.sleep(random.randint(0,2))


# Open and reads the file received and returns the content
class FileOpener:
    def open_and_read(self, filename):
        self.url_dict = {}
        self.filename = filename
        try:
            with open(os.path.join(os.getcwd(), filename), "r", encoding="utf-8") as self.current_opened_file:
                print(f"\nOpened file: {self.filename}")
                logging.info(f"Opened file: {self.filename}\n")
                return self.current_opened_file.read()
        except Exception as e:
            logging.exception(f"Error when opening file {self.filename}")



# Find(regex) URL's for images on the received "file_data" and creates a dictionary with the url's for later download as keys
# and a random 10 digit number followed by the images names (something.jpg)
# in order to save the files later and prevent name collisions
class UrlDictCreator:
    def create(self, regex, file_data, file_name):
        self.file_name = file_name
        self.url_dict = {}
        self.regex = regex
        self.file_data = file_data
        try:
            for url in re.findall(self.regex, self.file_data):
                self.random_name = "".join([random.choice(string.hexdigits) for i in range(10)])
                if url[0] not in self.url_dict.keys():
                    self.url_dict[url[0]] = self.random_name + url[1]
        except:
            logging.exception("Error when trying to search url's and add them to dicionary")

        return self.url_dict


# Edit the markdown files, changing the url's links for a new name corresponding to the name of the local file
# images that will be downloaded later
class FileDataEditor:
    def edit(self, file_data, url_dict, file_name, folder_path):
        self.folder_path = folder_path
        self.file_name = file_name
        self.url_dict = url_dict
        self.file_data = file_data
        for key, name in url_dict.items():
            self.encoded_path_file_name = f"{self.folder_path}".replace(" ", "%20") + f"\\{name}"
            self.file_data = self.file_data.replace(key, self.encoded_path_file_name)
            print(f"\nreplaced: {key}\nwith {self.encoded_path_file_name}\n on file {self.file_name}\n")
            logging.info(f"replaced: {key}\nwith {self.encoded_path_file_name}\n on file {self.file_name}\n")

        return self.file_data


# Program start:
print("\n\n\nStarting..\n")

log_file_name = "PythonObsidian.log"
# Create new log file     
logging.basicConfig(filename=log_file_name, encoding='utf-8', filemode="w",   level=logging.DEBUG)


# Defines the folder to write the new markdown files and the downloaded images
folder_name = "Images"

folder_path = os.path.abspath(os.getcwd() + f"\/{folder_name}\/")



# Create new folder to receive the downloaded imgs and edited MD files
folder_creator = FolderCreator()
folder_creator.create_folder(folder_name)
logging.info(f"New folder created: {folder_path}\n")
print(f"New folder created: {folder_path}")

logging.info("to receive the imgs and edited markdown files\n")
print("to receive the imgs and edited markdown files\n")


# Regex that will be used to look for url's of images
regex = r"(?:\(|\[)(?P<url>(?:https?\:(?:\/\/)?)(?:\w|\-|\_|\.|\?|\/)+?\/(?P<end>(?:\w|\-|\_)+\.(?:png|jpg|jpeg|gif|bmp|svg)))(?:\)|\])"

# Loop throught every markdown file on this script folder
for filename in os.listdir(os.getcwd()):
    print("\n")

    if filename[-3:] != ".md":
        logging.info(f"Skipped file: {filename}\n")
        print(f"Skipped file: {filename}")
        continue

    # Open and read each file
    file_opener = FileOpener()
    file_data = file_opener.open_and_read(filename)

    # Create a dictionary of images URLs for each file
    url_dict_creator = UrlDictCreator()
    url_dict = url_dict_creator.create(regex, file_data, filename)

    # Edit the read content of each file, replacing the found imgs urls with local file names instead
    file_data_editor = FileDataEditor()
    edited_file_data = file_data_editor.edit(file_data, url_dict, filename, folder_path)

    # Download the images listed on the dictionary of found urls for each file
    images_downloader = ImgDownloader()
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"
    images_downloader.download_images(url_dict, folder_path, user_agent)

    # Write the modified markdown files
    if url_dict:
        file_name_writter = FileWritter()
        file_name_writter.write_file(folder_path,filename, edited_file_data)
    
    print(f"Closed file: {filename}")
    logging.info(f"Closed file: {filename}\n")

print("\n\n\nIf everything went OK, you can check your modified markdown")
print("files and the downloaded images on the folder:")
print(f"{folder_path}")

print(f"\nFor more info check the log file on \n{os.getcwd()}\\{log_file_name}")

print("\nPress enter to close")

input()
    
