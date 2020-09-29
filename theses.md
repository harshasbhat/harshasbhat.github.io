---
layout: page
permalink: /theses/
title: 
---
{% include collecttags.html %}

{% for pub in site.data.theses.publications %}
<div class="group">

{% if pub.img %}

	<div class="lefty">
	    <br>
		{% if pub.pdf %}
			<a href="{{ base }}/files/{{pub.pdf}}">{{pub.title}}</a>
		{% else %} 
			{{pub.title}} 
		{% endif %}
	</div>
	
	<div class="lefty">	
		{{pub.author | replace: "H. S. Bhat", "<b>H. S. Bhat</b>"}}<br>
		<span style="color:grey">{{pub.school}}</span>
		{% if pub.doi %}
			<a href="https://doi.org/{{pub.doi}}">doi:{{pub.doi}}</a>
		{% endif %}
		({{pub.year}}) 
    </div>
    
	<div class="righty">
			<br>
			<img src="{{site.baseurl}}/images/pubimages/{{pub.img}}" class="responsive" width="80%">
	</div>
	
{% else %}

	<div class="fully2">
		{% if pub.pdf %}
			<a href="{{ base }}/files/{{pub.pdf}}">{{pub.title}}</a>
		{% else %} 
			{{pub.title}} 
		{% endif %}
	
		<br>{{pub.author | replace: "H. S. Bhat", "<b>H. S. Bhat</b>"}}<br>
		<span style="color:grey">{{pub.school}}</span>
		{% if pub.doi %}
			<a href="https://doi.org/{{pub.doi}}">doi:{{pub.doi}}</a>
		{% endif %}
		({{pub.year}}) 
	</div>	
{% endif %}

</div>	

{% endfor %}

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

[LG]: http://www.geologie.ens.fr
[ENS]: http://www.ens.fr
[topics]: /topics/
