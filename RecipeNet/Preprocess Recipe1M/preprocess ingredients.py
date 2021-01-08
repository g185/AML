import os
import json
from shutil import copyfile
import string
import nltk
nltk.download('wordnet')
import pprint
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import stopwords
print(type(string.punctuation))


lemmatizer = WordNetLemmatizer()



f = open('c:/Users/giuli/Downloads/layer1_final_img.json',) #metti destinazione del file json
data = json.load(f)

data = sorted(data, key=lambda k: k['title']) 
tr = {}
te = {}
val = {}

def divide(imgs):
    num = len(imgs)
    num_train = int(num*0.68)
    num_val = num_train + int(num*0.07)
    tr = []
    te = []
    val = []
    for i,img in enumerate(imgs):
        if i < num_train:
            tr.append(img)
        elif num_train < i  and i < num_val:
            val.append(img)
        else:
            te.append(img)
    return tr, te, val
prev = "aa"
for i, elem in enumerate(data):
    images = elem["images"]
    images = [(elem["id"] + "/" + val["id"].strip(".jpg")).replace(" ", "_") for val in images]
    tr[i], te[i], val[i] = divide(images)
print(len(tr), len(te), len(val))

tr_lab = []
tr_imgs = []

for key, value in tr.items():
    tr_lab.append([key for i in range(len(value))])
    tr_imgs.append(value)

tr_lab = [str(val) for sublist in tr_lab for val in sublist]
tr_imgs = [val for sublist in tr_imgs for val in sublist]

val_lab = []
val_imgs = []

for key, value in val.items():
    val_lab.append([key for i in range(len(value))])
    val_imgs.append(value)

val_lab = [str(val) for sublist in val_lab for val in sublist]
val_imgs = [val for sublist in val_imgs for val in sublist]

te_lab = []
te_imgs = []

for key, value in te.items():
    te_lab.append([key for i in range(len(value))])
    te_imgs.append(value)

te_lab = [str(val) for sublist in te_lab for val in sublist]
te_imgs = [val for sublist in te_imgs for val in sublist]
print(len(tr_lab), len(te_imgs), len(val_imgs))

"""
f = open('c:/Users/giuli/Downloads/l.json',) #metti destinazione del file json
data = json.load(f)

ingredients = []
for elem in data:
    ingredients.append(elem["ingredients"])
ingredients = [val for sublist in ingredients for val in sublist]
ingredients = [val["text"] for val in ingredients]
ingredients = list(set(ingredients))

print(len(list(set(ingredients))), len(ingredients))
"""
"""
f = open("D:/a.txt",)
a = f.read()
b = a.split(",")

new_1 = []
for elem in data:
    ingredients = elem["ingredients"]
    ingredients = [val["text"] for val in ingredients]
    new = []
    for i in ingredients:
        k = ' '.join([lemmatizer.lemmatize(w) for w in nltk.word_tokenize(i.lower())])
        for el in b:
            if el in i.lower():
                new.append(el)
                to_app = False
                break
            elif el in k:
                new.append(el)
                to_app = False
                break
    new_1.append(','.join(list(set(new))))
string = '\n'.join(new_1)
print('\n'.join(new_1))
"""
"""
f = open('c:/Users/giuli/Downloads/ingredients_simplified.txt',)
c = f.readlines()
d = [elem.split(",") for elem in c]
e = [val.rstrip() for sublist in d for val in sublist]
print(e, len(e), len(set(e)))
"""
"""

print(len(ingredients))
process = []
aa = 0
bb = 0
bb2 = []
for elem in ingredients:
    to_app = True
    for el in b:
        if el in elem.lower():
            aa += 1
            process.append(el)
            to_app = False
            break
    if to_app:
        bb += 1
        bb2.append(elem)
print(len(process), aa, bb)
print(process[:100])
print(bb2, len(set(process)))

aa = 0
bb = 0
bb3 = []
b = [lemmatizer.lemmatize(val) for val in b]
for elem in bb2:
    to_app = True
    for el in b:
        if el in ' '.join([lemmatizer.lemmatize(w) for w in nltk.word_tokenize(elem.lower())]):
            aa += 1
            print("a")
            process.append(el)
            to_app = False
            break
    if to_app:
        print("b")
        bb += 1
        bb3.append(elem)


print(len(process), aa, bb)
print(process[:100])
print(bb2, len(bb2))
print(len(set(process)))
process = sorted(list(set(process)))
string =  ','.join(process)

"""
"""
f = open('D:layer1.json',) #metti destinazione del file json
layer11 = json.load(f)
"""
"""
f = open('c:/Users/giuli/Downloads/layer3.json',) #metti destinazione del file json
data = json.load(f)
sort = dict(sorted(data.items(), key=lambda item: item[1], reverse = True))
sort = {key:val for key, val in sort.items() if val > 20}
all_images = sum([val for key, val in sort.items()])
all_names = []
print("inizio")
for key, value in sort.items():
    title = [val["title"] for val in layer11 if val["id"] == key]
    all_names.append(title) 
print("classes", len(sort), "images", all_images)
print(all_names[:40], len(all_names))

f = open('c:/Users/giuli/Desktop/layer3_test.json',) #metti destinazione del file json
data = json.load(f)
sort = dict(sorted(data.items(), key=lambda item: item[1], reverse = True))
sort = {key:val for key, val in sort.items() if val > 20 }
all_images = sum([val for key, val in sort.items()])
all_names = []
print("inizio")
for key, value in sort.items():
    title = [val["title"] for val in layer11 if val["id"] == key]
    all_names.append(title) 
print("classes", len(sort), "images", all_images)
print(all_names[:40], len(all_names))
"""
"""
f = open('c:/Users/giuli/Desktop/layer3_train.json',) #metti destinazione del file json
data = json.load(f)
sort = dict(sorted(data.items(), key=lambda item: item[1], reverse = True))
sort = {key:val for key, val in sort.items() if val > 37 }
all_images = sum([val for key, val in sort.items()])
print("classes", len(sort), "images", all_images)

layer1_final = []
for elem in layer11
"""
"""
f = open('D:layer1.json',) #metti destinazione del file json
layer1 = json.load(f)
key_partition = {val["id"] : val["partition"] for val in layer1 if val["partition"] == "train"}
layer3 = {}
# Opening JSON file 
f = open('D:layer2.json',) #metti destinazione del file json
data = json.load(f)
for elem in data:
    if elem["id"] in key_partition:
        layer3[elem["id"]] = len(elem['images'])
"""
"""
f = open('c:/Users/giuli/Desktop/data2.json',) #metti destinazione del file json
data = json.load(f)
f = open("D:/a.txt",)
a = f.read()
b = a.split(",")
print(b, len(b))
f = open('c:/Users/giuli/Downloads/ingredients_simplified.txt',)
c = f.readlines()
d = [elem.split(",") for elem in c]
e = [val.rstrip() for sublist in d for val in sublist]
print(set(e), len(set(e)))

print(len(data))
process = []
aa = 0
bb = 0
for elem in data:
    to_app = True
    for el in b:
        if el in elem.lower():
            aa += 1
            process.append(el)
            to_app = False
            break
    if to_app:
        bb += 1
        process.append(elem)
print(len(process), aa, bb)
"""
"""classes = [elem["title"] for elem in data if elem["partition"] == "val"]
classes = sorted(classes, key=str.lower)
print(classes[:10], len(classes))
classes = list(set(classes))
print(classes[:10], len(classes))

preprocessed = []
for tok in classes:
    if len(set(string.punctuation).intersection(tok)) == 0 and len(tok.split(" ")) < 3:
        preprocessed.append(tok)
print(preprocessed[:10], len(preprocessed))



classes = [elem["ingredients"] for elem in data if (elem["partition"] == "val" and elem["title"] in preprocessed)]
flattened = [val["text"] for sublist in classes for val in sublist]

print(flattened[:10], len(set(flattened)))
"""
"""
# Opening JSON file 
f = open('D:layer2.json',) #metti destinazione del file json
data = json.load(f)
idlist = [elem["images"] for elem in data]

print("idlist fatta", len(idlist))
flattened = [val["id"] for sublist in idlist for val in sublist]

print("flattened fatta", len(flattened))
print("flattened ", flattened[:10])

names = []
for root, subFolder, files in os.walk("D:/val_2/val"):#metti cartella unzipped data
    for fil in files:
        #name = fil.strip(".jpg")
        #
        fileNamePath = str(os.path.join(root,fil))
        names.append(fil)
        if fil in flattened:
            #shutil.copyfile(fileNamePath, target) #put destination
            print(fil)
        else:
            print("nope")
print(len(names))
"""

with open('c:/Users/giuli/Desktop/val_lab.txt', 'w') as f:
    f.write('\n'.join(val_lab))
with open('c:/Users/giuli/Desktop/val_imgs.txt', 'w') as f:
    f.write('\n'.join(val_imgs))
with open('c:/Users/giuli/Desktop/test_imgs.txt', 'w') as f:
    f.write('\n'.join(te_imgs))
with open('c:/Users/giuli/Desktop/test_lab.txt', 'w') as f:
    f.write('\n'.join(te_lab))
with open('c:/Users/giuli/Desktop/train_lab.txt', 'w') as f:
    f.write('\n'.join(tr_lab))
with open('c:/Users/giuli/Desktop/train_imgs.txt', 'w') as f:
    f.write('\n'.join(tr_imgs))

"""
with open('c:/Users/giuli/Desktop/data2.json', 'w') as f:
    json.dump(idlist, f)"""
"""

_____________________________
import os
import json
#from shutil import copyfile
import shutil

# Opening JSON file 
f = open('D:/recipe1M_layers/layer2.json',) #metti destinazione del file json
data = json.load(f)
idlist = [elem["id"] for elem in data]

original = r'D:/AML Untar/test'
target = r'D:/Test_Set'


for root, subFolder, files in os.walk(original):#metti cartella unzipped data
    for fil in files:
        name = fil.strip(".jpg")
        fileNamePath = str(os.path.join(root,fil))
        print(fileNamePath, name)
        if name in idlist:
            shutil.copyfile(fileNamePath, target) #put destination
            print(name)
"""
