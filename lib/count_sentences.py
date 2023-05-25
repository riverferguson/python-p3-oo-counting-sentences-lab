#!/usr/bin/env python3
from functools import reduce
import re 

class MyString:
  def __init__(self, value=""):
    self.value = value
  
  def get_value(self):
    return self._value 
  
  def set_value(self, stringValue):
    if(type(stringValue) == str):
      self._value = stringValue
    else:
      print('The value must be a string.')
      
  value = property(get_value, set_value)
  
  def is_sentence(self):
    return self._value.endswith(".")
  
  def is_question(self):
    return self._value.endswith("?")
  
  def is_exclamation(self):
    return self._value.endswith("!")
  
  def count_sentences(self):
    array_list = re.split(r"[.!?]", self.value)
    return reduce(lambda sum,el: sum + 1 if el != "" else sum, array_list, 0)
    
    
s = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
s.count_sentences()