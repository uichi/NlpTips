import pandas as pd
import MeCab
import random

    def sum_posi_nega(self, parse_texts, file_name):
        
        def conserve(text):
            rm_extension_name = file_name.split('.')[0]
            
            if not os.path.isdir(self.polarity_dir + '/' + item + '_polarity'):
                os.mkdir(self.polarity_dir + '/' + item + '_polarity')
            time.sleep(0.1)
            
            print(self.polarity_dir + '/' + item + '_polarity/' + rm_extension_name.split('/')[3])
            df = pd.DataFrame(posi_nega, columns=["parse_text","sum","mean"])
            df.to_csv(self.polarity_dir + '/' + item + '_polarity/' + rm_extension_name.split('/')[3] + ".csv", index=False, encoding='utf-8')
            
        posi_nega    = []
        parse_tweets = [parse_tweet for parse_tweet in parse_texts['parse_text']]
        for parse_tweet in parse_tweets:
            posi_nega_mean = 0
            positive_word  = 0
            negative_word  = 0
            sum_posi_nega  = 0
            
            sum_posi_nega = 0
            for word in parse_tweet.split():
                posi_nega_record = 0
                
                if word in substantive_words:
                    posi_nega_record = substantive_dictionary[substantive_dictionary['単語'].isin([word])]['ネガポジ値']
                elif word in declinable_words:
                    posi_nega_record = declinable_dictionary[declinable_dictionary['単語'].isin([word])]['ネガポジ値']
                
                try:
                    if int(posi_nega_record) != 0:
                        if int(posi_nega_record)   ==  1:
                            positive_word += 1
                        elif int(posi_nega_record) == -1:
                            negative_word -= 1
                        sum_posi_nega += int(posi_nega_record)
                except:
                    pass
                                    
            if sum_posi_nega != 0:
                posi_nega_mean = (positive_word + negative_word)/len(parse_tweet)
            posi_nega.append([parse_tweet, sum_posi_nega, posi_nega_mean])
        conserve(text=posi_nega)

item_genre   = str(input('ジャンルを入力してください。: '))
items        = pd.read_csv('keyword/' + item_genre + '_keyword.csv', encoding='utf-8')
parse_dir    = 'parse/' + item_genre + '_parse'
polarity_dir = 'polarity/' + item_genre + '_polarity'
    
substantive_dictionary = pd.read_csv('dictionary/PN_Table/substantive.csv', encoding='utf-8')
declinable_dictionary  = pd.read_csv('dictionary/PN_Table/declinable.csv', encoding='utf-8')
substantive_words      = [word for word in substantive_dictionary['単語']]
declinable_words       = [word for word in declinable_dictionary['単語']]
posi_nega_analysis     = PosiNegaAnalysis(substantive=substantive_words, declinable=declinable_words, polarity_dir=polarity_dir)
