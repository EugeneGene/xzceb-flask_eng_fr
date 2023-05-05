import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    This code translates english to french.
    Input: English text string
    Output: French text string
    """
    if english_text is None or english_text == "":
        french_text="Empty string"
    else:
        french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr'
        ).get_result()['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    """
    This code translates French to English.
    Input: French text string
    Output: English text string
    """

    if french_text is None or french_text == "":
        english_text="Empty string"
    else:
        english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en'
        ).get_result()['translations'][0]['translation']
    return english_text


TRANSLATE_EN_TO_FR = english_to_french("Hi. How are you?")
TRANSLATE_FR_TO_EN = french_to_english("Salut. Comment es-tu?")


def main():


    print(json.dumps(english_to_french(""), indent=2, ensure_ascii=False))
    print(json.dumps(french_to_english(""), indent=2, ensure_ascii=False))

    print(english_to_french(""))
    print(french_to_english(""))


if __name__ == '__main__':
    main()
