import scraperwiki
import lxml.html
url = scraperwiki.scrape("https://aidworkersecurity.org/incidents/search")
root = lxml.html.fromstring(url)
for tr in root.cssselect("div[align='left'] tr"):
    tds = tr.cssselect("td")
    if len(tds)==12:
        data = {
            'ID' : tds[0].text_content(),
            'Month' : tds[1].text_content(),
            'Day' : tds[2].text_content(),
            'Year' : int(tds[3].text_content()),
            'Country' : tds[4].text_content(),
            'UN' : int(tds[5].text_content()),
            'INGO' : int(tds[6].text_content())

        }
        print data

scraperwiki.sqlite.save(unique_keys=['ID', 'Month', 'Day', 'Year', 'Country', 'UN', 'INGO'], data=data)