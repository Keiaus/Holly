from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import torch
from torch.jit import script, trace
import torch.nn as nn
from torch import optim
import torch.nn.functional as F
import csv
import random
import re
import os
import unicodedata
import codecs
from io import open
import itertools
import math
import json

USE_CUDA = torch.cuda.is_available()
device = torch.device("cuda" if USE_CUDA else "cpu")

corpus_name = "movie-corpus"
corpus = os.path.join("data", corpus_name)

def printLines(file, n=10):
    with open(file, 'rb') as datafile:
        lines = datafile.readlines()
    for line in lines[:n]:
        print(line)

printLines(os.path.join(corpus, "utterances.jsonl"))

# # Splits each line of the file to create lines and conversations
# def load_lines_and_conversations(filename):
#     lines = {}
#     conversations = {}
#     with open(filename, 'r', encoding='iso-8859-1') as f:
#         for line in f:
#             line_json = json.loads(line)
#             line_obj = {}
#             line_obj["lineID"] = line_json["id"]
#             line_obj["characterID"] = line_json["speaker"]
#             line_obj["text"] = line_json["text"]
#             lines[line_obj['lineID']] == line_obj

#             # Extract fields for conversations object
#             if line_json["conversation_id"] not in conversations:
#                 conv_obj = {}
#                 conv_obj["conversationsID"] = line_json["conversation_id"]
#                 conv_obj["movieID"] = line_json["meta"]["movie_id"]
#                 conv_obj["lines"] = [line_obj]
#             else:
#                 conv_obj = conversations[line_json["conversation_id"]]
#                 conv_obj["lines"].insert(0, line_obj)
#             conversations[conv_obj["conversationsID"]] = conv_obj

#     return lines, conversations

# def extract_sentence_pairs(conversations):
#     qa_pairs = []
#     for conversation in conversations.values():
#         # Iterate over all the lines of the conversation
#         for i in range(len(conversation["lines"]) - 1):
#             input_line = conversation["lines"][i]["text"].strip()
#             target_line = conversation["lines"][i+1]["text"].strip()
#             # Filter wrong samples (if one of the lists is empty)
#             if input_line and target_line:
#                 qa_pairs.append([input_line, target_line])

#     return qa_pairs

# # Define path to new file
# data_file = os.path.join(corpus, "formatted_movie_lines.txt")

# delimeter = '\t'
# # Unescape the delimete 
# delimeter = str(codecs.decode(delimeter, "unicode_escape"))

# # Initialize lines dict and conversations dict
# lines = {}
# conversations = {}
# # Load lines and conversations
# print("\nProcessing corpus into lines and conversations...")
# lines, conversations = load_lines_and_conversations(os.path.join(corpus, "utterances.jsonl"))

# # Write new csv file 
# print("\nWriting newly formatted file...")
# with open(data_file, 'w', encoding='utf-8') as output_file:
#     writer = csv.writer(output_file, delimiter=delimeter, lineterminator='\n')
#     for pair in extract_sentence_pairs(conversations):
#         writer.writerow(pair)

# # Print samples of lines
# print("\nSample lines from a file:")
# printLines(data_file)