#!/usr/bin/env python3

class MyString:
  def __init__ (self, value = ""):
    self.value = value
    
  @property
  def value(self):
    return self._value
  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")


  def is_sentence(self):
    return self.value.endswith(".")
  
  def is_question(self):
    return self.value.endswith("?")
  
  def is_exclamation(self):
    return self.value.endswith("!")

  def count_sentences(self):
    with_out_question_mark = self.value.replace("?", ".")
    with_out_exclamation = with_out_question_mark.replace("!", ".")
    sentence_list = with_out_exclamation.split(".")
    edge_list = []
    for sentence in sentence_list:
      if sentence != "":
        edge_list.append(sentence)
      
    return len(edge_list)
  
  pass
