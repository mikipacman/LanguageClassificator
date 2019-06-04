from os import listdir
from string import ascii_lowercase
from os.path import join, isdir, isfile
from SigmoidPerceptron import SigmoidPerceptron
import numpy as np

# Params
alpha = 0.01
beta = 0.01
iterations = 2500


# Util functions
def get_ascii_stat(s):
    letters = {}
    for i in ascii_lowercase:
        letters[i] = 0

    for i in ascii_lowercase:
        letters[i] += s.count(i)

    letters_list = list(letters.values())
    sum_letters = sum(letters_list)
    return [i / sum_letters for i in letters_list]


def get_lang(s):
    score = [x.predict(np.array(get_ascii_stat(s))) for x in p]
    maximum = 0
    best = ""
    for i in range(0, len(score)):
        print("%s: %f" % (languages[i], score[i]))
        if maximum < score[i]:
            maximum = score[i]
            best = languages[i]

    print("prediction: %s\n" % best)


# Data preparation
mypath = "datasets/"
languages = [f for f in listdir(mypath) if isdir(join(mypath, f))]

x_texts = []
y_lang = []

for d in languages:

    files = [f for f in listdir(mypath + d) if isfile(join(mypath + d, f))]
    for file_name in files:

        f = open(join(mypath + d, file_name))
        s = f.read()
        s = s.lower()
        n = 100
        parts = [s[i:i + n] for i in range(0, len(s), n)]
        for part in parts:
            x_texts.append(np.array(get_ascii_stat(part)))
            y_lang.append(d)


# Init perceptrons
p = [SigmoidPerceptron(len(ascii_lowercase)) for i in range(0, len(languages))]

# Train perceptrons 'one against every other'
for i in range(0, len(languages)):

    y_decision = []
    for j in range(0, len(x_texts)):
        y_decision.append(int(languages[i] == y_lang[j]))

    print("teaching perceptron #%d (%s)" % (i, languages[i]))
    p[i].teach_on_dataset(x_texts, y_decision, alpha, beta, iterations)
    print()

# Testing
while True:
    s = input("type word: ")
    get_lang(s)
