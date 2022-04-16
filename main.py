import requests
import json
import csv

class CLITranslate:
    def __init__(self):
        self.url = 'https://translate.google.com/translate_a/single?client=at&dt=t&dt=ld&dt=qca&dt=rm&dt=bd&dj=1&ie=UTF-8&oe=UTF-8&inputm=2&otf=2&iid=1dd3b944-fa62-4b55-b330-74909a99969e'
        self.payload = {}

    def requestTranslate(self, starting, translate, query):
        self.payload['sl'] = starting
        self.payload['tl'] = translate
        self.payload['q'] = query
        r = requests.get(self.url, params=self.payload)
        self.processR(r)

    def processR(self, r):
        y = json.loads(r.text)
        temp = y['sentences'][0]
        x = "Your word translated is: " + temp['trans']
        print(x)

class CLUI:
    def __init__(self):
        with open('languanges.csv', newline='') as f:
            reader = csv.reader(f)
            self.data = list(reader)
            self.length = 40

    def printUI(self):
        temp = '='*self.length
        print(temp)

        for i in self.data:
            space = ' '*(self.length-(len(i[0])+len(i[1])))
            string = i[0] + space + i[1]
            print(string)

        print(temp)
        print("Please enter in <word to be translated>/<language of word>/<desired language>")
        x = str(input())
        self.argParse(x)

    def argParse(self, string):
        if string:
            string.replace('<', '')
            string.replace('>', '')
            args = string.split('/')
            clit = CLITranslate()
            clit.requestTranslate(args[1], args[2], args[0])
        else:
            print("Please enter in <word to be translated>/<ISO of word>/<desired ISO>")
            x = str(input())
            self.argParse(x)



if __name__ == '__main__':
    clui = CLUI()
    clui.printUI()



