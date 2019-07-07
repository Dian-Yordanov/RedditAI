import os
import subprocess
import threading
import time
import json
import html
import sys
import urllib
from collections import defaultdict
from subprocess import check_call
from termcolor import colored
# import pip3

while True:
    try:
        import setuptools
        break
    except ImportError:
        subprocess.call("pip3 install setuptools", shell=True)
        import setuptools
while True:
    try:
        import certifi
        break
    except ImportError:
        subprocess.call("pip3 install -Iv certifi==2018.4.16", shell=True)
        import certifi
while True:
    try:
        import chardet
        break
    except ImportError:
        subprocess.call("pip3 install -Iv chardet==3.0.4", shell=True)
        import chardet
while True:
    try:
        import html5lib
        break
    except ImportError:
        subprocess.call("pip3 install -Iv html5lib==1.0.1", shell=True)
        import html5lib
while True:
    try:
        import idna
        break
    except ImportError:
        subprocess.call("pip3 install -Iv idna==2.7", shell=True)
        import idna
while True:
    try:
        import prawcore
        break
    except ImportError:
        subprocess.call("pip3 install -Iv prawcore==1.0.0", shell=True)
        import prawcore
while True:
    try:
        import six
        break
    except ImportError:
        subprocess.call("pip3 install -Iv six==1.11.0", shell=True)
        import six
# while True:
#     try:
#         import update-checker
#         break
#     except ImportError:
#         subprocess.call("pip3 install -Iv update-checker==0.16", shell=True)
#         import update-checker
while True:
    try:
        import webencodings
        break
    except ImportError:
        subprocess.call("pip3 install -Iv webencodings==0.5.1", shell=True)
        import webencodings
while True:
    try:
        import requests
        break
    except ImportError:
        subprocess.call("pip3 install -Iv requests==2.19.1", shell=True)
        import requests
while True:
    try:
        import praw
        break
    except ImportError:
        subprocess.call("pip3 install -Iv praw==6.0.0", shell=True)
        import praw
while True:
    try:
        import feedparser
        break
    except ImportError:
        subprocess.call("pip3 install -Iv feedparser==5.2.1", shell=True)
        import feedparser
while True:
    try:
        from bs4 import BeautifulSoup
        break
    except ImportError:
        subprocess.call("pip3 install -Iv beautifulsoup4==4.6.1", shell=True)
        from bs4 import BeautifulSoup
while True:
    try:
        from urllib.request import urlopen
        from urllib.parse import urlparse
        break
    except ImportError:
        subprocess.call("pip3 install -Iv urllib3==1.23", shell=True)
        from urllib.request import urlopen
        from urllib.parse import urlparse
while True:
    try:
        import bleach
        break
    except ImportError:
        subprocess.call("pip3 install -Iv bleach==2.1.3", shell=True)
        import bleach
while True:
    try:
        import codecs
        break
    except ImportError:
        subprocess.call("pip3 install -Iv codecs", shell=True)
        import codecs
while True:
    try:
        import sqlite3
        break
    except ImportError:
        subprocess.call("pip3 install -Iv sqlite3", shell=True)
        import sqlite3
while True:
    try:
        import configparser
        break
    except ImportError:
        subprocess.call("pip3 install -Iv configparser", shell=True)
        import configparser


DONE_CONFIGFILE = "done.txt"
feed_database_name = 'feed_sources_and_urls_database.sqlite'
feed_table_name = 'feed_database'
feed_sources = 'feed_sources'
feed_urls = 'feed_urls'
cashed_feed_urls = 'cashed_feed_urls'

class GoogleDriveDownloadClass:
    string_before_spliting = ""
    def __init__(self, google_url):
        file_id = 'TAKE ID FROM SHAREABLE LINK'
        returned_string_with_the_whole_html = self.download_file_from_google_drive(file_id, google_url)
        str1 = ''.join(returned_string_with_the_whole_html)
        clean_text = BeautifulSoup(str1, "html.parser")

        encoded_text = str(clean_text).replace('\\u000b', '')
        self.string_before_spliting = bleach.clean(encoded_text,tags=[],strip=True)
        self.string_before_spliting = html.unescape(self.string_before_spliting)
        self.string_before_spliting = self.string_before_spliting.split('DOCS_modelChunk = [{', 1)[-1]

        self.string_before_spliting = self.string_before_spliting.split('},{', 1)[0]
        self.string_before_spliting = self.string_before_spliting.split(':1,"s":', 1)[1]
        self.string_before_spliting = self.string_before_spliting[:-1]
        self.string_before_spliting = self.string_before_spliting[1:]

        self.string_before_spliting = self.string_before_spliting.replace('    \\', '')
        self.string_before_spliting = self.string_before_spliting.replace('     \\', '')
        self.string_before_spliting = self.string_before_spliting.replace('      \\', '')
        self.string_before_spliting = self.string_before_spliting.replace('       \\', '')
        self.string_before_spliting = self.string_before_spliting.replace('        \\', '')
        self.string_before_spliting = self.string_before_spliting.replace('         \\', '')
        self.string_before_spliting = self.string_before_spliting.replace('          \\', '')
        self.string_before_spliting = self.string_before_spliting.replace('           \\', '')
        self.string_before_spliting = self.string_before_spliting.replace('            \\', '')
        self.string_before_spliting = self.string_before_spliting.replace('\\",        ', '",')
        self.string_before_spliting = self.string_before_spliting.replace('\\",       ', '",')
        self.string_before_spliting = self.string_before_spliting.replace('\\",      ', '",')
        self.string_before_spliting = self.string_before_spliting.replace('\\",     ', '",')
        self.string_before_spliting = self.string_before_spliting.replace('\\",    ', '",')
        self.string_before_spliting = self.string_before_spliting.replace('\\",   ', '",')
        self.string_before_spliting = self.string_before_spliting.replace('\\",  ', '",')
        self.string_before_spliting = self.string_before_spliting.replace('\\", ', '",')
        self.string_before_spliting = self.string_before_spliting.replace('\\",', '",')
        self.string_before_spliting = self.string_before_spliting.replace(' ', '')
        self.string_before_spliting = self.string_before_spliting.replace('\\"', '"')
        self.string_before_spliting = self.string_before_spliting.replace(" ", "").replace("\t", "")

    def download_file_from_google_drive(self,id,google_url):
        URL = google_url
        session = requests.Session()
        response = session.get(URL, params = { 'id' : id }, stream = True)
        token = self.get_confirm_token(response)

        if token:
            params = { 'id' : id, 'confirm' : token }
            response = session.get(URL, params = params, stream = True)
        returned_string_with_the_whole_html = self.save_response_content(response)
        return returned_string_with_the_whole_html

    def get_confirm_token(self,response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value
        return None

    def save_response_content(self,response):
        CHUNK_SIZE = 32768
        StringSum = ""

        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                StringSum += str(chunk)
        return StringSum

    def get_downloaded_string(self):
        string = self.string_before_spliting
        return string


class ClusterableBots:

    def __init__(self, threadName, waitTime):
        Launcher_Thread_For_ClusterableBot = threading.Thread(target=self.initCode(threadName, waitTime))
        Launcher_Thread_For_ClusterableBot.start()

# This Method should be overwritten
    def RunBot(user_agent, client_id, client_secret, username, password, subreddit, waitTime):
        print("Runned. Therefore it is not overwritten")

    def initCode(self, threadName, waitTime):
        try:
            if sys.argv[1] is not None:
                user_agent = sys.argv[1]
                client_id = sys.argv[2]
                client_secret = sys.argv[3]
                username = sys.argv[4]
                password = sys.argv[5]
                subreddit = sys.argv[6]
        except IndexError:

            parser = configparser.ConfigParser()
            parser.read('credentials.ini')

            user_agent = parser.get('Credentials_RedditAPI', 'user_agent')
            client_id = parser.get('Credentials_RedditAPI', 'client_id')
            client_secret = parser.get('Credentials_RedditAPI', 'client_secret')
            username = parser.get('Credentials_RedditAPI', 'username')
            password = parser.get('Credentials_RedditAPI', 'password')
            subreddit = parser.get('Settings_Subreddit', 'subreddit')


        self.RunBot = RatingCounter_ClusterableBots
        self.RunBot(user_agent, client_id, client_secret, username, password, subreddit, waitTime)

def main(threadName, waitTime):
    operation_mode = ""
# Windows based calling by args given from the autostart script on call. If args are detected, this should be the way to go
    try:
        if sys.argv[1] is not None:
            user_agent = sys.argv[1]
            client_id = sys.argv[2]
            client_secret = sys.argv[3]
            username = sys.argv[4]
            password = sys.argv[5]
            subreddit = sys.argv[6]
            operation_mode = sys.argv[7]
    except IndexError:

# This method of credentials taking is used for linux based systems like rasberry pi. If no args are detected, this should be the way to go

#         with open('credentials', 'r') as myfile:
#             data = myfile.read()
#
#         StringTranslator = []
#         StringTranslator = data.split('\n')
#
#         user_agent = StringTranslator[0]
#         client_id = StringTranslator[1]
#         client_secret = StringTranslator[2]
#         username = StringTranslator[3]
#         password = StringTranslator[4]
#         subreddit = StringTranslator[5]
#         operation_mode = StringTranslator[6]

        parser = configparser.ConfigParser()
        parser.read('credentials.ini')

        user_agent = parser.get('Credentials_RedditAPI', 'user_agent')
        client_id = parser.get('Credentials_RedditAPI', 'client_id')
        client_secret = parser.get('Credentials_RedditAPI', 'client_secret')
        username = parser.get('Credentials_RedditAPI', 'username')
        password = parser.get('Credentials_RedditAPI', 'password')
        subreddit = parser.get('Settings_Subreddit', 'subreddit')
        operation_mode =parser.get('Settings_Subreddit', 'operation_mode')
        source1 = parser.get('URL_Sources', 'source1')
        source2 = parser.get('URL_Sources', 'source2')
        source3 = parser.get('URL_Sources', 'source3')
        source4 = parser.get('URL_Sources', 'source4')
        source5 = parser.get('URL_Sources', 'source5')
        source6 = parser.get('URL_Sources', 'source6')
        source7 = parser.get('URL_Sources', 'source7')
        source8 = parser.get('URL_Sources', 'source8')
        source9 = parser.get('URL_Sources', 'source9')
        source10 = parser.get('URL_Sources', 'source10')

    while True:
        try:

# Modes of operation: defined with operation_mode they are responsible for the moderation of rss sources.

# OnlineRealTimeComparison posts any rss links to Reddit and after they are posted any duplicates are removed.
# This is done by scanning for duplicates and removing them. This means that there is a limit of how much can be checked for duplicates.
# 1 source could have 1 and the same link posted multiple times in the span of a couple of hours.
# While that may be a downside, the upside is that everything is run in memory and no local read/white operations are executed.

# LocalDatabasePostOnChange keeps a database on the local drive and compared new rss links to existing ones.
# If there is a change, post it. This means that local read/write operations are needed, but duplicates are avoided.

            data = get_data_from_all_google_sources(source1, source2, source3, source4, source5, source6, source7, source8, source9, source10)

            # print(source1)
            # print(data)

            x = 0
            dataIndexArray1 = []
            dataIndexArray2 = []
            dataIndexArray3 = []

            for dataIndexer1 in data:

                dataIndexArray1.append(dataIndexer1)
                x = x + 1
                for dataIndexer2 in data[dataIndexer1]['urls']:
                    dataIndexer2 = codecs.decode(dataIndexer2, 'unicode_escape').encode('latin1').decode('utf8')

                    # print("dataIndexer2: " + str(dataIndexer2))
                    # print(dataIndexer2 = codecs.decode(dataIndexer2, 'unicode_escape').encode('latin1').decode('utf8'))

                    dataIndexArray2.append(dataIndexer2)
                    dataIndexArray3.append(dataIndexer2+" "+dataIndexer1+" "+ data[dataIndexer1]['cssClass'])

            threadsList = []
            threadsList = dataIndexArray3

    # The type of thread comes from the arguments from the main method.
    # Thus it is not needed to have more than check for the operation mode.
    # Just have different ifs for the different thread types.

            # if (threadName == "CashingThread"):
            #     CashingThreadStarter = threading.Thread(target=CashingThread, args=(
            #         user_agent, client_id, client_secret, username, password, subreddit))
            #     CashingThreadStarter.start()
            #     time.sleep(waitTime * 3 / 2)  # increasing to 25 from 20

            if(threadName=="ModeratingThread"):
                print(colored(threadName + " id " + str(threading.current_thread().ident), 'green', 'on_red'))
                ModeratingThread = threading.Thread(target=ModerationThread, args=(
                    user_agent, client_id, client_secret, username, password, subreddit))
                ModeratingThread.start()
                time.sleep(waitTime/3) # increasing to 25 from 20

            if (threadName == "PostingThread"):
                print(colored(threadName + " id " + str(threading.current_thread().ident), 'cyan'))
                # print(str(threadsList) + " <-- " + "This is the threadsList")
                for threadsInstance in threadsList:
                    threads = []
                    PostingThread = threading.Thread(target=PostThread,
                                                     args=(waitTime-10, threadsInstance.split(" ")[0]
                    , user_agent, client_id, client_secret, username, password, subreddit
                        , threadsInstance.split(" ")[1], threadsInstance.split(" ")[2], operation_mode))

                    threads.append(PostingThread)
                    PostingThread.start()
                    # time.sleep(waitTime*3/2) # reducing to 75 from 90
                    time.sleep(waitTime-9)

        except Exception as e:
            # print("success111")
            s = str(e)
            indexExistingCheckBoolean = False
            print('EXCEPTION2                                                                                ')
            print(s)
            pass

def GetJsonData(google_url):
    google_url1 = google_url.replace("https://docs.google.com/document/d/", "")
    google_url2 = google_url1.replace("/edit", "")
    try:
        # Try to get the data from the google link
        gddc = GoogleDriveDownloadClass
        returned_string_with_the_whole_html = gddc(google_url).get_downloaded_string()
        returned_string_with_the_whole_html = ManualUnicodeToStringConverter(returned_string_with_the_whole_html)
        returned_string_with_the_whole_html = returned_string_with_the_whole_html.replace("\\\\n", "").replace("\\\"","\"")
        data = returned_string_with_the_whole_html

        with open(google_url2, "w") as text_file:
            text_file.write(data)

        # print(data)
        # print("success 2")
    except:
        # Version 2 of getting sources - a legacy approach that should be used if the new version does not work.

        # as of 02/07/2019 it is not a good idea to use that method and
        # the new method to fight problems with getting sources is to cashe the sources to a file and read from it
        # with the idea that eventually new sources are going to be downloaded

        # print("urls source 1 failed, switching to urls source 2")
        # target_url = 'https://pastebin.com/raw/n8aCxq1F'
        # dataFromURL = urlopen(target_url)  # it's a file like object and works just like a file
        # data = json.load(dataFromURL)

        print("getting sources from Google failed, cashed local sources are going to be used instead.")
        with open(google_url2, "r") as f:
            data = f.read()

    return data

def ManualUnicodeToStringConverter(ProvidedString):
    ProvidedString = ProvidedString.replace("\\\\u0020"," ").replace("\\\\u0021","!").replace("\\\\u0022","\"").replace("\\\\u0023","#")\
        .replace("\\\\u0024","$").replace("\\\\u0024","$").replace("\\\\u0025","%").replace("\\\\u0026","&").replace("\\\\u0027","'")\
        .replace("\\\\u0028", "(").replace("\\\\u0029", ")").replace("\\\\u002A", "*").replace("\\\\u002B", "+").replace("\\\\u002C", ",")\
        .replace("\\\\u002D", "-").replace("\\\\u002E", ".").replace("\\\\u002F", "/").replace("\\\\u003A", ":").replace("\\\\u003B", ";")\
        .replace("\\\\u003C", "<").replace("\\\\u003D", "=").replace("\\\\u003E", ">").replace("\\\\u003F", "?").replace("\\\\u0040", "@")\
        .replace("\\\\u005B", "[").replace("\\\\u005C", "\\").replace("\\\\u005D", "]").replace("\\\\u005E", "^").replace("\\\\u005F", "_")\
        .replace("\\\\u0060", "`").replace("\\\\u007B", "{").replace("\\\\u007C", "|").replace("\\\\u007D", "}").replace("\\\\u007E", "~")\
        .replace("\\\\u0024","$").replace("\\\\u0024","$").replace("\\\\u0025","%").replace("\\\\u0026","&").replace("\\\\u0027","'")\
        .replace("\\\\u0028", "(").replace("\\\\u0029", ")").replace("\\\\u002a", "*").replace("\\\\u002b", "+").replace("\\\\u002c", ",")\
        .replace("\\\\u002d", "-").replace("\\\\u002e", ".").replace("\\\\u002f", "/").replace("\\\\u003a", ":").replace("\\\\u003b", ";")\
        .replace("\\\\u003c", "<").replace("\\\\u003d", "=").replace("\\\\u003e", ">").replace("\\\\u003f", "?").replace("\\\\u0040", "@")\
        .replace("\\\\u005b", "[").replace("\\\\u005c", "\\").replace("\\\\u005d", "]").replace("\\\\u005e", "^").replace("\\\\u005f", "_")\
        .replace("\\\\u0060", "`").replace("\\\\u007b", "{").replace("\\\\u007c", "|").replace("\\\\u007d", "}").replace("\\\\u007e", "~")
    return ProvidedString

def get_data_from_all_google_sources(source1, source2, source3, source4, source5, source6, source7, source8, source9, source10):
    # You have to manually add the other sources because if they are empty I get errors.
    # Empty google urls for new sources:
    # source3 = https://docs.google.com/document/d/1Vz7vJvnny6VADcRiMNSAxbS6WtVw-__SC0DQIP97QAs/edit
    # source4 = https://docs.google.com/document/d/17C0LaRSz7wEanXJo-dhch7b1qqNx6fsfM6vNltmCK74/edit
    # source5 = https://docs.google.com/document/d/1_BVHl1GMjFXZP-zzBo6y8cHY1A_lV9sq0jt7w14ueSM/edit
    # source6 = https://docs.google.com/document/d/1RSao06WuRyQkqZ9VCVuXjtLelNkYpXlNQlDQuhzL_ag/edit
    # source7 = https://docs.google.com/document/d/1GWs1dDkV_wBrnxrt7Qk6eXePUsMSeH-MxB8446LFjvU/edit
    # source8 = https://docs.google.com/document/d/1wekU3tHBxkdeaigoh4LfFS-feFVAhvzwce0PuGBIF40/edit
    # source9 = https://docs.google.com/document/d/1mpUVDUvAGPROM9DBU-Ex230qBbNAndI3wVCHGEwDDBM/edit
    # source10 = https://docs.google.com/document/d/131C1Ps551K0UmSyMa3b0sjm_brDt400r4FQQ1ooOSOA/edit
    # , source3, source4, source5, source6, source7, source8, source9, source10

    googleSources = [source1, source2]
    finalStringData = ""
    for dataSource in googleSources:
        finalStringData += GetJsonData(dataSource)

    try:
        if(json_validator(finalStringData)):
            with open("GoogleDocsJsonCashe.json", "w") as text_file:
                text_file.write(finalStringData)
        else:
            # print("not valid json")
            raise ValueError("Not valid json. Do not read/save from/to cashe.")

    except Exception as e:
        s = str(e)
        print("Either json cashe file read/write operation failed, or the json was not valid " + " \n" +s)
        pass

    with open("GoogleDocsJsonCashe.json", "r") as f:
        finalStringData2 = f.read()
        finalStringData2 = json.loads(str(finalStringData2))

    return finalStringData2

def json_validator(data):
    try:
        json.loads(data)
        return True
    except ValueError as error:
        print("invalid json: %s" % error)
        return False

def PostThread(waitTime, rss_str, user_agent, client_id, client_secret, username, password, subreddit_var, tag, cssClass, operation_mode):

    start_time = time.time()
    reddit = praw.Reddit(user_agent=user_agent,
                         client_id=client_id, client_secret=client_secret,
                         username=username, password=password)

    subreddit = reddit.subreddit(subreddit_var)
    updateChecker1 = ''
    submit = ''
    SourceNonReddit = ''
    SourceReddit= ''

    t_end = time.time() + waitTime # reducing to 50 from 60

    # while time.time() < t_end:
    # TODO see if it needs to be always true
    # while True:
    # print("thread id " + str(threading.current_thread().ident))
    # print("t_end       " + str(t_end)[7:])
    # print("time.time() " + str(time.time())[7:])

    print(colored("PostThread Thread id " + str(threading.current_thread().ident), 'green'))
    print(threading.enumerate())

    feed = feedparser.parse(rss_str)
    indexExistingCheckBoolean = True

    try:

        if feed['entries'][0] is not None and indexExistingCheckBoolean is True:
            title = feed['entries'][0].title
            description = feed['entries'][0].summary,
            url = feed['entries'][0].link,
            updated = feed['entries'][0].updated

            NumberOfComments = ''
            ItemExistingChecker = False
            link = ''

            # print(operation_mode)
            if (operation_mode == "OnlineRealTimeComparison"):
                if updateChecker1 != str(updated):
                    # print("> " + rss_str + " <--Posting From this URL (feed_sources)")
                    updateChecker1 = str(updated)

                    link = str(url)
                    link = link.replace('(u\'', '', 1)
                    link = link[0: len(link) - 3]

                    print("> " + str(url) + " <-- Specific URL (feed_urls)")

                    if 'https://www.reddit.com/' in link:
                        submission1 = reddit.submission(url=link)
                        NumberOfComments = str(submission1.num_comments).encode('utf-8')
                    else:
                        NumberOfComments = ''

                    SubmitFunction(link, NumberOfComments, title, url, subreddit, feed, cssClass, tag)

            if (operation_mode == "LocalDatabasePostOnChange" or operation_mode == "HybridOperationMode"):

                if updateChecker1 != str(updated):
                    # print("> " + rss_str + " <--Posting From this URL (feed_sources)")
                    updateChecker1 = str(updated)

                    # link = str(url)
                    # link = link.replace('(u\'', '', 1)
                    # link = link[0: len(link) - 3]

                    # print("> " + str(url) + " <-- Specific URL (feed_urls)")

                    if 'https://www.reddit.com/' in link:
                        submission1 = reddit.submission(url=link)
                        NumberOfComments = str(submission1.num_comments).encode('utf-8')
                    else:
                        NumberOfComments = ''

                try:
                    databaseFeedURLcashed_feed_urls = str(GetTargetRowFromDBcashed_feed_urls(rss_str, str(url)[:-3][2:], feed_database_name, feed_table_name, cashed_feed_urls))
                    print("The same URL already exists in the cashed database - " + str(url)[:-3][2:])

                except Exception as e:
                    s = str(e)
                    # print(" failed to make the check if url " + str(url)[:-3][2:] + " exists in the database, "
                    #       "you should get an 'index out of range' because you return the 0 index of an empthy array: " + s)
                    # print("The Url " + str(url)[:-3][2:] + " has not been found in the database")
                    print(colored("The Url is not in the cashed database", "red"))

                    try:
                        databaseFeedURLfeed_urls = str(GetTargetRowFromDBfeed_urls(rss_str, str(url)[:-3][2:], feed_database_name, feed_table_name,feed_urls))
                        print(colored("The same URL already exists in the database - " + str(url)[:-3][2:], "red","on_grey"))

                    except Exception as e:
                        s = str(e)
                        # print(" failed to make the check if url " + str(url)[:-3][2:] + " exists in the database, "
                        #       "you should get an 'index out of range' because you return the 0 index of an empthy array: " + s)
                        print(colored("   ", "red","on_green") + colored(" The Url " + str(url)[:-3][2:] +
                              " has not been found in the database so lets try to post it on reddit", "green"))

                        try:
                            # print(str(url)[:-3][2:] + "<-- str(url)[:-3][2:]")
                            # print(str(url) + "<-- URL")

                            databaseFeedURL = str(GetTargetRowFromDBfeed_sources(rss_str, str(url)[:-3][2:] , feed_database_name, feed_table_name, feed_sources))

                            if(str(url)[:-3][2:] in databaseFeedURL):
        # Both links are the same. Do nothing
        #                           print("Both links are the same. Do nothing")
                                pass
                            else:
        # Different links, should update the database with the new link
                                print("Different links, should update the database with the new link. "
                                      "This means a change in urls and a link to be posted.")
                                # print(str(str(url)[:-3][2:]))
                                # print(databaseFeedURL)
                                ExecuteUPDATE_SQL_Query(databaseFeedURL, str(url)[:-3][2:])#[:-3][2:]
                                databaseFeedURL = str(GetTargetRowFromDBfeed_sources(rss_str, str(url), feed_database_name, feed_table_name, feed_sources))
                                # print("databaseFeedURL: "  + databaseFeedURL)

                                # url = str("('" + databaseFeedURL + "',)")
                                url = str("" + databaseFeedURL + "")
                                link = str(url)
                                link = link.replace('(u\'', '', 1)
                                link = link[0: len(link) - 3]
                                # print(url + "<-- URL.2 \n")
                                SubmitFunction(link, NumberOfComments, title, url, subreddit, feed, cssClass, tag)
                                #         "\""+str(url)[:-2]
                        except Exception as e:
                            s = str(e)
                            print("Failed. Either because of an error with the query "
                                  "or because the database is not populated. Populating regardless." + " \n" + s)
                            print("stryrl "+str(url))
                            PopulateSQLTableForBot(str(rss_str), str(url)[:-3][2:], feed_database_name, feed_table_name, feed_sources, feed_urls, cashed_feed_urls)
                            databaseFeedURL = str(GetTargetRowFromDBfeed_sources(rss_str, str(url), feed_database_name, feed_table_name, feed_sources))
                            # url = str("('" + databaseFeedURL + "',)")
                            url = str("" + databaseFeedURL + "")
                            link = str(url)
                            link = link.replace('(u\'', '', 1)
                            link = link[0: len(link) - 3]
                            print(url + "<-- URL.2 \n")
                            SubmitFunction(link, NumberOfComments, title, url, subreddit, feed, cssClass, tag)
                            pass
                        pass
                    pass

                # print(str(url)[:-3][2:] + "<-- URL \n")

                # PopulateSQLTableForBot(str(rss_str), str(url))

            submit = ''
            SourceNonReddit = ''
            SourceReddit= ''

    except Exception as e:
        s = str(e)
        indexExistingCheckBoolean = False
        if "DOMAIN_BANNED" in s or "received 503 HTTP response" in s:
            print("Error: " + s + "<-- not sending an email because of it, but not posting either.")
        # else:
            # send_email("Error with this feed source: " + rss_str + " ||| Error code: " + s)
        print('EXCEPTION       '+rss_str)
        print(s)
        pass
    # print("--- %s seconds ---" % (time.time() - start_time))

def ModerationThread(user_agent, client_id, client_secret, username, password, subreddit_var):

    start_time = time.time()
    reddit = praw.Reddit(user_agent=user_agent,
                         client_id=client_id, client_secret=client_secret,
                         username=username, password=password)

    subreddit = reddit.subreddit(subreddit_var)
    dic = defaultdict(list)
    lis = []
    coordinatedGeneratedById = []

    print(colored("ModerationThread Thread id " + str(threading.current_thread().ident), 'yellow'))
    print(threading.enumerate())

    i=0
    for submission in subreddit.new(limit=100): # was 1000, changed to 100 for better speed

        coordinatedGeneratedById.append(submission.id)
        lis.append(submission.url)
        i=i+1

    for ii, x in enumerate(lis):
        x = str(x).encode('utf-8')
        dic[x].append((ii))
    for num, coords in dic.items():
        if len(coords) > 1:
            print("{0} was repeated at coordinates {1}".format(num.decode("utf-8")," ".join(str(x) for x in coords)))
            iii = 0
            for numIndex in coords:
                if(iii==0):
                    submission = reddit.submission(id=coordinatedGeneratedById[numIndex])
                    submission.delete()
                    # pass
                if (iii >= 1):
                    # print "second+ - " + coordinatedGeneratedById[numIndex]
                    pass
                    # submission = reddit.submission(id=coordinatedGeneratedById[numIndex])
                    # submission.delete()

                iii=iii+1

# # Do not delete the code for Cashing thread but it is not really useful. Commended because of low usefullness.
# def CashingThread(user_agent, client_id, client_secret, username, password, subreddit_var):
# #Cashing thread calls are made for the local cashing idea that proves, for now, to be slower and thus inefficient
#
#     print("CashingThread")
#     submissionArray = []
#     reddit = praw.Reddit(user_agent=user_agent,
#                          client_id=client_id, client_secret=client_secret,
#                          username=username, password=password)
#
#     subreddit = reddit.subreddit(subreddit_var)
#
#
#     f = open('data', 'w+')
#     f.truncate()
#     f = open('data1', 'w+')
#     f.truncate()
#
#     for submission in subreddit.new(limit=100):
#         with open('data', 'a') as the_file:
#             the_file.write(str(submission) + "\n")
#
#     with open('data', 'r') as the_file:
#         texSpliter = the_file.read().split("\n")
#         for indexObject in texSpliter:
#             # print(indexObject + " <--- indexObject")
#
#             # submission1 = reddit.submission(id=texSpliter[len(texSpliter)-2])
#             submission1 = reddit.submission(id=indexObject)
#             submissionArray.append(submission1)
#
#             print(submission1.url + " <--- submission1.url")
#
#             with open('data1', 'a') as the_file:
#                 the_file.write(str(submission1.url) + "\n")

def AutomoderationCssClassCreator(typeOfPost):
    # print typeOfPost
    cssClassToUse = ""
    if "kaldata.com" in typeOfPost:
        cssClassToUse = "orange"
    # elif typeOfPost.find("twitter.com") == 1:
    elif "twitter.com" in typeOfPost:
        cssClassToUse = "green"
    # elif typeOfPost.find("boards.4chan.org") == 1:
    elif "boards.4chan.org" in typeOfPost:
        cssClassToUse = "red"
    # elif typeOfPost.find("r/hearthstone") == 1:
    elif "r/hearthstone" in typeOfPost:
        cssClassToUse = "purple"
    # elif typeOfPost.find("r/") == 1:
    elif "r/" in typeOfPost:
        cssClassToUse = "brown"
    # elif typeOfPost.find("channelfireball.com") == 1:
    elif "channelfireball.com" in typeOfPost:
        cssClassToUse = "cyan"
    elif "--^Tech^--" in typeOfPost:
        cssClassToUse = "redcustom1"
    elif "gaming" in typeOfPost:
        cssClassToUse = "redcustom2"
    else:
        cssClassToUse = "custom"
    # print cssClassToUse
    return cssClassToUse

#The functions bellow are here just in case read/write from the device is implemented as the main way of comparing
# new posts to old in order to search for dublication
def read_config_done():
    done = set()
    try:
        with open(DONE_CONFIGFILE, "r") as f:
            for line in f:
                if line.strip():
                    done.add(line.strip())
    except OSError:
        pass
    return done

def write_config_done(done):
    with open(DONE_CONFIGFILE, "w") as f:
        for d in done:
            if d:
                f.write(d + "\n")

def RemoveUsersReddit(str):
    word2 = ''
    for word in str.split():
        word2 += word.replace('/u/', '') + ' '
    return word2

def send_email(message_string):

# Try to get all the email sending api keys, domains and secret info. If there is a failure, do not send emails or use the API

    mailgun_top_domain_name = ""
    mailgun_api_key = ""
    mailgun_from_domain_name = ""
    mailgun_to_domain_name = ""

# Windows based calling by args given from the autostart script on call. If args are detected, this should be the way to go
    try:
        if sys.argv[1] is not None:
            mailgun_top_domain_name = sys.argv[8]
            mailgun_api_key = sys.argv[9]
            mailgun_from_domain_name = sys.argv[10]
            mailgun_to_domain_name = sys.argv[11]

            requests.post(
                mailgun_top_domain_name,
                auth=("api", mailgun_api_key),
                data={"from": mailgun_from_domain_name,
                      "to": [mailgun_to_domain_name],
                      "subject": "Error with some of the feed sources",
                      "text": message_string})

    except IndexError:
# This method of credentials taking is used for linux based systems like rasberry pi. If no args are detected, this should be the way to go
        try:
            # with open('credentials', 'r') as myfile:
            #     data = myfile.read()
            # StringTranslator = []
            # StringTranslator = data.split('\n')
            #
            # mailgun_top_domain_name = StringTranslator[7]
            # mailgun_api_key = StringTranslator[8]
            # mailgun_from_domain_name = StringTranslator[9]
            # mailgun_to_domain_name = StringTranslator[10]

            parser = configparser.ConfigParser()
            parser.read('credentials.ini')

            mailgun_top_domain_name = parser.get('Credentials_mailgunAPI', 'mailgun_top_domain_name')
            mailgun_api_key = parser.get('Credentials_mailgunAPI', 'mailgun_api_key')
            mailgun_from_domain_name = parser.get('Credentials_mailgunAPI', 'mailgun_from_domain_name')
            mailgun_to_domain_name = parser.get('Credentials_mailgunAPI', 'mailgun_to_domain_name')

            requests.post(
                mailgun_top_domain_name,
                auth=("api", mailgun_api_key),
                data={"from": mailgun_from_domain_name,
                      "to": [mailgun_to_domain_name],
                      "subject": "Error with some of the feed sources",
                      "text": message_string})

        except Exception as e:
            s = str(e)
            print("There was an error with getting the email sending API details.")
            print(s)
            pass

""" Make connection to an SQLite database file """
def connect(sqlite_file):
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    return conn, c

""" Commit changes and close connection to the database """
def close(conn):
    conn.commit()
    conn.close()

def CreateNewDatabase(sqlite_file, table_name, feed_sources, feed_urls, field_type, cashed_feed_urls):

    sqlite_file = str(sqlite_file)
    table_name = str(table_name)
    feed_sources = str(feed_sources)
    feed_urls = str(feed_urls)
    cashed_feed_urls = str(cashed_feed_urls)

    # print("works")

    conn, c = connect(sqlite_file)

    try:
        c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'.format(tn=table_name, nf=feed_sources, ft=field_type))
    except Exception as e:
        s = str(e)
        print("Query ignored -> You tried to create a table that already exists: " + s)
        pass
    try:
        c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_name, cn=feed_urls, ct=field_type))
    except Exception as e:
        s = str(e)
        print("Query ignored -> Duplicate column name: " + s)
        pass
    try:
        c.execute("ALTER TABLE {tn} ADD COLUMN '{cfu}' {ct}".format(tn=table_name, cfu = cashed_feed_urls, ct=field_type))
    except Exception as e:
        s = str(e)
        print("Query ignored -> Duplicate column name: " + s)
        pass


    close(conn)


def PopulateDatabase(sqlite_file, table_name, feed_sources, feed_urls, source_value,feeds_value):
    conn, c = connect(sqlite_file)

    try:
        c.execute("INSERT INTO {tn} ({fs}, {fu}) VALUES (?, ?)"
                  .format(tn=table_name, fs=feed_sources, fu=feed_urls), (source_value, feeds_value))

    except sqlite3.IntegrityError:
        print('ERROR: ID already exists in PRIMARY KEY column {}'.format(source_value))

    close(conn)

def ShowDataFromAFieldRow(sqlite_file, table_name, feed_sources, feed_urls, row_value):
    conn, c = connect(sqlite_file)

    # 1) Contents of all columns for row that match a certain value in 1 column
    c.execute("SELECT * FROM {tn} WHERE {fs}={rv}".format(tn=table_name, fu=feed_urls, fs=feed_sources, rv=row_value))
    all_rows = c.fetchall()
    # print('1):', all_rows)

    conn.close()
    return all_rows

def ShowAllData(sqlite_file, table_name):
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute("SELECT * FROM {tn}".format(tn=table_name))
    all_rows = c.fetchall()

    conn.close()
    return all_rows

def ExecuteScriptCustomSQLQuery(sqlite_file, sql_query, boolean_return):
    conn, c = connect(sqlite_file)
    # print(sql_query)

    try:
        c.executescript(sql_query)
    except Exception as e:
        s = str(e)
        print("Query ignored -> ExecuteScriptCustomSQLQuery failed: " + s)
        pass


    if (boolean_return is "No"):
        conn.close()
    if (boolean_return is "Yes"):
        all_rows = c.fetchall()
        conn.close()
        return all_rows

def ExecuteINSERT_INTO_SQL_withAtributes(attributes, params):
    conn, c = connect(attributes[0][0])

    # try:
    c.execute("INSERT INTO {table_name} ({feed_sources}, {feed_urls}) VALUES (?, ?)"
              .format(table_name=attributes[0][1], feed_sources=attributes[1][0], feed_urls=attributes[1][1]),
              params)

    # except sqlite3.IntegrityError:
    #     print('ERROR: the above INSERT OPERATION FAILED.')

    close(conn)

def ExecuteUPDATE_SQL_Query(old_row_var, new_url_var):
    sqlite_file = 'feed_sources_and_urls_database.sqlite'
    table_name = 'feed_database'
    feed_sources = 'feed_sources'
    feed_urls = 'feed_urls'
    field_type = 'varchar'
    cashed_feed_urls = 'cashed_feed_urls'

    system_params = (sqlite_file, table_name)
    # variables_params = (feed_sources, feed_urls)
    # atributes = (system_params, variables_params)

    print("new_url_var: "+new_url_var)
    print("old_row_var: "+old_row_var)

    # new_url_var = str("('" + str(new_url_var) + "',)")
    # new_url_var = str("" + str(new_url_var) + "")
    # print(new_url_var)

    params = (old_row_var, new_url_var)
    conn, c = connect(sqlite_file)

    ExecuteScriptCustomSQLQuery(sqlite_file, """ UPDATE {table_name} SET {feed_urls} = '{var_two}' WHERE {feed_urls} = '{var_one}';"""
                                .format(table_name=table_name, feed_sources=feed_sources,
                                        feed_urls=feed_urls, var_one=params[0],var_two=params[1]), "No")

    # print(""" UPDATE {table_name} SET {cashed_feed_urls} = '{var_one}' WHERE {feed_urls} = '{var_two}';"""
    #                             .format(table_name=table_name, feed_sources=feed_sources,
    #                                     cashed_feed_urls=cashed_feed_urls, feed_urls=feed_urls, var_one=params[0],var_two=params[1]))

    ExecuteScriptCustomSQLQuery(sqlite_file, """ UPDATE {table_name} SET {cashed_feed_urls} = '{var_one}' WHERE {feed_urls} = '{var_two}';"""
                                .format(table_name=table_name, feed_sources=feed_sources,
                                        cashed_feed_urls=cashed_feed_urls, feed_urls=feed_urls, var_one=params[0],var_two=params[1]), "No")

    # CREATE TABLE table_name (column1 varchar(255),column2 varchar(255));


    # try:
    #     c.execute("INSERT INTO {table_name} ({feed_sources}, {feed_urls}) VALUES (?, ?)"
    #               .format(table_name=attributes[0][1], feed_sources=attributes[1][0], feed_urls=attributes[1][1]), params)
    #
    # except sqlite3.IntegrityError:
    #     print('ERROR: the above INSERT OPERATION FAILED.')

    close(conn)

def GetTargetRowFromDBfeed_sources(
        rss_str_var_feed_sources, url_var_feed_urls, database_name, table_name, feed_sources):

    params = (rss_str_var_feed_sources, url_var_feed_urls)
    row_string = ExecuteCustomSQLQuery(database_name,
    """ SELECT * FROM {table_name} WHERE {feed_sources} = '{var_one}';""".format(
        table_name=table_name, feed_sources=feed_sources, var_one=params[0]), "Yes")



    row_string = str(row_string).split(',')
    # print("row_string " + str(row_string[1])[:-1][2:] + " end")
    # row_string[1][:-3][2:]
    return str(row_string[1])[:-1][2:]

def GetTargetRowFromDBfeed_urls(
        rss_str_var_feed_sources, url_var_feed_urls, database_name, table_name, feed_urls):

    params = (rss_str_var_feed_sources, url_var_feed_urls)

    # print("params[0] " + str(params[0]))
    # print("params[1] " + str(params[1])[:-3][2:])

    row_string = ExecuteCustomSQLQuery(database_name,
    """ SELECT * FROM {table_name} WHERE {feed_urls} = '{var_one}';""".format(
        table_name=table_name, feed_urls=feed_urls, var_one= str(params[1])), "Yes")

    # print("feed_urls " + str(row_string) + " end")
    # row_string = str(row_string).split(',')

    return row_string[0]

def GetTargetRowFromDBcashed_feed_urls(
        rss_str_var_feed_sources, url_var_feed_urls, database_name, table_name, cashed_feed_urls):

    params = (rss_str_var_feed_sources, url_var_feed_urls)

    # print("params[0] " + str(params[0]))
    # print("params[1] " + str(params[1])[:-3][2:])

    row_string = ExecuteCustomSQLQuery(database_name,
    """ SELECT * FROM {table_name} WHERE {cashed_feed_urls} = '{var_one}';""".format(
        table_name=table_name, cashed_feed_urls=cashed_feed_urls, var_one= str(params[1])), "Yes")

    # print("feed_urls " + str(row_string) + " end")
    # row_string = str(row_string).split(',')

    return row_string[0]


def ExecuteCustomSQLQuery(sqlite_file, sql_query, boolean_return):
    conn, c = connect(sqlite_file)
    # print(sql_query)

    # try:
    c.execute(sql_query)
    # except Exception as e:
    #     s = str(e)
    #     print("Query ignored -> ExecuteCustomSQLQuery failed: " + s)
    #     pass


    if (boolean_return is "No"):
        conn.close()
    if (boolean_return is "Yes"):
        all_rows = c.fetchall()
        conn.close()
        return all_rows


def GetTargetRowFromDBVersion2(rss_str_var_feed_sources, url_var_feed_urls, database_name, table_name, feed_sources, feed_urls):
    # print(table_name)
    params = (rss_str_var_feed_sources, url_var_feed_urls)
    row_string = ExecuteCustomSQLQuery(database_name,
     """ SELECT * FROM {table_name} WHERE {feed_sources} = '{var_one}';""".format(
         table_name=table_name, feed_sources=feed_sources, var_one=params[0]), "Yes")

    row_string = str(row_string).split(',')
    # print(row_string)
    return row_string

def GetFirstValueFromDatabaseString(database_string):
    FirstValue_string = str(database_string).split(',')
    return FirstValue_string[0][:-2][5:]

def GetSecondValueFromDatabaseString(database_string):
    SecondValue_string = str(database_string).split(',')
    return SecondValue_string[1][:-5][4:]

def SimplePopulateSQLTable(database_name, table_name, column1, column2, variable1, variable2):
    system_params = (database_name, table_name)
    variables_params = (column1, column2)
    atributes = (system_params, variables_params)
    params = (variable1, variable2)

    ExecuteINSERT_INTO_SQL_withAtributes(atributes, params)


def PopulateSQLTableForBot(rss_str_var_feed_sources, url_var_feed_urls, database_name, table_name, feed_sources, feed_urls, cashed_feed_urls):
    # sqlite_file = 'feed_sources_and_urls_database.sqlite'
    # table_name = 'feed_database'
    # feed_sources = 'feed_sources'
    # feed_urls = 'feed_urls'

    field_type = 'varchar'

    system_params = (database_name, table_name)
    variables_params = (feed_sources, feed_urls)
    atributes = (system_params, variables_params)

    params = (rss_str_var_feed_sources, url_var_feed_urls)

    CreateNewDatabase(database_name, table_name, feed_sources, feed_urls, field_type, cashed_feed_urls)
    ExecuteINSERT_INTO_SQL_withAtributes(atributes, params)

def CreateNewTableInDatabase(database_name, new_table_name, feed_sources, frequency):
    ExecuteScriptCustomSQLQuery(database_name,
                                """ CREATE TABLE {table_name} ({feed_sources} varchar(255),{frequency} varchar(255)); """
                                .format(table_name=new_table_name, feed_sources=feed_sources,frequency=frequency), "No")

def SubmitFunction(link, NumberOfComments, title, url, subreddit, feed, cssClass, tag):
    # The code part that --> SUBMITS <--- . Commend it when doing changes.
    # ---------------------------------------------------------

    if 'https://www.reddit.com/' in link:
        SourceReddit = link.replace('https://www.reddit.com/r/', '')
        SourceReddit = 'r/' + SourceReddit.split("/")[0]
        submit = u' '.join(('[', str(NumberOfComments), '] ', str(title[0:265]))).encode('utf-8')
        # print("> " + str(url) + " <-- Specific URL (feed_urls)")
        # print("url: " + str(url))
        subreddit.submit(submit, url=url)
    else:
        SourceNonReddit = link.split("/")[2]
        SourceNonReddit = SourceNonReddit.replace('www.', '')
        # print("> " + str(url) + " <-- Specific URL (feed_urls)")
        # print("url: " + str(url))
        submit = str(title[0:265]).encode('utf-8')
        subreddit.submit(submit, url=url)

    # #This is the part that is used for local css updates, but it may no be needed.
    # # Removed due to seeing that the flair adding part is lower in the code.
    # # You can see the git history for the code of this part
    # The code part that --> ADDS CSS FLAIRS <--- . Commend it when doing changes.

    # ---------------------------------------------------------
    for submission in subreddit.new(limit=100):
        if link in submission.url:
            if 'https://www.reddit.com/' in link:
                reply = RemoveUsersReddit(BeautifulSoup(feed['entries'][0]["description"],
                                                        'html.parser').get_text()) \
                        + "\n" + "\n" + 'submission.num_comments --> ' + NumberOfComments
                submission.reply(reply[0:9999])
                submission.mod.flair(text=tag, css_class=cssClass)  # unicode(SourceReddit)

            else:
                reply = RemoveUsersReddit(BeautifulSoup(feed['entries'][0]["description"], 'html.parser').get_text())
                submission.reply(reply[0:9999])
                submission.mod.flair(text=tag, css_class=cssClass)  # unicode(SourceNonReddit)

            break

""" METHOD OVERRIDE """
def RatingCounter_ClusterableBots(user_agent, client_id, client_secret, username, password, subreddit, waitTime):
    # print("runs324324")
    RatingCounter_Thread = threading.Thread(target=RatingCounter, args=(user_agent, client_id, client_secret, username, password, subreddit))
    RatingCounter_Thread.start()
    # time.sleep(waitTime / 3)
    # Trying this with increased waitTime
    time.sleep(waitTime)
    # RatingCounter(user_agent, client_id, client_secret, username, password, subreddit)

""" RatingCounter counts if the rating on posts is float and if it, it sends email to mod so that
# the rated news source is taken actions against. If the source scores multiple downvotes, mod can delete it,
# or lower its rating. """
def RatingCounter(user_agent, client_id, client_secret, username, password, subreddit_var):

    # dic = defaultdict(list)
    # lis = []
    # coordinatedGeneratedById = []

    # while True:

    rating_database_name = 'rating_sources_and_urls_database.sqlite'
    rating_table_name = 'rating_database'
    rating_sources = 'rating_sources'
    rating_boolean_ifsend = 'rating_boolean_ifsend'

    start_time = time.time()


    print(colored("RatingCounter Thread id " + str(threading.current_thread().ident),'magenta'))

    while True:
        # print("gggg")

        reddit = praw.Reddit(user_agent=user_agent,
                             client_id=client_id, client_secret=client_secret,
                             username=username, password=password)

        subreddit = reddit.subreddit(subreddit_var)

        source1 = parser.get('URL_Sources', 'source1')
        source2 = parser.get('URL_Sources', 'source2')
        source3 = parser.get('URL_Sources', 'source3')
        source4 = parser.get('URL_Sources', 'source4')
        source5 = parser.get('URL_Sources', 'source5')
        source6 = parser.get('URL_Sources', 'source6')
        source7 = parser.get('URL_Sources', 'source7')
        source8 = parser.get('URL_Sources', 'source8')
        source9 = parser.get('URL_Sources', 'source9')
        source10 = parser.get('URL_Sources', 'source10')

        try:

            data = get_data_from_all_google_sources(source1, source2, source3,
                                                    source4, source5, source6, source7, source8, source9, source10)

            x = 0
            dataIndexArray1 = []
            dataIndexArray2 = []
            dataIndexArray3 = []

            for dataIndexer1 in data:

                dataIndexArray1.append(dataIndexer1)
                x = x + 1
                for dataIndexer2 in data[dataIndexer1]['urls']:
                    dataIndexer2 = codecs.decode(dataIndexer2, 'unicode_escape').encode('latin1').decode('utf8')

                    dataIndexArray2.append(dataIndexer2)
                    dataIndexArray3.append(dataIndexer2 + " " + dataIndexer1 + " " + data[dataIndexer1]['cssClass'])

            threadsList = []
            threadsList = dataIndexArray3


        except Exception as e:
            # print("success111")
            s = str(e)
            indexExistingCheckBoolean = False
            print('EXCEPTION1                                                                                ')
            print(s)
            pass

        i = 0
        for submission in subreddit.new(limit=100):  # was 1000, changed to 100 for better speed
            # print(submission.url + " "  + str(submission.upvote_ratio)) #+ str(submission.ups) + " " + str(submission.downs) + " "

            # print(submission.url)
            # print(submission.upvote_ratio)

            # print("submission.url " + submission.url + " submission.upvote_ratio " + str(submission.upvote_ratio))

        # Have a database of all float values and send emails for float values
            if (str(submission.upvote_ratio) == "1.0"):
                # Link is not upvoted or downvoted. Do nothing.
                # print("Both links are the same. Do nothing")
                pass
            else:
                # Link is upvoted or downvoted. Do something.
                try:
                    # The gist of this try catch is to to find posts with different than 1 second value and
                    # add then to the db and send email, all done in the except statement

                    print(colored("$$$$$$$@@@@@@@@@@ success submission.url "
                                  + submission.url + " submission.upvote_ratio " + str(submission.upvote_ratio), 'red'))

                    # A trigger for the rating in the try that also works for all but the first element
                    databaseFeedURL = GetTargetRowFromDBVersion2(submission.url, "1",
                                                                 str(rating_database_name), str(rating_table_name),
                                                                 str(rating_sources), str(rating_boolean_ifsend))

                    # print("databaseFeedURL " + str(len(databaseFeedURL))+ " databaseFeedURL " +str(databaseFeedURL))

                    if (len(databaseFeedURL) == 1):
                        PopulateSQLTableForBot(submission.url, "1",
                                               str(rating_database_name), str(rating_table_name),
                                               str(rating_sources), str(rating_boolean_ifsend), cashed_feed_urls)
                        databaseFeedURL = GetTargetRowFromDBVersion2(submission.url, "1",
                                                                     str(rating_database_name), str(rating_table_name),
                                                                     str(rating_sources), str(rating_boolean_ifsend))
                        parsed_uri = urlparse(submission.url)
                        base_url = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
                        # print(base_url)
                        incraesing_variable_for_database = 0

                        SimplePopulateSQLTable(str(rating_database_name), 'frequency_table'
                                               ,'feed_sources', 'frequency'
                                               , base_url, incraesing_variable_for_database)

                        # UPDATE frequency_table SET frequency = frequency + 1 WHERE feed_sources='https://askubuntu.com/'

                        ExecuteScriptCustomSQLQuery(str(rating_database_name),
                                """UPDATE frequency_table SET frequency = frequency + 1 WHERE feed_sources='{fs}'"""
                                                    .format(fs=base_url), 0)

                        # print("ExecuteScriptCustomSQLQuery: " + str(ExecuteCustomSQLQuery(str(rating_database_name),
                        # """SELECT DISTINCT feed_sources, MAX(frequency) FROM frequency_table WHERE feed_sources='{fs}'
                        # GROUP BY feed_sources ORDER BY feed_sources DESC;""".format(fs=base_url), "Yes")))

                        send_email("URL: " + str(submission.url) + " Source + Score: " +
                                   str(ExecuteCustomSQLQuery(str(rating_database_name),
                        """SELECT DISTINCT feed_sources, MAX(frequency) FROM frequency_table WHERE feed_sources='{fs}' 
                        GROUP BY feed_sources ORDER BY feed_sources DESC;""".format(fs=base_url), "Yes")))

                except Exception as e:
                    s = str(e)
                    print("Failed. Either because of an error with the query "
                          "or because the database is not populated. Populating regardless." + " \n" + s)

                    # A dt action that works first element
                    PopulateSQLTableForBot(submission.url, "1",
                                           str(rating_database_name), str(rating_table_name),
                                           str(rating_sources), str(rating_boolean_ifsend), cashed_feed_urls)

                    # print("Added:" + str(submission.url) + " "  + str(submission.upvote_ratio))

                    CreateNewTableInDatabase(str(rating_database_name), 'frequency_table', 'feed_sources', 'frequency')

                    parsed_uri = urlparse(submission.url)
                    base_url = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
                    # print(base_url)
                    incraesing_variable_for_database = 0

                    SimplePopulateSQLTable(str(rating_database_name), 'frequency_table'
                                           , 'feed_sources', 'frequency'
                                           , base_url, incraesing_variable_for_database)

                    ExecuteScriptCustomSQLQuery(str(rating_database_name),
                                                """UPDATE frequency_table SET frequency = frequency + 1 WHERE feed_sources='{fs}'"""
                                                .format(fs=base_url), 0)

                    # print("ExecuteScriptCustomSQLQuery: " + str(ExecuteCustomSQLQuery(str(rating_database_name),
                    #   """SELECT DISTINCT feed_sources, MAX(frequency) FROM frequency_table WHERE feed_sources='{fs}'
                    #   GROUP BY feed_sources ORDER BY feed_sources DESC;""".format(
                    #       fs=base_url), "Yes")))

                    # send_email("This url was downvoted:" + str(submission.url) + " "  + str(submission.upvote_ratio))

                    send_email("URL: " + str(submission.url) + " Source + Score: " + str(ExecuteCustomSQLQuery(str(rating_database_name),
                    """SELECT DISTINCT feed_sources, MAX(frequency) FROM frequency_table WHERE feed_sources='{fs}' 
                    GROUP BY feed_sources ORDER BY feed_sources DESC;""".format(
                        fs=base_url), "Yes")))

if __name__ == '__main__':
#Cashing thread calls are made for the local cashing idea that proves, for now, to be slower and thus inefficient
    # waitTime = 50

    try:
        if sys.argv[1] is not None:
            waitTime = int(sys.argv[12])
    except IndexError:
        parser = configparser.ConfigParser()
        parser.read('credentials.ini')
        waitTime = int(parser.get('Settings_Subreddit', 'waitTime'))

    ModeratingThreadString = "ModeratingThread"
    PostingThreadString = "PostingThread"
    CashingThreadString = "CashingThread"

    operation_mode = ""
# Windows based calling by args given from the autostart script on call. If args are detected, this should be the way to go
    try:
        if sys.argv[1] is not None:
            operation_mode = sys.argv[7]
    except IndexError:
# This method of credentials taking is used for linux based systems like rasberry pi. If no args are detected, this should be the way to go
#         with open('credentials', 'r') as myfile:
#             data = myfile.read()
#         StringTranslator = []
#         StringTranslator = data.split('\n')
#         operation_mode = StringTranslator[6]

        parser = configparser.ConfigParser()
        parser.read('credentials.ini')
        operation_mode = parser.get('Settings_Subreddit', 'operation_mode')

# OnlineRealTimeComparison works by launching all the threads and have them work together
    if(operation_mode == "OnlineRealTimeComparison"):
        LauncherModeratingThread = threading.Thread(target=main, args=(ModeratingThreadString, waitTime))
        LauncherModeratingThread.start()

        LauncherPostingThread = threading.Thread(target=main, args=(PostingThreadString, waitTime))
        LauncherPostingThread.start()

        # LauncherCashingThread = threading.Thread(target=main, args=(CashingThreadString, waitTime))
        # LauncherCashingThread.start()

# LocalDatabasePostOnChange works launching PostingThread and filtering the information that it can post
    if(operation_mode == "LocalDatabasePostOnChange"):
        LauncherPostingThread = threading.Thread(target=main, args=(PostingThreadString, waitTime))
        LauncherPostingThread.start()

# HybridOperationMode combines both of the above modes.
# Advantage: it will both filter links from a database before posting and
# launch a moderation thread that deletes duplicate threads.
# Disadvantage: needs to write and read from a database located on the drive.
# May not be best for a raspberry pi setup because it holds the disadvantages of LocalDatabasePostOnChange.
# Also will be rather resource intensive.

    if(operation_mode == "HybridOperationMode"):
        LauncherPostingThread = threading.Thread(target=main, args=(PostingThreadString, waitTime))
        LauncherPostingThread.start()

        LauncherModeratingThread = threading.Thread(target=main, args=(ModeratingThreadString, waitTime))
        LauncherModeratingThread.start()

# Bots made from other people are a good way to enhance the functionality of this bot.
# They should be launched in their own thread and they should not directly be interfering with the main operation modes.
# Also it is possible to have a cluster of raspberry pi-s run different bots without interfering with each other.
# Requires local read/write operations in a database

# July 2019 update: ClusterableBots has a problematic thread management where new threads are created constantly
# and never terminated. I have a theory that it shut downs the whole execution of the bot.
    RatingCounter = ClusterableBots('RatingCounter', waitTime)
