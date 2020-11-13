---
layout: page
permalink: /theses/
title: 
---

{% include collecttags.html %}

{% for pub in site.data.theses.publications %}
<div class="pubs">
	<div class="articles">
			<img src="{{site.baseurl}}/images/pubimages/{{pub.img}}" class="responsivepubimg">
	</div>	

	<div class="articles">
		{% if pub.pdf %}
			<a display:inline href="{{ base }}/files/{{pub.pdf}}" style="text-transform:capitalize;font-size:100%"><span class="pubyear">{{pub.year}}: {{pub.title}}</span></a>
		{% else %} 
			<span class="pubyear">{{pub.year}}:{{pub.title}}</span> 
		{% endif %}
		
		<span style="font-size:85%">{{pub.author}}</span>
		<span style="font-size:85%">{{pub.school}}</span>
		{% if pub.doi %}
			<a href="https://doi.org/{{pub.doi}}">doi:{{pub.doi}}</a>
		{% endif %}
    </div>
    
</div>	

{% endfor %}

