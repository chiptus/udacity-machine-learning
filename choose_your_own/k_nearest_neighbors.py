def create_and_train(features_train, labels_train, k = 5):
  from sklearn.neighbors import KNeighborsClassifier
  clf = KNeighborsClassifier(n_neighbors = k)
  clf.fit(features_train, labels_train)
  return clf
