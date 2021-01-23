from flask import Flask, request
from text_similarity import cosine_similarity

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Text Similarity</h1><p>This site is a prototype API for calculating similarity of two texts.</p>"


@app.route('/text_similarity/api', methods=['POST'])
def text_similarity():
    if request.method == 'POST':
        t1 = request.args.get('text1', '')
        t2 = request.args.get('text2', '')
        return str(round(cosine_similarity(t1, t2), 4))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
