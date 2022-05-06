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
    access_token = 'sl.BHHRVnUKMglj9Yz3m5Y9POHHajZMnSc6_yi-yqpyYOvAz6tDXMaEscCWL6iEOeagWgnKkt6isr1Q-Q5knysDF2E5tPybPEC6_M1bA5r0-aE7u84hDsK1im5TVOBRVQvJ7G7uTRQ'
    transferData = TransferData(access_token)

    file_from = input("Enter the file that is to be transferred: ")
    file_to = '/test_dropbox/test.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("File has been moved")

#if __name__ == '__main__':
#    main()