# Korean Name Entity Recognition + KOGPT

## 1. Introduce
- 한국어 개체명 인식을 통해 개체명을 추출한 개체를 토대로 문장을 생성해내기 위해 [kakaobrain/kogpt](https://github.com/kakaobrain/kogpt) 모델을 사용하여 진행 하였다.

## 2. Used
- > pip install -r requirements.txt
- > conda env create -f koner_kogpt.yaml
- > python -m spacy download ko_core_news_lg

<br></br>

# KoGPT Hardware requirements
## KoGPT6B-ryan1.5b
### GPU
The following is the recommended minimum GPU hardware guidance for a handful of example KoGPT.
- 32GB GPU RAM in the required minimum memory size

## KoGPT6B-ryan1.5b-float16
### GPU
The following is the recommended minimum GPU hardware guidance for a handful of example KoGPT.

- half-precision requires NVIDIA GPUS based on Volta, Turing or Ampere
- 16GB GPU RAM in the required minimum memory size

# Reference
연구를 할 수 있게 PLM(Pre-trained Language Model)을 공유해주신 [kakaobrain](https://kakaobrain.com/) 팀 연구진 분들에게 감사의 말씀을 드립니다.
- [kakaobrain/kogpt](https://github.com/kakaobrain/kogpt)

