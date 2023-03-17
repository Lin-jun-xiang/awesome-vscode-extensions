import numpy as np
from collections import Counter
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

def entropy(y):
    """
    Parameters
    ----------
    y : labels of class, ex: 0, 1

    Variables
    ---------
    ps : probability of each labels

    Returns
    -------
    Entropy : I(p) = -Sum(pi * log(pi))
    """
    hist = np.bincount(y)
    ps = hist / len(y)

    return -np.sum([p * np.log2(p) for p in ps if p > 0])

class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, *, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

    def is_leaf_node(self):
        return self.value is not None

class DecisionTree:
    def __init__(self, min_samples_split=2, max_depth=100, n_features=None):
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        self.n_features = n_features
        self.root = None

    def fit(self, X, y):
        # grow tree
        self.n_features = X.shape[1] if not self.n_features else min(self.n_features, X.shape[1])
        self.root = self._grow_tree(X, y)

    def _grow_tree(self, X, y, depth=0):
        n_samples, n_features = X.shape
        n_labels = len(np.unique(y))

        # stopping criteria
        if (depth >= self.max_depth or n_labels == 1 or n_samples < self.min_samples_split):
            leaf_value = self._most_common_label(y)

            return Node(value=leaf_value)

        feat_idxs = np.random.choice(n_features, self.n_features, replace=False)

        # greedy search
        best_feat, best_thresh = self._best_criteria(X, y, feat_idxs)
        # split
        left_idxs, right_idxs = self._split(X[:, best_feat], best_thresh)

        # recursion for grow tree
        left = self._grow_tree(X[left_idxs, :], y[left_idxs], depth+1)
        right = self._grow_tree(X[right_idxs, :], y[right_idxs], depth+1)

        return Node(best_feat, best_thresh, left, right)

    def _best_criteria(self, X, y, feat_idxs):
        best_gain = -1
        split_idx, split_thresh = None, None

        for feat_idx in feat_idxs:
            X_column = X[:, feat_idx]
            thresholds = np.unique(X_column)

            for threshold in thresholds:
                gain = self._information_gain(y, X_column, threshold)

                if gain > best_gain:
                    best_gain = gain
                    split_idx, split_thresh = feat_idx, threshold

        return split_idx, split_thresh

    def _information_gain(self, y, X_column, split_thresh):
        """
        Returns
        -------
        Information gain : IG(p, feature) = I_parent - Sum(I_son_i)
        """
        # get the entropy of parent node (I_parent)
        parent_entropy = entropy(y)

        # generate split
        left_idxs, right_idxs = self._split(X_column, split_thresh)

        if len(left_idxs) == 0 or len(right_idxs) == 0:
            # IG = 0, means the split is meaningless
            return 0

        # weighted avg child E
        n = len(y)
        n_l, n_r = len(left_idxs), len(right_idxs)
        # get the entropy of son nodes (I_son_i)
        e_l, e_r = entropy(y[left_idxs]), entropy(y[right_idxs])
        child_entropy = (n_l/n) * e_l + (n_r/n) * e_r

        ig = parent_entropy - child_entropy

        return ig

    def _split(self, X_column, split_thresh):
        # split data by threshold
        left_idxs = np.argwhere(X_column <= split_thresh).flatten()
        right_idxs = np.argwhere(X_column > split_thresh).flatten()

        return left_idxs, right_idxs

    def predict(self, X):
        # traverse tree
        return np.array([self._traverse_tree(x, self.root) for x in X])

    def _traverse_tree(self, x, node):
        if node.is_leaf_node():
            return node.value

        if x[node.feature] <= node.threshold:
            return self._traverse_tree(x, node.left)

        return self._traverse_tree(x, node.right)

    def _most_common_label(self, y):
        counter = Counter(y)

        return counter.most_common(1)[0]

def visualize_classifier(model, X, y, ax=None, cmap="rainbow"):
    ax = ax or plt.gca()

    ax.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=cmap, clim=(y.min(), y.max()), zorder=3)
    ax.axis("tight")
    ax.axis("off")
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    model.fit(X, y)
    xx, yy = np.meshgrid(np.linspace(*xlim, num=200),
                         np.linspace(*ylim, num=200))

    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])[:, 0].reshape(xx.shape[0], yy.shape[0])

    n_class = len(np.unique(y))
    contours = ax.contourf(xx, yy, Z, alpha=0.3,
                           levels=np.arange(n_class+1) - 0.1,
                           cmap=cmap, clim=(y.min(), y.max()),
                           zorder=1)
    ax.set(xlim=xlim, ylim=ylim)

if __name__ == "__main__":
    X, y = make_blobs(n_samples=300,
                  centers=4,
                  random_state=0,
                  cluster_std=1.)

    model = DecisionTree()
    visualize_classifier(model, X, y)
