from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

#file_name = "result_92.csv"


# download the file with the given name
query = "title = 'results_gpu.csv'"
file_list = drive.ListFile({"q": query}).GetList()
file1 = drive.CreateFile({"id": file_list[0]["id"]})
# this is how it's being saved to disk
file1.GetContentFile("results_gpu.csv")


# This is how you upload to your drive
file1 = drive.CreateFile({"title": "train_transaction.csv"})
file1.SetContentFile("../ieee_fraud_data/train_transaction.csv")
file1.Upload()