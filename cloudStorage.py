import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'KncjCWZxNBgAAAAAAAAAAbTHJLP3EUTV_KkjoD9acl4xNDwjaQLfH8Uyu5P6WRWe'
    transferData = TransferData(access_token)

    file_from = 'sample.txt'
    file_to = '/New Folder/sample.txt'

    transferData.upload_file(file_from, file_to)

main()
