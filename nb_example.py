from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from texts import texts, text_labels


def text_counter(texts):
    vectorizer = CountVectorizer()
    txt_train = vectorizer.fit_transform(texts)
    return vectorizer, txt_train


def text_training(txt_train, text_labels):
    text_classifier = MultinomialNB()
    text_classifier.fit(txt_train, text_labels)
    return text_classifier


def run():
    vectorizer, txt_train = text_counter(texts)

    text_classifier = text_training(txt_train, text_labels)

    text = input('Type a creative text: ')

    intercepted_text = [text]

    text_counts = vectorizer.transform(intercepted_text)

    final_pos = text_classifier.predict_proba(text_counts)[0][1]
    
    final_neg = text_classifier.predict_proba(text_counts)[0][0]

    if final_pos > final_neg:
        print("The text is positive.")
    else:
        print("The text is negative.")


if __name__ == '__main__':
    run()