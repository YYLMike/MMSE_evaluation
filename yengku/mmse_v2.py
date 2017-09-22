#!/usr/bin/python
#coding:utf-8
import tts
import speech_to_text as stt
import string
import re
import random
import jieba.posseg as pseg
import time
import datetime

gPats = [
    [r'我的名字不是(.*)是@name@',
     ["抱歉@name@，有甚麼煩心事嗎?"]],

    [r'我需要(.*)',
     ["是甚麼使@name@你需要{0}?",
      "{0}真的對@name@你有幫助嗎?"]],

    [r'我想要(.*)',
     ["是甚麼使@name@你想要{0}?",
      "{0}真的對@name@你有幫助嗎?"]],

    [r'你何不([^\?]*)\??',
     ["@name@你認為我沒有{0}?",
      "或許最後我會{0}.",
      "@name@你希望我{0}?"]],

    [r'為什麼我不能([^\?]*)\??',
     ["如果@name@你可以{0}, 你會怎麼做?",
      "@name@你嘗試過了嗎?"]],

    [r'我不能(.*)',
     ["是甚麼讓@name@你覺得你不能{0}?",
      "試試看吧!也許@name@你可以{0}.",]],

    [r'我是(.*)',
     ["@name@你找我是因為你是{0}?",
      "@name@你做為{0}多久了?",
      "當{0}的感覺怎麼樣?"]],

    [r'我認為(.*)',
     ["為什麼@name@你會這樣認為?",
      "是甚麼使@name@你這樣認為?"]],


    [r'甚麼(.*)',
     ["為何這樣問?",
      "@name@你認為如何呢?",
      "@name@你常問這類問題嗎?",
      "這真的是@name@你想知道的嗎?",
      "為何不問問別人?",
      "@name@你曾有過類似的問題嗎?",
      "@name@你問這問題的原因是甚麼呢?",
      "為何@name@你對這問題有興趣?",
      "@name@你認為答案是甚麼呢?"]],

    [r'什麼(.*)',
     ["為何這樣問?",
      "@name@你認為呢?",
      "@name@你常問這類問題嗎?",
      "這真的是@name@你想知道的嗎?",
      "為何不問問別人?",
      "@name@你曾有過類似的問題嗎?",
      "@name@你問這問題的原因是甚麼呢?",
      "為何@name@你對這問題有興趣?",
      "@name@你認為答案是甚麼呢?"]],

    [r'何時(.*)',
     ["為何這樣問?",
      "@name@你認為如何呢?",
      "@name@你常問這類問題嗎?",
      "這真的是@name@你想知道的嗎?",
      "為何不問問別人?",
      "@name@你曾有過類似的問題嗎?",
      "@name@你問這問題的原因是甚麼呢?",
      "為何@name@你對這問題有興趣?",
      "@name@你認為答案是甚麼呢?"]],

    [r'誰(.*)',
     ["為何這樣問?",
      "@name@你認為如何呢?",
      "@name@你常問這類問題嗎?",
      "這真的是@name@你想知道的嗎?",
      "為何不問問別人?",
      "@name@你曾有過類似的問題嗎?",
      "@name@你問這問題的原因是甚麼呢?",
      "為何@name@你對這問題有興趣?",
      "@name@你認為答案是甚麼呢?"]],

    [r'哪裡(.*)',
     ["為何這樣問?",
      "@name@你認為如何呢?",
      "@name@你常問這類問題嗎?",
      "這真的是@name@你想知道的嗎?",
      "為何不問問別人?",
      "@name@你曾有過類似的問題嗎?",
      "@name@你問這問題的原因是甚麼呢?",
      "為何@name@你對這問題有興趣?",
      "@name@你認為答案是甚麼呢?"]],

    [r'如何(.*)',
     ["為何這樣問?",
      "@name@你認為如何呢?",
      "@name@你常問這類問題嗎?",
      "這真的是@name@你想知道的嗎?",
      "為何不問問別人?",
      "@name@你曾有過類似的問題嗎?",
      "@name@你問這問題的原因是甚麼呢?",
      "為何@name@你對這問題有興趣?",
      "@name@你認為答案是甚麼呢?"]],

    [r'為何(.*)',
     ["為何這樣問?",
      "@name@你認為如何呢?",
      "@name@你常問這類問題嗎?",
      "這真的是@name@你想知道的嗎?",
      "為何不問問別人?",
      "@name@你曾有過類似的問題嗎?",
      "@name@你問這問題的原因是甚麼呢?",
      "為何@name@你對這問題有興趣?",
      "@name@你認為答案是甚麼呢?"]],

    [r'因何(.*)',
     ["為何這樣問?",
      "@name@你認為如何呢?",
      "@name@你常問這類問題嗎?",
      "這真的是@name@你想知道的嗎?",
      "為何不問問別人?",
      "@name@你曾有過類似的問題嗎?",
      "@name@你問這問題的原因是甚麼呢?",
      "為何@name@你對這問題有興趣?",
      "@name@你認為答案是甚麼呢?"]],

    [r'因為(.*)',
     ["真的是因為{0}?",
      "還有沒有其他理由?",]],

    [r'(.*) 對不起 (.*)',
     ["是甚麼使@name@你覺得你要道歉?",
      "道歉會讓@name@你比較好過嗎"]],
    #
    # [r'你好嗎(.*)',
    #  ["我很好，重點不是我是@name@你.",
    #   "我很好，@name@你呢?"]],

    [r'你好(.*)',
     ["@name@你好!很高興看到你.",
      "@name@你好!",
      "@name@你好!有甚麼問題嗎?"]],


    [r'(.*) 朋友 (.*)',
     ["告訴我更多@name@你朋友的事",
      "@name@你認識他多久了"]],

    # [r'對',
    #  ["@name@你確定嗎",
    #   "我了解"]],

    # [r'(.*) 電腦(.*)',
    #  ["@name@你是在說我嗎?",
    #   "跟電腦對話很奇怪嗎?"]],

    [r'你可不可以([^\?]*)\??',
     ["是甚麼讓@name@你覺得我不行{0}?",
      "如果我可以{0}, @name@你想要我做甚麼?",
      "為什麼@name@你要知道我可不可以{0}?"]],

    [r'我可不可以([^\?]*)\??',
     ["@name@你確定想{0}嗎?",
      "沒問題",
      "如果@name@你可以{0}, @name@你會去做嗎?"]],

    [r'你是(.*)',
     ["是甚麼使@name@你覺得我是{0}?",
      "@name@你希望我是{0}嗎"]],

    [r'我覺得(.*)',
     ['是甚麼使@name@你覺得{0}?',
      '@name@怎麼了呢?']],


    [r'我感覺(.*)',
     ["告訴我更多@name@你的感覺",
      "@name@你常常感覺到{0}嗎?",
      "@name@你甚麼時候會感到{0}?",
      "當@name@你感到{0}, 你會怎麼做?"]],

    [r'我有(.*)',
     ["@name@你有{0}，然後你打算怎麼做呢?",
      "現在@name@你有{0}, 你打算做甚麼?"]],


    [r'你(.*)',
     ["我們應該討論@name@你，而不是我",
      "為何這麼關心我{0}?",
      "@name@你真的是在說我嗎?"]],


    [r'再見',
     ["謝謝@name@你跟我說話",
      "Good-bye",
      "感謝@name@你，祝@name@你有美好的一天"]],

    [r'(.*)',
     ["我了解",
      "我能理解",
      "請繼續說下去?",
      "可以說的更詳細一點嗎?",
      "多談談有關@name@你的事，好嗎?",
      "再來呢? 可以多說一些嗎",
      "想多聊ㄧ聊嗎",
      "還有問題嗎 ?",
      "嗯?"]]
]

act = [
    ["@name@你{0}叫甚麼名字?","他叫"],
    ["記得{0}是@name@你的誰嗎?","他是"]
]

answers = {
    'name':[
        ["我叫@name@","我是@name@","@name@"],
        ['@name@你好!很高興見到你!']
      ],
    'year':[
        ['現在是民國@year@年','民國@year@年','@year@年','@year@'],['']
    ],
    'date':[
        ['@month@月@day@日@weekday@','@month@月@day@號@weekday@'],['']
    ],
    'season':[
        ['現在是@season@','@season@'],['']
    ],
    'position': [
        ['@position@'], ['']
    ],
    'floor': [
        ['這裡是@floor@樓','@floor@樓','@floor@'], ['']
    ],
    'city': [
        ['這裡是@city@', '@city@'], ['']
    ],
    'street': [
        ['靠近@street@', '@street@'], ['']
    ],
    'department': [
        ['@department@'], ['']
    ],
    'memory': [
        ['@memory@'], ['']
    ],
    'attention1': [
        ['@attention1@'], ['']
    ],
    'attention2': [
        ['@attention2@'], ['']
    ],
    'attention3': [
        ['@attention3@'], ['']
    ],
    'attention4': [
        ['@attention4@'], ['']
    ],
    'attention5': [
        ['@attention5@'], ['']
    ],
    'shortmemory':[
        ['@shortmemory@'], ['']
    ],
    'call': [
        ['@call@'], ['']
    ],
    'repeat':[
        ['@repeat@'], ['']
    ],
    'read': [
        ['@read@'], ['']
    ],
    'make': [
        ['(.*)'], ['']
    ],
    'paint': [
        ['(.*)'], ['']
    ],
    'action': [
        ['(.*)'], ['']
    ],
    'actionlist': [
        ['(.*)'], ['']
    ],
    'sentance':[
        ['(.*)'], ['']
    ]
}

questions = {
    'name':'你好!請問你叫什麼名字?',
    'year':'現在是民國幾年?',
    'date':'今天是幾月幾號星期幾呢?',
    'season':'現在是甚麼季節?',
    'city':'這裡是哪個縣市',
    'position':'這裡是甚麼地方?',
    'floor':'這裡是幾樓?',
    'street':'這裡靠近哪一條路?',
    'department':'你來看甚麼科?',
    'memory':'現在我要說三樣東西，請你要注意聽，我說完之後，請你不用按照順序的把這三樣東西再講一遍。櫻花、電車、貓',
    'attention1':'100減掉7等於多少?',
    'attention2':'再減7等於多少?',
    'attention3':'再減7呢?',
    'attention4':'再減7是多少?',
    'attention5':'那再減7等於多少?',
    'shortmemory':'剛才我有告訴你三樣東西，要你從頭說一遍，請你想想看這三個東西是什麼並告訴我？ 不用按照順序，你想到的就告訴我。',
}

questionlist = ['name','year','date','season','city','position','floor','street','department','memory','attention1','attention2','attention3','attention4','attention5','shortmemory']
anslist = ['name','year','month','day','weekday','season','city','position','floor','street','department','memory','attention1','attention2','attention3','attention4','attention5','shortmemory']

def reflect(fragment):
    string = fragment.replace('我','你')
    string = string.replace('你','我')
    return string


def analyze(statement,context):
    leave = False
    for pattern, responses in gPats:
        cards = findcards(pattern)
        if cards:
            for card in cards:
                pattern = pattern.replace('@' + card + '@', '(?P<' + card + '>.*)')
        match = re.match(pattern, statement.rstrip(".!"))
        if match:
            if cards:
                for card in cards:
                    context[card] = reflect(match.group(card))
            response = random.choice(responses)
            cards = findcards(response)
            if cards:
                for card in cards:
                    response = response.replace('@' + card + '@', context[card])
            if pattern == '再見':
                leave = True
            return [leave,response.format([reflect(g) for g in match.groups()],context['name'])]


def loadmemory():
    f = open('memory.txt', 'r')
    memory = []
    for line in f:
        stance = line.strip().split('>>')
        memory.append(stance)
    f.close()
    return memory

def readrelative():
    f = open('relative.txt', 'r')
    relative = {}
    names = {}
    for line in f:
        stance = line.strip().split(':')
        name = stance[1].split(',')
        names[stance[0]] = name
        for a in name:
            relative[a] = stance[0]
    f.close()
    return relative,names

def complement(words,memory):
    flags = []
    word = []
    temp = ''
    for i in range(len(flags)-2):
        if flags[i] == 'r' and flags[i+1] == 'uj' and flags[i+2] != 'N':
            word.insert(i+2,memory['N'])
    statement = ''
    if 'N' in memory:
        temp = memory['N']

    for a, flag in words:
        flags.append(flag)
        word.append(a)
        if flag == 'N':
            memory['N'] = a
    if 'N' in memory:
        if temp != memory['N'] and temp != '':
            memory['recall'] = temp
    # print(memory)
    for a in word:
        statement = statement+a
    return statement,memory

def command_interface():
    dialog()


def getans(statement):
    response = ''
    try:
        longmemory = loadmemory()
    except:
        return response
    words = pseg.cut(statement)
    for pattern, responses in longmemory:
        score = 0
        pat = pseg.cut(pattern)
        total = 0
        example = []
        for a,flag in pat:
            example.append([a,flag])
            if flag == 'Vt' or flag == 'N':
                total += 1.5
            else:
                total +=0.5
        for a,flag in words:
            if [a,flag] in example:
                if flag == 'Vt' or flag == 'N':
                    score += 1.5
                else:
                    score += 0.5
            else:
                if flag == 'Vt' or flag == 'N':
                    score -= 1.5
                else:
                    score -= 0.5
        if score/total > 0.7:
            response = responses
            break
    return response

def completeAns(statement,question,context): #分析回答
    patterns,responses = answers[question]
    for pattern in patterns:
        cards = findcards(pattern)
        if cards:
            for card in cards:
                pattern = pattern.replace('@' + card + '@', '(?P<'+card+'>.*)')
        match = re.match(pattern, statement.rstrip(".!"))
        if match:
            if cards:
                for card in cards:
                    context[card] = reflect(match.group(card))
            response = random.choice(responses)
            cards = findcards(response)
            if cards:
                for card in cards:
                    response = response.replace('@' + card + '@', context[card])
    return response

def findcards(pattern):
    findstart = -1
    cards = []
    while True:
        findstart = pattern.find('@', findstart + 1)
        if findstart == -1:
            break
        findend = pattern.find('@', findstart + 1)
        cards.append(pattern[findstart + 1:findend])
        findstart = findend
    return cards



def dialog():
    print('=' * 72)
    tts.speak("您好，請問您叫甚麼名字？")
    print("您好，請問你叫甚麼名字?")
    context = {}  #短期記憶
    question = questionlist.pop(0)
    while True:
        response = ''
        f = open(time.strftime("%Y-%m-%d %H%M", time.localtime()) + '.txt', 'a')

        statement = input("")
        if question != '':
            response = completeAns(statement, question,context)
        question = ''
        f.write('HUMAN:'+statement+'\n')
        if questionlist:
            question = questionlist.pop(0)
            if response:
                tts.speak(response)
                print(response)
            response = questions[question]
        else:
            fmmse = open('MMSE.txt', 'w')
            for ans in anslist:
                fmmse.write(ans+':' + context[ans] + '\n')
            fmmse.closed
        if response == '':
            statement = searchClause(statement, context)
            response = getans(statement)

        if response == '':
            leave, response = analyze(statement,context)
        else:
            leave = False
        tts.speak(response)
        #print(response)
        f.write('BOT:'+response+'\n')
        f.close()
        if leave:
            break



conjunction = [
    ['random',['不但(.*)而且(.*)']],
    ['front',['(.*)由於(.*)','(.*)但是(.*)','(.*)不過(.*)','(.*)甚至(.*)','因為(.*)所以(.*)']],
    ['behind',['(.*)因此(.*)','(.*)所以(.*)','(.*)雖然(.*)','(.*)然後(.*)','(.*)那(.*)']],

]

def searchClause(statement,memory):
    for type,patterns in conjunction:
        for pattern in patterns:
            template = re.search('@(.*)@', pattern)
            if template:
                name = template.group(1)
                pattern = pattern.replace(template.group(0), '(?P<name>.*)')
            match = re.search(pattern, statement.rstrip(".!"))
            if match:
                if template:
                    memory[name] = match.group('name')
                if type == 'because':
                    statement = match.groups()[1]
                elif type == 'therefore':
                    statement = match.groups()[0]
                else:
                    statement = random.choice(match.groups())
                return statement
    return statement





if __name__ == "__main__":
    command_interface()
