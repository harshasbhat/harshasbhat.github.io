---
layout: page
permalink: /team/
title: 
---

{% include new-window-fix.html %}

 
<h3>Post Doctoral Researchers</h3>   
<div class="teams">
{% for mem in site.data.team.postdoc %}
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

	<span style="font-size:85%">{{mem.dates}} onwards</span>

	<!-- <div class="web">

		{% if mem.tweet %} 
			<a href="https://twitter.com/{{mem.tweet}}">
			<i class="fa fa-twitter fa-lg fa-fw" aria-hidden="true"></i>
			</a>
		{% else %}	
			<a href="#">
			<i class="fa fa-link fa-lg fa-fw" aria-hidden="true" style="color:white"></i>
			</a>
		{% endif %}  
	</div>     -->
	
</div>
{% endfor %}  
</div>


<h3>PhD Students</h3>
<div class="teams">
{% for mem in site.data.team.phd %}
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

	<span style="font-size:85%">{{mem.dates}} onwards</span>

	<!-- <div class="web">

		{% if mem.tweet %} 
			<a href="https://twitter.com/{{mem.tweet}}">
			<i class="fa fa-twitter fa-lg fa-fw" aria-hidden="true"></i>
			</a>
		{% else %}	
			<a href="#">
			<i class="fa fa-link fa-lg fa-fw" aria-hidden="true" style="color:white"></i>
			</a>
		{% endif %}  
	</div>     -->
	
</div>
{% endfor %}  
</div>

<h3>IT Research Engineer</h3>   
<div class="teams">
<div class="member">

	
		<img src="{{ base }}/images/team/pierpaolo.jpg" width="125px">

		<span style="font-size:90%; font-weight:bold">Pierpaolo Dubernet</span>
	
</div> 
</div>

{% if site.data.team.masters %}

<h3>Masters Students</h3>
<div class="teams">
{% for mem in site.data.team.masters %}
<div class="member">

	{% if mem.image %}
		<img src="{{ base }}/images/team/{{mem.image}}" width="125px">
	{% else %}
		<img src="{{ base }}/images/team/dummy.jpg" width="125px">
	{% endif %}

	<span style="font-size:90%; font-weight:bold">{{mem.name}}</span>
	<span style="font-size:85%">{{mem.dates}} onwards</span>

	<div class="web">
		{% if mem.web %} 
			<a href="{{mem.web}}">
			<i class="fa fa-link fa-lg fa-fw" aria-hidden="true"></i>
			</a>
		{% else %}	
			<i class="fa fa-link fa-lg fa-fw" aria-hidden="true" style="color:white"></i>
		{% endif %}  

		<!-- {% if mem.tweet %} 
			<a href="https://twitter.com/{{mem.tweet}}">
			<i class="fa fa-twitter fa-lg fa-fw" aria-hidden="true"></i>
			</a>
		{% else %}	
			<a href="#">
			<i class="fa fa-link fa-lg fa-fw" aria-hidden="true" style="color:white"></i>
			</a>
		{% endif %}   -->
	</div>    
	
</div>
{% endfor %}  
</div>

{% endif %}  

