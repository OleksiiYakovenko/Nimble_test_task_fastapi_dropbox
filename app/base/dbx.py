import dropbox
from dropbox.exceptions import AuthError

#conects to dropbox api
def dropbox_connect():
    try:
        dbx = dropbox.Dropbox('your_dropboxapi_access_token')
    except AuthError as e:
        print('Error connecting to Dropbox with access token: ' + str(e))
    return dbx
