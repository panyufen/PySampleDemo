import pickle


class PickleSample:


    @staticmethod
    def print():
        data1 = {'a': [1, 2.0, 3, 4 + 6j],
                 'b': ('string', u'Unicode string'),
                 'c': None,
                 "d": "汉字"}
        output = open('./files/data.pkl', 'wb')
        pickle.dump(data1, output)
        output.close()

        pkl_file = open('./files/data.pkl', 'rb')
        data1 = pickle.load(pkl_file)
        pkl_file.close()
        print(repr(data1))
