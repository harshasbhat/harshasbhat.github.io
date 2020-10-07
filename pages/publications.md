---
layout: page
permalink: /articles/
title: 
---
{% include usemath.html %}

{% include collecttags.html %}
{% include lazyload.html %}

{% assign year = 1980 %}
{% assign j = site.data.pubs.publications.size %}

{% for pub in site.data.pubs.publications %}
{% if pub.year == year %} 
{% else %} 

{% assign year = pub.year %}
{% endif %} 

{% assign uniqetopics = "" %}
{% assign uniqetopics = pub.topics | split: ', ' | sort_natural | uniq %} 

{% assign imgs = "" %}
{% assign imgs = pub.img | split: ', ' | sort_natural | uniq %} 

{% assign auth = pub.author %}

<div class="group">
{% if pub.img %}
    <div class="lefty">
 	
		{% if pub.pdf %}
			<a display:inline href="{{ base }}/files/{{pub.pdf}}">{{pub.title}}</a>
		{% else %} 
			{{pub.title}}
		{% endif %}
	</div>	

		
	<div class="lefty2">
		{{pub.author | replace: "H. S. Bhat", "<b>H. S. Bhat</b>"}}<br>
		
		{% if pub.type == "article" %}
			<span ><em>{{pub.journal}}</em><br></span>
		{% elsif pub.type == "inproceeding" or pub.type == "incollection" %}
			in <span >{{pub.booktitle}}</span>
			eds. {{pub.editor | replace: "H. S. Bhat", "<b>H. S. Bhat</b>"}}
		{% endif %}
		
		{% if pub.doi %}
			<a href="https://doi.org/{{pub.doi}}">doi:{{pub.doi}}</a>
		{% endif %}
		
		{% if pub.arxiv %}
			<a href="https://arxiv.org/pdf/{{pub.arxiv}}.pdf">arXiv:{{pub.arxiv}}[physics.geo-ph]</a>
		{% endif %}
		
		({{pub.year}})
    </div>
    
	
    {% if pub.topics %}
		<div class="lefty2">
			{% for topic in uniqetopics %}
				<span id="topicbtn">
					<a href="{{ base }}/topics/#{{topic|slugify}}">{{topic | upcase }}</a>
				</span>
			{% endfor %}
		</div>
	{% endif %}
	
	<div class="righty">
    	{% for image in imgs %}
			<img src="{{site.baseurl}}/images/pubimages/blank.png" data-echo="{{site.baseurl}}/images/pubimages/{{image}}" class="responsive" width="100%">
    	{% endfor %}
	</div>

	
{% else %}

    <div class="fully2">
    <br>
		{% if pub.pdf %}
			<a display:inline href="{{ base }}/files/{{pub.pdf}}">{{pub.title}}</a>
		{% else %} 
			{{pub.title}}
		{% endif %}
		
		<br>{{pub.author | replace: "H. S. Bhat", "<b>H. S. Bhat</b>"}}<br>		
		
		{% if pub.type == "article" %}
			<span ><em>{{pub.journal}}</em><br></span>
		{% elsif pub.type == "inproceeding" or pub.type == "incollection" %}
			in <span >{{pub.booktitle}}</span>
			eds. {{pub.editor}}
		{% endif %}
		
		{% if pub.doi %}
			<a href="https://doi.org/{{pub.doi}}">doi:{{pub.doi}}</a>
		{% endif %}
		
		{% if pub.arxiv %}
			<a href="https://arxiv.org/pdf/{{pub.arxiv}}.pdf">arXiv:{{pub.arxiv}}[physics.geo-ph]</a>
		{% endif %}
		
		({{pub.year}})<br>

    {% if pub.topics %}
			{% for topic in uniqetopics %}
				<span id="topicbtn">
					<a href="{{ base }}/topics/#{{topic|slugify}}">{{topic | upcase }}</a>
				</span>
			{% endfor %}
	{% endif %}
	
	</div>

{% endif %}
	
	
	
</div>  
{% assign j = j | minus:1 %}
{% endfor %}



{% include new-window-fix.html %}

<style>
.responsive {
width: 100%; 
height: 100%; 
object-fit: contain; 
max-width: 350px;
max-height: 200px;
float: left;
}
</style>

[LG]: http://www.geologie.ens.fr
[ENS]: http://www.ens.fr
[topics]: /topics/
