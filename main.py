import os
from flask import Flask, render_template
from keyvox.keyvox import KeyVox
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='static', static_url_path='', template_folder='templates')

base_url = os.environ.get('BASE_URL')
api_key = os.environ.get('API_KEY')

kv = KeyVox(api_key, base_url)


@app.route('/', methods=['GET'])
def index():
    articles = kv.articles.list()
    return render_template('index.html', articles=articles)

@app.route('/<id_or_slug>', methods=['GET'])
def article(id_or_slug):
    article = kv.articles.retrieve(id_or_slug)
    return render_template('article.html', article=article)


app.run(host='127.0.0.1', port=3000, debug=True)
