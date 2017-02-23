import json
import urllib.request
import datetime
import smtplib
from email.mime.text import MIMEText ## work on sending e-mail

def showGuide():
    fid = open("shows.txt","w")
    showDict = {}
    while True:
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
        try: ## for seasons
            for item in data['Episodes']:
                date1 = item['Released']
                showDate = datetime.datetime.strptime(date1,"%Y-%m-%d")
                currentDate = datetime.datetime.now()
                if currentDate > showDate:
                    print ((item['Episode']),(item['Title']),(item['Released']))

        except: ## For individual episodes
            break
            for item in data['Episode']:
                item['Released'] = item['Released'][5:7] + "/" + item['Released'][8:] + "/" + item['Released'][2:4]
                date1 = item['Released']
                print(date1)
     #           newDate1 = time.strftime(date1, "%m/%d/%y")
                currentDate = time.strftime("%x")
                print(currentDate)
                if currentDate > date1:
                    print ((item['Episode']),(item['Title']),(item['Released']))

showGuide()

#def showDict(title,released):
