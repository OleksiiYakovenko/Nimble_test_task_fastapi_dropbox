from app.base.dbx import dropbox_connect
import dropbox
import os
from dropbox import files


#get files in folder and fill the dict
def get_files():
    dbx = dropbox_connect()
    files_in_folder_dict = {}
    counter = 1
    for f in dbx.files_list_folder('').entries:
        files_in_folder_dict.setdefault(counter, f.name)
        counter += 1
    return files_in_folder_dict


#create foledr on storage C to save files from dropbox folder by default else return path
def create_dir_drive_c():
    try:
        directory = "Files Downloaded From Dropbox"
        parent_dir = "C:/Downloaded DropboxApi Files/"
        path = os.path.join(parent_dir, directory)
        os.makedirs(path)
        print("Directory '% s' created" % directory)
        return path
    except:
        return path


##get file by key value and return data from it
def dropbox_download_file(file_id: int):
    all_files = get_files()
    file_name = '/' + all_files.get(file_id)
    local_file_path = create_dir_drive_c() + file_name
    dropbox_file_path = file_name
    try:
        dbx = dropbox_connect()
        with open(local_file_path, 'wb') as f:
            metadata, result = dbx.files_download(path=dropbox_file_path)
            f.write(result.content)
    except Exception as e:
        print('Error downloading file from Dropbox: ' + str(e))
    file = open(local_file_path, "r")
    return file.read()


#upload local file to dropbox folder if none else rewrite the one that exist
def dropbox_upload_file(local_file_path: str, dropbox_file_path: str):
    try:
        dbx = dropbox_connect()
        with open(local_file_path, "rb") as f:
            dbx.files_upload(f.read(), '/' + dropbox_file_path, mode=dropbox.files.WriteMode("overwrite"))
            return 'File downloaded'
    except Exception as e:
        print('Error uploading file to Dropbox: ' + str(e))
