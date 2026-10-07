# Machine Learning

This directory contains machine learning algorithms implemented from scratch in Python and NumPy.

The goal is to understand the mathematical and computational foundations behind machine learning models rather than relying entirely on existing machine learning libraries.

## Algorithms

### Linear Regression
Predicts a continuous numerical value by modeling the relationship between input features and a target variable.

- **Type:** Supervised Learning
- **Task:** Regression
- **Key Concepts:** Least Squares, Mean Squared Error, Gradient Descent

### Logistic Regression
Predicts the probability of an observation belonging to a class.

- **Type:** Supervised Learning
- **Task:** Classification
- **Key Concepts:** Sigmoid Function, Binary Classification, Gradient Descent

### K-Nearest Neighbors (KNN)
Classifies or predicts a value based on the closest observations in the dataset.

- **Type:** Supervised Learning
- **Task:** Classification / Regression
- **Key Concepts:** Distance, Neighbors, Feature Scaling

### Decision Tree
Makes predictions by recursively splitting data based on feature values.

- **Type:** Supervised Learning
- **Task:** Classification / Regression
- **Key Concepts:** Entropy, Information Gain, Tree Splitting

### K-Means Clustering
Groups observations into clusters based on their similarity.

- **Type:** Unsupervised Learning
- **Task:** Clustering
- **Key Concepts:** Centroids, Distance, Iterative Optimization

## Implementation Philosophy

The implementations in this directory are primarily written using:

- Python
- NumPy

External machine learning libraries such as Scikit-learn are avoided when implementing the core algorithms so that the underlying mathematics and mechanics can be understood.

## Learning Goals

Through these implementations, I aim to develop a deeper understanding of:

- Machine learning mathematics
- Optimization
- Model training
- Loss functions
- Gradient descent
- Classification and regression
- Overfitting and generalization
- Model evaluation
- Numerical computation
