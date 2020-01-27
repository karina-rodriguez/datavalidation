import numpy as np
import pandas as pd
    
class Reader:
    
    file_name = './data/db.csv'
    tableRead = []
    
    def __init__(self, file_name):
        self.file_name = file_name
        
    def fillEmptySpaces(self):
        for column in self.tableRead.columns.values:
            print(column.count)
#             self.tableRead.CatalogedDate.fillna('', inplace=True)
        
        
    def readData(self):
        tableWAllValues = pd.read_csv(self.file_name, sep=',', encoding='utf-8', index_col=False, low_memory=False)
        # crustaceas.fillna(' ', inplace=True)
#        self.tableRead.fillna('', inplace=True)
        
# =============================================================================
#  Step 1. Check if the column contain any values, if it does keep it.
#  Otherwise, discard it.   
# =============================================================================
#        print(self.tableRead.count())
        columnsToKeep=[]
        for column in tableWAllValues.columns.values:
            if tableWAllValues[[column]].count()[0]>0:
                columnsToKeep.append(column)

        self.tableRead  = tableWAllValues[columnsToKeep]
        self.tableRead.fillna('', inplace=True) 
        

        
#        crustaceas.CatalogedDate.fillna('', inplace=True)
#        crustaceas.State.fillna('Unknown', inplace=True)
#        
#        Table_Date = self.tableRead[['CatalogedDate','Class1','Order1','Species1','Kingdom','StardDepth','State','Determiner Last Name1','TypeStatus1']]
#        d = []
#        counter=0
#        for row in Table_Date['CatalogedDate']:
#            #check state......
#            state = Table_Date.loc[counter,'State']
#            region = 1
##            getRegion(state)
#        
#            d.append({'order':Table_Date.loc[counter,'Order1'],'clasS': Table_Date.loc[counter,'Class1'], 
#                                  'species':Table_Date.loc[counter,'Species1'],
#                                  'region':region,'state':Table_Date.loc[counter,'State'],
#                                  'author':Table_Date.loc[counter,'Determiner Last Name1'],
#                                  'typestatus':Table_Date.loc[counter,'TypeStatus1']})
#          
#            counter = counter+1  
#        
#        
#        
#        NewTable_Date = pd.DataFrame(d)
#        # avg_depth = avg_depth/counter
#        # print(NewTable_Date)
#        # print(min_depth)
#        # print(max_depth)
#        
#        classes = NewTable_Date.clasS.unique()
#        types = NewTable_Date.typestatus.unique()
        e = []
#        subtable = []
#        for theclass in classes:
#        #     print(pd.isna(theclass))
#        #        print(types.size)
#            numbtypes = np.zeros((types.size))
#            subtable = NewTable_Date.loc[NewTable_Date['clasS']==theclass]
#        #     print(subtable)
#            counter=0
#            if (pd.isna(theclass)):
#        #            print("I am")
#                subtable = NewTable_Date.loc[pd.isna(NewTable_Date['clasS'])]
#                for type1 in types:  
#            #         print(type)
#            #         df.loc[df['shield'] > 6, ['max_speed']]
#                    pp = subtable.loc[subtable.loc[:,'typestatus']==type1,:].typestatus.count()
#        #                print(pp)
#                    e.append({'clasS':theclass,'type':type,'number':pp})
#                    counter = counter + 1
#                
#            for type in types:
#        #         print(type)
#        #         df.loc[df['shield'] > 6, ['max_speed']]
#                bb = subtable.loc[subtable.loc[:,'typestatus']==type,:].typestatus.count()
#        #         print(bb)
#                e.append({'clasS':theclass,'type':type,'number':bb})
#                counter = counter + 1
        #                   , 'Material Tipo':numbtypes[3] , 'Alotipo':numbtypes[4] , 'PARATIPO':numbtypes[5] 
        #                   , 'Paralectotipo':numbtypes[6] , 'Co-Tipo':numbtypes[7] , 'Lectotipo':numbtypes[8] 
        #                   , 'Neotipo':numbtypes[9] , 'Sintipo':numbtypes[10] , 'Topotipo':numbtypes[11] 
        #              , 'Tipo':numbtypes[12] })
        #             e.append({'clasS':theclass,'nan':numbtypes[0],'Paratipo':numbtypes[1], 'Holotipo':numbtypes[2]
        #                   , 'Material Tipo':numbtypes[3] , 'Alotipo':numbtypes[4] , 'PARATIPO':numbtypes[5] 
        #                   , 'Paralectotipo':numbtypes[6] , 'Co-Tipo':numbtypes[7] , 'Lectotipo':numbtypes[8] 
        #                   , 'Neotipo':numbtypes[9] , 'Sintipo':numbtypes[10] , 'Topotipo':numbtypes[11] 
        #              , 'Tipo':numbtypes[12] })
#        tableResult = pd.DataFrame(e)
        tableResult = self.tableRead 
        return tableResult

    
#def getRegion(state):
#    region = 'Unknown'
#    if (state=='Maranhao') or (state=='Piaui') or (state=='Ceara') or (state=='Rio Grande do Norte') or (state=='Paraiba') or (state=='Pernambucoe') or (state=='Alagoas') or (state=='Sergipe') or (state=='Bahia'):
#            region = 'NE'
#    if (state=='Amapa') or (state=='Para') or (state=='Acre') or (state=='Amazonas') or (state=='Rondonia') or (state=='Roraima') or (state=='Tocantins'):
#            region = 'N'
#    if (state=='Destrito Federal') or (state=='Goias') or (state=='Mato Grosso') or (state=='Mato Grosso do Sul'):
#            region = 'CO'
#    if (state=='Espirito Santo') or (state=='Rio de Janeiro') or (state=='Sao Paulo') or (state=='Minas Gerais'):
#            region = 'SE'
#    if (state=='Parana') or (state=='Santa Catarina') or (state=='Rio Grande do Sul'):
#            region = 'SU'
#    return region


# =============================================================================
# Code starts here.... it reads a database
# =============================================================================
