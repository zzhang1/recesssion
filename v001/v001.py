import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def check_recession_ma3():
    def is_recession_ma3(data):
        return data <= -0.7

    def write_result(result_string):
        with open(output_directory + '/v001.txt', 'w') as f:
            f.write(result_string)
        print("Wrote results to " + output_directory)

    def export_chart(df):
        sns.set()
        plot_df = df[['USREC', 'CFNAIMA3']].copy()
        plot_df['threshold'] = -0.7
        plot_df.columns = ['Recession Periods', 'CFNAI 3-Month Avg', 'Recession Threshold']
        graph = plot_df.plot(figsize=(12,5))
        graph.get_figure().savefig(output_directory + '/v001.svg')

    result_string = ""
    try:
        df=get_combined_cfnai_recession_df().dropna()
        latest_row = df[-1:]
        latest_MA3 = latest_row.iloc[0]['CFNAIMA3']
        result = is_recession_ma3(latest_MA3)
        if result:
            result_string = "Uh oh, the United States appears to be in a recession!"
        else:
            result_string = "Nope! We are not in a recession."
    except:
        result_string = "We don't know! Something must have gone wrong with the crystal ball."

    write_result(result_string)
    export_chart(df)

    print(result_string)
    return result
