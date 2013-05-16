joshua_translation_engine
=========================

RESTful wrapper for the [Joshua machine translation decoder](https://github.com/joshua-decoder/joshua)


## Description

This is a translation engine server written in Python that provides
translations of documents http requests as responses to http requests.


## Use

This translation server is meant to be run in a specific manner. It launches
"run bundles". The directory that is the root of each run bundle should be
passed as an argument for each concurrent decoder that will be running.


### Installation

install the dependencies with `pip`:

    pip install -r requirements.txt


### Starting the translation engine

You must use the command line options to Specify at least one bundle and source
and target languages for each bundle.  The order of repeated `-s` and `-t`
correspond to the order of `-b` options.

Run the command, for example:

    python app.py \
      -b /path/to/bundledir-es-en /path/to/bundledir-de-en \
      -s es                       de \
      -t en                       en \
      -p 8001                     8002

or a different version of the same command:

    python app.py \
      --bundle-dir  /path/to/bundledir-es-en /path/to/bundledir-de-en \
      --source-lang es                       de \
      --target-lang en                       en \
      --port        8001                     8002


### Requesting translations

To request a translation, send a POST http request to the running server at the
following address:

    curl http://localhost:5000/joshua/translate/english \
      -i -H "Content-Type: application/json" \
      -X POST -d '{"inputLanguage": "Spanish", "inputText": "vuelo"}' -v
