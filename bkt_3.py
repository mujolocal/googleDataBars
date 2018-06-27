"""
upwork.com
hubstaff.com
facebook groups
face to face and networks
use your networks
linkedin, fiverr, peopleperhour, angellist
"""
import datetime as dt
from bokeh.plotting import figure, show, output_file
from bokeh.models import formatters
import numpy as np

days = [1]
y_var = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13])
time_format = formatters.DatetimeTickFormatter()
time_format.hours = ["%H:%M"]
datetime = dt.datetime(2018,6,1,6)
one_hour = dt.timedelta(hours=1)
one_day = dt.timedelta(days=1)
time_var =[datetime]


for x in range(12):
    datetime = datetime+one_hour
    time_var.append(datetime)
    
for item in days:
    output_file("week1.html".format(item))
    p = figure( width = 750,height=750,title="Week of _____",x_axis_type="datetime", logo = None)#fill week
    
    p.xaxis.formatter= time_format
    p.yaxis.axis_label = "Population"
    p.xaxis.axis_label = "Time"
    p.circle(time_var,y_var**2-10*y_var,legend="{0}".format(item))
    p.line(time_var,y_var**2-10*y_var)
    show(p)