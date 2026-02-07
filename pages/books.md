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

		{% if pub.pdf %}
			<a href="https://filedn.eu/lg5rE6ReEB4XtX4pGFBGRh4/CollectedPapers/{{pub.type}}/{{pub.pdf}}" style="font-size:100%"><span>{{pub.title}} ({{pub.year}})</span></a>
		{% else %}
		    <span>{{pub.title}} ({{pub.year}})</span> 
		{% endif %}
		
		<span style="font-size:85%">eds. {{pub.editor}}</span>
		<span style="font-size:85%">{{pub.publisher}}</span>
		{% if pub.doi %} <a href="https://doi.org/{{pub.doi}}" style="font-size:85%">DOI:{{pub.doi}}</a> {% endif %}

		
    </div>	
</div>
	
{% endfor %}


