---
layout: page
permalink: /team/
title: 
---

{% include new-window-fix.html %}


<div class="cardtxthl2" text-align="center">Post Doctoral Researchers</div>
<ul class="cards">
{% for mem in site.data.team.postdoc %}
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
          <h6 class="card_text">{{mem.post}}</h6>
          <h6 class="card_text3">{{mem.dates}} onwards</h6>
          {% if mem.tweet %} 
          <a href="https://twitter.com/{{mem.tweet}}">
          <img src="{{site.baseurl}}/images/tweet.png" class="responsive" width="10%" align="right"> 
          </a>
          {% else %}
          <img src="{{site.baseurl}}/images/blank.png" class="responsive" width="10%" align="right"> 
          {% endif %}
        </div>
      </div>
</li>    
{% endfor %}  
</ul>

<hr>

<div class="cardtxthl2" text-align="center">PhD Students</div>
<ul class="cards">
{% for mem in site.data.team.phd %}
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
          <h6 class="card_text">{{mem.post}}</h6>
          <h6 class="card_text3">{{mem.dates}} onwards</h6>
          {% if mem.tweet %} 
          <a href="https://twitter.com/{{mem.tweet}}">
          <img src="{{site.baseurl}}/images/tweet.png" class="responsive" width="10%" align="right"> 
          </a>
          {% else %}
          <img src="{{site.baseurl}}/images/blank.png" class="responsive" width="10%" align="right"> 
          {% endif %}
        </div>
      </div>
</li>    
{% endfor %}  
</ul>

{% if site.data.team.masters %}
<hr>
<div class="cardtxthl2" text-align="center">Masters Students</div>
<ul class="cards">
{% for mem in site.data.team.masters %}
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
          <h6 class="card_text">{{mem.post}}</h6>
          <h6 class="card_text3">{{mem.dates}} onwards</h6>
          {% if mem.tweet %} 
          <a href="https://twitter.com/{{mem.tweet}}">
          <img src="{{site.baseurl}}/images/tweet.png" class="responsive" width="10%" align="right"> 
          </a>
          {% else %}
          <img src="{{site.baseurl}}/images/blank.png" class="responsive" width="10%" align="right"> 
          {% endif %}
        </div>
      </div>
</li>    
{% endfor %}  
</ul>
{% endif %}

{% include new-window-fix.html %}

