import plotly
import plotly.graph_objs as go
from wordcloud import WordCloud, STOPWORDS
from plotly.graph_objs import *
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import json
from nltk.tokenize import word_tokenize  # to split sentences into words
from nltk.corpus import stopwords  # to get a list of stopwords
from collections import Counter


layout = Layout(
	autosize=False,
	paper_bgcolor='rgba(0,0,0,0)',
	plot_bgcolor='rgba(0,0,0,0)',
	width=500,
	height=300,
	xaxis= go.layout.XAxis(linecolor = None,
                          # showline=False,
                          showgrid=False),
	yaxis= go.layout.YAxis(linecolor = None,
		showline=False,
		showgrid=False),
	margin=go.layout.Margin(
		l=50,
		r=50,
		b=50,
		t=50,

		)
	)


def create_plot():
	N = 40
	x = np.linspace(0, 1, N)
	y = np.random.randn(N)
	df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe
	data = [
	go.Bar(
		x=df['x'], # assign x as the dataframe column 'x'
		y=df['y']
		)
	]
	fig = Figure(data=data, layout=layout)
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON


def word_cloud(feat):
	df = pd.read_excel('reviews_features_sentiment.xlsx')
	df = df[df["Feature"].isin([feat])]
	reviews=df["Review_amazon"].str.lower()

	sentences = ""
	for review in reviews:
		description = review
		sentences = sentences + " " + description
	# split sentences into words
	words = word_tokenize(sentences)

    # get stopwords
	stop_words = set(stopwords.words('english'))

    # remove stopwords from our words list and also remove any word whose length is less than 3
    # stopwords are commonly occuring words like is, am, are, they, some, etc.
	words = [word for word in words if word not in stop_words and len(word) > 3]

    # now, get the words and their frequency
	words_freq = Counter(words)
	word_freqs = dict(words_freq)
	word_freqs_js = []
	for key,value in word_freqs.items():
		temp = {"text": key, "size": value}
		word_freqs_js.append(temp)
	print(word_freqs.values())

	max_freq = max(word_freqs.values())
	return  word_freqs_js, max_freq

def feature():
	df = pd.read_excel('reviews_features_sentiment.xlsx').dropna(axis=0)
	feats=df["Feature"].astype("str").unique()
	return feats