def writing(filename,text):
    f = open(filename,"w")
    f.write(text)
    f.close()

def append(filename,text):
    f = open(filename,"a")
    f.write(text)
    f.close()

def reading(filename):
    try:
        f = open(filename,"r")
        text = f.read()
        print(text)
        f.close()
    except FileNotFoundError:
        print("File not found error")

def search (filename,word):
    try:
        f = open(filename,"r")
        line_count = 0
        for line in f.readlines():
            line_count+=1
            strlist = line.split(' ')
            word_count = 0 
            for w in strlist:
                word_count +=1
                if word == w:
                    return(line_count,word_count)
        else : 
            return None
        f.close()
    except FileNotFoundError:
        print("File not fount error")


def modify(filename,oldword,newword):
    t = search(filename,oldword)
    if t!=None:
        mylist = []
        try:
            f = open(filename,"r")
            for line in f.readline():
                line = line.replace(oldword, newword)
                mylist.append(line)
            f.close()
            f = open(filename,"w")
            f.write(''.join(mylist)) # mylist is a list of string , so join all string using join
            f.close()
        except FileNotFoundError:
            print("file not Found")

    else: 
        print("Search is fail")
writing("file1.txt", "Hello Word")
append("file1.txt", " This is my hello word")
# reading("file.txt")
s = " MySirg Education Services private Limited"
s += "Saurabh Shukla Classes"
s+= "Premium website of Mysirg"
append("file1.txt",s)
print(search("file1.txt", "website"))
modify("file1.txt", "Services", "SAURABH")
