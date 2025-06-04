# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset

dataset_sample = [['1', '35', '12', '5', '1', '100', '0'],
                  ['1', '29', '7', '5', '1', '96', '1'],
                  ['1', '50', '8', '1', '3', '132', '0'],
                  ['1', '32', '11.75', '7', '3', '750', '0'],
                  ['1', '67', '9.25', '1', '1', '42', '0']]

def transform_x(dataset):
    dataset2 = []
    for row in dataset:
        row2 = [float(el) for el in row]
        dataset2.append(row2)

    return dataset2

def transform_y(dataset):
    dataset2 = []
    for row in dataset:
        row2 = int(row)
        dataset2.append(row2)

    return dataset2

if __name__ == '__main__':
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score

    train_set = dataset_sample[:int(0.85 * len(dataset_sample))]
    train_X = [row[:-1] for row in train_set]
    train_X = transform_x(train_X)
    train_Y = [row[-1] for row in train_set]
    train_Y = transform_y(train_Y)

    test_set = dataset_sample[int(0.85 * len(dataset_sample)):]
    test_X = [row[:-1] for row in test_set]
    test_X = transform_x(test_X)
    test_Y = [row[-1] for row in test_set]
    test_Y = transform_y(test_Y)

    classifier = GaussianNB()
    classifier.fit(train_X, train_Y)

    predictions = classifier.predict(test_X)
    print(accuracy_score(test_Y, predictions))

    new_sample = input()
    new_sample = [float(el) for el in new_sample.split(' ')]

    predicted_class = classifier.predict([new_sample])[0]
    probabilities = classifier.predict_proba([new_sample])

    print(predicted_class)
    print(probabilities)


# Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
# klasifikatorot i encoderot so povik na slednite funkcii

# submit na trenirachkoto mnozestvo
# submit_train_data(train_X, train_Y)

# submit na testirachkoto mnozestvo
# submit_test_data(test_X, test_Y)

# submit na klasifikatorot
# submit_classifier(classifier)

# povtoren import na kraj / ne ja otstranuvajte ovaa linija