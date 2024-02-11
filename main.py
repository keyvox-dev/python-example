from flask import Flask, render_template
from keyvox.keyvox import KeyVox
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__, static_folder='static', static_url_path='', template_folder='templates')

kv = KeyVox(api_key='<KEY>', base_url='http://127.0.0.1:8080/api')



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


app.run(host='127.0.0.1', port=3000, debug=True)
