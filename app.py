from flask import Flask
from flask.ext.restful import reqparse, Api, Resource
import socket
import subprocess
import sys
app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('inputText', type=str, location='json')
parser.add_argument('inputLanguage', type=str, location='json')

decoders = {}


class Decoder(object):
    def __init__(self, source_lang, target_lang):
        self._source_lang = source_lang
        self._target_lang = target_lang
        self._start_decoder_server()

    @property
    def source_lang(self):
        return self._source_lang

    @property
    def target_lang(self):
        return self._target_lang

    def translate(self, input_text):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('localhost', 5674))
        sock.send('%s\n' % input_text)
        result = sock.recv(1024)
        return {'outputText': '"%s" is a translation from %s into %s of %s' %
                (result, self.source_lang, self.target_lang, input_text)}

    def _start_decoder_server(self):
        env = {'JOSHUA': '/Users/orluke/workspace/mt/joshua'}
        args = ['/Users/orluke/workspace/mt/expts/es-en-small-bundle/run-joshua.sh']
        subprocess.Popen(args, env=env)


class TranslationEngine(Resource):
    def post(self, target_lang):
        args = parser.parse_args()
        source_lang = args['inputLanguage']
        input_text = args['inputText']
        lang_pair = (source_lang, target_lang.capitalize())
        print source_lang
        print input_text
        translation = decoders[lang_pair].translate(input_text)
        return translation, 201

api.add_resource(TranslationEngine, '/joshua/translate/<string:target_lang>')

if __name__ == '__main__':
    lang_pair = ('Spanish', 'English')
    decoders[lang_pair] = Decoder(*lang_pair)
    app.run(debug=True, use_reloader=False)
    #app.run()
