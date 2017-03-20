def create_and_train(features_train, labels_train):
  from sklearn.ensemble import AdaBoostClassifier
  clf = AdaBoostClassifier()
  clf.fit(features_train, labels_train)
  return clf
