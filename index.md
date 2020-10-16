---
layout: page
title: null
permalink: /
published: true
---



<div class="row112">

<div class="columnimg1">
	<li class="cards_itemnews">
    <div class="cardnews">
      <a href="#">
      <img src="{{site.baseurl}}/images/tsunami/composite_tsunami.jpg" width="100%"/>
      </a> 
      <a href="#" class="card_titlenews">Supershear Tsunami</a>  
    </div>
    </li>
</div>

<div class="columntxt1">
<h3 align="right">Updates</h3>

{% for news in site.data.news.news %}
{% if forloop.index <= 6 %}
	<div class="cardtxtnohl"> 
	● 
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


