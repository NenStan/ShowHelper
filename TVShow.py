import json
import urllib.request
import datetime
#from email.mime.text import MIMEText ## work on sending e-mail

def episodesAired(showName,episodeNum,episodeTitle,releaseDate):
    showEpisodeList = ["%s : %s %s %s" % (showName, episodeNum, episodeTitle, releaseDate)]
    return showEpisodeList

def showGuide():
    fid = open("shows.txt","w")
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
        showAired = []
        imdbApi = "http://www.omdbapi.com/?t=%s" % (each)
        jsonObj = urllib.request.urlopen(imdbApi)
        jsonObj = jsonObj.read().decode("utf-8")
        data = json.loads(jsonObj)
        try: ## for seasons
            showName = data["Title"]
            for episode in data['Episodes']:
                episodeDate = episode['Released']
                showDate = datetime.datetime.strptime(episodeDate,"%Y-%m-%d")
                currentDate = datetime.datetime.now()
                showEpisodeNum = episode['Episode']
                episodeTitle = episode['Title']
                releaseDate = episode['Released']
                if currentDate > showDate:
                    showAired += episodesAired(showName, showEpisodeNum, episodeTitle, releaseDate)
            return showAired
                    #print ((episode['Episode']),(episode['Title']),(episode['Released']))

        except: ## For individual episodes
            print ("Not supposed to be here")
            showName = data["Title"]
            for episode in data['Episode']:
                episodeDate = episode['Released']
                showDate = datetime.datetime.strptime(episodeDate,"%Y-%m-%d")
                currentDate = datetime.datetime.now()
                showEpisodeNum = episode['Episode']
                episodeTitle = episode['Title']
                releaseDate = episode['Released']
                print(currentDate)
                showEpisodeNum = episode['Episode']
                episodeTitle = episode['Title']
                releaseDate = episode['Released']
                if currentDate > showDate:
                    episodesAired(showName, showEpisodeNum, episodeTitle, releaseDate)

showGuide()

