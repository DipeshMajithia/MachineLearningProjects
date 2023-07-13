from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import streamlit as st
import pickle
import string
import nltk
nltk.download('stopwords')
ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")
print(input_sms)
if st.button('Predict'):

    # 1. preprocess
    transformed_sms = transform_text(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    print("Result===>", result)
    # 4. Display
    prob = model.predict_proba(vector_input)[0][1]
    st.write("Spam Probability: ", prob)
    if result == 0:
        st.header("Billing Department")
    elif result == 7:
        st.header("Sales Department")
    elif result == 2:
        st.header("HR Department")
    elif result == 1:
        st.header("Financial Accounting Department")
    elif result == 3:
        st.header("Maintenance Department")
    elif result == 5:
        st.header("Marketing Department")
    elif result == 6:
        st.header("Operational management")
    elif result == 4:
        st.header("Management Department")
