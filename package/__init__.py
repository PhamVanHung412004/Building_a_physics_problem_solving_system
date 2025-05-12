import os
import re
import numpy 
import pandas
import json
import faiss
import torch
import json
from groq import Groq
from sentence_transformers import SentenceTransformer
import ast
from pathlib import Path
from pypdf import PdfReader
from docx import Document
from typing import Dict
from numpy.typing import NDArray
import streamlit

