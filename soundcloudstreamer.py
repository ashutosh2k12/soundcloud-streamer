from bs4 import BeautifulSoup
import urllib,re,sys, argparse, json

#url = "https://soundcloud.com/djvipulkhuranabangalore/yeh-kali-kali-aankhen-remix"
clientid = "e77417802c4e7a8c4f5eaa54b8990ee9"

def getTrackJSON(query):
    global clientid
    apiurl = "https://api.soundcloud.com/tracks/?q="+query+"&client_id="+clientid
    pageapi = urllib.urlopen(apiurl).read()
    data = json.loads(pageapi)
    if data and len(data) > 0:
        return data[0].get('id') #Get only top result
    
def getTrackId(url):
    metaprop = {"property":"al:android:url"}

    page3 = urllib.urlopen(url).read()
    soup3 = BeautifulSoup(page3,"html.parser")

    desc = soup3.findAll(attrs=metaprop)
    trackid = desc[0]['content'].encode('utf-8')

    if not trackid:
        return False
    else:
        #Get only string from whole meta data(Ex- soundcloud://sounds:152756177)
        trackidstr = re.findall('\d+',trackid)
        return trackidstr[0] if len(trackidstr) > 0 else False
        

def getDownloadableUrl(trackid):
    if not trackid:
        return False

    global clientid
    return "https://api.soundcloud.com/tracks/%s/stream?client_id=%s" %(trackid, clientid)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-q", help="SoundCloud Track URL")
    args = argparser.parse_args()

    if getattr(args, 'q') is None:
        print "Please provide a valid query string"
        sys.exit(0)

    query = getattr(args, 'q')
    #sys.stdout.write(getDownloadableUrl(getTrackId(url))) (useful to get trackid from url)
    sys.stdout.write(getDownloadableUrl(getTrackJSON(query)))
