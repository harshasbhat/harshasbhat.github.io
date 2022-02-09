---
layout: pageall
permalink: /allteam/
title: 
---

{% include new-window-fix.html %}

{% assign allmembers = site.data.team.postdoc | concat: site.data.team.phd | concat: site.data.oldteam.phd | concat: site.data.oldteam.postdoc | concat: site.data.oldteam.masters | concat: site.data.oldteam.undergrad %}

{% assign sorted = allmembers | sort: "name" | uniq: "name" %}

<!-- {% assign allmembers = site.data.oldteam.postdoc | concat: site.data.oldteam.phd | concat: site.data.oldteam.masters %} -->

<div class="allteams">
{% for mem in sorted %}
<div class="member">

	{% if mem.image %}
		<img src="{{ base }}/images/team/{{mem.image}}" width="175px">
	{% else %}
		<img src="{{ base }}/images/team/dummy2.jpg" width="175px">
	{% endif %}

	
	<span style="font-size:110%; font-weight:bold">{{mem.name}}</span>
	
</div>
{% endfor %}  
</div>


