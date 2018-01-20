# coding= utf-8
import json

f = open("a.json", encoding='utf-8')
setting = json.load(f)
print(setting)