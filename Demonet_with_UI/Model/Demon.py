import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from datetime import datetime,timedelta
from tkinter import messagebox


class Demon:
    def __init__(self):
        os.chdir('/home/manobhav/PycharmProjects/demonetisation analysis')
        self.ndata=pd.read_csv('Data/demonetlatlong.csv')
        self.ndata.Date = pd.to_datetime(self.ndata.Date).dt.normalize()
        self.ndata.sort_values(by='Date',inplace=True)
        self.ndata['year'] = self.ndata.Date.dt.year
        self.ndata['month'] = self.ndata.Date.dt.month
        self.ndata['day'] = self.ndata.Date.dt.day



    def getBarSentiment(self,param):
        temp = pd.crosstab(self.ndata[param], self.ndata['Sentiment']).apply(lambda r: r / r.sum(), axis=1)
        temp.plot(kind='bar', stacked=True)
        k = pd.DataFrame(temp.idxmax(axis=0))
        string="Max positive sentiment is in "+str(k.loc[1][0])+".\n Max negative sentiment is in "+str(k.loc[-1][0])
        messagebox._show(message=string)
        plt.show()

    def showmap(self,sentiment):
        mydata=self.ndata.loc[(self.ndata.Sentiment==sentiment)]
        col='red'
        if sentiment==1:
            col='green'
        from mpl_toolkits.basemap import Basemap
        m = Basemap(projection='mill', llcrnrlat=6.74678, urcrnrlat=35.674520,
                    llcrnrlon=68.03215, urcrnrlon=97.40238, resolution='c', epsg=4269)
        x, y = m(tuple(mydata.Long[(mydata.Long.isnull() == False)]), tuple(mydata.Lat[(mydata.Lat.isnull() == False)]))
        plt.figure(figsize=(40, 20))
        m.arcgisimage(service="NatGeo_World_Map", xpixels=2000,verbose=True)
        m.plot(x, y, 'ro', markersize=15, alpha=0.3,color=col)
        plt.show()

    def showDateGraph(self,startdate,enddate,sentiment,paper,granularity):
        d1 = datetime.strptime(startdate, "%Y-%m-%d")-timedelta(days=1)
        d2 = datetime.strptime(enddate, "%Y-%m-%d")+timedelta(days=1)
        print(startdate,enddate,sentiment,paper,granularity)
        alldata=self.ndata[(self.ndata.Sentiment.isin(sentiment))&(self.ndata.Paper.isin(paper))&(self.ndata.Date > d1) & (self.ndata.Date < d2)]
        print(alldata)


        if sentiment==[-1,1]:
            Group = alldata[alldata.Sentiment==-1].groupby(granularity)['day'].count() / alldata.groupby(granularity)['day'].count()
        else:
            Group = alldata.groupby(granularity)['day'].count()

        Group.plot(kind='line')
        plt.show()












