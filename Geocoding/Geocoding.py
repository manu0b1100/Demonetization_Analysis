import requests
import json
import os
import pandas as pd
from queue import Queue
from threading import Thread
from time import time


class Geocoding:

    def __init__(self,input_file,output_file):
	
	os.chdir('/home/manobhav/PycharmProjects/demonetisation analysis/Geocoding')
        self.frame = pd.read_excel(input_file)
        #self.frame.head() #Testing
        self.baseurl="https://maps.googleapis.com/maps/api/geocode/json?"
        self.key="YOUR_API_KEY"
        self.q=Queue()
        self.results=[]
        self.outputfile=output_file
        self.startThreads()


    def getCityNames(self):
        self.cities=self.frame.city[self.frame.city.isnull() == False].unique().tolist()
        for c in self.cities:
            self.q.put(c)


    def getLongLat(self,i):
        while True:
            print('thread {} running'.format(i))
            resultdict={}
            resultdict['city']=self.q.get()
            payload={'address':resultdict['city'],'key':self.key}
            jsonstring=requests.get(self.baseurl,payload).text

            jsondict=json.loads(jsonstring)

            if jsondict['status']=='OK':
                resultdict['lat']=jsondict['results'][0]['geometry']['location']['lat']
                resultdict['long']=jsondict['results'][0]['geometry']['location']['lng']
                for l in jsondict['results'][0]['address_components']:
                    if l['types'][0] == "administrative_area_level_1":
                        resultdict['state']=l['long_name']
            self.results.append(resultdict)
            print(self.results)
            self.q.task_done()


    def startThreads(self):
        ts=time()
        for i in range(4):
            t1=Thread(target=self.getLongLat, args=(i,))
            t1.setDaemon(True)
            t1.start()

        self.getCityNames()
        self.q.join()
        print("the process took {} seconds".format(ts-time()))
        self.update_Data()

    def update_Data(self):

        res=pd.DataFrame(self.results)
        updatedframe=pd.merge(self.frame,res,on='city',how='left',sort=False)
        updatedframe.to_excel(self.outputfile)



geo=Geocoding('articlesexcel.xlsx','updated_articlesexcel.xlsx')
