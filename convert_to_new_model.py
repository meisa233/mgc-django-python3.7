import pickle
from sklearn.externals import joblib
def rename_attribute(obj, old_name, new_name):
    obj.__dict__[new_name] = obj.__dict__.pop(old_name)
# with open('/path/to/old.pkl', 'rb') as f:
#     pkl = pickle.load(f)
pkl = joblib.load('/path/to/old.pkl')
rename_attribute(pkl, 'n_support_', '_n_support')
rename_attribute(pkl, 'probA_', '_probA')
rename_attribute(pkl, 'probB_', '_probB')
setattr(pkl, 'break_ties', False)
with open('/path/to/new.pkl', 'wb') as f:
    pickle.dump(pkl, f)