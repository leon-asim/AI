# import os
#
# os.environ['OPENBLAS_NUM_THREADS'] = '1'
# from submission_script import *
# from dataset_script import dataset

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset = [[180.0, 23.6, 25.2, 27.9, 25.4, 14.0, 'Roach'],
                  [12.2, 11.5, 12.2, 13.4, 15.6, 10.4, 'Smelt'],
                  [135.0, 20.0, 22.0, 23.5, 25.0, 15.0, 'Perch'],
                  [1600.0, 56.0, 60.0, 64.0, 15.0, 9.6, 'Pike'],
                  [120.0, 20.0, 22.0, 23.5, 26.0, 14.5, 'Perch']]

if __name__ == '__main__':
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score

    col_index = int(input())
    num_trees = int(input())
    criterion = input()

    train_set = dataset[:int(len(dataset) * 0.85)]
    train_set2 = []
    for row in train_set:
        new_row = [row[i] for i in range(len(row)) if i != col_index]
        train_set2.append(new_row)
    train_set = train_set2
    train_X = [row[:-1] for row in train_set]
    train_Y = [row[-1] for row in train_set]

    test_set = dataset[int(len(dataset) * 0.85):]
    test_set2 = []
    for row in test_set:
        new_row = [row[i] for i in range(len(row)) if i != col_index]
        test_set2.append(new_row)
    test_set = test_set2
    test_X = [row[:-1] for row in test_set]
    test_Y = [row[-1] for row in test_set]

    classifier = RandomForestClassifier(n_estimators=num_trees, criterion=criterion, random_state=0)
    classifier.fit(train_X, train_Y)

    predictions = classifier.predict(test_X)


    new_sample = input()
    new_sample = [float(el) for el in new_sample.split(' ')]
    new_sample = [new_sample[i] for i in range(len(new_sample)) if i != col_index]

    new_prediction = classifier.predict([new_sample])[0]

    print(f"Accuracy: {accuracy_score(test_Y, predictions)}")
    print(new_prediction)
    print(classifier.predict_proba([new_sample])[0])

# Na kraj potrebno e da napravite submit na podatochnoto mnozestvo
# i klasifikatorot so povik na slednite funkcii

# submit na trenirachkoto mnozestvo
# submit_train_data(train_X, train_Y)

# submit na testirachkoto mnozestvo
# submit_test_data(test_X, test_Y)

# submit na klasifikatorot
# submit_classifier(classifier)
