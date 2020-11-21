import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt 
plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import seaborn as sns

import get_data

def check_recession_logistic():
    def is_recession_cfnai_components(logmodel, df):
        result = logmodel.predict(df[['PANDI','EUANDH','CANDH','SOANDI']].iloc[-1:])[0]
        return result == 1

    def write_result(result_string):
        with open(output_directory + '/v002.txt', 'w') as f:
            f.write(result_string)
        print("Wrote results to " + output_directory)
    
    def export_chart(df):
        sns.set()
        plot_df = df[['USREC','prob_recession']].copy()
        plot_df.columns = ['Recession Periods', 'Probability of Current Recession']
        graph = plot_df.plot(figsize=(12,5))
        graph.get_figure().savefig(output_directory + '/v002.svg')

    result_string = ""
    try:
        df = get_data.get_combined_cfnai_recession_df()
        logmodel = LogisticRegression()
        logmodel.fit(df[['PANDI','EUANDH','CANDH','SOANDI']],df['USREC'])
        predictions = logmodel.predict_proba(df[['PANDI','EUANDH','CANDH','SOANDI']])
        predictions_df = pd.DataFrame(predictions, columns=['prob_no_recession','prob_recession'])
        result = is_recession_cfnai_components(logmodel, df)
        results_df = pd.concat([df.reset_index(),predictions_df.reset_index()], axis=1)
        export_chart(results_df.set_index('DATE'))
        if result:      
            result_string = "The United States appears to be in a recession with a probability of %.0f percent." % (100*results_df['prob_recession'][-1:],)
        else:
            result_string = "We are not in a recession, with a probability of %.0f percent." % (100*results_df['prob_no_recession'][-1:],)
    except:
        result_string = "We don't know! Something must have gone wrong with the crystal ball."
        result = None
        raise

    print(result_string)
    write_result(result_string)

    return result
