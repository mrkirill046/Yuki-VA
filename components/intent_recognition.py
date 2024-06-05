# Imports | kazuha046 creator
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

# Variables
vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(2, 3))
classifier_probability = LogisticRegression()
classifier = LinearSVC()

config = {
    'intents': {
        'greetings': {
            'examples': ['привет', 'здравствуй', 'здравствуйте', 'алло', 'добрый день', 'добрый вечер', 'доброе утро']
        },
        'farewell': {
            'examples': ['пока', 'до свидания', 'увидимся', 'всего доброго', 'до встречи', 'прощай', 'всего хорошего']
        },
        'window_off': {
            'examples': ['спрячься', 'закрой своё окно', 'выключись', 'спрятайся', 'уйди']
        },
        'window_on': {
            'examples': ['покажись', 'открой своё окно', 'включись', 'появись']
        },
        'computer_off': {
            'examples': ['выключи пк', 'выключи компьютер', 'выключи комп', 'выключи ноут']
        },
        'youtube': {
            'examples': ['открой youtube', 'поиск на ютубе', 'поиск на youtube', 'найди на youtube', 'найди на ютуби',
                         'найди в ютуби']
        },
        'google': {
            'examples': ['найди в гугле', 'поищи в google', 'посик в гугл', 'найди в google']
        }
    }
}


# Methods
def prepare_corpus():
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
    best_intent = classifier.predict(vectorizer.transform([request]))[0]

    index_of_best_intent = list(classifier_probability.classes_).index(best_intent)
    probabilities = classifier_probability.predict_proba(vectorizer.transform([request]))[0]

    best_intent_probability = probabilities[index_of_best_intent]

    if best_intent_probability > 0.34:
        return best_intent
