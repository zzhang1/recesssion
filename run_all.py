import datetime
import v001
import v002
import v003
import v004

output_directory = '/var/www/html/results'

results_list = []

v001.output_directory = output_directory
results_list.append(v001.check_recession_ma3())

v002.output_directory = output_directory
results_list.append(v002.check_recession_logistic())

v003.output_directory = output_directory
results_list.append(v003.check_recession_logistic_lagged())

v004.output_directory = output_directory
results_list.append(v004.check_recession_logistic_lagged_f12m())

total = 0
true_count = 0
for result in results_list:
    if result is not None:
        total += 1
        if result:
            true_count += 1

prediction = (true_count / total) >= 0.5

combined_result = 'Nope!<br>We are not in a recession :)'
if prediction:
    combined_result = 'Yes!<br>We appear to be in a recession :('
with open(output_directory + '/combined_result.txt', 'w') as f:
    f.write(combined_result)


# Write timestamp of update date and time.
with open(output_directory + '/timestamp2.txt', 'w') as f:
    f.write('Last updated: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
    print('Wrote timestamp to ' + output_directory)
