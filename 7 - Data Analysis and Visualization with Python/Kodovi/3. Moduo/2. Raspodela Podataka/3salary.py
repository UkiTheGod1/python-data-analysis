import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pltdis import *

df = pd.read_csv("human_behavior_patterns.csv")
plot_distribution(df, "household_income", title="Salary Distribution", xlabel="Salary ($)")