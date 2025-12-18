---
layout: page
permalink: /articles/
title:
---
{% include collecttags.html %}
{% include lazyload.html %}
{% include usemath.html %}

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
			<img src="{{site.baseurl}}/images/pubimages/{{pub.img}}" class="responsivepubimg">
	</div>	

   <div class="articles">

		{% if pub.pdf %}
			<a href="{{site.baseurl}}/files/{{pub.pdf}}" style="font-size:100%"><span>{{pub.title}} ({{pub.year}})</span></a>
		{% else %}
		    <span><em>{{pub.title}}</em> ({{pub.year}})</span> 
		{% endif %}

		<span style="font-size:85%">&nbsp;{{pub.author}}</span>

		{% if pub.type == "article" %}
			<span style="font-size:85%">&nbsp;<b>{{pub.journal}}</b></span>
			{% if pub.doi %} 
				<a href="https://doi.org/{{pub.doi}}" style="font-size:75%">DOI:{{pub.doi}}</a> 
			{% endif %}
		{% elsif pub.type == "inproceeding" or pub.type == "incollection" %}
			<span style="font-size:85%">&nbsp;in <b>{{pub.booktitle}}</b></span>
			<span style="font-size:85%">&nbsp;eds. {{pub.editor}}</span>
			{% if pub.doi %} <a href="https://doi.org/{{pub.doi}}" style="font-size:85%">DOI:{{pub.doi}}</a> {% endif %}
		{% endif %}



		<div class="pubbuttons">

			<!-- {% if pub.pdf %}
			<div id="newsbtn">
				<a href="{{site.baseurl}}/files/{{pub.pdf}}" style="font-size:65%">PDF</a>
			</div>
			{% endif %} -->

			<!-- {% if pub.doi %}
			<div id="newsbtn">
				<a href="https://doi.org/{{pub.doi}}" style="font-size:65%">DOI</a>
			</div>
			{% endif %} -->

			{% if pub.arxiv %}
			<div id="newsbtn">
				<a href="https://arxiv.org/pdf/{{pub.arxiv}}.pdf" style="font-size:65%">arXiv:{{pub.arxiv}}</a>
			</div>
			{% endif %}

			{% if pub.hal %}
			<div id="newsbtn">
				<a href="https://hal.archives-ouvertes.fr/{{pub.hal}}/document" style="font-size:65%">HAL:{{pub.hal}}</a>
			</div>
			{% endif %}

			{% if pub.insu %}
				<div id="watchbtn">
					<a href="{{pub.insu}}" style="font-size:65%">INSU</a>
				</div>
			{% endif %}

			{% if pub.readmore %}
				<div id="watchbtn">
					<a href="{{ base }}/{{pub.readmore}}" style="font-size:65%">READ MORE ...</a>
				</div>
			{% endif %}
				
			</div>   

			


    </div>

</div>  
{% assign j = j | minus:1 %}
{% endfor %}
