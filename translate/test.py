import requests
from docx import Document
import hashlib


class TranslationWord:
    def __init__(self):
        self.base_url = 'http://openapi.youdao.com/api'
        self.app_key = '5106d81e1458807f'  # 需要替换成自己的应用ID
        self.secret_key = 'pzcAOIIkXO8jKNiN8QuBh5UM7Y3QUTn4'  # 需要替换成自己的应用密钥
        self.salt = '123'

    def translate_text(self, text):
        sign = self.calculate_sign(text)
        params = {
            'q': text,
            'from': 'en',
            'to': 'zh-CHS',
            'appKey': self.app_key,
            'salt': self.salt,
            'sign': sign
        }
        r = requests.post(self.base_url, params=params)
        result_dict = r.json()
        if 'translation' in result_dict:
            return result_dict['translation'][0]
        return ''

    def calculate_sign(self, text):
        sign_str = self.app_key + text + self.salt + self.secret_key
        sign = hashlib.md5(sign_str.encode()).hexdigest()
        return sign

    def read_english_word_and_translate(self, word_path, output_path):
        document = Document(word_path)

        for paragraph in document.paragraphs:
            text = paragraph.text.strip()
            if text:
                translated_text = self.translate_text(text)
                paragraph.text = translated_text

        document.save(output_path)


if __name__ == '__main__':
    translator = TranslationWord()
    translator.read_english_word_and_translate('input.docx', 'output.docx')