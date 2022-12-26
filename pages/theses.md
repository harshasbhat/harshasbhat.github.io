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
			<a href="{{site.baseurl}}/files/{{pub.pdf}}" style="font-size:100%"><span>{{pub.title}} ({{pub.year}})</span></a>
		{% else %}
		    <span>{{pub.title}} ({{pub.year}})</span> 
		{% endif %}

		
		<span style="font-size:85%">{{pub.author}}</span>
		<span style="font-size:85%">{{pub.school}}</span>

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
			
			
		{% if pub.slides %} 
		<div id="newsbtn">
		<a href="{{site.baseurl}}/files/{{news.slides}}" style="font-size:65%">SLIDES</a>
		</div>
		{% endif %}
		
		{% if pub.watch %} 
		<div id="watchbtn">
		<a href="{{news.watch}}" style="font-size:65%">WATCH IT ONLINE</a>
		</div>
		{% endif %}


			</div>    	


  </div>
    
</div>	

{% endfor %}

