import pandas as pd
from requests import get
import os
import time

#put your own api key
api_key = 'SK0ELkbDinjHhocbZAu75iWORIZiuVpq'
#specify where to save the articles as csv files
output_path = 'data/NYTimes_articles/'

def get_url(query, begin_date, end_date, api_key, page=1):
    '''
    This function sepcifically looks in the NY Times articles API using specified query
        e.g 'terrorism'or 'attack' and begin and end dates in YYYYMMDD format. 
    ''' 
    url = ("http://api.nytimes.com/svc/search/v2/articlesearch.json?q={0}&begin_date={1}&end_date={2}&sort=relevance&page={3}&api-key={4}").format(query, begin_date, end_date, page, api_key)
    return url

def parse_articles(query):
    '''
    This function takes in a response to the NYT API as the json format and parses
    the articles into a list of dictionaries.
    '''
    news = []
    for i in query['response']['docs']:
        dic = {}
        dic['id'] = i['_id']
        if i['abstract'] is not None:
            dic['abstract'] = i['abstract'].encode("utf8")
        dic['headline'] = i['headline']['main'].encode("utf8")
        dic['desk'] = i['news_desk']
        dic['date'] = i['pub_date'][0:10] # cutting time of day.
        dic['section'] = i['section_name']
        if i['snippet'] is not None:
            dic['snippet'] = i['snippet'].encode("utf8")
        dic['source'] = i['source']
        dic['type'] = i['type_of_material']
        dic['url'] = i['web_url']
        dic['word_count'] = i['word_count']
        # locations
        locations = []
        for x in range(0,len(i['keywords'])):
            if 'glocations' in i['keywords'][x]['name']:
                locations.append(i['keywords'][x]['value'])
        dic['locations'] = locations
        # subject
        subjects = []
        for x in range(0,len(i['keywords'])):
            if 'subject' in i['keywords'][x]['name']:
                subjects.append(i['keywords'][x]['value'])
        dic['subjects'] = subjects   
        news.append(dic)
    return(news) 
    
    
def get_articles(query, year):
    '''
    This function accepts a year in string format (e.g.'1980')
    and a query (e.g.'Amnesty International') and it will 
    return a list of parsed articles (in dictionaries)
    for that year.
    '''
    all_articles = []
    
    
    for i in range(0,100): #NYT limits pager to first 100 pages. Try other ranges.
        time.sleep(6)
        try: 
            r = get(get_url(query, str(year)+'0101', str(year)+'1231', api_key, page=i))
            articles = parse_articles(r.json())
            all_articles = all_articles + articles
        except: break
    return(all_articles)
    
    
def get_store_csv(query, year, output_path):
    '''
    Using the previous fucntions, it takes the query, year and output_path to save
    the articles found by NY Times API into a csv format for later use. 
    '''
    nytimes = get_articles(query, year)
    df_nytimes = pd.DataFrame(nytimes)
    #print(df_nytimes.shape)

    df_nytimes.to_csv(os.path.join(output_path,"NYT"+str(query)+"_"+str(year)+".csv"))
    df_nytimes.head()
    
    return df_nytimes