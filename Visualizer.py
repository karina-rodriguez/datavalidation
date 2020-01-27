import numpy as np
import pandas as pd
import altair as alt

    
class Visualizer:
    
    dataFrame = []
    
    def __init__(self, dataFrame):
        self.dataFrame = dataFrame
        
    def plotClassOrder(self):
         alt.data_transformers.disable_max_rows()
         chart2 = alt.Chart(self.dataFrame).mark_bar().encode(
         x=alt.X('sum(number)',type='quantitative',title='Total Number'),
         y=alt.Y('clasS', type='nominal',title='Class',sort = alt.SortField('number', order='descending')),
         color='type',
         order=alt.Order(
           # Sort the segments of the bars by this field
           'type',
           sort='ascending'
         )
         )
         chart2.display()
        
        

