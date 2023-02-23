import re
from predict import predict
from pdata import Data

sentence = "한국 축구대표팀이 브라질과 친선 경기에서 1-5로 패했습니다."

text = Data().stopword(sentence)
tx = predict().generate(text)
for t in tx:
    re_a = re.sub(r'[.,"\'-?:!;]', '', t[0])
    re_b = re.sub(r'\[[^)]*\]', '', re_a) 
    print(re_b)
    
    
    
    

