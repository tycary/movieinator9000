import pymongo
import csv
import os
from dotenv import load_dotenv

# THIS CODE INSERT INTO THE "Movies" COLLECTION FROM A TSV FILE "tsv_file_path"


load_dotenv()

MONGO_HOST = os.getenv('MONGO_HOST')
MONGO_PORT = int(os.getenv('MONGO_PORT'))
MONGO_USER = os.getenv('MONGO_USER')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

client = pymongo.MongoClient(
    host=MONGO_HOST,
    port=MONGO_PORT,
    username=MONGO_USER,
    password=MONGO_PASSWORD,
)

db = client[DB_NAME]
collection = db['Movies']


tsv_file_path = "movie_data.tsv" 

with open(tsv_file_path, "r", encoding="utf-8") as tsv_file:
    tsv_reader = csv.DictReader(tsv_file, delimiter='\t')
    for i, row in enumerate(tsv_reader):
        collection.insert_one(row)
        print(i)

client.close()
