import os
import socket
import subprocess
import env

env.assert_valid_env()


class Decoder(object):
    """
    Joshua decoder
    """
    def __init__(self, bundle_dir, port):
        self._bundle_dir = bundle_dir
        self._port = port

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

    def translate(self, input_text, sock=None):
        if not sock:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(('localhost', self.port))

        tx_msg = input_text + u'\n'
        sock.send(tx_msg.encode('utf8'))

        num_lines = len(input_text.split('\n'))
        rx_msg = u''
        for i in range(num_lines):
            rx_msg += sock.recv(1024).decode('utf8')

        return rx_msg

    def start_decoder_server(self):
        runner_path = os.path.join(self.bundle_dir, 'run-joshua.sh')
        options = ['-server-port', str(self.port)]
        subprocess.Popen([runner_path] + options, env=os.environ)
