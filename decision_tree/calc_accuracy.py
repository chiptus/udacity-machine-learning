def create_classifier(min_samples_split=40):
    from sklearn.tree import DecisionTreeClassifier
    return DecisionTreeClassifier(min_samples_split=min_samples_split)

def train_classifier(clf, features_train, labels_train):
    clf.fit(features_train, labels_train)
    return clf

def calc_accuracy(trained_clf, features_test, labels_test):
    from sklearn.metrics import accuracy_score
    preds = trained_clf.predict(features_test)
    return accuracy_score(labels_test, preds)

def train_and_calc_acc(features_train, features_test, labels_train, labels_test, min_samples_split=40):
  clf = create_classifier(min_samples_split=min_samples_split)
  trained_clf = train_classifier(clf, features_train, labels_train)
  return calc_accuracy(trained_clf, features_test, labels_test)