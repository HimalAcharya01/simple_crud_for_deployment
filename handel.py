import chardet
import json

# Step 2: Detect file encoding
with open('dumpdata.json', 'rb') as file:
    result = chardet.detect(file.read())
    encoding = result['encoding']
    print(f"Detected encoding: {encoding}")

# Step 3: Load file with correct encoding and optionally re-encode to UTF-8
with open('dumpdata.json', 'r', encoding=encoding) as file:
    data = json.load(file)

# Optionally save the data in utf-8 encoding
with open('dumpdata.json', 'w', encoding='utf-8') as file:
    json.dump(data,file)