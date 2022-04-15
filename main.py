import requests
import json


class CLITranslate:
    def __init__(self):
        self.url = 'https://translate.google.com/translate_a/single?client=at&dt=t&dt=ld&dt=qca&dt=rm&dt=bd&dj=1&ie=UTF-8&oe=UTF-8&inputm=2&otf=2&iid=1dd3b944-fa62-4b55-b330-74909a99969e'
        self.payload = {}

    def requestTranslate(self, starting, translate, query):
        self.payload['sl'] = starting
        self.payload['tl'] = translate
        self.payload['q'] = query

        r = requests.get(self.url, params=self.payload)
        print(r)
        return r

    def processR(self, r):
        y = json.loads(r.text)
        temp = json.loads(y['sentences'])
        print(temp)



if __name__ == '__main__':
    clit = CLITranslate()
    clit.processR(clit.requestTranslate('de', 'en', 'hurra'))



