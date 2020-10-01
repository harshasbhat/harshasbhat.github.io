---
layout: page
permalink: /team/
title: 
---

{% include new-window-fix.html %}


<ul class="cards">
{% for mem in site.data.team.team %}
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

{% include new-window-fix.html %}

