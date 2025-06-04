import os


os.environ['OPENBLAS_NUM_THREADS'] = '1'
# from dataset_script import dataset

from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score

dataset = []

if __name__ == '__main__':
    C = int(input())
    P = int(input())

    good_set = [row for row in dataset if row[-1] == 'good']
    bad_set = [row for row in dataset if row[-1] == 'bad']

    if C == 0:
        train_set = good_set[:int(len(good_set) * (P / 100))] + bad_set[:int(len(bad_set) * (P / 100))]
        test_set = good_set[int(len(good_set) * (P / 100)):] + bad_set[int(len(bad_set) * (P / 100)):]
    else:
        train_set = good_set[int(len(good_set) * ((100 - P) / 100)):] + bad_set[int(len(bad_set) * ((100 - P) / 100)):]
        test_set = good_set[:int(len(good_set) * ((100 - P) / 100))] + bad_set[:int(len(bad_set) * ((100 - P) / 100))]

    train_X = [row[:-1] for row in train_set]
    train_X2 = []
    for row in train_X:
        new_row = []
        new_el = row[0] + row[-1]
        new_row.append(new_el)
        for i in range(len(row)):
            if i != 0 and i != len(row) - 1:
                new_row.append(row[i])

        train_X2.append(new_row)

    train_Y = [row[-1] for row in train_set]

    test_X = [row[:-1] for row in test_set]
    test_X2 = []
    for row in test_X:
        new_row = []
        new_el = row[0] + row[-1]
        new_row.append(new_el)
        for i in range(len(row)):
            if i != 0 and i != len(row) - 1:
                new_row.append(row[i])

        test_X2.append(new_row)
    test_Y = [row[-1] for row in test_set]

    classifier1 = GaussianNB()
    classifier1.fit(train_X2, train_Y)
    predictions1 = classifier1.predict(test_X2)

    scaler = MinMaxScaler(feature_range=(-1, 1))
    scaler.fit(train_X2)
    train_X2 = scaler.transform(train_X2)
    test_X2 = scaler.transform(test_X2)

    classifier2 = GaussianNB()
    classifier2.fit(train_X2, train_Y)
    predictions2 = classifier2.predict(test_X2)

    print(f"Tochnost so zbir na koloni: {accuracy_score(test_Y, predictions1)}")
    print(f"Tochnost so zbir na koloni i skaliranje: {accuracy_score(test_Y, predictions2)}")
