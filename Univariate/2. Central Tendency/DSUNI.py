class Univariate():
    def quanqual(dataset):
        qual=[]
        quan=[]
        for columnName in dataset.columns:
            if(dataset[columnName].dtypes=='O'):
                qual.append(columnName)
            else:
                quan.append(columnName)
        return quan,qual

    def freqtable(columnName,dataset):
        freqtable=pd.DataFrame(columns=['unique_values','frequency','relative_frequency','cusum'])
        freqtable['unique_values']= dataset[columnName].value_counts().index
        freqtable['frequency']= dataset[columnName].value_counts().values
        freqtable['relative_frequency']= freqtable['frequency']/215
        #there is an inbuilt function for Cumulative frequency
        freqtable['cusum']= freqtable['relative_frequency'].cumsum()
        return freqtable

    def Univariate(quan,dataset):
         descriptive= pd.DataFrame(index=['mean','median','mode','Q1:25th','Q2:50th',                                                                                              'Q3:75th','99th','Q4:100th','IQR','1.5RULE','LESSER','GREATER','min','max'], columns=quan)
        for columnName in quan:
            descriptive[columnName]["mean"] = dataset[columnName].mean()
            descriptive[columnName]["median"] = dataset[columnName].median()
            descriptive[columnName]["mode"] = dataset[columnName].mode()[0]
            descriptive[columnName]["Q1:25th"] = dataset.describe()[columnName]['25%']
            descriptive[columnName]["Q2:50th"] = dataset.describe()[columnName]['50%']
            descriptive[columnName]["Q3:75th"] = dataset.describe()[columnName]['75%']
            descriptive[columnName]["99th"] = np.percentile(dataset[columnName],99)
            descriptive[columnName]["Q4:100th"] = dataset.describe()[columnName]['max']
            descriptive[columnName]["IQR"]= descriptive[columnName]["Q3:75th"]- descriptive[columnName]["Q1:25th"] 
            descriptive[columnName]["1.5RULE"] = 1.5* descriptive[columnName]["IQR"]
            descriptive[columnName]["LESSER"]=  descriptive[columnName]["Q1:25th"] - descriptive[columnName]["1.5RULE"]
            descriptive[columnName]["GREATER"]= descriptive[columnName]["Q3:75th"]+ descriptive[columnName]["1.5RULE"]
            # MAX AND MIN ARE FOUND FROM THE DATASET TABLE ANED NOT DESCRIPTIVE TABLE
            descriptive[columnName]["min"]=dataset[columnName].min()
            descriptive[columnName]["max"]=dataset[columnName].max()
        return descriptive
 
    def find_outliers(quan,descriptive):
        lesser=[]
        greater=[]
        for columnName in quan:
            if (descriptive[columnName]['min']<descriptive[columnName]['LESSER']):
                lesser.append(columnName)
            if(descriptive[columnName]['max']>descriptive[columnName]['GREATER']):
                greater.append(columnName)
        return lesser, greater

     def replace_outlier(lesser,greater,dataset,descriptive):
        for columnName in lesser:
            dataset[columnName][dataset[columnName]< descriptive[columnName]['LESSER']] = descriptive[columnName]['LESSER']
            #Here all the cell value of a particular column is cgecked with descriptive column cell value
        for columnName in greater:
            dataset[columnName][dataset[columnName]> descriptive[columnName]['GREATER']] = descriptive[columnName]['GREATER']
        return dataset   














