---
layout: page
permalink: /articles/
title: 
---

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

<div class="pubs">
	<div class="articles">
    	{% for image in imgs %}
		<img src="{{site.baseurl}}/images/pubimages/blank.png" data-echo="{{site.baseurl}}/images/pubimages/{{image}}" class="responsivepubimg1">
		{% endfor %}
	</div>

   <div class="articles">
 	  <span class="pubyear">{{pub.year}}</span>
		
		{% if pub.pdf %}
			<a display:inline href="{{ base }}/files/{{pub.pdf}}" style="text-transform:capitalize;">{{pub.title}}</a>
		{% else %} 
			{{pub.title}}
		{% endif %}

		{{pub.author}}
		
		{% if pub.type == "article" %}
			<span ><em>{{pub.journal}}</em><br></span>
		{% elsif pub.type == "inproceeding" or pub.type == "incollection" %}
			<span >in <em>{{pub.booktitle}}</em><br></span>
			eds. {{pub.editor}}
		{% endif %}
		
		{% if pub.doi %}
			<a href="https://doi.org/{{pub.doi}}">doi:{{pub.doi}}</a>
		{% endif %}
		
		{% if pub.arxiv %}
			<a href="https://arxiv.org/pdf/{{pub.arxiv}}.pdf">arXiv:{{pub.arxiv}}[physics.geo-ph]</a>
		{% endif %}
	
		{% if pub.readmore %} 
			<div id="newsbtn">
				<a href="{{ base }}/{{pub.readmore}}">READ MORE ...</a>
			</div>
		{% endif %}
		
<!-- 		{% if pub.topics %} -->
<!-- 			<div class="pubbuttons"> -->
<!-- 				{% for topic in uniqetopics %} -->
<!-- 					<div id="topicbtn"> -->
<!-- 						<a href="{{ base }}/topics/#{{topic|slugify}}">{{topic | upcase }}</a> -->
<!-- 					</div> -->
<!-- 				{% endfor %} -->
<!-- 			</div>	 -->
<!-- 		{% endif %} -->

    </div>
    	

</div>  
{% assign j = j | minus:1 %}
{% endfor %}



{% include new-window-fix.html %}
