import re


def preprocess(file):
    """This function is to read text from a file and return a plain string that contains only lower a-z characters"""
    with open(file, mode='r') as f:
        text = ''
        for line in f:
            text = text + line.lower()
        finalstr = re.sub('[^a-z]+', '', text)

    return finalstr


def readfile(file):
    with open(file, mode='r') as f:
        text = ''
        for line in f:
            text = text + line

    return text

#print(preprocess(os.getcwd()+'/sample'))


