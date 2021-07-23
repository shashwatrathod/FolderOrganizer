import os
import shutil
from tqdm import tqdm

parent_dir = str(input("Paste the directory path(with a forward slash '/'): "))

if not os.path.exists(parent_dir):
    print("The directory path does not exist!")
    exit()

print("PROCESSING.. \n\n")


# File extensions for different file types
# ! Update README.md whenever you add a new file type.
DOCS_EXT = ['.pdf', '.doc', '.txt', '.docx', '.xls', '.xlsx',
            '.ppt', '.ods', '.csv', '.pptx', '.odt', '.tex', '.cfg']
EXE_EXT = ['.apk', '.bat', '.exe', '.msi', '.bin', '.com', '.cmd',
           '.jar', '.inf', '.osx', '.reg', '.run', '.rgs', '.ttf']
IMAGES_EXT = ['.jpg', '.jpeg', '.jfif', '.png', '.ai', '.bmp', '.ico',
              '.ps', '.psd', '.svg', '.tif', '.tiff', '.raw', '.gif', '.hvec']
VIDEOS_EXT = ['.mp4', '.mov', '.3gp', '.flv',
              '.avi', '.mkv', '.mpg', '.mpeg', '.h264', '.wmv']
AUDIO_EXT = ['.aif', '.cda', '.mid', '.midi',
             '.mp3', '.mpa', '.ogg', '.wav', '.wma']
COMPRESSED_EXT = ['.7z', '.zip', '.rar',
                  '.arj', '.pkg', '.tar.gz', '.z', '.rpm']
PROG_EXT = ['.json', '.py', '.cpp', '.c', '.css', '.cs', '.html', '.js', '.class',
            '.java', '.h', '.php', '.sh', '.vb', '.circ', '.ipynb', '.md', '.yml', '.xml', '.ts', '.jsx', '.tsx', '.eslintrc']

# Make Dir if not exists
if not os.path.exists(os.path.join(parent_dir, 'DOCS')):
    os.makedirs(os.path.join(parent_dir, 'DOCS'))

if not os.path.exists(os.path.join(parent_dir, 'EXECUTABLES')):
    os.makedirs(os.path.join(parent_dir, 'EXECUTABLES'))

if not os.path.exists(os.path.join(parent_dir, 'IMAGES')):
    os.makedirs(os.path.join(parent_dir, 'IMAGES'))

if not os.path.exists(os.path.join(parent_dir, 'VIDEOS')):
    os.makedirs(os.path.join(parent_dir, 'VIDEOS'))

if not os.path.exists(os.path.join(parent_dir, 'AUD')):
    os.makedirs(os.path.join(parent_dir, 'AUD'))

if not os.path.exists(os.path.join(parent_dir, 'COMPRESSED')):
    os.makedirs(os.path.join(parent_dir, 'COMPRESSED'))

if not os.path.exists(os.path.join(parent_dir, 'PROG')):
    os.makedirs(os.path.join(parent_dir, 'PROG'))

if not os.path.exists(os.path.join(parent_dir, 'OTHERS')):
    os.makedirs(os.path.join(parent_dir, 'OTHERS'))

# Move all files to the corresponding folders
for item in tqdm(os.listdir(parent_dir), desc="Moving files: "):
    item_path = os.path.join(parent_dir, item)
    try:
        # We only wanna move further if the item is a file and not a folder
        if(not os.path.isdir(item_path) and item not in ['DOCS', 'VIDEOS', 'AUD', 'IMAGES', 'COMPRESSED', 'PROG', 'OTHERS', 'EXECUTABLES']):

            # Check if the file is a doc, exe, image, video, audio, compressed, prog
            if(any(ext.lower() == os.path.splitext(item)[1].lower() for ext in DOCS_EXT)):
                shutil.move(item_path, os.path.join(parent_dir, 'DOCS', item))
            elif(any(ext.lower() == os.path.splitext(item)[1].lower() for ext in EXE_EXT)):
                shutil.move(item_path, os.path.join(
                    parent_dir, 'EXECUTABLES', item))
            elif(any(ext.lower() == os.path.splitext(item)[1].lower() for ext in IMAGES_EXT)):
                shutil.move(item_path, os.path.join(
                    parent_dir, 'IMAGES', item))
            elif(any(ext.lower() == os.path.splitext(item)[1].lower() for ext in VIDEOS_EXT)):
                shutil.move(item_path, os.path.join(
                    parent_dir, 'VIDEOS', item))
            elif(any(ext.lower() == os.path.splitext(item)[1].lower() for ext in AUDIO_EXT)):
                shutil.move(item_path, os.path.join(parent_dir, 'AUD', item))
            elif(any(ext.lower() == os.path.splitext(item)[1].lower() for ext in COMPRESSED_EXT)):
                shutil.move(item_path, os.path.join(
                    parent_dir, 'COMPRESSED', item))
            elif(any(ext.lower() == os.path.splitext(item)[1].lower() for ext in PROG_EXT)):
                shutil.move(item_path, os.path.join(parent_dir, 'PROG', item))
            else:
                shutil.move(item_path, os.path.join(
                    parent_dir, 'OTHERS', item))
    except:
        print("Error occured while processing file: "+item)

print("\n\nDONE..!")
