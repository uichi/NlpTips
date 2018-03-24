import pandas as pd
import MeCab

text = 'メロスは激怒した。必ず、かの邪智暴虐じゃちぼうぎゃくの王を除かなければならぬと決意した。メロスには政治がわからぬ。メロスは、村の牧人である。'
#分かち書き
tagger = MeCab.Tagger("-Owakati")
words = tagger.parse(text)

substantive_dictionary = pd.read_csv('dictionary/substantive.csv', encoding='utf-8')
declinable_dictionary  = pd.read_csv('dictionary/declinable.csv', encoding='utf-8')
substantive_words      = [word for word in substantive_dictionary['単語']]
declinable_words       = [word for word in declinable_dictionary['単語']]

for word in words:
    if word in substantive_words: print(substantive_dictionary[substantive_dictionary['単語'].isin([word])])
    if word in declinable_words: print(substantive_dictionary[substantive_dictionary['単語'].isin([word])])
