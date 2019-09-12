import flask,re
from flask import request
from spellchecker import SpellChecker

app = flask.Flask(__name__)
app.config["DEBUG"] = True

checkspelling = SpellChecker()

def reduce_length(text):
    pattern = re.compile(r"(.)\1{2,}")
    return pattern.sub(r"\1\1", text)

#@app.route('/sp/<string:input_word>', methods=['GET'])
@app.route('/spellCorrect', methods=['GET'])
def f():
    input_word = request.args.get('word')    ### get paramter

    input_word = input_word.lower() ## convert the tex to lowercase
    
    input_word = input_word.encode('ascii', 'ignore').decode('ascii') ### removing emojis 
    
    input_word=re.sub('[^A-Za-z0-9]+', '', input_word)##removing special characters
    
    input_word=''.join([i for i in input_word if not i.isdigit()]) ##removing numerics
    
    input_word=input_word.replace(" ", "")###remove all type of white spaces
    
    reduced_word = reduce_length(input_word) #####removing repeated characters
    
    result = checkspelling.candidates(reduced_word)

    return str(result)

app.run()
