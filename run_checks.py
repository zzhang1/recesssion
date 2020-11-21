import datetime
from v001 import check_recession as v001

output_directory = '/var/www/html/results'

v001.check_recession_ma3()


# Write timestamp of update date and time.
with open(output_directory + '/timestamp.txt', 'w') as f:
	f.write('Last updated: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
	print('Wrote timestamp to ' + output_directory)

