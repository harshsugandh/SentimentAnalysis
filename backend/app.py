from flask import Flask, render_template
import charts
import wordcloudplot
import scraper

app = Flask(__name__)

@app.route('/wordcloud', methods=['POST'])
def wordcloud():
    wordcloudplot.plotwordcloud()
    return "Image created"

@app.route('/plots', methods=['POST'])
def plots():
    charts.all_plots()
    return "Image created"

@app.route('/predict',methods=['POST'])
def predict():
    output = scraper.scrape()
    return output
    
if __name__ == "__main__":
    app.run(debug=True)