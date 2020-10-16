---
layout: page
permalink: /books/
title: 
---

<br>
{% include collecttags.html %}

{% for pub in site.data.books.publications %}
<div class="pagewidthpub">
<div class="group">

{% if pub.img %}

    <div class="lefty">
		{% if pub.pdf %}
			<a display:inline href="{{ base }}/files/{{pub.pdf}}" style="text-transform:capitalize;">{{pub.title}}</a>
		{% else %} 
			{{pub.title}} 
		{% endif %}
		<br>
		edited by {{pub.editor}}<br>
		
		{% if pub.doi %}
			{{pub.publisher}}<br>
			<a href="https://doi.org/{{pub.doi}}">doi:{{pub.doi}}</a> ({{pub.year}}) 
		{% else %}
			{{pub.publisher}} ({{pub.year}})
		{% endif %}
    </div>
	
	<div class="righty">
			<img src="{{site.baseurl}}/images/pubimages/{{pub.img}}" class="responsivepubimg">
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

</div>
{% include new-window-fix.html %}

