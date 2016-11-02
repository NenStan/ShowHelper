import json
import urllib.request
import time
import datetime

def showGuide():
    fid = open("shows.txt","w")
    a = 1
    showDict = {}
    while a == 1:
        title = input("What is the title of your show? \n(if you are done, type stop)")
        if title == "stop":
            fid.close()
            break
        title = title.replace(" ", "%20")
        season = input("Season:")
        episode = input("Episode Number:")
        if episode == "none":
            fid.write("%s&Season=%s\n" % (title,season))
        else:
            fid.write("%s&Season=%s&Episode=%s\n" % (title,season,episode))
    fid.close()
    fid = open("shows.txt","r")
    for each in fid:
        imdbApi = "http://www.omdbapi.com/?t=%s" % (each)
        jsonObj = urllib.request.urlopen(imdbApi)
        jsonObj = jsonObj.read().decode("utf-8")
        data = json.loads(jsonObj)
        for item in data['Episodes']:
            item['Released'] = item['Released'][5:7] + "/" + item['Released'][8:] + "/" + item['Released'][2:4]
            date1 = item['Released']
 #           newDate1 = time.strftime(date1, "%m/%d/%y")
            currentDate = time.strftime("%x")
            if currentDate > date1:
                print ((item['Episode']),(item['Title']),(item['Released']))
            
