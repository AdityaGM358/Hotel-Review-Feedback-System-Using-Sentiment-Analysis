import joblib
import pickle
import csv
model = joblib.load("svcModel.pickle")
vectorizer = pickle.load(open("vect.pickle","rb"))

def predict(input_sentence):
    text=input_sentence
    trans_text=vectorizer.transform([text])
    result=model.predict(trans_text)
    if(result==1):
        return "Positive"
    else:
        return "Negative"
def predict_file(file_name):
    file1 = open(file_name, 'r')
    csvfile= open('C:\\Users\\91702\\OneDrive\\Desktop\\project\\result.csv', 'w')
    Lines = file1.readlines()
    count=0
    for line in Lines:
        count += 1
        res=""
        #text=input_sentence
        text=line.strip()
        if len(text)==0:
            count -= 1
            continue
        trans_text=vectorizer.transform([text])
        result=model.predict(trans_text)
        if(result==1):
            res= "Positive"
        else:
            res= "Negative"
        fields=[count, text, res]  
        csvwriter = csv.writer(csvfile)         
        csvwriter.writerow(fields)  
  
def predict_file_stats(file_name):
    file1 = open(file_name, 'r')
    csvfile= open('C:\\Users\\91702\\OneDrive\\Desktop\\project\\result.csv', 'w')
    Lines = file1.readlines()
    count=0
    pc=0
    nc=0
    for line in Lines:
        count += 1
        res=""
        #text=input_sentence
        text=line.strip()
        if len(text)==0:
            count -= 1
            continue
        trans_text=vectorizer.transform([text])
        result=model.predict(trans_text)
        if(result==1):
            res= "Positive"
            pc+=1
        else:
            res= "Negative"
            nc+=1
        fields=[count, text, res]  
        csvwriter = csv.writer(csvfile)         
        csvwriter.writerow(fields)
    return "postive: "+str(pc)+"\tnegative: "+str(nc)

