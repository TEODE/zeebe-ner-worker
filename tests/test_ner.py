import unittest
from libs.classifier import Classifier

class TestClassifier(unittest.TestCase):

    def test_sequence_fr_inference(self):
        model = "models/camembert-ner-with-dates"
        classifier = Classifier.get_instance(model)
        sequence = "Apple est créée le 1er avril 1976 dans le garage de la maison d'enfance de Steve Jobs à Los Altos en Californie par Steve Jobs, Steve Wozniak et Ronald Wayne14, puis constituée sous forme de société le 3 janvier 1977 à l'origine sous le nom d'Apple Computer, mais pour ses 30 ans et pour refléter la diversification de ses produits, le mot « computer » est retiré le 9 janvier 2015."
        output = classifier.infer(sequence)
        self.assertEqual(output[0]["word"], "▁Apple")
        self.assertEqual(output[0]["score"], 0.9776379466056824)
    
    # def test_sequence_en_inference(self):
    #     model = ""
    #     # forces recreate Classifier singleton
    #     Classifier.destroy_instance()
    #     classifier = Classifier.get_instance(model)
    #     sequence = "L'exécutif est reparti en campagne"
    #     output = classifier.infer(sequence, candidate_labels)
    #     # camembert-base-xnli score = 0.922779381275177

if __name__ == '__main__':
    unittest.main()        