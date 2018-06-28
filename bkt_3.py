"""
upwork.com
hubstaff.com
facebook groups
face to face and networks
use your networks
linkedin, fiverr, peopleperhour, angellist
"""
import datetime as dt
import numpy as np
from bokeh.plotting import figure, show, output_file,ColumnDataSource
from bokeh.models import formatters
from bokeh.models.tools import HoverTool
from dem_simulator import Demographics as Dem

colors = [
"#c6e3cb",
"#9ed5cd",
"#83cacf",
"#47aed0",
"#3984b6",
"#2c5a9c",
"#1e3082",
]
name_o_days = [
"Monday",
"Tuesday",
"Wednesday",
"Thursday",
"Friday",
"Saturday",
"Sunday",
]

dem = Dem()
dem.create_week_pop()
dem.create_week_volume()
dem.create_week_density()
days = [1]

time_format = formatters.DatetimeTickFormatter()
time_format.hours = ["%H:%M"]
datetime = dt.datetime(2018,6,1,6)
one_hour = dt.timedelta(hours=1)
one_day = dt.timedelta(days=1)
time_var =[datetime]




output_file("week1.html")
p = figure( width = 1200,height=650,title="Week",x_axis_type="datetime", logo = None,tools="pan, wheel_zoom,reset", active_drag="pan")#fill week    
for day in range(7):
    time_var = [datetime]
    hours_open = len(dem.week_pop[day])-1
    for x in range(hours_open):
        datetime = datetime+one_hour
        time_var.append(datetime)
    # datetime= datetime+one_day
    datetime = datetime - hours_open*one_hour
    source = ColumnDataSource(dict(
        x=time_var,
        y=dem.week_pop[day],
        volume=dem.week_volume[day],
        density=dem.week_density[day],


    ))
    hover = HoverTool()
    hover.tooltips = [
        ("(x,y)","($x,$y)"),
        ("volume","@volume"),
        ("density","@density")

    ]
    
    
    p.xaxis.formatter= time_format
    p.yaxis.axis_label = "Population"
    p.xaxis.axis_label = "Time"
    p.circle("x","y",source=source,legend="{0}".format(name_o_days[day]),color = colors[day])
    p.line("x","y",source=source,color = colors[day])
p.tools.append(hover)
show(p)