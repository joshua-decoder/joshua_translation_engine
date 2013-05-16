import os
import socket
import subprocess
import sys

if not os.environ.get('JOSHUA'):
    sys.stderr.write('FATAL: the JOSHUA environment variable is not set.\n')
    sys.exit(-1)


class Decoder(object):
    """
    Joshua decoder
    """
    def __init__(self, bundle_dir, port):
        self._bundle_dir = bundle_dir
        self._port = port
        self._start_decoder_server()

    @property
    def bundle_dir(self):
        return self._bundle_dir

    @property
    def port(self):
        return self._port

    @property
    def source_lang(self):
        return self._source_lang

    @property
    def target_lang(self):
        return self._target_lang

    def translate(self, input_text):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('localhost', self.port))
        sock.send('%s\n' % input_text)
        result = sock.recv(1024)
        return {
            'outputText': '"%s" is a translation of %s.'
            % (result, input_text)
        }

    def _start_decoder_server(self):
        runner_path = os.path.join(self.bundle_dir, 'run-joshua.sh')
        options = ['-server-port', str(self.port)]
        subprocess.Popen([runner_path] + options, env=os.environ)
