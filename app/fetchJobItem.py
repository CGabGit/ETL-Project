from requests.models import stream_decode_response_unicode
import dbConnection
import scraper
import re, requests, json, time
from datetime import datetime
from bs4 import BeautifulSoup
import pandas as pd
#from requests_html import HTMLSession
from random import randrange

def extractData():
    df_searchResults = dbConnection.loadTblSR()
    print(df_searchResults.head(n=10))
    for i, row in df_searchResults.iterrows():
        rel_url = row['job_link']
        job_id = row['job_id']
        if dbConnection.rowExists(job_id) == False:
            url = f"https://www.stepstone.de{rel_url}"            
            #s = HTMLSession()

            ## base request
            # resp = requests.get('https://www.stepstone.de/',
            #             headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'en-US,en;q=0.9','accept-encoding': 'gzip, deflate, br','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','upgrade-insecure-requests':'1'})
            # cookies_dict = resp.cookies
            cookies_dict = scraper.setCookieRequest('https://www.stepstone.de/')
            time.sleep(randrange(8,41))

            # # request with cookies
            # r = requests.get(url,cookies = cookies_dict,
            #                     headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
            #                             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            #                             'accept-language': 'en-US,en;q=0.9',
            #                             'upgrade-insecure-requests': '1',
            #                             'sec-fetch-dest' : 'document',
            #                             'sec-fetch-mode' : 'navigate',
            #                             'sec-fetch-site': 'none'})
            r = scraper.scrapeRequest(url, cookies_dict)
            soup = BeautifulSoup(r.content, 'html.parser')

            print("get request ok for id:",job_id )
            print("url: \n",url )

            #r.html.render(sleep=30, timeout=120)
            if r.status_code != 200:
                print("Bad Status Code:",r.status_code)
                continue
            
            #soup_meta = BeautifulSoup(r.html.raw_html,"html.parser")
            #print(soup_meta)
            #break

            print(r.status_code)
            # data = r.content
            data = r.text

            # meta data extraction:
            soup_meta = BeautifulSoup(r.text,"html.parser")
            try:
                script_html = soup_meta.find("script", id="js-section-preloaded-HeaderStepStoneBlock").text
                script_html = script_html.strip()[113:-1]
            except:
                continue

            pattern_listingData = re.compile(r'(?:\"listingData\":)(.+?)}}')
            pattern_companyData = re.compile(r'(?:\"companyData\":)(.+?)}')

            listingData = str(re.search(pattern_listingData,script_html).group(0))
            companyData = str(re.search(pattern_companyData,script_html).group(0))

            listingData = "{"+listingData+"}"
            companyData = "{"+companyData+"}"

            json_listingData = json.loads(listingData)
            json_companyData = json.loads(companyData)

            job_id = json_listingData['listingData']['id']
            title = json_listingData['listingData']['title']
            company_name = json_companyData['companyData']['name']
            location = json_listingData['listingData']['metaData']['location']
            
            try:
                contractType = json_listingData['listingData']['metaData']['contractType']
            except:
                contractType = "none"
            try:
                workType = json_listingData['listingData']['metaData']['workType']
            except:
                workType = "none"
            try:
                onlineDate = json_listingData['listingData']['metaData']['onlineDate']
            except:
                onlineDate = "none"
            # extract text content:
            # description-content (Aufgaben) & profile content (Qualifikationen)
            soup = BeautifulSoup(data, 'html5lib')
            print('html5 lib soup erfolgreich erstellt')
            profile_content = soup.select_one('div[class*="at-section-text-profile-content"]')
            profile_content = str(profile_content)
            description_content = soup.select_one('div[class*="at-section-text-description-content"]')
            description_content = str(description_content)
            
            def clean(content):
                content = content.replace('\xad','').replace('\t', ' ').replace('&nbsp;',' ').replace('\xa0','').replace('&amp;','und').replace('\r','').replace('\n','')
                return content

            profile_content = clean(profile_content)
            description_content = clean(description_content)

            # insert into db:

            print(job_id)
            print(title)
            print(company_name)
            print(location)
            print(contractType)
            print(workType)
            print(onlineDate)
            print(type(description_content))
            print("\n")
            print(description_content)
            print("\n")
            print(profile_content)

            connection = dbConnection.openDBConnection()
            jobitem = [job_id, title, company_name, location, contractType,workType ,onlineDate,description_content,profile_content]
            dbConnection.insertToTblJobitems(connection, jobitem, "tbl_jobitems")
            dbConnection.closeDBConnection(connection)

            print("\n")
            print(f"job posting {job_id} saved to DB")
            time.sleep(randrange(29,96))


            

