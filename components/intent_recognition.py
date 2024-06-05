# Imports | kazuha046 creator
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Variables
vectorizer = CountVectorizer()
classifier = LogisticRegression()
classifier_probability = LogisticRegression()

config = {
    'intents': {
        'greetings': {
            'examples': ['привет', 'здравствуй', 'здравствуйте', 'алло', 'добрый день', 'добрый вечер', 'доброе утро']
        },
        'farewell': {
            'examples': ['пока', 'до свидания', 'увидимся', 'всего доброго', 'до встречи', 'прощай', 'всего хорошего']
        }
    }
}


# Methods
def prepare_classifier():
    corpus = []
    target_vector = []
    for intent_name, intent_data in config['intents'].items():
        for example in intent_data['examples']:
            corpus.append(example)
            target_vector.append(intent_name)

    training_vector = vectorizer.fit_transform(corpus)
    classifier_probability.fit(training_vector, target_vector)
    classifier.fit(training_vector, target_vector)


def get_intent(request):
    if not request:
        return None

    best_intent = classifier.predict(vectorizer.transform([request]))[0]

    index_of_best_intent = list(classifier_probability.classes_).index(best_intent)
    probabilities = classifier_probability.predict_proba(vectorizer.transform([request]))[0]

    best_intent_probability = probabilities[index_of_best_intent]

    if best_intent_probability > 0.57:
        return best_intent
    else:
        return None

prepare_classifier()
