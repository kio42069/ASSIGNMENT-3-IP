fileList = ['File1.txt','File2.txt','File3.txt']
from random import choice
for file in fileList:
    
    #FACTOR 1
    with open(file, "r") as obj:
        record = obj.readlines()
    string = ""
    for i in record:
        string = string + i
    string = string.lower()
    unique_words = list(set(string.split()))
    total_words = string.split()
    F1 = len(unique_words)/len(total_words)
    
    
    #FACTOR 2
    word_count = dict()
    for i in unique_words:
        word_count[i] = total_words.count(i)
    sortedList = [x for x in sorted(word_count.items(),key=lambda x:x[1], reverse=True)]
    total_occurences = 0
    for i in range(5):
        total_occurences += sortedList[i][1]
    F2 = total_occurences/len(total_words)
    
    
    
    #FACTOR 3
    sentences = string.split(".")
    for i in sentences:
        if i == "":
            sentences.remove(i)
    valid_sentences = 0
    for i in sentences:
        words = i.split()
        if len(words) < 5 or len(words) > 35:
            valid_sentences += 1
    F3 = valid_sentences/len(sentences)
    
    
    
    #FACTOR 4
    F4 = 0
    count = -1
    frequency = 0
    for i in string:
        if i not in ".,;:":
            if count > 0:
                frequency += 1
            count = -1
            
        else:
            count += 1
        
    F4 = frequency/len(total_words)
    
    #FACTOR 5
    F5 = 1 if len(total_words) > 750 else 0
    
    
    
    netscore = 4 + F1*6 + F2 - F3 - F4 - F5
    with open("file scores.txt","w") as obj:
        obj.write(file+"\n")
        obj.write(f"score: {netscore}\n")
        obj.write("5 most used words in decending order: ")
        for i in range(5):
            obj.write(sortedList[i][0] + " ")
        obj.write("\n")
        obj.write("5 random words from assignment submission: ")
        for i in range(5):
            obj.write(choice(total_words)+" ")
        obj.write("\n\n")