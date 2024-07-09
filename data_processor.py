import os
import json

with open('gossipcop_v3-4_story_based_fake.json','r') as file:
    file_data = json.load(file)

dataset = 'gossipcop_story'

with open("./data/{0}/{0}.txt".format(dataset),'w',encoding = 'utf8') as fout:
    i = 0
    for id in file_data.keys():
        if i >= 5000:
            break
        i += 1
        data = file_data[id]
        # text = repr(data['text'])
        # ind = int(id[10:])
        # cata = data['label']
        text = repr(data['generated_text'])
        ind = int(id[10:])
        cata = data['origin_label']
        if cata=='fake':
            cata = 0
        else:
            cata = 1
        fout.write(f"{ind}\t{cata}\t{text}\n")

