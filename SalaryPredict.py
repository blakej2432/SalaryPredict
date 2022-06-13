sta_sal = pd.read_csv('c:/data/sta.csv')
sta_sal.info()

sta_sal.salary = sta_sal.salary.str.replace(',','')
sta_sal.salary = sta_sal.salary.astype('int64')
sta_sal.columns

del sta_sal['Unnamed: 0']

sta_sal
