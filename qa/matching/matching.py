from nltk import stem
from nltk.corpus import wordnet
from nltk.corpus import stopwords

def match(stored_answers, user_answer):
	common_word_list = stopwords.words('english')
	#common_word_list = [];
	stemmer = stem.PorterStemmer()
	user_words = user_answer.split()
	stored_words = list()

	for k, sentence in enumerate(stored_answers):
		stored_words.extend(sentence.split())


	stored_words = set(stored_words) - set(common_word_list)
	user_words = set(user_words) - set(common_word_list)
	user_syn = list()
	user_syn_and_words = set()
	stored_stems = []
	user_stems = []
	
	for p, word in enumerate(user_words):
		synonyms = wordnet.synsets(word)
		if len(synonyms) >= 1:
			for l, syn in enumerate(synonyms[0].lemmas):
				user_syn.append(syn.name)

	user_syn_and_words.update(user_words)
	user_syn_and_words.update(set(user_syn))

	for i, word in enumerate(stored_words):
		stored_stems.append(stemmer.stem(word))

	for j, word in enumerate(user_syn_and_words):
		user_stems.append(stemmer.stem(word))

	matched = set(user_stems) & set(stored_stems)
	raw_score = len(matched)/float(len(stored_stems))
	score = raw_score * 100;
	print matched
	return score
