---
layout: page
permalink: /team/
title: 
---

{% include new-window-fix.html %}

<h1 align="center">Current Members</h1>

<h3 align="center">Post Doctoral Researchers</h3>
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
          <h6 class="card_text2">{{mem.dates}} -</h6>
        </div>
      </div>
</li>    
{% endfor %}  
</ul>

<h3 align="center">PhD Students</h3>
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
        </div>
      </div>
</li>    
{% endfor %}  
</ul>
{% endif %}

<br>
<hr>
<br>


<h1 align="center">Former Members</h1>

<h3 align="center">Post Doctoral Researchers</h3>
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

<h3 align="center">PhD Students</h3>
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

<h3 align="center">Masters Students</h3>
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

<h3 align="center">Undergraduate Students</h3>
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

