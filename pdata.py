import spacy
import ko_core_news_lg
import nltk
import konlpy
from spacy import displacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from konlpy.tag import Okt

nlp = spacy.load("ko_core_news_lg")
okt = Okt()

class Data:
    def __init__(self):
        self.nlp = nlp
        self.okt = okt
        
    def stopword(self, text):
        doc = self.nlp(text)
        stop_words = "의 에 이 가 는 를 와 과 같은 그리고 그런데 그러나 그래서 그러면 그리하여 그러므로 그런즉 이에 나 너 저 그 그녀 우리 그들 누구 무엇 어디 언제 어느 몇 모두 매우 많은 아주 매우 무척 대단히 조금 좀 다소 정말 진실로 이외에 이 그 저 해당 그런 에 에서 에게 을 의 이 으로 와 에서부터 까지 각 관련"
        stop_words = set(stop_words.split(' '))
        word_tokens = self.okt.morphs(str(doc))
        result = [word for word in word_tokens if not word in stop_words]
        
        spacing_text = (', '.join(result))
        rtext = nlp(spacing_text)
        
        result_list = []
        for txt in rtext.ents:
            result_list.append(txt.text)
                    
        return result_list
