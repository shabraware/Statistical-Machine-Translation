from nltk.translate.stack_decoder import StackDecoder

class Decoder:
    def __init__(self, translation_model, e_language_model = None):
        self.stack_decoder = StackDecoder(translation_model.f_e_phrase_table, e_language_model)

    def translate(self, f):
        e_tokens = self.stack_decoder.translate(f.split())
        e = ' '.join(e_tokens)
        return e