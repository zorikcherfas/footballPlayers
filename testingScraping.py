# import urllib2
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

filename_100_players = "players.csv"
filename_wiki_dump = "wikiDump.csv"
filename_errors = "errors.csv"
def main():

    fWiki = open(filename_wiki_dump,"w")
    fError = open(filename_errors , "w")
    headersWiki = "name,date,team\n"
    fWiki.write(headersWiki)
    for name in buildTop100Players():
        buildWiki(name,fWiki, fError)
    fWiki.close()
    fError.close()

def buildWiki(originalName ,fWiki, fError):
    try:

        import ssl
        name = originalName
        name = name.replace(' ','_')
        name = name.title()

        url ="https://en.wikipedia.org/wiki/" + name
        print(url)
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        client = urlopen(url, context=ctx)
        page_html = client.read()
        client.close()
        page_soup = soup(page_html , "html.parser")

        table = page_soup.find('table')
        rows = table.find_all('tr')

        interator = 0
        teamIndexStart =0
        taemIndexEnd = 0

        for row in rows:
            interator = interator +1
            if "Senior career" in row.text:
                teamIndexStart = interator+1;

            if "National" in row.text:
                taemIndexEnd = interator-1
                break

        # print("teamIndexStart: %d"% teamIndexStart)
        # print("taemIndexEnd: %s"% taemIndexEnd)
        for i in range(teamIndexStart, taemIndexEnd):
            # print("text: %s" % rows[i].text)
            list = rows[i].text.split("\n")
            print("years: %s team %s" % (list[1], list[2]))
            fWiki.write(originalName + "," + list[1] + "," + list[2]+"\n")

            # url = "https://en.wikipedia.org/wiki/Cristiano_Ronaldo"
        # client = urlopen(url)
        # page_html = client.read()
        # client.close()
        # page_soup = soup(page_html, "html.parser")
        # f.write(page_soup.text)
    except:
        print("there was some error, continue...")
        fError.write(originalName)


def buildTop100Players():
    import csv
    url = "http://www.goal.com/en/news/fifa-18-player-ratings-the-complete-list-of-the-top-100/141gsqcxv5djl11pm1cq061eks"
    client = urlopen(url)
    page_html = client.read()
    client.close()
    page_soup = soup(page_html , "html.parser")

    players = page_soup.findAll('center')

    filename = "players.csv"
    f = open(filename , "w")

    headers = "name,team\n"

    f.write(headers)

    listOfNames=[]
    for player in players:
        row = player.h2.strong.text.strip()
        indexStartName = row.index('.')
        indexEndName = row.index('|')
        name = row[indexStartName+1 : indexEndName].strip()
        team = row[indexEndName+1:].strip()
        # print("Name: %s"% name.strip())
        listOfNames.append(name)
        # print("Team: %s"% team.strip())
        f.write(name +"," + team + "\n")


    f.close()
    print ("buildTop100Players succesded")
    return listOfNames

def dumpRonaldoWiki():
    filename = "ronaldoWiki.html"
    f =open("")



if __name__ == "__main__":
    main()
