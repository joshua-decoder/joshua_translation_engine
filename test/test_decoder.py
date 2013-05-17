# -*- coding: utf-8 -*-
import unittest
from decoder import Decoder
from mock import patch, Mock


class TestDecoder(unittest.TestCase):

    def test_translate(self):
        socket = Mock()
        socket.send.return_value = None
        socket.recv.return_value = 'adiós'
        d = Decoder('path', '8000')
        self.assertEqual(
            'adiós'.decode('utf8'),
            d.translate('whatever', socket)
        )
