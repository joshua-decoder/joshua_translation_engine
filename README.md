joshua_translation_engine
=========================

RESTful wrapper for the Joshua machine translation decoder

## Description

This is a translation engine server written in Python that provides
translations of documents http requests as responses to http requests.

## Use

### Starting the translation engine

The first command line argument is the directory containing the Joshua Bundle
to run as a TCP server.

### Requesting translations

To request a translation, send a POST http request to the running server at the
following address:

    curl http://localhost:5000/joshua/translate/english \
      -i -H "Content-Type: application/json" \
      -X POST -d '{"inputLanguage": "Spanish", "inputText": "vuelo"}' -v
