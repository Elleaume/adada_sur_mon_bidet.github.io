---
layout: home
header:
  overlay_image: img/HomeImg.jpg
  overlay_filter: 0.5 # same as adding an opacity of 0.5 to a black background
  caption: "Photo credit: [_0_h_m_](https://www.instagram.com/_0_h_m_/?hl=fr)"
  actions:
    - label: "More Info"
      url: "https://unsplash.com"
---

<body>


Since September 11 2001, terrorism has been in the headlines around the globe. A general fear reappears every few years as events labeled as "terrorist attacks" occur. Certain parties have gained in popularity in the past few years, often using the anxiety of "dangerous terrorists" as a pretext to defend anti-immigrant policies. Have terrorist attacks increased in the past years as we are lead to believe? or has the rate been more or less constant? Are foreigners or immigrants really more likely to commit these terrorist attacks? News coverage plays a big role in how we perceive these events, some events are debated and discussed during weeks, while others are never mentioned. We want to explore the rate and distribution of these attacks over the world, and dive into their news coverage in the western hemisphere.


{% capture notice-1 %}
#### New Site Features
* You can now have cover images on blog pages
* Drafts will now auto-save while writing
{% endcapture %}

<div class="notice">
  <h4>Number of terrorist attacks across years</h4>
  {% include CountAttacks.html %}
  <p>Looking over the years from 1970 to 2017, we can see an increase of incidents, especially in recent years starting around 2010.
There is a strange gap in the data in 1993. Looking into terror attacks in 1993, we can clearly see that it is not that no attacks happened during this year (ex, attack on worldtrade center on February 23 1993 https://www.state.gov/1993-world-trade-center-bombing/) Reading into the information on the dataset, we found that the data was lost prior to addition to the dataset. This explanes the gap observed. 
(https://www.start.umd.edu/gtd/downloads/Codebook.pdf)

.</p>
</div>

<div class="notice">
  <h4>Link of human casualties with an increase in terrorist attacks</h4>
  <p>We observed before that there is a clear increase of the number of terrorist attacks over the more recent years. What does this imply for the general population? Are there more casualties as the number of attacks increase? Are the extent of the attacks constant, or are there more "small" attacks over the recent years? 

  Do all attacks result in injured victims? If not, what is the percentage of attacks which result in the death or wounded victims ?</p>

  {% include CasualtiesPerYear.html %}

  <p>The amount of wounded follows the amount of killed victims quite closely. Interestingly in the early 2000s there is a high peak of wounded, and we hypothesize that this is due to the extent of the terrorist attack on the worldtrade center in 2001. Further analysis will be required to confirm this hypothesis however. 
  We have also seen that the number of terror attacks continue to increase up to 2017, however here, it seems that the amount of human casualties decreases. Are the terror attacks touching less people? What could this decrease be do to? 

  We will now also look into the average number of casualties per attack over the years</p>

  {% include AvCasualtiesPerYear.html %}

  <p> Observing the average number of casualties (both wounded and killed) due to attacks, we can tell that around 2000, there were peaks of years where there were a larger number of people touched per incident than the other years. This could follow the hypothesis evoqued in the point before, that there may be a few larger attacks which happened during this period (ex, 9.11.2001), which bring the number of casualties of that year, up significantly, eventhough there were not more attacks per se.  </p>
  
</div>

</body>

