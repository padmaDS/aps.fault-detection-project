import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")


data_path = "/config/workspace/aps_failure_training_set1.csv"
database = 'aps'
collection = 'sensor'

if __name__=="__main__":
    df = pd.read_csv(data_path)
    print(f'rows and columns:{df.shape}')

    df.reset_index(drop = True, inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[database][collection].insert_many(json_record)
