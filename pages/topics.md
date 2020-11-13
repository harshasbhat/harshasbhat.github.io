---
layout: page
permalink: /topics/
title: 
---
<div class="pagewidthpub">
<br><br>
This page is being updated...
<br><br>



Listed below are my publications sorted by various research topics.<br><br> 


{% include collecttags.html %}
{% include lazyload.html %}

{% assign sorttags = uniqTags | sort_natural %} 

<div class="dropdown">
  <button class="dropbtn">Topics <i class="fa fa-caret-down"></i></button>
  <div class="dropdown-content">
  	{% for tag in sorttags %}
 	<a href="#{{ tag  | slugify }}"> {{ tag | upcase }} </a>
 	{% endfor %}
  </div>
</div>

<br><br>

{% for tag in sorttags %}
<a id="{{ tag  | slugify }}" class="anchor"></a>
<div id="topicshl">
{{ tag | upcase }}
</div>
<br><br>

{% for pub in site.data.pubs.publications %}
{% assign uniqetopics = "" %}
{% assign uniqetopics = pub.topics | split: ', ' | sort_natural | uniq %} 

{% assign imgs1 = "" %}
{% assign imgs1 = pub.img | split: ', ' | sort_natural | uniq %} 

{% if pub.topics contains tag %}
<div class="group">


    <div class="lefty">
		{% if pub.pdf %}
			<a display:inline href="{{ base }}/files/{{pub.pdf}}" style="text-transform:capitalize;">{{pub.title}}</a>
		{% else %} 
			{{pub.title}}
		{% endif %}
		<br>
		{{pub.author}}<br>
		
		{% if pub.type == "article" %}
			<span ><em>{{pub.journal}}</em><br></span>
		{% elsif pub.type == "inproceeding" or pub.type == "incollection" %}
			in <span ><em>{{pub.booktitle}}</em><br></span>
			eds. {{pub.editor}}<br>
		{% endif %}
		
		{% if pub.doi %}
			<a href="https://doi.org/{{pub.doi}}">doi:{{pub.doi}}</a>
		{% endif %}
		
		{% if pub.arxiv %}
			<a href="https://arxiv.org/pdf/{{pub.arxiv}}.pdf">arXiv:{{pub.arxiv}}[physics.geo-ph]</a>
		{% endif %}
		
		({{pub.year}})<br>
    
		{% if pub.topics %}
				<br>
				{% for topic in uniqetopics %}
					<span id="topicbtn">
						<a href="{{ base }}/topics/#{{topic|slugify}}">{{topic | upcase }}</a>
					</span>
				{% endfor %}
		{% endif %}
    </div>
	
	<div class="righty">
		{% for image in imgs1 %}
			<img src="{{site.baseurl}}/images/pubimages/blank.png" data-echo="{{site.baseurl}}/images/pubimages/{{image}}" class="responsivepubimg">
		{% endfor %}
	</div>
</div> 

{% endif %}
{% endfor %}
{% endfor %}

</div>

[pubs]: /articles/
