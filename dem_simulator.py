import numpy as np
"""
from dem_simulator import Demographics as Dem
dem = Dem()
dem.create_week_data()
"""
class Demographics(object):
    # template data form == [
    # [0day_of_the_week,1[hours of the day],2[pop data for hour]],
    # ]

    # Density == current_pop/max_pop*10 rounded
    # guy 2 girl == based on last g t g and random based
    # age will be a std random number at what ever
    # num employees current_pattrons/4 min 2
    # music is music music affects population -1 +1
    # event is event affects +2 -1
    #
    week_template_data = [['Monday', ['6 AM', '7 AM', '8 AM', '9 AM', '10 AM', '11 AM', '12 PM', '1 PM', '2 PM', '3 PM', '4 PM', '5 PM', '6 PM', '7 PM', '8 PM'], [17, 38, 57, 66, 59, 46, 35, 37, 48, 62, 68, 64, 51, 33, 17]], ['Tuesday', ['6 AM', '7 AM', '8 AM', '9 AM', '10 AM', '11 AM', '12 PM', '1 PM', '2 PM', '3 PM', '4 PM', '5 PM', '6 PM', '7 PM', '8 PM'], [12, 30, 51, 68, 74, 68, 60, 57, 58, 62, 60, 53, 42, 29, 17]], ['Wednesday', ['6 AM', '7 AM', '8 AM', '9 AM', '10 AM', '11 AM', '12 PM', '1 PM', '2 PM', '3 PM', '4 PM', '5 PM', '6 PM', '7 PM', '8 PM'], [8, 26, 47, 66, 75, 71, 60, 53, 49, 50, 49, 44, 37, 26, 15]], ['Thursday', ['6 AM', '7 AM', '8 AM', '9 AM', '10 AM', '11 AM', '12 PM', '1 PM', '2 PM', '3 PM', '4 PM', '5 PM', '6 PM', '7 PM', '8 PM'], [13, 28, 44, 58, 64, 62, 57, 55, 58, 62, 64, 58, 47, 32, 19]], ['Friday', ['6 AM', '7 AM', '8 AM', '9 AM', '10 AM', '11 AM', '12 PM', '1 PM', '2 PM', '3 PM', '4 PM', '5 PM', '6 PM', '7 PM', '8 PM'], [28, 46, 57, 57, 50, 44, 46, 55, 65, 67, 60, 46, 28, 13, 3]], ['Saturday', ['7 AM', '8 AM', '9 AM', '10 AM', '11 AM', '12 PM', '1 PM', '2 PM', '3 PM', '4 PM', '5 PM', '6 PM', '7 PM', '8 PM'], [17, 39, 62, 73, 73, 68, 65, 64, 58, 49, 37, 24, 13, 5]], ['Sunday', ['7 AM', '8 AM', '9 AM', '10 AM', '11 AM', '12 PM', '1 PM', '2 PM', '3 PM', '4 PM', '5 PM', '6 PM', '7 PM', '8 PM'], [17, 39, 57, 63, 63, 63, 61, 53, 50, 59, 68, 60, 37, 15]]]
    max_capacity = 75
    #population is pop guy girl
    week_data = []
    # volume out of 10
    music_type_optimum = 2
    music_volume =2
    volume_optimum = 4
    #density out of 10
    density_optimum = 4
    num_employees = None
    ave_patron_age = 19
    last_metric = None
    
    # starting with mondays the weeks population
    week_pop = []
    week_volume = []
    week_density = []
    
    
    # hour_o_day =  [
    # "730","830","930","1030","1130","1230","1330","1430","1530","1630"
    # ,"1730","1830","1930","2030","2130",
    # ]
    hour_o_day =[i for i in range(15)]
    









    """docstring for ."""
    def __init__(self,templateData= None, capacity = None):
        if templateData != None:
            self.templateData = templateData
        if capacity != None:
            self.max_capacity = capacity

    def create_week_data(self):
        for day in self.week_template_data:
            temp_day_data = []
            temp_music = np.random.randint(1,6)
            self.last_metric = {
            "den":0,
            "vol":self.music_volume,
            "mus":temp_music,
            "g2g":0,
            "age":0,
            "pop":0,
            }
            temp_set = False
            for metric in day[2]:
                if temp_set:
                    temp_population = (
                    metric
                    +self.norm_metric(self.density_optimum,self.last_metric["den"])
                    +self.norm_metric(self.volume_optimum,self.last_metric["vol"])
                    +self.norm_metric(self.music_type_optimum,self.last_metric["mus"]
                    )
                    +self.norm_metric(self.ave_patron_age,self.last_metric["age"])
                    )
                else:
                    temp_population = metric
                    temp_set = True
                temp_density = np.round(temp_population/self.max_capacity*10)
                temp_volume = np.round(temp_density/2+self.music_volume)
                temp_volume = temp_volume if temp_volume >1 else 2
                g2g_ratio = np.round(np.random.normal(3,2/3))
                patron_age = np.random.exponential(21)
                patron_age = patron_age if patron_age > 18 else 18
                patron_age = patron_age if patron_age < 120 else 120
                self.last_metric = {
                "den":temp_density,
                "vol":temp_volume,
                "mus":temp_music,
                "g2g":g2g_ratio,
                "age":20,
                "pop":temp_population,
                }
                temp_day_data.append(self.last_metric)

            self.week_data.append(temp_day_data)

    def norm_metric(self, optimum, real):
        # normalizes all features so they may be added to random ness
        x = np.abs(optimum-real)
        if x==0:
            return 5
        elif x==1:
            return 3
        elif x==2:
            return -3
        elif x>2:
            return -7
            
    def set_optimum(density,volume,music_type, patron_age):
        # set the values that are normalized agaianst
        self.density_optimum = density
        self.volume_optimum = volume
        self.music_type_optimum = music_type
        self.ave_patron_age = patron_age
    
    def create_week_pop(self):
        # create one week of data
        if self.week_data == []:
            self.create_week_data()
        for x in range(len(self.week_data)):
            temp_array = self.iso_varibble(self.week_data[x],"pop")
            self.week_pop.append(temp_array)
            
    def create_week_volume(self):
        if self.week_data == []:
            self.create_week_data()
        for x in range(len(self.week_data)):
            temp_array = self.iso_varibble(self.week_data[x],"vol")
            self.week_volume.append(temp_array)
    
    def create_week_density(self):
        if self.week_data == []:
            self.create_week_data()
        for x in range(len(self.week_data)):
            temp_array = self.iso_varibble(self.week_data[x],"den")
            self.week_density.append(temp_array)
    
    def create_month_pop(self):
        if self.week_data == []:
            self.create_month_data()
        
    def create_month_volume(self):
        if self.week_data == []:
            self.create_week_data()
    def create_month_density(self):
        if self.week_data == []:
            self.create_week_data()
    
    # def create_week_graph(self, graph_name = "sim.html"):
    #     # where file is going
    #     output_file(graph_name)
    #     source = ColumnDataSource(
    #         data=dict(
    #             x=self.hour_o_day,
    #             y=self.week_pop[0],
    # 
    #         )
    #     )
    #     hover = HoverTool(
    #         tooltips=[
    #             ("index","$index"),
    #             ("(x,y)","($x,$y)"),
    #         ]
    #     )
    #     p = figure(width=800, height=800, tools = [hover], title="monday",x_axis_type="datetime",)
    #     p.circle("x","y",size=10,source=source,  color = self.colors[0])
    #     p.line(x=self.hour_o_day,y=self.week_pop[0], line_width=5,color=self.colors[0])
    #     show(p)
        
        # create graphs for week of data mon-sun all on same graph
         
            
            
            
            
            
            
        # mon = self.week_data[0]
        # tues = self.week_data[1]
        # wed = self.week_data[2]
        # thurs = self.week_data[3]
        # fri = self.week_data[4]
        # sat = self.week_data[5]
        # sun = self.week_data[6]
        
    def iso_varibble(self,list,id):
        new_list = []
        for item in list:
            new_list.append(item[id])
        return np.array(new_list)
        
        
        

if __name__ == "__main__":
    dem = Demographics()
    dem.create_week_data()
    dem.create_week_graph()
