from typing import Optional, List, Dict

from collections import defaultdict
from dataclasses import dataclass
import numpy as np

from sklearn.datasets import load_iris


features = ["petal_length", "petal_width"]

class Tree:
    feature: str
    split_point: int
    datapoints: List[Dict] = []
    left = None
    right = None

data = load_iris()

datapoints = []

for index in range(len(data.data)):
    datapoints.append({
        "class": data.target[index],
        "petal_length": data.data[index, 2],
        "petal_width": data.data[index, 3],
    })


def calculate_gini(datapoints):
    classes = defaultdict(int)
    for point in datapoints:
        classes[point["class"]] += 1

    total = sum(classes.values())
    probs = 0
    for val in classes.values():
        probs += (val/total) ** 2
    
    return 1 - probs


def get_split_points(datapoints, feature):
    values = [point[feature] for point in datapoints]
    return np.linspace(min(values), max(values), 10)

def split(datapoints, split_point, feature):

    left = []
    right = []
    for datapoint in datapoints:
        if datapoint[feature] < split_point:
            left.append(datapoint)
        else:
            right.append(datapoint)

    return left, right

def find_best_tree(datapoints, depth):
    if len(datapoints) == 0:
        return datapoints

    if depth == 2:
        return datapoints
    
    best = 100
    best_left, best_right, best_feat = None, None, None
    best_split_point = None
    n = len(datapoints)
    for feature in features:
        split_points = get_split_points(datapoints, feature)
        for split_point in split_points:
            left, right = split(datapoints, split_point, feature)
            gini = len(left)/n * calculate_gini(left) + len(right)/n * calculate_gini(right)
            if gini < best:
                best = gini
                best_split_point = split_point
                best_left = left
                best_right = right
                best_feat = feature
  
    t = Tree()
    t.feature = best_feat
    t.split_point = best_split_point
    t.datapoints = datapoints
    if best_left != 0 and best_right != 0:
        t.left = find_best_tree(best_left, depth + 1)
        t.right = find_best_tree(best_right, depth + 1)

    return t

tree = find_best_tree(datapoints, 0)