---
layout: page
permalink: /books/
title: 
---

{% include collecttags.html %}

{% for pub in site.data.books.publications %}
<div class="group">

{% if pub.img %}

    <div class="lefty">
	    <br>
		{% if pub.pdf %}
			<a display:inline href="{{ base }}/files/{{pub.pdf}}">{{pub.title}}</a>
		{% else %} 
			{{pub.title}} 
		{% endif %}
	</div>	

	<div class="lefty">	
		edited by {{pub.editor | replace: "H. S. Bhat", "<b>H. S. Bhat</b>"}}<br>
		
		{% if pub.doi %}
			{{pub.publisher}}<br>
			<a href="https://doi.org/{{pub.doi}}">doi:{{pub.doi}}</a> ({{pub.year}}) 
		{% else %}
			{{pub.publisher}} ({{pub.year}})
		{% endif %}
    </div>
	
	<div class="righty">
	<br>
			<img src="{{site.baseurl}}/images/pubimages/{{pub.img}}" class="responsive" width="80%">
	</div>

{% else %}

    <div class="fully2">
    <br>
		{% if pub.pdf %}
			<a display:inline href="{{ base }}/files/{{pub.pdf}}">{{pub.title}}</a>
		{% else %} 
			{{pub.title}} 
		{% endif %}
		<br>edited by {{pub.editor | replace: "H. S. Bhat", "<b>H. S. Bhat</b>"}},
		
		{% if pub.doi %}
			{{pub.publisher}}<br>
			<a href="https://doi.org/{{pub.doi}}">doi:{{pub.doi}}</a> ({{pub.year}}) 
		{% else %}
			{{pub.publisher}} ({{pub.year}})
		{% endif %}
		
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