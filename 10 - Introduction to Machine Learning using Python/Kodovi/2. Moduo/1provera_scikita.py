from sklearn import datasets
 
iris = datasets.load_iris()

print("Dataset name:", iris['target_names'])
print("Feature names:", iris['feature_names'])
print("Number of instances:", len(iris['data']))