import pandas as pd


class Fixer:

    def fix_file(self, path):
        counter = 0
        with open(path) as input, open('../data/fixed.csv', 'w') as output:
            output.write("frameNum,x,y,objectNum,size,sequenceNum,TBD,TBD,TBD,filename,time,path time,delta time,TBD\n")
            for line in input:
                items = line.split(',')  # items is a list of strings
                if len(items) != 14:  # the line is OK as it stands
                    counter += 1
                    continue
                output.write(line.replace(', ', ','))
        print(f"{counter} removed lines")
        df = pd.read_csv('../data/fixed.csv', usecols=['objectNum', 'x', 'y', 'sequenceNum', 'filename', 'time'])
        df = df.drop_duplicates(subset=['objectNum', 'x', 'y', 'sequenceNum', 'filename', 'time'], keep=False)
        df = df.astype(
            {'x': 'uint16', 'y': 'uint16', 'objectNum': 'uint32', 'sequenceNum': 'uint32', 'time': 'datetime64[ns]',
             'filename': 'category'})
        df.to_pickle("../data/paths.pkl.xz")
