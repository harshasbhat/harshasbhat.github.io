---
layout: page
permalink: /teamold/
title: 
---

{% include new-window-fix.html %}


<div class="cardtxthl2" text-align="center">Former Post Doctoral Researchers</div>
<ul class="cards">
{% for mem in site.data.oldteam.postdoc %}
<li class="cards_item">
      <div class="card">
	    {% if mem.image %}
        <img src="{{ base }}/images/team/{{mem.image}}" width="227px">
        {% else %}
        <img src="{{ base }}/images/team/dummy.jpg" width="227px">
        {% endif %}
        <div class="card_content">
          {% if mem.web %} 
          <a href="{{mem.web}}" style="text-align: center"><h6 class="card_title">{{mem.name}}</h6></a> 
          {% else %}
          <h6 class="card_title">{{mem.name}}</h6>
          {% endif %}
          {% if mem.post %}
          <h6 class="card_text3">{{mem.post}}</h6>
          {% else %}
          <img src="{{site.baseurl}}/images/blank.png" class="responsive" width="10%" align="right"> 
          {% endif %}          
        </div>
      </div>
</li>    
{% endfor %}  
</ul>
<hr>
<div class="cardtxthl2" text-align="center">Former PhD Students</div>
<ul class="cards">
{% for mem in site.data.oldteam.phd %}
<li class="cards_item">
      <div class="card">
	    {% if mem.image %}
        <img src="{{ base }}/images/team/{{mem.image}}" width="227px">
        {% else %}
        <img src="{{ base }}/images/team/dummy.jpg" width="227px">
        {% endif %}
        <div class="card_content">
          {% if mem.web %} 
          <a href="{{mem.web}}" style="text-align: center"><h6 class="card_title">{{mem.name}}</h6></a> 
          {% else %}
          <h6 class="card_title">{{mem.name}}</h6>
          {% endif %}
          {% if mem.post %}
          <h6 class="card_text3">{{mem.post}}</h6>
          {% else %}
          <img src="{{site.baseurl}}/images/blank.png" class="responsive" width="10%" align="right"> 
          {% endif %}          
        </div>
      </div>
</li>    
{% endfor %}  
</ul>
<hr>
<div class="cardtxthl2" text-align="center">Former Masters Students</div>
<ul class="cards">
{% for mem in site.data.oldteam.masters %}
<li class="cards_item">
      <div class="card">
	    {% if mem.image %}
        <img src="{{ base }}/images/team/{{mem.image}}" width="227px">
        {% else %}
        <img src="{{ base }}/images/team/dummy.jpg" width="227px">
        {% endif %}
        <div class="card_content">
          {% if mem.web %} 
          <a href="{{mem.web}}" style="text-align: center"><h6 class="card_title">{{mem.name}}</h6></a> 
          {% else %}
          <h6 class="card_title">{{mem.name}}</h6>
          {% endif %}
          {% if mem.post %}
          <h6 class="card_text3">{{mem.post}}</h6>
          {% else %}
          <img src="{{site.baseurl}}/images/blank.png" class="responsive" width="9.5%" align="right"> 
          {% endif %}          
        </div>
      </div>
</li>    
{% endfor %}  
</ul>
<hr>
<div class="cardtxthl2" text-align="center">Former Undergraduate Students</div>
<ul class="cards">
{% for mem in site.data.oldteam.undergrad %}
<li class="cards_item">
      <div class="card">
	    {% if mem.image %}
        <img src="{{ base }}/images/team/{{mem.image}}" width="227px">
        {% else %}
        <img src="{{ base }}/images/team/dummy.jpg" width="227px">
        {% endif %}
        <div class="card_content">
          {% if mem.web %} 
          <a href="{{mem.web}}" style="text-align: center"><h6 class="card_title">{{mem.name}}</h6></a> 
          {% else %}
          <h6 class="card_title">{{mem.name}}</h6>
          {% endif %}
          {% if mem.post %}
          <h6 class="card_text3">{{mem.post}}</h6>
          {% else %}
          <img src="{{site.baseurl}}/images/blank.png" class="responsive" width="10%" align="right"> 
          {% endif %}          
        </div>
      </div>
</li>    
{% endfor %}  
</ul>


{% include new-window-fix.html %}

