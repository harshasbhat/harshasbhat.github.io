---
layout: page
permalink: /theses/
title: 
---
<br>
{% include collecttags.html %}

{% for pub in site.data.theses.publications %}
<div class="pagewidthpub">
<div class="group">
{% if pub.img %}

	<div class="lefty">
		{% if pub.pdf %}
			<a href="{{ base }}/files/{{pub.pdf}}" style="text-transform:capitalize;">{{pub.title}}</a>
		{% else %} 
			{{pub.title}} 
		{% endif %}
		<br>
		{{pub.author}}<br>
		<span><em>{{pub.school}}</em></span>
		{% if pub.doi %}
			<a href="https://doi.org/{{pub.doi}}">doi:{{pub.doi}}</a>
		{% endif %}
		({{pub.year}}) 
    </div>
    
	<div class="righty">
			<img src="{{site.baseurl}}/images/pubimages/{{pub.img}}" class="responsivepubimg">
	</div>
	
{% else %}

	<div class="fully2">
		{% if pub.pdf %}
			<a href="{{ base }}/files/{{pub.pdf}}">{{pub.title}}</a>
		{% else %} 
			{{pub.title}} 
		{% endif %}
	
		<br>{{pub.author | replace: "H. S. Bhat", "<b>H. S. Bhat</b>"}}<br>
		<span>{{pub.school}}</span>
		{% if pub.doi %}
			<a href="https://doi.org/{{pub.doi}}">doi:{{pub.doi}}</a>
		{% endif %}
		({{pub.year}}) 
	</div>	
{% endif %}

</div>	

{% endfor %}
</div>

{% include new-window-fix.html %}

<style>
.responsive {
width: 100%; 
height: 100%; 
object-fit: contain; 
max-width: 300px;
max-height: 150px;
float: left;
}
</style>