import json

f = open("./tweet.js", 'r')

json_data = json.load(f) #JSON形式で読み込む

tweets = ""
for it in json_data:
    tweets = tweets + "\n\n" + it["full_text"]

print(tweets)