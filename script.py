import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from PIL import Image


train_df = pd.read_csv("mnist_train.csv")
test_df  = pd.read_csv("mnist_test.csv")

train_images = dict()
test_images  = dict()


