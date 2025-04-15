import numpy as np
from numpy.typing import NDArray
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
import matplotlib.pyplot as plt

class Eblow:
    def __init__(self, data : NDArray[np.float32]) -> None:
        '''
        data : Là một vector chứa dữ liệu ban đầu chưa có nhãn
        '''
        self.__data :  NDArray[np.float32] = data
        
    def show(self) -> None:        
        model = KMeans()
        show_screen = KElbowVisualizer(model, k = (1,100))
        fig = plt.figure(figsize=(10,8))
        show_screen.fit(self.__data)
        show_screen.poof()  





