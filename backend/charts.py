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
    data.head()

    sns.countplot(x="sentiment", data=data)
    plt.savefig('C:/Users/Harsh Sugandh/Desktop/SentimentAnalysis/frontend/src/assets/images/sentiment_barplot.jpg', bbox_inches='tight') 
    """
    x=["neutral", "positive", "negative"]
    y= data['sentiment'].value_counts()

    plt.bar(x,y)
    plt.show()

    data['length'] = [len(x) for x in data['comment']]
    data.head()

    lenghts_before = sns.distplot(data['length'],kde=True)
    lenghts_before.savefig('C:/Users/Harsh Sugandh/Desktop/SentimentAnalysis/frontend/src/assets/images/lenghts_before.jpg', bbox_inches='tight')

    #https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/calculate-tweet-word-frequencies-in-python/

    data['clean_comment'] = [comment.lower() for comment in data['comment']]

    stop = stopwords.words('english')
    data['clean_comment']= data['clean_comment'].apply(lambda x: [item for item in str(x).split() if item not in stop])

    data['clean_comment'][0]

    all_words= list(itertools.chain(*data['clean_comment'])) 
    all_words

    dict_word = collections.Counter(all_words)
    dict_word.most_common(15)

    clean_dict_word = pd.DataFrame(dict_word.most_common(15),
                                columns=['words', 'count'])

    clean_dict_word.head()

    ax = plt.subplots(figsize=(8, 8))

    # Plot horizontal bar graph
    clean_dict_word.sort_values(by='count').plot.barh(x='words',
                        y='count',
                        ax=ax)

    ax.set_title("Common Words Found in Comments (Including All Words)")

    plt.show()
    plt.savefig('C:/Users/Harsh Sugandh/Desktop/SentimentAnalysis/frontend/src/assets/images/word_frequency.jpg', bbox_inches='tight')

    sns.scatterplot(data=data, x="length", y="length", hue="sentiment")

    sns.distplot(data["length"])

    target_0 = data.loc[data['sentiment'] == -1]
    target_1 = data.loc[data['sentiment'] == 1]
    target_2 = data.loc[data['sentiment'] == 0]

    sns.distplot(target_0[['length']], hist=False, rug=True, color='red', label='negative')
    sns.distplot(target_1[['length']], hist=False, rug=True, color='green', label='positive')
    sns.distplot(target_2[['length']], hist=False, rug=True, color='blue', label='neutral')
    sentiment_length = plt.legend()
    plt.savefig('C:/Users/Harsh Sugandh/Desktop/SentimentAnalysis/frontend/src/assets/images/sentiment_length.jpg', bbox_inches='tight')

    sns.boxplot(data=data, x='length')

    length_count = sns.displot(
        data=data, 
        x="length",  hue="sentiment",
    )
    length_count.savefig('C:/Users/Harsh Sugandh/Desktop/SentimentAnalysis/frontend/src/assets/images/length_count.jpg', bbox_inches='tight')

    Q1 = data['length'].quantile(0.25)
    Q3 = data['length'].quantile(0.75)
    IQR = Q3 - Q1    #IQR is interquartile range. 

    filter = (data['length'] >= Q1 - 1.5 * IQR) & (data['length'] <= Q3 + 1.5 *IQR)
    removed_data=data.loc[filter]  
    print(data.shape, removed_data.shape)

    print(data.shape, removed_data.shape)

    sns.displot(
        data=removed_data,
        x="length",  hue="sentiment",
    )

    length_count2 = sns.displot(
        data=removed_data, kind="hist", kde=True,
        x="length",  hue="sentiment",
    )
    length_count2.savefig('C:/Users/Harsh Sugandh/Desktop/SentimentAnalysis/frontend/src/assets/images/length_count2.jpg', bbox_inches='tight')
    """
if __name__ == "__main__":
    all_plots()