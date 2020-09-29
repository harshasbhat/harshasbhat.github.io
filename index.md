---
layout: page
title: null
permalink: /
published: true
---

{% include new-window-fix.html %}

<div class="row112">
<div class="columnimg1">
    <div class="cardimg1">
      <img src="{{site.baseurl}}/images/tsunami/tsunamibig.png" width="100%"/>
      <h6>Supershear Tsunami</h6>
    </div>    
</div>


<div class="columntxt1">
{% for news in site.data.news.news %}
{% if forloop.index <= 4 %}
{% if news.hl == 1 %} 
    <div class="cardtxthl"> 
{% else %}
	<div class="cardtxtnohl"> 
{% endif %}       
      ➤ {{news.title}}
      {% if news.pdf %} 
      <span id="link_bar2">
					<a href="{{ base }}/files/{{news.pdf}}">PDF</a>
	  </span>
	  {% endif %}
	  {% if news.readmore %} 
      <span id="link_bar2">
					<a href="{{ base }}/{{news.readmore}}">READ MORE</a>
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



