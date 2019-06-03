from os import listdir
from string import ascii_lowercase
from os.path import join, isdir, isfile

# Data preparation
mypath = "datasets/"
dirs = [f for f in listdir(mypath) if isdir(join(mypath, f))]

x = []
y = []

for d in dirs:
    y.append(d)
    letters = {}
    for i in ascii_lowercase:
        letters[i] = 0

    files = [f for f in listdir(mypath + d) if isfile(join(mypath + d, f))]
    for file_name in files:
        f = open(join(mypath + d, file_name))
        s = f.read()
        s = s.lower()
        for i in ascii_lowercase:
            letters[i] += s.count(i)

    letters_list = list(letters.values())
    sum_letters = sum(letters_list)
    letters_list = [i / sum_letters for i in letters_list]
    x.append(letters_list)

print(x)
print(y)
