from django.test import TestCase

# Create your tests here.
# import csv
# import os
def testttt():
    import numpy as np, pandas as pd
    from skimage import io, color, img_as_ubyte
    from skimage.feature import greycomatrix, greycoprops
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split

    data = pd.read_csv('C:\\Fermier\\FermierApp\\App\\static\\features.csv')
    X = data.values[1:, 0:5]
    Y = data.values[1:, 5]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
    rgbImg = io.imread(r"C:\Fermier\FermierApp\App\static\\a.png")  # images of disease in rgb
    print(rgbImg, "jjjjjjjjjjjj")
    grayImg = img_as_ubyte(color.rgb2gray(rgbImg))  # images of disease gray
    print(grayImg)
    distances = [1, 2, 3]
    angles = [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4]

    glcm = greycomatrix(grayImg, distances=distances, angles=angles, symmetric=True, normed=True)

    properties = ['energy', 'homogeneity', 'dissimilarity', 'correlation', 'contrast']
    feats = np.hstack([greycoprops(glcm, 'energy').ravel() for prop in properties])
    feats1 = np.hstack([greycoprops(glcm, 'homogeneity').ravel() for prop in properties])
    feats2 = np.hstack([greycoprops(glcm, 'dissimilarity').ravel() for prop in properties])
    feats3 = np.hstack([greycoprops(glcm, 'correlation').ravel() for prop in properties])
    feats4 = np.hstack([greycoprops(glcm, 'contrast').ravel() for prop in properties])

    aa = []
    k = np.mean(feats)  # mean value of features
    l = np.mean(feats1)
    m = np.mean(feats2)
    n = np.mean(feats3)
    o = np.mean(feats4)
    aa.append(k)  # append to array aa
    aa.append(l)
    aa.append(m)
    aa.append(n)
    aa.append(o)

    arr = np.array([aa])
    rf = RandomForestClassifier(n_estimators=100)
    print("Start prediction===")
    rf.fit(X_train, Y_train)
    print(arr)
    cls = rf.predict(arr)

    print("Result=======", cls)
    return str(cls[0])
