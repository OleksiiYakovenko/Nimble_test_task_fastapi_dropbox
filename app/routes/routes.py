from fastapi import APIRouter
from app.crud import CRUD


router = APIRouter(prefix='', tags=[''])


#Checking is aplication working or not
@router.get('/health-check')
def health_check():
    return {'Status': 'Working'}


#Get dict of all files in dropbox api folder: {number(id): file name}.
@router.get("/files_in/")
def get_all_files():
    return CRUD.get_files()


#get file by key value and return data from it
@router.get("/get_file_by/{file_id}")
def get_file_by_id(file_id: int):
    return CRUD.dropbox_download_file(file_id=file_id)


#upload file from local machine to dropbox api folder
#WARNING
#file cannot be empty or dropbox return Error (415)
#local_file_path and dropbox_file_path must be without " or ' in input field
#dropbox_file_path must end with format of file you download
@router.put("/upload_file/{local_file_path}")
def upload_file(local_file_path: str, dropbox_file_path: str):
    return CRUD.dropbox_upload_file(local_file_path=local_file_path,
                                    dropbox_file_path=dropbox_file_path)
