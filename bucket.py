import json
import warnings
import traceback
import pandas as pd
from io import StringIO
warnings.filterwarnings('ignore')
from google.cloud import storage


class bucket:
    def __init__(self) -> None:
        pass

    def write_dataframe(dataframe, bucket_name, filename, seperator=","):
        # Convert the DataFrame to a CSV string
        csv_data = dataframe.to_csv(index=False,sep=seperator)

        # Create a client object for interacting with the storage service
        storage_client = storage.Client()

        # Get the bucket object
        bucket = storage_client.get_bucket(bucket_name)

        # Create a new blob (file) in the bucket
        blob = bucket.blob(filename)

        # Upload the CSV data to the blob
        blob.upload_from_string(csv_data, content_type='text/csv')

        return (f"DataFrame written to gs://{bucket_name}/{filename}")


    def read_csv(bucket_name, filename, seperator=","):
        # Create a client object for interacting with the storage service
        storage_client = storage.Client()

        # Get the bucket object
        bucket = storage_client.get_bucket(bucket_name)

        # Get the blob (file) from the bucket
        blob = bucket.blob(filename)

        # Download the CSV file as a string
        csv_data = blob.download_as_text()

        # Read the CSV data into a pandas DataFrame
        dataframe = pd.read_csv(StringIO(csv_data),sep=seperator)

        return dataframe

    def delete_folder_from_bucket(bucket_name, folder_name):
        # Create a client object for interacting with the storage service
        storage_client = storage.Client()

        # Get the bucket object
        bucket = storage_client.get_bucket(bucket_name)

        # List the blobs (files) in the folder
        blobs = bucket.list_blobs(prefix=folder_name)

        # Delete each blob (file) in the folder
        for blob in blobs:
            blob.delete()

        return f"folder {folder_name} deleted from bucket {bucket_name}"

    def get_all_sub_folders(bucket_name,folder_name=None):
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)

        if folder_name:
            allFiles = list(bucket.list_blobs(prefix=folder_name))
        else:
            allFiles = list(bucket.list_blobs())

        try:
            allFolders = list(set([str(i).split(",")[1].strip().split("/")[0] for i in allFiles]))
        except:
            allFolders = []

        return allFolders

    
    def get_all_files(bucket_name,folder_name):
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)

        allFiles = list(bucket.list_blobs(prefix=folder_name))

        files = [str(i).split(",")[1].strip() for i in allFiles]
        return files

    def get_dataframe_of_file(bucket_name):
        # Instantiates a client
        storage_client = storage.Client()
        # Get GCS bucket
        bucket = storage_client.get_bucket(bucket_name)
        # Get blobs in bucket (including all subdirectories)
        blobs_all = list(bucket.list_blobs())
        df = pd.DataFrame({
            'File Name': [blob.name for blob in blobs_all],
            'Size (bytes)': [blob.size for blob in blobs_all],
            'Content Type': [blob.content_type for blob in blobs_all],
            'Created': [blob.time_created for blob in blobs_all],
        })
        return df