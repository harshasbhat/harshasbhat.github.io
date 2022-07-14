---
layout: page
permalink: /teamold/
title: 
---

{% include new-window-fix.html %}


<h3>Former Post Doctoral Researchers</h3>
<div class="teams">
{% for mem in site.data.oldteam.postdoc %}
<div class="member">

	{% if mem.image %}
		<img src="{{ base }}/images/team/{{mem.image}}" width="125px">
	{% else %}
		<img src="{{ base }}/images/team/dummy.jpg" width="125px">
	{% endif %}

	{% if mem.web %} 	
		<a href="{{mem.web}}">
			<span style="font-size:90%; font-weight:bold">{{mem.name}}</span>
		</a>
	{% else %}	
		<span style="font-size:90%; font-weight:bold">{{mem.name}}</span>
	{% endif %}  

	<span style="font-size:85%">{{mem.post}}</span>
	
</div>
{% endfor %}  
</div>

<h3>Former PhD Students</h3>
<div class="teams">
{% for mem in site.data.oldteam.phd %}
<div class="member">

	{% if mem.image %}
		<img src="{{ base }}/images/team/{{mem.image}}" width="125px">
	{% else %}
		<img src="{{ base }}/images/team/dummy.jpg" width="125px">
	{% endif %}

	{% if mem.web %} 	
		<a href="{{mem.web}}">
			<span style="font-size:90%; font-weight:bold">{{mem.name}}</span>
		</a>
	{% else %}	
		<span style="font-size:90%; font-weight:bold">{{mem.name}}</span>
	{% endif %}  

	<span style="font-size:85%">{{mem.post}}</span>
	
</div>
{% endfor %}  
</div>

<h3>Former Masters Students</h3>
<div class="teams">
{% for mem in site.data.oldteam.masters %}
<div class="member">

	{% if mem.image %}
		<img src="{{ base }}/images/team/{{mem.image}}" width="125px">
	{% else %}
		<img src="{{ base }}/images/team/dummy.jpg" width="125px">
	{% endif %}

	{% if mem.web %} 	
		<a href="{{mem.web}}">
			<span style="font-size:90%; font-weight:bold">{{mem.name}}</span>
		</a>
	{% else %}	
		<span style="font-size:90%; font-weight:bold">{{mem.name}}</span>
	{% endif %}  

	<span style="font-size:85%">{{mem.post}}</span>
	
</div>
{% endfor %}  
</div>

<h3>Former Undergraduate Students</h3>
<div class="teams">
{% for mem in site.data.oldteam.undergrad %}
<div class="member">

	{% if mem.image %}
		<img src="{{ base }}/images/team/{{mem.image}}" width="125px">
	{% else %}
		<img src="{{ base }}/images/team/dummy.jpg" width="125px">
	{% endif %}

	{% if mem.web %} 	
		<a href="{{mem.web}}">
			<span style="font-size:90%; font-weight:bold">{{mem.name}}</span>
		</a>
	{% else %}	
		<span style="font-size:90%; font-weight:bold">{{mem.name}}</span>
	{% endif %}  

	<span style="font-size:85%">{{mem.post}}</span>
	
</div>
{% endfor %}  
</div>
