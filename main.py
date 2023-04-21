# import pandas
# import sys
# from sklearn import svm
# sys.modules['sklearn.svm.classes'] = svm
# load1 = pandas.read_pickle('models/classifier_10class.pkl')

from mysvm import svm
Genre = svm.getGenre('classical_music.mp3')
print(1)