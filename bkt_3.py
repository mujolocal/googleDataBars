# from bokeh.plotting import output_file, figure, show
# import numpy as np
# from bokeh.models.annotations import Span
# 
# 
# output_file = "boobsandbutts.html"
# x = np.linspace(0,20,200)
# y = np.sin(x)

# p = figure()
# p.line(x,y)
# 
# upper = Span(location=1,dimension="width",line_color="olive",line_width=4)
# p.add_layout(upper)
# 
# lower = Span(location=-1, dimension = "width",line_color="firebrick",line_width=4)
# p.add_layout(lower)
# 
# show(p)

# from bokeh.models.annotations import BoxAnnotation
# 
# upper = BoxAnnotation(bottom = 1,fill_alpha= 0.1,fill_color="olive")
# p.add_layout(upper)
# 
# lower = BoxAnnotation(top = -1, fill_alpha= 0.1, fill_color = "firebrick")
# p.add_layout(lower)
# 
# center = BoxAnnotation(top= 0.6,bottom = -0.3,left = 7, right = 12, fill_alpha=0.1,fill_color="navy")
# p.add_layout(center)
# 
# show(p)

# from bokeh.models.annotations import Label
#  # p = figure(x_range=(0,10),y_range=(0,10))
# p.circle(x,y, color="olive",size=10)
# label = Label(x=5,y=7, x_offset =12,text="Second Point",text_baseline="middle")
# p.add_layout(label)
# 
# show(p)
# 
# from bokeh.models import ColumnDataSource
# source = ColumnDataSource(data={
#     'x' : [1, 2, 3, 4, 5],
#     'y' : [3, 7, 8, 5, 1],
# })
# p.circle('x','y',size=20,source=source)
# show(p)


# 
# from bokeh.layouts import row, gridplot
# x = list(range(11))
# y0,y1,y2 = x,[10-i for i in x],[abs(i-5) for i in x]
# 
# s1 = figure(width=200, height= 350)
# s1.circle(x,y0,size=10,color="navy", alpha=0.5)
# 
# s2 = figure(width=450, height=250)
# s2.triangle(x,y1, size=10, color="firebrick", alpha=0.5)
# 
# s3 = figure(width=100, height=400)
# s3.square(x,y2,size=10,color="olive",alpha=0.5)
# 
# p = gridplot([[s1, s2], [s3, None]], toolbar_location=None)
# 
# show(p)


# from bokeh.models import TapTool, CustomJS, ColumnDataSource
# 
# callback = CustomJS(code="alert('hello world')")
# tap = TapTool(callback=callback)
# 
# p = figure(width=600, height = 300, tools=[tap])
# 
# p.circle(x=[1,2,3,4,5],y=[2,5,8,2,7], size = 20)
# 
# show(p)

# from bokeh.layouts import column
# from bokeh.models import CustomJS, ColumnDataSource, Slider
# 
# x = [x*0.005 for x in range(0, 201)]
# 
# source = ColumnDataSource(data=dict(x=x, y=x))
# 
# plot = figure(plot_width=400, plot_height=400)
# plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)
# 
# slider = Slider(start=0.1, end=6, value=1, step=.1, title="power")
# 
# update_curve = CustomJS(args=dict(source=source, slider=slider), code="""
#     var data = source.get('data');
#     var f = slider.value;
#     x = data['x']
#     y = data['y']
#     for (i = 0; i < x.length; i++) {
#         y[i] = Math.pow(x[i], f)
#     }
#     source.change.emit();
# """)
# slider.js_on_change('value', update_curve)
# 
# 
# show(column(slider, plot))

# from bokeh.layouts import column
# from bokeh.models import CustomJS, ColumnDataSource, Slider
# from random import random
# 
# x = [random() for x in range(500)]
# y = [random() for y in range(500)]
# color = ["navy"] * len(x)
# 
# s = ColumnDataSource(data=dict(x=x, y=y, color=color))
# p = figure(plot_width=400, plot_height=400, tools="lasso_select", title="Select Here")
# p.circle('x', 'y', color='color', size=8, source=s, alpha=0.4)
# 
# s2 = ColumnDataSource(data=dict(xm=[0,1],ym=[0.5, 0.5]))
# p.line(x='xm', y='ym', color="orange", line_width=5, alpha=0.6, source=s2)
# 
# s.callback = CustomJS(args=dict(s2=s2), code="""
#     var inds = cb_obj.get('selected')['1d'].indices;
#     var d = cb_obj.get('data');
#     var ym = 0
# 
#     if (inds.length == 0) { return; }
# 
#     for (i = 0; i < d['color'].length; i++) {
#         d['color'][i] = "navy"
#     }
#     for (i = 0; i < inds.length; i++) {
#         d['color'][inds[i]] = "firebrick"
#         ym += d['y'][inds[i]]
#     }
# 
#     ym /= inds.length
#     s2.get('data')['ym'] = [ym, ym]
# 
#     cb_obj.trigger('change');
#     s2.trigger('change');
# """)
# 
# show(p)

# from bokeh.plotting import figure, output_file, show, ColumnDataSource
# from bokeh.models import HoverTool
# 
# output_file("toolbar.html")
# # #add  tools 
# # TOOLS = 'crosshair,hover,reset,box_zoom'
# # #create a new plot with the toolbar below
# # p = figure(width=400, height =400, title=None, toolbar_location="below", tools=TOOLS)
# # p.circle([1,2,3,4,5],[2,5,8,2,7],size=10)
# # show(p)
# source = ColumnDataSource(
#     data=dict(
#         x=[1,2,3,4,5],
#         y=[2,5,8,2,7],
#         desc= ['a','b','c','d','e'],
#         red=["people","person","sheeple","sheep","man"]
#     )
# )
# hover = HoverTool(
#     tooltips=[
#         ("index","$index"),
#         ("(x,y)","($x,$y)"),
#         ("desc","@desc"),
#         ("red","@red")
#     ]
# )
# p = figure(width=400, height=400, tools=[hover], title= 
# "Mouse Over Data")
# p.circle("x","y",size=20,source=source)
# show(p)

from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import HoverTool
import numpy as np



make date stuff you dumbass






# import the formatters
from bokeh.models import formatters
# set an object == to type of formatter you want
time_format = formatters.DatetimeTickFormatter()
# modify format accordingly
time_format.hours = ["%H:%M"]

output_file("toolbar.html")
# #add  tools 
# TOOLS = 'crosshair,hover,reset,box_zoom'
# #create a new plot with the toolbar below
# p = figure(width=400, height =400, title=None, toolbar_location="below", tools=TOOLS)
# p.circle([1,2,3,4,5],[2,5,8,2,7],size=10)
# show(p)
source = ColumnDataSource(
hover = HoverTool(
    tooltips=[
        ("index","$index"),
        ("(x,y)","($x,$y)"),
        ("desc","@desc"),
        ("red","@red"),
    ]
)
x = 
p = figure(width=800, height=800, tools=[hover,""], title= 
"Mouse Over Data", x_axis_type="datetime")
# attach format to graph
p.xaxis.formatter= time_format
# set xaxis orientation to vertical
p.xaxis.major_label_orientation= "vertical"
p.circle()
show(p)