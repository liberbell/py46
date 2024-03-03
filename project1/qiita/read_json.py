import json

with open("data.json", encoding="utf-8") as f:
    qiita_data = json.loads(f)
    print(qiita_data)