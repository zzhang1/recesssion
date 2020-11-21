import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import get_data

def check_recession_ma3():
    def is_recession_ma3(data):
        return data <= -0.7

    def write_result(result_string):
        with open(output_directory + '/v001.txt', 'w') as f:
            f.write(result_string)
        print("Wrote results to " + output_directory)
    
    def export_chart(df):
        sns.set()
        plot_df = df[['CFNAIMA3']].copy()
        plot_df['threshold'] = -0.7
        plot_df.columns = ['CFNAI 3-Month Avg', 'Recession Threshold']
        graph = plot_df.plot(figsize=(14,5))
        graph.set(xlabel=None)
        ymin, ymax = graph.get_ylim()
        graph.fill_between(plot_df.index, ymin, ymax, where=df['USREC'].values, color='gray', alpha=0.3)
        graph.get_figure().savefig(output_directory + '/v001.svg')

    result_string = ""
    try:
        df=get_data.get_combined_cfnai_recession_df().dropna()
        latest_row = df[-1:]
        latest_MA3 = latest_row.iloc[0]['CFNAIMA3']
        result = is_recession_ma3(latest_MA3)
        if result:      
            result_string = "The United States appears to be in a recession."
        else:
            result_string = "We are not in a recession."
        export_chart(df.set_index('DATE'))
    except:
        result_string = "We don't know! Something must have gone wrong with the crystal ball."
        result = None
        raise

    write_result(result_string)

    print(result_string)
    return result
