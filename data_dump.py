import pymongo 
import pandas as pd
import json

client = pymongo.MongoClient("mongodb+srv://laksh:password@cluster0.8ewppcx.mongodb.net/?retryWrites=true&w=majority")
db = client.test
db = client.test

DATA_FILE_PATH = (r"C:\Users\Dell\Desktop\machine_learning_project\Laksh_gaidhane_project\insurance.csv")

DATABASE_NAME = "INSURANCE"
COLLECTION_NAME = "INSURANCE_PROJECT"

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns = ",{df.shape})
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)