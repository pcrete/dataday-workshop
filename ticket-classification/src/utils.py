import spacy
import pickle
import re
import os
import logging


logging.basicConfig(level=os.getenv('LOG_LEVEL', 'INFO'))
logger = logging.getLogger(__name__)


spacy_model = spacy.load("en_core_web_sm")
topics ={
    0: 'bank account services',
    1: 'credit_card',
    2: 'mortgage/loans',
    3: 'theft/dispute reporting',
    4: 'others'
}

logistic_model, tf_idf = None, None

def load_model():
    global logistic_model, tf_idf
    if logistic_model is None:
        model_path = os.path.join('src', 'model', 'logistic_model.pkl')
        tf_idf_path = os.path.join('src', 'model', 'tf_idf.pkl')

        try:
            with open(model_path, 'rb') as f:
                logistic_model = pickle.load(f)
            with open(tf_idf_path, 'rb') as f:
                tf_idf = pickle.load(f)


        except Exception as e:
            raise Exception(f"Error loading model: {e}")

def pre_process_text(text):
	"""
	This function is to clean the text and remove punctuations,digits, text in square brackets and masked characters.
	"""
	text = text.lower()
	text = re.sub(r'\[.*?\]','',text)
	text = re.sub(r'[^\w\s]', '',text)
	text = re.sub(r'[\d]','',text)
	text = re.sub(r'[*x]?','',text)
	logger.debug(f"\t1. Pre-processed: {text}")

	return text

def get_lemma(text):
	"""
	This function returns only noun words
	"""
	modified_text =""
	tokens = spacy_model(text)

	for token in tokens :
		if(token.tag_=='NN'):
			modified_text += token.lemma_ +" "

	logger.debug(f"\t2. lemmatization: {modified_text}")
	return modified_text

def get_tf_idf_features(text):
	logger.debug("\t3. tf_idf transformation")
	X = tf_idf.transform([text])
	return X.toarray()

def get_predict(X):
	y = logistic_model.predict(X)
	cls = topics[y[0]]
	logger.debug(f'\t4. prediction: "{cls}" class')
	return cls

def predict_class(text):
	logger.debug(f"\t0. Input Text: {text}")
	if logistic_model is None or tf_idf is None:
		load_model()

	preprocessedText = pre_process_text(text)
	lemmatizedText = get_lemma(preprocessedText)

	X = get_tf_idf_features(lemmatizedText)
	category = get_predict(X)

	return category


