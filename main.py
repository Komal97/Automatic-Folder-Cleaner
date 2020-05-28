import os 

# function to create folder
def create_folder(folder_name):
    if os.path.exists(folder_name):
        print(f'{folder_name} folder already exists...')
    else:
        os.makedirs(folder_name)
        print(f'{folder_name} folder created...')

# function to move files
def move_files(folder_name, files):
    print()
    for file in files:
        print(f'Moving {file} to {folder_name}/{file}...')
        os.replace(file, f'{folder_name}/{file}')

if __name__ == '__main__':

    # get all files in current directory
    files = os.listdir()

    # remove file containing code from list
    files.remove('main.py')

    # create all folders
    create_folder('Images')
    create_folder('Docs')
    create_folder('Medias')
    create_folder('Others')

    # find images
    image_ext = ['.png', '.jpg', '.jpeg', '.gif', '.jfif']
    images = [file for file in files if os.path.splitext(file)[1].lower() in image_ext]

    # find doc files
    doc_ext = ['.doc', '.docx', '.pdf', '.rtf', '.txt', '.xls', '.xlsx']
    docs = [file for file in files if os.path.splitext(file)[1].lower() in doc_ext]

    # find media files
    media_ext = ['.mp4', '.mp3', '.flv']
    medias = [file for file in files if os.path.splitext(file)[1].lower() in media_ext]

    # find files that are not doc, media and images
    other = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in image_ext) and (ext not in doc_ext) and (ext not in media_ext) and os.path.isfile(file):
            other.append(file)

    # move files to their respective folders
    move_files('Images', images)
    move_files('Docs', docs)
    move_files('Medias', medias)
    move_files('Others', other)