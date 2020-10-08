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
        <img src="{{ base }}/images/team/{{mem.image}}" width="175px">
        {% else %}
        <img src="{{ base }}/images/team/dummy.jpg" width="175px">
        {% endif %}
        <div class="card_content">
          <h6 class="card_title">{{mem.name}}</h6>
          <h6 class="card_text3">{{mem.dates}} onwards</h6>
          
          {% if mem.web %} 
          <a href="{{mem.web}}">
          <img src="{{site.baseurl}}/images/web.png" class="responsive"> 
          </a>
          {% else %}
          <img src="{{site.baseurl}}/images/blank.png" class="responsive"> 
          {% endif %}  
         
          {% if mem.tweet %} 
          <a href="https://twitter.com/{{mem.tweet}}">
          <img src="{{site.baseurl}}/images/tweet.png" class="responsive"> 
          </a>
          {% else %}
          <img src="{{site.baseurl}}/images/blank.png" class="responsive"> 
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
        <img src="{{ base }}/images/team/{{mem.image}}" width="175px">
        {% else %}
        <img src="{{ base }}/images/team/dummy.jpg" width="175px">
        {% endif %}
        <div class="card_content">
          <h6 class="card_title">{{mem.name}}</h6>
          <h6 class="card_text3">{{mem.dates}} onwards</h6>
          
          {% if mem.web %} 
          <a href="{{mem.web}}">
          <img src="{{site.baseurl}}/images/web.png" class="responsive"> 
          </a>
          {% else %}
          <img src="{{site.baseurl}}/images/blank.png" class="responsive"> 
          {% endif %}  
         
          {% if mem.tweet %} 
          <a href="https://twitter.com/{{mem.tweet}}">
          <img src="{{site.baseurl}}/images/tweet.png" class="responsive"> 
          </a>
          {% else %}
          <img src="{{site.baseurl}}/images/blank.png" class="responsive"> 
          {% endif %}
        
        </div>
      </div>
</li>    
    
{% endfor %}  
</ul>

{% if site.data.team.masters %}

<div class="cardtxthl2" text-align="center">Masters Students</div>
<ul class="cards">
{% for mem in site.data.team.masters %}
<li class="cards_item">
      <div class="card">
	    {% if mem.image %}
        <img src="{{ base }}/images/team/{{mem.image}}" width="175px">
        {% else %}
        <img src="{{ base }}/images/team/dummy.jpg" width="175px">
        {% endif %}
        <div class="card_content">
          <h6 class="card_title">{{mem.name}}</h6>
          <span class="card_text3">{{mem.dates}} --</span>
          
          {% if mem.web %} 
          <a href="{{mem.web}}">
          <img src="{{site.baseurl}}/images/web.png" class="responsive"> 
          </a>
          {% else %}
          <img src="{{site.baseurl}}/images/blank.png" class="responsive"> 
          {% endif %}  
         
          {% if mem.tweet %} 
          <a href="https://twitter.com/{{mem.tweet}}">
          <img src="{{site.baseurl}}/images/tweet.png" class="responsive"> 
          </a>
          {% else %}
          <img src="{{site.baseurl}}/images/blank.png" class="responsive"> 
          {% endif %}
        
        </div>
      </div>
</li>    
   
{% endfor %}  
</ul>
{% endif %}


<style>
.responsive {
width: 100%; 
height: 100%; 
object-fit: contain; 
padding-left: 5px;
max-width: 15px;
max-height: 100px;
float: right;
}
</style>

{% include new-window-fix.html %}

