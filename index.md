---
layout: page
title: null
permalink: /
published: true
---

{% include new-window-fix.html %}

<br>

<div class="row112">

<div class="columnimg1">
	<li class="cards_item">
    <div class="card">
      <img src="{{site.baseurl}}/images/tsunami/tsunami.gif"/>
      <h6 class="card_title">Supershear Tsunami</h6>  
    </div>
    </li>
    
</div>

<div class="columntxt1">
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
					<a href="{{ base }}/{{news.readmore}}">READ MORE ...</a>
	  </span>
	  {% endif %}
    </div>   
{% endif %}     
{% endfor %}  
</div>  
</div>

{% include new-window-fix.html %}
[hdr]: files/Bhat2021a.pdf
[aftershocks]: files/JaraBruhatAntoine2020a.pdf
[tsunami]: files/AmlaniBhatSimons2020a.pdf
[erosion]: files/Jeandet-RibesCubasBhat2020a.pdf
[tsunami2]: /tsunami/explanation/



