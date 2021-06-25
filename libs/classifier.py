from json.encoder import JSONEncoder
import logging, os, json
from dotenv import load_dotenv
from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer
from .np_encoder import NpEncoder

load_dotenv() # Loading env vars
logging.basicConfig(format='%(levelname)s:%(message)s', 
   level=int(os.environ["LOGGING_LEVEL"]))

class Classifier:
   
   __instance = None
   
   @staticmethod 
   def get_instance(model: str=None):
      """ Static access method. """
      if Classifier.__instance == None:
          logging.debug("Classifier.get_instance: instanciate the singleton Classifier") 
          if model:  
            Classifier(model)
          else:
            Classifier()
      logging.debug("Classifier.get_instance: retrieve the singleton Classifier instance")
      return Classifier.__instance
   
   @staticmethod 
   def destroy_instance():
      Classifier.__instance = None
      logging.debug("Classifier.destroy_instance: destroy the singleton Classifier") 


   def __init__(self, model: str=None):
      """ Virtually private constructor. """
      if Classifier.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         """
         Hugging Face zero-shot classification pipeline
         """ 
         logging.debug("Classifier.__init__: pipeline creation...")
         self.pipeline = pipeline("ner", 
                        model=model,
                        tokenizer=model)
         logging.debug("Classifier.__init__: created!")   
         Classifier.__instance = self
   

   def infer(self, sequence: str) -> str:
        """
        Hugging Face token classification inference
        """   
        
        logging.info("Classifier.infer: infering for \"" + sequence + "\"...") 
        result = self.pipeline(sequence)
        logging.info("Classifier.infer: entities=\"" + json.dumps(result, cls=NpEncoder) + "\"")

        return {'entities': json.dumps(result, cls=NpEncoder)}