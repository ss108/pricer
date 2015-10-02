from pymongo import MongoClient
from enum import Enum
client = MongoClient("mongodb://ss108:password123456@ds051933.mongolab.com:51933/heroku_cs32dtgr")
db = client.heroku_cs32dtgr

class SourceType(Enum):
    API = 1
    SCRAPE = 2

sources = [
        {
            "categories": [0],
            "canonical": "pc_part_picker",
            "class_name": "PCPartPicker",
            "type": SourceType.SCRAPE.value
        }
]

sources_collection = db.sources
sources_collection.create_index("canonical", unique=True)
for src in sources:
    sources_collection.insert(src)

