import os
import re
import numpy 
import pandas
import json
import numpy 
import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from pathlib import Path
from pypdf import PdfReader
from docx import Document
from typing import Dict
from numpy.typing import NDArray
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

