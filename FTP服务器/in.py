import pickle

data = {'root':'root'}
with open(r'D:\wps\ftp_root\user_data.pkl', 'wb') as f:
    pickle.dump(data, f)
