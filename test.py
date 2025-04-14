from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import pandas as pd
from Init_KMeans import Build_KMeans
from labels_points import Convert_labels_points
from pathlib import Path
def main():
    path = Path(__file__).parent / "test.json"

    X, y_true = make_blobs(n_samples=300, centers=3, cluster_std=1.0, random_state=42)    
    n_clusters = 3
    labels = Build_KMeans(n_clusters,X).get_labels()
    center_points = Build_KMeans(n_clusters,X).get_center_points()
    data_test = Convert_labels_points(path,X,labels,n_clusters).save_file_json()

main()