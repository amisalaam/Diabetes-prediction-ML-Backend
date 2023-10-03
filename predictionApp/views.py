from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


# Create your views here.

def home(request):
    return render(request, 'home.html')


def result(request):
    # LOADING DATASET USING PANDAS
    data = pd.read_csv('DataSet/diabetes.csv')

    # DATA TRAIN TEST SPLIT USING SK-LEARN
    X = data.drop("Outcome", axis=1)
    Y = data["Outcome"]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    # CREATING MODEL USING LOGISTIC REGRESSION
    model = LogisticRegression(solver='lbfgs', max_iter=1000)
    model.fit(X_train, Y_train)

    try:
        val1 = float(request.GET['n1'])
        val2 = float(request.GET['n2'])
        val3 = float(request.GET['n3'])
        val4 = float(request.GET['n4'])
        val5 = float(request.GET['n5'])
        val6 = float(request.GET['n6'])
        val7 = float(request.GET['n7'])
        val8 = float(request.GET['n8'])

        # Check for empty input values
        if val1 == '' or val2 == '' or val3 == '' or val4 == '' or val5 == '' or val6 == '' or val7 == '' or val8 == '':
            raise ValueError('Input values cannot be empty.')

        pred = model.predict(
            [[val1, val2, val3, val4, val5, val6, val7, val8]])

        output = 'Positive' if pred == 1 else 'Negative'

    except ValueError as e:
        output = str(e)

    return render(request, 'home.html', {"output": output})
