---
layout: page
title: null
permalink: /
published: true
---

<div class="row112">

<div class="columnimg1">
<div class="newsheading">
<a href="{{site.baseurl}}/tsunami-en/">Tsunami Induced By Supershear Earthquakes</a>
</div>
	<li class="cards_itemnews">
    <div class="cardnews">
      <a href="{{site.baseurl}}/tsunami-en/">
      <img src="{{site.baseurl}}/images/tsunami/composite_tsunami.jpg" width="100%"/>
      </a> 
    </div>
    </li>
</div>

<div class="columntxt1">
<h3 align="center" style="color:black; font-weight:normal">Recent News</h3>

{% for news in site.data.news.news %}
{% if forloop.index <= 6 %}
	<div class="cardtxtnohl"> 
	 
		{% if news.hl == 1 %} 
			<b>{{news.title}}</b>
		{% else %}
			 {{news.title}}
		{% endif %}       

      
      {% if news.pdf %} 
      &nbsp;&nbsp;
      <span id="topicbtn">
					<a href="{{ base }}/files/{{news.pdf}}">PDF</a>
	  </span>
	  {% endif %}
	  {% if news.readmore %} 
      &nbsp;&nbsp;
      <span id="topicbtn">
					<a href="{{news.readmore}}">READ MORE ...</a>
	  </span>
	  {% endif %}
    </div>   
{% endif %}     
{% endfor %} 
</div>  
</div>


{% include new-window-fix.html %}