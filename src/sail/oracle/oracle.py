#!/usr/bin/env python
"""Loads an oracle from a file and stores it. Provides functions to query optimal q value for a given node"""
import pickle
import json

class Oracle():
  def __init__(self):
    self.initialized = False
    self.cost_to_go = dict()
  
  def initialize(self, oracle_file, file_type="json"):
    if file_type=="pickle":
      try:
        with open(oracle_file, 'rb') as fh:
          self.cost_to_go = pickle.load(fh)
      except:
        print('Could not find pickle file at %s'%oracle_file)
    elif file_type=="json":
      try:
        with open(oracle_file, 'r') as fh:
          self.cost_to_go = json.load(fh)        
      except:
        print('Could not load json file at %s'%oracle_file)
    self.file_type = file_type
    self.initialized = True
    print('Oracle Computed')

  def get_optimal_q(self, node):
    if self.file_type == "json":
      node = str(node)

    if node in self.cost_to_go:
      q_val = self.cost_to_go[node]
      return q_val
    else:
      if not self.initialized:
        raise ValueError("Oracle not initialized yet")
      raise ValueError("Node not in graph")

  def clear(self):
    self.cost_to_go.clear()
    self.initialized = False
    

