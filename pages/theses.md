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
 	  <span class="pubyear">{{pub.year}}</span>
		{% if pub.pdf %}
			<a href="{{ base }}/files/{{pub.pdf}}" style="text-transform:capitalize;">{{pub.title}}</a>
		{% else %} 
			{{pub.title}} 
		{% endif %}
		
		{{pub.author}}<br>
		<span><em>{{pub.school}}</em></span>
		{% if pub.doi %}
			<a href="https://doi.org/{{pub.doi}}">doi:{{pub.doi}}</a>
		{% endif %}
    </div>
    
</div>	

{% endfor %}

{% include new-window-fix.html %}

