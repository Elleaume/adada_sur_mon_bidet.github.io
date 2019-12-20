# Terrorism perceived though western news

## Data Story

**Main link** : https://elleaume.github.io/adada_sur_mon_bidet.github.io/

Source code: https://github.com/Elleaume/adada_sur_mon_bidet.github.io

Two jupyter notebooks were used to build the whole data story, one with the whole Global Terrorism Dataset processing and analysis : `GlobalTerrorismProject.ipynb` and another with the processing of American News related datatsets : `Clean_journals.ipynb`.
Due to the size of the merged jupyter notebooks, some plots may not be correctly visible on juypter however all these are present in the data story (link above). 

# Abstract

Since September 11 2001, terrorism has been in the headlines around the globe. A general fear reappears every few years as events labeled as "terrorist attacks" occur. Certain parties have gained in popularity in the past few years, often using the anxiety of "dangerous terrorists" as a pretext to defend anti-immigrant policies. Have terrorist attacks increased in the past years as we are lead to believe? or has the rate been more or less constant? Are foreigners or immigrants really more likely to commit these terrorist attacks? News coverage plays a big role in how we perceive these events, some events are debated and discussed during weeks, while others are never mentioned. We want to explore the rate and distribution of these attacks over the world, and dive into their news coverage in the western hemisphere.  

# Research questions

- Have the terrorist attack rates, motives, locations, changed over the past 50 years?
- Where do terrorist attacks occur?
- Who commit terrorist attacks and by what motive?
- How are is global terrorism depicted in some selected popular western newpapers? 

# Datasets

## Global Terrorism Database

This database is a collection of facts about terrorist attacks from 1970-2017. The facts cover location, date, motive, and who claimed the attack and a very large variety of other very specific metrics. 
https://www.kaggle.com/START-UMD/gtd

Also all the data from 1993 was lost during the digitalisation process. We plan to scrap to Wikipedias attacks for this year in the future. Another limitation regards entries before 1997. The entries were not quite as standardized, and certain parameters are missing for these attacks. Analysis according to some parameters may have to be done concerning only the data after 1997. 

From data collection, terrorists attacks from the last 50 years were reviewed to measure the extent of terrorist attacks around the world. More specifically by focusing on:
- the number of attacks per year
- attacks resulting or not in dead and wounded
- the values of the damaged properties

## All the news 
This database is a collection of news coverage from CNN, New York Times, Breitbart, Fox news, the Guardian, 
https://www.kaggle.com/snapcrack/all-the-news#articles3.csv 

After investigating all-the-news datset, we found out that the distribution in time of the articles was highly imbalanced and most of the data was dated from 2017 and 2016 with very few entries for earlier yeares. After a first fitlering of the articles using a sentence matcher on the titles, only about 3000 articles corresponding to a custom-build dictionary, were found. One limitation which we will need to tackle in the upcoming weeks is how we identify if an article concerns a terror attack. For the time being, we have given a naive list of a few words which we thought matched with terrorism. This induces a bias in what type of articles we are analysing. We will need to create a less biased library, using a liwc dictionary for example, to search for unbiased word comparison in the upcoming weeks. 

The country concerned in the article was extracted from the content and saved as the location. We realise that this is a rather naive way to depict which countries are covered, and we will need to do the same regarding cities. As this dataset concerns only american news, the "United States" is probably under-represented in our way of identifying the countries. An article concerning an attack in "Oklahoma City" may not necessarily have the country specified as it is obvious to the public reading the news that this concerns the United States. Another potential issue is that for the time being, as soon as one country is found within the content, we consider that this is the "location" of the attack. However, it could be that the country appearing first in the text could be part of an introduction giving political or historical background for example, and that this country is not the country where the attack occured. We may have to modify this technique to make sure that cities extracted as well as the countries overlap, or possibly count the amount of appearances of different country words within the content, and identify as the country appearing the most as the location of the attack.

### New York Times articles

As the amount of articles from all the news resulted in a rather narrow dataset, we decided to merge the articles found so far with another dataset. We had to narrow down the diversity of publishers and chose to start using only New York Times articles. The New York Times provides a very robust Application Programming Interfaces (APIs) to enable computer applications to request informations on a large diversity of subjects. Article Search API retrieves headlines, abstracts and links to associated multimedia from 1851 to today and can be used to look up articles by keyword. To contrsuct a preliminary database, we used the keyword `terrorism` and data was returned in a  `JSON` format. We therefore extracted articles from 1997 to 2017 which contained a terrorism tag. This dataset will need to be elaborated by broadening the tag search, as this may still be too "restrictive".

New York Times data contains an abstract, date, headline, location when available, section, list of subjects, the url	and a word count.
The country was extracted from the location column to allow for comparison with the Global terrorism database dataset. 

### Limitations

Our main limitation concerns the articles dataset. Most articles in All-the-news were published in 2015, 2016 and 2017. This has a great impact on news coverage in time, since the datataset with articles has not an uniform distribution in time and has much more articles for years 2015-2017 any plot with analysis in time of terror attacks coverage will end up having few datapoints for years before 2015 and then the plot shall not be as representative as we would have wanted.

### Points of interest

**Specific events** We have looked into the amount of casualties and property damage over time according to areas. Spcefiic peaks have beed detected, indicating significant events. We will want to look into the peaks of the different graphs to understand where these come from, and see how these events are covered in the news. 
**Groups claiming attacks** The groups which have claimed the largest number of attacks have been plotted. We would like to dive deeper into this subject and unsderstand a few things, including:
* which groups are active over what period?
* which populations and locations are targeted?
* what motives are the most prevalant according to the various groups?
* which methods are employed to try to pass their message? is property dammage a goal? or human casualties?
* how is the news coverage distributed according to the different actors?
**linking with news** we will be looking at the number of articles during the major events identified by the peaks in material dammage and human casualties. To look into the coverage, we will be looking at the length of the articles in question, which can give a general insight as to if the article is more factual and to the point, or if it is a an extensive article. The number of articles will also give an indication of the general publics awareness.

## Contributions

#### 1. Processing Global Terrorism dataset
* Dataset cleaning and recovery of wronlgy formatted data - Annina Stuber 
* Data exploration - Camille Elleaume and Annina Stuber
* Statistics of interest - Camille Elleaume and Annina Stuber

#### 2. Processing of Articles related dataset
* Cleaning cleaningr - Francesca Luongo
* Data exploration - Francesca Luongo
* Creation of a 'terrorism score' to filter out articles of interest and selection of articles - Annina Stuber
* Topics detection and attribution of a theme score per article - Francesca Luongo and Annina Stuber
* Find geographical information in the articles - Annina Stuber and Francesca Lunongo 
* Web scraping of New York Times articles on terrorism and missing 1993 data on Wikipedia - Christelle Schneuwly
* Merging and formatting of All-the-news dataset and New York Times articles - Francesca Luongo and Annina Stuber
* Linking of articles specifically covering terror attacks - Christelle Schneuwly

#### 3. Datastory and plots
* Creation and style of the website - Camille Elleaume
* Plots with structural variables in Global Terrorism Dataset - Camille Elleaume
* World map with terror attacks - Christelle Schneuwly
* Terrorist groups analysis with their targets and the weapons they use - Camille Elleaume
* Repartition of attacks per continents for most active groups - Annina Stuber
* Word maps of most active groups per continent - Annina Stuber
* Themes covered by terrorism related articles - Annina Stuber
* Radar plots with themes coverd by articles on terrorism in all continents - Francesca Luongo
Mirror bar plot of terror attacks covered by news articles and average length of the articles for a selection of countries - Christelle Schneuwly
* Most active groups in Iraq line plot and themes scores in Iraq and the US - Annina Stuber and Francesca Luongo

#### 4. Poster presentation

* Poster creation - all 
* Poster oral presentation 


## Plan and temporal objectives

**2 Dec 2019**:  
* Scrape data to complete as much as possible the Global terrorism database of 1993
* Extend our article database by having a less biased dictionnary

**9 Dec 2019**:
* Complete analysis on the groups claiming terror attacks
* Complete analysis concerning specific events

**16 Dec 2019**
* Complete analysis of article coverage
* Add everything to datastory

**19 Dec 2019**
* Finish updating the datastory

**20 Dec 2019**
* Reread datastory and last minute adjustments before hand in

**6 Jan 2020**
* Have started the Poster for the presentation

**15 Jan 2020**
* Print the poster 
* Prepare presentation

