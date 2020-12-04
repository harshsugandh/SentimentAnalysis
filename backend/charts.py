# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import operator
import collections
import itertools
from nltk.corpus import stopwords

def all_plots():
    data = pd.read_csv("./comment.csv")

    #sentiment_barplot
    sns.countplot(x="sentiment", data=data)
    plt.savefig('../frontend/src/assets/images/sentiment_barplot.jpg', bbox_inches='tight')

    #lenghts_before
    data['length'] = [len(x.strip()) for x in data['comment']]
    sns.displot(data['length'],kde=True)
    plt.savefig('../frontend/src/assets/images/lenghts_before.jpg', bbox_inches='tight')
    plt.clf()
    
    #https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/calculate-tweet-word-frequencies-in-python/
    #word_frequency
    data['clean_comment'] = [comment.lower() for comment in data['comment']]
    stop = stopwords.words('english')
    data['clean_comment']= data['clean_comment'].apply(lambda x: [item for item in str(x).split() if item not in stop])
    data['clean_comment'][0]
    all_words= list(itertools.chain(*data['clean_comment'])) 
    dict_word = collections.Counter(all_words)
    dict_word.most_common(15)
    clean_dict_word = pd.DataFrame(dict_word.most_common(15),
                                columns=['words', 'count'])
    clean_dict_word.head()
    ax = plt.subplots(figsize=(8, 8))
    clean_dict_word = clean_dict_word.sort_values(by='count')
    sns.barplot(y="words",x="count", data=clean_dict_word, palette="Blues_d")
    plt.savefig('../frontend/src/assets/images/word_frequency.jpg', bbox_inches='tight')
    plt.clf()

    #sentiment_length
    sns.scatterplot(data=data, x="length", y="length", hue="sentiment")
    plt.clf()
    sns.distplot(data["length"])
    plt.clf()
    target_0 = data.loc[data['sentiment'] == -1]
    target_1 = data.loc[data['sentiment'] == 1]
    target_2 = data.loc[data['sentiment'] == 0]
    sns.distplot(target_0[['length']], hist=False, rug=True, color='red', label='negative')
    sns.distplot(target_1[['length']], hist=False, rug=True, color='green', label='positive')
    sns.distplot(target_2[['length']], hist=False, rug=True, color='blue', label='neutral')
    plt.legend()
    plt.savefig('../frontend/src/assets/images/sentiment_length.jpg', bbox_inches='tight')
    plt.clf()

    #length_count
    sns.boxplot(data=data, x='length')
    sns.displot(
        data=data, 
        x="length",  hue="sentiment",
    )
    plt.savefig('../frontend/src/assets/images/length_count.jpg', bbox_inches='tight')
    plt.clf()

    #length_count2
    Q1 = data['length'].quantile(0.25)
    Q3 = data['length'].quantile(0.75)
    IQR = Q3 - Q1    #IQR is interquartile range. 
    filter = (data['length'] >= Q1 - 1.5 * IQR) & (data['length'] <= Q3 + 1.5 *IQR)
    removed_data=data.loc[filter]
    sns.displot(
        data=removed_data,
        x="length",  hue="sentiment",
    )
    sns.displot(
        data=removed_data, kind="hist", kde=True,
        x="length",  hue="sentiment",
    )
    plt.savefig('../frontend/src/assets/images/length_count2.jpg', bbox_inches='tight')
    plt.clf()

if __name__ == "__main__":
    all_plots()