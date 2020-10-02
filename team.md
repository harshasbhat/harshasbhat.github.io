---
layout: page
permalink: /team/
title: 
---

{% include new-window-fix.html %}


<div class="cardtxt2"> 
Current Members:    </div>  

<div class="cardtxthl2" text-align="center">Post Doctoral Researchers</div>
<ul class="cards">
{% for mem in site.data.team.postdoc %}
<li class="cards_item">
      <div class="card">
	    {% if mem.image %}
        <img src="{{ base }}/images/team/{{mem.image}}" width="100%">
        {% else %}
        <img src="{{ base }}/images/team/dummy.jpg" width="100%">
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

<div class="cardtxthl2" text-align="center">PhD Students</div>
<ul class="cards">
{% for mem in site.data.team.phd %}
<li class="cards_item">
      <div class="card">
	    {% if mem.image %}
        <img src="{{ base }}/images/team/{{mem.image}}" width="100%">
        {% else %}
        <img src="{{ base }}/images/team/dummy.jpg" width="100%">
        {% endif %}
        <div class="card_content">
          {% if mem.web %} 
          <a href="{{mem.web}}" style="text-align: center"><h6 class="card_title">{{mem.name}}</h6></a> 
          {% else %}
          <h6 class="card_title">{{mem.name}}</h6>
          {% endif %}
          <h6 class="card_text">{{mem.post}}</h6>
          <h6 class="card_text2">{{mem.dates}} -</h6>
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
<h3 align="center">Masters Students</h3>
<ul class="cards">
{% for mem in site.data.team.masters %}
<li class="cards_item">
      <div class="card">
	    {% if mem.image %}
        <img src="{{ base }}/images/team/{{mem.image}}" width="100%">
        {% else %}
        <img src="{{ base }}/images/team/dummy.jpg" width="100%">
        {% endif %}
        <div class="card_content">
          {% if mem.web %} 
          <a href="{{mem.web}}" style="text-align: center"><h6 class="card_title">{{mem.name}}</h6></a> 
          {% else %}
          <h6 class="card_title">{{mem.name}}</h6>
          {% endif %}
          <h6 class="card_text">{{mem.post}}</h6>
          <h6 class="card_text2">{{mem.dates}} -</h6>
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

<br>
<div class="cardtxt2"> 
Former Members:    </div>  
<div class="cardtxthl2" text-align="center">Post Doctoral Researchers</div>
<ul class="cards">
{% for mem in site.data.oldteam.postdoc %}
<li class="cards_item">
      <div class="card">
	    {% if mem.image %}
        <img src="{{ base }}/images/team/{{mem.image}}" width="100%">
        {% else %}
        <img src="{{ base }}/images/team/dummy.jpg" width="100%">
        {% endif %}
        <div class="card_content">
          {% if mem.web %} 
          <a href="{{mem.web}}" style="text-align: center"><h6 class="card_title">{{mem.name}}</h6></a> 
          {% else %}
          <h6 class="card_title">{{mem.name}}</h6>
          {% endif %}
          <h6 class="card_text">{{mem.post}}</h6>
        </div>
      </div>
</li>    
{% endfor %}  
</ul>

<div class="cardtxthl2" text-align="center">PhD Students</div>
<ul class="cards">
{% for mem in site.data.oldteam.phd %}
<li class="cards_item">
      <div class="card">
	    {% if mem.image %}
        <img src="{{ base }}/images/team/{{mem.image}}" width="100%">
        {% else %}
        <img src="{{ base }}/images/team/dummy.jpg" width="100%">
        {% endif %}
        <div class="card_content">
          {% if mem.web %} 
          <a href="{{mem.web}}" style="text-align: center"><h6 class="card_title">{{mem.name}}</h6></a> 
          {% else %}
          <h6 class="card_title">{{mem.name}}</h6>
          {% endif %}
          <h6 class="card_text">{{mem.post}}</h6>
        </div>
      </div>
</li>    
{% endfor %}  
</ul>

<div class="cardtxthl2" text-align="center">Masters Students</div>
<ul class="cards">
{% for mem in site.data.oldteam.masters %}
<li class="cards_item">
      <div class="card">
	    {% if mem.image %}
        <img src="{{ base }}/images/team/{{mem.image}}" width="100%">
        {% else %}
        <img src="{{ base }}/images/team/dummy.jpg" width="100%">
        {% endif %}
        <div class="card_content">
          {% if mem.web %} 
          <a href="{{mem.web}}" style="text-align: center"><h6 class="card_title">{{mem.name}}</h6></a> 
          {% else %}
          <h6 class="card_title">{{mem.name}}</h6>
          {% endif %}
          <h6 class="card_text">{{mem.post}}</h6>
        </div>
      </div>
</li>    
{% endfor %}  
</ul>

<div class="cardtxthl2" text-align="center">Undergraduate Students</div>
<ul class="cards">
{% for mem in site.data.oldteam.undergrad %}
<li class="cards_item">
      <div class="card">
	    {% if mem.image %}
        <img src="{{ base }}/images/team/{{mem.image}}" width="100%">
        {% else %}
        <img src="{{ base }}/images/team/dummy.jpg" width="100%">
        {% endif %}
        <div class="card_content">
          {% if mem.web %} 
          <a href="{{mem.web}}" style="text-align: center"><h6 class="card_title">{{mem.name}}</h6></a> 
          {% else %}
          <h6 class="card_title">{{mem.name}}</h6>
          {% endif %}
          <h6 class="card_text">{{mem.post}}</h6>
        </div>
      </div>
</li>    
{% endfor %}  
</ul>


{% include new-window-fix.html %}

