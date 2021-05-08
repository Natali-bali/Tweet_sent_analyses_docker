# from sent_an import sentAnalysis
# tweet = 'There are NOT enough Publix or other sites in Lee County and surrounding counties. Thank you for the data. Publix GREATLY needs to hire a data analyst to reallocate appointments.'
# newClass = sentAnalysis(tweet)
# result = newClass.easy()
# print(result)

import time
import datetime
from dateutil.parser import parse



date = "Thu Mar 04 07:50:57 +0000 2021"
dt = parse(date)
date = str(dt.date())+' '+str(dt.time())
print(time.mktime(datetime.datetime.strptime(date,
                        "%Y-%m-%d %H:%M:%S").timetuple()))



                        def parseDate(date):
    dt = parse(date)
    date = str(dt.date())+' '+str(dt.time())
    return time.mktime(datetime.datetime.strptime(date,
                            "%Y-%m-%d %H:%M:%S").timetuple())