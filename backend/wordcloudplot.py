from wordcloud import WordCloud, STOPWORDS
import pandas as pd
import matplotlib.pyplot as plt

def plotwordcloud():
    stopwords = set(STOPWORDS)
    test = pd.read_csv('comment.csv', encoding='Latin-1', low_memory=False)
    all_words = ' '.join([text for text in test.iloc[:, 0]])
    wordcloud = WordCloud(width=800, height=500, random_state=21, max_words=50, 
                        max_font_size=110, stopwords=stopwords).generate(all_words)
    plt.figure(figsize=(10, 7))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis('off')
    # plt.show()
    plt.savefig('C:/Users/Harsh Sugandh/Desktop/SentimentAnalysis/frontend/src/assets/images/wordcloud.jpg', bbox_inches='tight')

if __name__ == "__main__":
    plotwordcloud()