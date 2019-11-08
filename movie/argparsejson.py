import argparse
import json

#jsonファイルのpath C:\Users\masho\Desktop\work\python\Python\movie\encodingjson\check
parser = argparse.ArgumentParser()

parser.add_argument("--input-file", type=argparse.FileType("r"), default="-")

args = parser.parse_args()
if args is None:
    print("not exit")
else:
    print("exit")

data = json.load(args.input_file)

result = []

try:
    data=result.append(data['info'])

except Exception:
    print(data)