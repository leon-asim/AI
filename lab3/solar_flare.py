from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import accuracy_score

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]

if __name__ == '__main__':

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset_sample])

    train_set = dataset_sample[:int(len(dataset_sample) * 0.75)]
    train_X = [row[:-1] for row in train_set]
    train_Y = [row[-1] for row in train_set]
    train_X = encoder.transform(train_X)

    test_set = dataset_sample[int(len(dataset_sample) * 0.75):]
    test_X = [row[:-1] for row in test_set]
    test_Y = [row[-1] for row in test_set]
    test_X = encoder.transform(test_X)

    classifier = CategoricalNB()
    classifier.fit(train_X, train_X)

    predictions = classifier.predict(test_X)
    print(accuracy_score(test_Y, predictions))

    # entry = [el for el in input().split(" ")]
    # encoded_entry = encoder.transform([entry])
    # predicted_class = classifier.predict(encoded_entry)[0]
    # print(predicted_class)
    # print(classifier.predict_proba(encoded_entry))

    new_sample = input()
    new_sample = new_sample.split(' ')
    new_sample = encoder.transform([new_sample])

    predicted_class = classifier.predict(new_sample)[0]
    probabilities = classifier.predict_proba(new_sample)

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

# submit na encoderot
# submit_encoder(encoder)
