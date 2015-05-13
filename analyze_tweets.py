
import json                                           # Importacion de modulos de python : json,pandas,plot.
import pandas as pd
import matplotlib.pyplot as plt
import re


def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False


def extract_link(text):
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return ''


def main():


	# Leyendo tweets...
	print 'Leyendo tweets..\n'
	tweets_data_path = 'twitter_data.txt'

	tweets_data = []
	tweets_file = open(tweets_data_path, "r")
	for line in tweets_file:
	    try:
	        tweet = json.loads(line)
	        tweets_data.append(tweet)
	    except:
	        continue


	# Estructurando tweets...
	print 'Estructurando tweets...\n'
	tweets = pd.DataFrame()
	tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
	tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
	tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)


	# Analizando tweets segun idioma...
	print 'Analizando tweets segun idioma...\n'
	tweets_by_lang = tweets['lang'].value_counts()
	fig, ax = plt.subplots()
	ax.tick_params(axis='x', labelsize=15)
	ax.tick_params(axis='y', labelsize=10)
	ax.set_xlabel('Idiomas', fontsize=15)
	ax.set_ylabel('Numero de tweets' , fontsize=15)
	ax.set_title('Top 5 Idiomas', fontsize=15, fontweight='bold')
	tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')
	plt.savefig('tweet_by_lang', format='png')


	# Anadiendo columnas de lenguajes de programacion a la fuente de datos de los tweets
	print 'Anadiendo columnas de lenguajes de programacion a la fuente de datos de los tweets\n'
	tweets['python'] = tweets['text'].apply(lambda tweet: word_in_text('python', tweet))
	tweets['javascript'] = tweets['text'].apply(lambda tweet: word_in_text('javascript', tweet))
	tweets['ruby'] = tweets['text'].apply(lambda tweet: word_in_text('ruby', tweet))


	# Analizando tweets segun lenguaje de programacion...
	print 'Analizando tweets segun lenguaje de programacion...\n'
	prg_langs = ['python', 'javascript', 'ruby']
	tweets_by_prg_lang = [tweets['python'].value_counts()[True], tweets['javascript'].value_counts()[True], tweets['ruby'].value_counts()[True]]
	x_pos = list(range(len(prg_langs)))
	width = 0.8
	fig, ax = plt.subplots()
	plt.bar(x_pos, tweets_by_prg_lang, width, alpha=1, color='blue')
	ax.set_ylabel('Numero de tweets', fontsize=15)
	ax.set_title('Ranking: python vs. javascript vs. ruby (Datos informales)', fontsize=10, fontweight='bold')
	ax.set_xticks([p + 0.4 * width for p in x_pos])
	ax.set_xticklabels(prg_langs)
	plt.grid()
	plt.savefig('tweet_by_prg_language_1', format='png')


	# Marcando tweets relevantes...
	print 'Marcando tweets relevantes...\n'
	tweets['programming'] = tweets['text'].apply(lambda tweet: word_in_text('programming', tweet))
	tweets['tutorial'] = tweets['text'].apply(lambda tweet: word_in_text('tutorial', tweet))
	tweets['relevant'] = tweets['text'].apply(lambda tweet: word_in_text('programming', tweet) or word_in_text('tutorial', tweet))


	# Extrayendo links de informacion
	tweets['link'] = tweets['text'].apply(lambda tweet: extract_link(tweet))
	tweets_relevant = tweets[tweets['relevant'] == True]
	tweets_relevant_with_link = tweets_relevant[tweets_relevant['link'] != '']

	print '\nAbajo hay algunos links de python que se han extraido...\n'
	print tweets_relevant_with_link[tweets_relevant_with_link['python'] == True]['link'].head()

if __name__=='__main__':
	main()




