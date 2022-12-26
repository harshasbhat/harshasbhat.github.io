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
			<a href="{{site.baseurl}}/files/{{pub.pdf}}" style="font-size:100%"><span>{{pub.title}} ({{pub.year}})</span></a>
		{% else %}
		    <span>{{pub.title}} ({{pub.year}})</span> 
		{% endif %}
		
		<span style="font-size:85%">eds. {{pub.editor}}</span>
		<span style="font-size:85%">{{pub.publisher}}</span>
		{% if pub.doi %} <a href="https://doi.org/{{pub.doi}}" style="font-size:85%">DOI:{{pub.doi}}</a> {% endif %}

		<div class="pubbuttons">
		
			<!-- {% if pub.pdf %}
			<div id="newsbtn">
				<a href="{{site.baseurl}}/files/{{pub.pdf}}" style="font-size:65%">PDF</a>
			</div>
			{% endif %}
			
			{% if pub.doi %}
			<div id="newsbtn">
				<a href="https://doi.org/{{pub.doi}}" style="font-size:65%">DOI</a>
			</div>
			{% endif %} -->
		
			{% if pub.arxiv %}
			<div id="newsbtn">
				<a href="https://arxiv.org/pdf/{{pub.arxiv}}.pdf" style="font-size:65%">arXiv</a>
			</div>
			{% endif %}
		
			{% if pub.readmore %} 
				<div id="newsbtn">
					<a href="{{ base }}/{{pub.readmore}}" style="font-size:65%">READ MORE ...</a>
				</div>
			{% endif %}
			</div>    	
		
    </div>	
</div>
	
{% endfor %}


