from django.shortcuts import render
import joblib
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import jieba.analyse


# Create your views here.


def main(request):
    return render(request,'main.html')

def classfi(request):
    value_text = request.POST.get('input_value')
    sentences = []
    stopwords = [line.strip() for line in open("classfication/templates/stopwords.txt", "r", encoding="utf-8").readline()]
    segs = jieba.lcut(value_text)
    segs = filter(lambda x: len(x) > 1, segs)
    segs = filter(lambda x: x not in stopwords, segs)
    sentences.append((" ".join(segs)))
    model1 = joblib.load('classfication/templates/model1.pkl')
    result = model1.predict(sentences[0])
    return render(request, 'main.html', context={'data': value_text, 'result': result[0]})

# def result(request):
