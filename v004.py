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

# Check recession with 12 lagged variables (lag on trailing 12 month)
def check_recession_logistic_lagged_f12m():
    def is_recession_cfnai_components(logmodel, df):
        result = logmodel.predict(df[lagged_variables].iloc[-1:])[0]
        return result == 1

    def write_result(result_string):
        with open(output_directory + '/v004.txt', 'w') as f:
            f.write(result_string)
        print("Wrote results to " + output_directory)
    
    def export_chart(df):
        df = df.set_index('DATE')
        sns.set()
        plot_df = df[['prob_recession']].copy()
        plot_df.columns = ['Probability of Recession Within a Year']
        graph = plot_df.plot(figsize=(14,5))
        graph.set(xlabel=None)
        ymin, ymax = graph.get_ylim()
        graph.fill_between(plot_df.index, ymin, ymax, where=df['USREC'].values, color='gray', alpha=0.3)
        graph.get_figure().savefig(output_directory + '/v004.svg')

    result_string = ""
    try:
        df = get_data.get_combined_cfnai_recession_df()
        
        #Lag all dummy variables 12 months
        variables = ['PANDI', 'EUANDH', 'CANDH', 'SOANDI', 'CFNAIDIFF']
        lagged_variables = variables.copy()
        lagged_df = df.copy()
        for var in variables:
            for i in range(1,12):
                lagged_df[var+str(i)] = df[var].shift(i)
                lagged_variables.append(var+str(i))

        #Forward lag recession so that any recession in next 12 months is counted as 1 currently
        lagged_df['USREC_fw_lag'] = 0
        for i in range(1,12):
            lagged_df['USREC_fw_lag'] += df['USREC'].shift(-i)
        lagged_df['USREC_fw_lag'] = lagged_df['USREC_fw_lag'].clip(0,1)
        lagged_df = lagged_df.interpolate(method='linear', limit_direction ='forward')  # Very important--keep forward-lagged variable as we can't see 12 months into real future.
        lagged_df = lagged_df.dropna().reset_index()
        logmodel = LogisticRegression()
        logmodel.fit(lagged_df.iloc[:-3,:][lagged_variables],lagged_df.iloc[:-3,:]['USREC_fw_lag'])
        predictions = logmodel.predict_proba(lagged_df[lagged_variables])
        predictions_df = pd.DataFrame(predictions, columns=['prob_no_recession','prob_recession'])
        results_df = pd.concat([lagged_df,predictions_df], axis=1)
        result = is_recession_cfnai_components(logmodel, lagged_df)
        export_chart(results_df)
        if result:      
            result_string = "A recession appears to be headed our way with a probability of %.0f percent. Of course, the recession may already be here..." % (100*results_df['prob_recession'][-1:],)
        else:
            result_string = "Imminent recession is unlikely, with a probability of %.0f percent." % (100*results_df['prob_no_recession'][-1:],)
    except:
        result_string = "We don't know! Something must have gone wrong with the crystal ball."
        result = None
        raise

    print(result_string)
    write_result(result_string)

    return result
