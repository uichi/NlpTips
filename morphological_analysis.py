import MeCab

text = 'メロスは激怒した。必ず、かの邪智暴虐じゃちぼうぎゃくの王を除かなければならぬと決意した。メロスには政治がわからぬ。メロスは、村の牧人である。'
#単語ごとの情報を出力
tagger = MeCab.Tagger("-Ochasen")
result = tagger.parse(text)
print(result, "\n")

text = 'メロスは激怒した。必ず、かの邪智暴虐じゃちぼうぎゃくの王を除かなければならぬと決意した。メロスには政治がわからぬ。メロスは、村の牧人である。'
#分かち書き
tagger = MeCab.Tagger("-Owakati")
result = tagger.parse(text)
print(result, "\n")

