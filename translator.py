#!/usr/bin/env python3

import sys

import requests

import urllib.parse

API_ROOT = 'https://translation.googleapis.com'
API_VERSION = 'v2'
API_KEY = <ADD_YOUR_API_KEY>

def get(url):
    return requests.get(url)

#detection
def detectLang(detect_language_api, api_key, text):
    detect_url = '{}/?q={}&key={}'.format(detect_language_api, urllib.parse.quote(text), api_key)
    detect_response = get(detect_url)
    source_lang = detect_response.json()['data']['detections'][0][0]['language']
    return source_lang

#translation
def translate(translate_api, api_key, text, source_lang, target_lang):
    tranlate_url = '{}/?q={}&source={}&target={}&key={}'.format(translate_api, urllib.parse.quote(text), source_lang, target_lang, api_key)
    tranlate_response = get(tranlate_url)
    translation = tranlate_response.json()['data']['translations'][0]['translatedText']
    return translation


def main():
    detect_language_api = '{}/language/translate/{}/detect'.format(API_ROOT, API_VERSION)
    translate_api = '{}/language/translate/{}'.format(API_ROOT, API_VERSION)
    text_to_tranlate = sys.argv[1]
    target_lang = sys.argv[2]

    source_lang  = detectLang(detect_language_api, API_KEY, text_to_tranlate)
    if source_lang == target_lang:
        tranlation =  text_to_tranlate
    else:
        tranlation = translate(translate_api, API_KEY, text_to_tranlate, source_lang, target_lang)
    print(tranlation)


if __name__ == '__main__':
    main()
