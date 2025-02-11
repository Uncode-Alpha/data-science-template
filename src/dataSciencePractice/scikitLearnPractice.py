import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn import linear_model, datasets
from sklearn.model_selection import train_test_split


#Scikit-Learn (sklearn) is a devoted machine learning platform introduced in Python.
#It provides simple and efficient tools for data mining and data analysis.

def linearRegression():
    #Used when a given target attribute is quantitative or continuous in nature

    # Load California housing dataset
    boston = fetch_california_housing()

    # Convert to DataFrame
    df = pd.DataFrame(boston.data, columns=boston.feature_names)
    df['PRICE'] = boston.target

    # Split data into training and test sets
    X = df.drop('PRICE', axis=1)
    X_train, X_test, y_train, y_test = train_test_split(
        X, df['PRICE'], test_size=0.33, random_state=42)

    # Train the Linear Regression model
    lm = LinearRegression()
    lm.fit(X_train, y_train)

    # Predict test values
    pred_test = lm.predict(X_test)

    # **Modify scatter plot (dot size & color)**
    plt.scatter(y_test, pred_test, color='blue', s=50, alpha=0.6, label="Data Points")  # s=50 makes dots larger

    # **Modify trend line (color & thickness)**
    plt.plot(np.unique(y_test), 
            np.poly1d(np.polyfit(y_test, pred_test, 1))(np.unique(y_test)),
            color='red', linewidth=3, label="Trend Line")  # Red trend line

    # Labels and legend
    plt.xlabel('Actual Price')
    plt.ylabel('Predicted Price')
    plt.legend()
    plt.grid(True)

    # Display feature coefficients
    coeff_df = pd.DataFrame({'Feature': X_train.columns, 'Coefficient': lm.coef_})
    print(coeff_df)

    # Calculate and print Mean Squared Error (MSE)
    mse = sklearn.metrics.mean_squared_error(y_test, pred_test)
    print("Mean Squared Error:", mse)

    # Show plot
    plt.show()

    return

def logisticRegression():
    #Used when a given target is categorical in nature, logistic regression gives
    #a bounded probability value between 0 and 1
    iris = datasets.load_iris() #Contains info of flower species
    X = iris.data[:, :2]  # Sepal Width and Sepal Height
    Y = iris.target       # Species -> Setosa, Versicolor, Virginica
    
    #Create a logistic regression model with a very large regularization parameter (c=1e5)
    #This also can mean no regularization
    lm = linear_model.LogisticRegression(C=1e5)
    #Train the model to classify the three species with sepal length and sepal width
    lm.fit(X, Y)
    # Range of X and Y axis, 0.5 added to avoid cutting off data points
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    # Step size in the mesh
    h = .02  
    # Creating Mesh Grid
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = lm.predict(np.c_[xx.ravel(), yy.ravel()])
    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)
    # Labeling
    plt.figure(1, figsize=(4, 3))
    plt.xlabel('Sepal length')
    plt.ylabel('Sepal width')
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(());
    plt.yticks(());
    
    plt.scatter(X[:, 0], X[:, 1],c=Y, edgecolors='k', cmap=plt.cm.Paired)
    plt.show()

    return

logisticRegression()