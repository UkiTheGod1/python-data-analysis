import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pltdis import *

df = pd.read_csv("human_behavior_patterns.csv")
plot_distribution(df, "store_visit_hour", title="Store Visit Distribution", xlabel="Hours")