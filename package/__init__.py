# path_utils.py
import numpy 
import pandas
import json
from pathlib import Path
from pypdf import PdfReader
from docx import Document
from typing import Dict
from numpy.typing import NDArray
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
import os


