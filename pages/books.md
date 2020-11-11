---
layout: page
permalink: /books/
title: 
---

{% include collecttags.html %}

{% for pub in site.data.books.publications %}
<div class="pubs">
	<div class="articles">
			<img src="{{site.baseurl}}/images/pubimages/{{pub.img}}" class="responsivepubimg">
	</div>	

    <div class="articles">
 	  <span class="pubyear">{{pub.year}}</span>
		{% if pub.pdf %}
			<a display:inline href="{{ base }}/files/{{pub.pdf}}" style="text-transform:capitalize;">{{pub.title}}</a>
		{% else %} 
			{{pub.title}} 
		{% endif %}

		edited by {{pub.editor}}<br>
		
		{% if pub.doi %}
			{{pub.publisher}}<br>
			<a href="https://doi.org/{{pub.doi}}">doi:{{pub.doi}}</a>
		{% else %}
			{{pub.publisher}}
		{% endif %}
    </div>	
</div>
	
{% endfor %}

{% include new-window-fix.html %}

