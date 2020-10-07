---
layout: page
permalink: /topics/
title: 
---

**This page is being updated...**
<br><br>


Listed below are my publications sorted by various research topics. You can browse my full list of publications [here][pubs].
<br><br>

{% include collecttags.html %}
{% include lazyload.html %}

{% assign sorttags = uniqTags | sort_natural %} 


<div class="container">
	{% for tag in sorttags %}
		<div class="section">
			<div id="topicbtnlst">
			   <a href="#{{ tag  | slugify }}"> {{ tag | upcase }} </a>
			</div>
		</div>
	{% endfor %}
</div>

<br><br>

{% for tag in sorttags %}
<div class="cardtxthl2" text-align="center">{{ tag | upcase }}</div>
{% for pub in site.data.pubs.publications %}
{% assign uniqetopics = "" %}
{% assign uniqetopics = pub.topics | split: ', ' | sort_natural | uniq %} 

{% assign imgs1 = "" %}
{% assign imgs1 = pub.img | split: ', ' | sort_natural | uniq %} 

{% if pub.topics contains tag %}
<div class="group1">


    <div class="lefty">
    	<br>
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
			<div class="lefty">
				{% for topic in uniqetopics %}
					<span id="topicbtn">
						<a href="{{ base }}/topics/#{{topic|slugify}}">{{topic | upcase }}</a>
					</span>
				{% endfor %}
			</div>
		{% endif %}
	
	<div class="righty">
		<br>
		{% for image in imgs1 %}
			<img src="{{site.baseurl}}/images/pubimages/blank.png" data-echo="{{site.baseurl}}/images/pubimages/{{image}}" class="responsive" width="100%">
		{% endfor %}
	</div>
</div> 
<hr style="width:100%;text-align:center;margin-left:0;">
{% endif %}
{% endfor %}
<br>
{% endfor %}

<style>
.responsive {
width: 100%; 
height: 100%; 
object-fit: contain; 
max-width: 300px;
max-height: 150px;
float: left;
}
</style>

[pubs]: /articles/
