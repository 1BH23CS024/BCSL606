# Cell 1
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

# Cell 2
iris = load_iris()
X_pca = PCA(2).fit_transform(iris.data)

# Cell 3
for i, name in enumerate(iris.target_names):
    plt.scatter(X_pca[iris.target == i, 0], X_pca[iris.target == i, 1], label=name)

plt.title("PCA on Iris Dataset")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.legend()
plt.grid()
plt.show()
