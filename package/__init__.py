import numpy 
import pandas
import json
from pypdf import PdfReader
from docx import Document
from typing import Dict
from read_file import Get_Path
from numpy.typing import NDArray
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score

# package tự viết
from save_file_json import Save_File_Json
from read_file import (
    Get_Path,
    Read_File_CSV,
    Read_File_PDF,
    Read_File_WORD
)
