---
layout: page
permalink: /publications/
title: 
---
<script type="text/javascript" src="//cdn.plu.mx/widget-popup.js"></script>

{% include collecttags.html %}

<div class="container">
	<div class="section">
		<div id="link_bar">
		   <a href="#peer-reviewed-publications">Peer Reviewed Articles</a> 
		</div>
	</div>
	<div class="section">
		<div id="link_bar">
		   <a href="#books">Edited Books</a>
		</div>
	</div>
	<div class="section">
		<div id="link_bar">
		   <a href="#theses">Doctoral Theses</a>
		</div>
	</div>
	<div class="section">
		<div id="link_bar">
		   <a href="/topics/">Research Topics</a>
		</div>
	</div>
</div>

<br>


## Articles
{: style="text-decoration: underline; color:black; font-size: 110%; font-weight: bold; text-align: center;"}
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
    	<br>
     	●
		{% if pub.pdf %}
			<a display:inline href="{{ base }}/files/{{pub.pdf}}">{{pub.title}}</a>
		{% else %} 
			{{pub.title}}
		{% endif %}
	</div>	

		
	<div class="lefty">
		{{pub.author | replace: "H. S. Bhat", "<b>H. S. Bhat</b>"}}<br>
		
		{% if pub.type == "article" %}
			<span style="color:grey"><em>{{pub.journal}}</em><br></span>
		{% elsif pub.type == "inproceeding" or pub.type == "incollection" %}
			in <span style="color:grey">{{pub.booktitle}}</span>
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
				<span id="link_bar2">
					<a href="{{ base }}/topics/#{{topic|slugify}}">{{topic | upcase }}</a>
				</span>
			{% endfor %}
		</div>
	{% endif %}
	
	<div class="righty">
    <br>
    	{% for image in imgs %}
			<img src="{{site.baseurl}}/images/pubimages/{{image}}" class="responsive" width="100%">
    	{% endfor %}
	</div>

	
{% else %}

    <div class="fully2">
    <br>
     	●
		{% if pub.pdf %}
			<a display:inline href="{{ base }}/files/{{pub.pdf}}">{{pub.title}}</a>
		{% else %} 
			{{pub.title}}
		{% endif %}
		
		<br>{{pub.author | replace: "H. S. Bhat", "<b>H. S. Bhat</b>"}}<br>		
		
		{% if pub.type == "article" %}
			<span style="color:grey"><em>{{pub.journal}}</em><br></span>
		{% elsif pub.type == "inproceeding" or pub.type == "incollection" %}
			in <span style="color:grey">{{pub.booktitle}}</span>
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
				<span id="link_bar2">
					<a href="{{ base }}/topics/#{{topic|slugify}}">{{topic | upcase }}</a>
				</span>
			{% endfor %}
	{% endif %}
	
	</div>

{% endif %}
	
	
	
</div>  
	
{% endfor %}


<br><br>
## Books
{: style="text-decoration: underline; color:black; font-size: 110%; font-weight: bold; text-align: center;"}


{% for pub in site.data.books.publications %}
<div class="group">

{% if pub.img %}

    <div class="lefty">
	    <br>
     	●
		{% if pub.pdf %}
			<a display:inline href="{{ base }}/files/{{pub.pdf}}">{{pub.title}}</a>
		{% else %} 
			{{pub.title}} 
		{% endif %}
	</div>	

	<div class="lefty">	
		edited by {{pub.editor | replace: "H. S. Bhat", "<b>H. S. Bhat</b>"}}<br>
		
		{% if pub.doi %}
			{{pub.publisher}}<br>
			<a href="https://doi.org/{{pub.doi}}">doi:{{pub.doi}}</a> ({{pub.year}}) 
		{% else %}
			{{pub.publisher}} ({{pub.year}})
		{% endif %}
    </div>
	
	<div class="righty">
	<br>
			<img src="{{site.baseurl}}/images/pubimages/{{pub.img}}" class="responsive" width="80%">
	</div>

{% else %}

    <div class="fully2">
    <br>
     	●
		{% if pub.pdf %}
			<a display:inline href="{{ base }}/files/{{pub.pdf}}">{{pub.title}}</a>
		{% else %} 
			{{pub.title}} 
		{% endif %}
		<br>edited by {{pub.editor | replace: "H. S. Bhat", "<b>H. S. Bhat</b>"}},
		
		{% if pub.doi %}
			{{pub.publisher}}<br>
			<a href="https://doi.org/{{pub.doi}}">doi:{{pub.doi}}</a> ({{pub.year}}) 
		{% else %}
			{{pub.publisher}} ({{pub.year}})
		{% endif %}
		
	</div>
{% endif %}		
</div>
	
{% endfor %}

<br><br>
## Theses
{: style="text-decoration: underline; color:black; font-size: 110%; font-weight: bold; text-align: center;"}


{% for pub in site.data.theses.publications %}
<div class="group">

{% if pub.img %}

	<div class="lefty">
	    <br>
		●
		{% if pub.pdf %}
			<a href="{{ base }}/files/{{pub.pdf}}">{{pub.title}}</a>
		{% else %} 
			{{pub.title}} 
		{% endif %}
	</div>
	
	<div class="lefty">	
		{{pub.author | replace: "H. S. Bhat", "<b>H. S. Bhat</b>"}}<br>
		<span style="color:grey">{{pub.school}}</span>
		{% if pub.doi %}
			<a href="https://doi.org/{{pub.doi}}">doi:{{pub.doi}}</a>
		{% endif %}
		({{pub.year}}) 
    </div>
    
	<div class="righty">
			<br>
			<img src="{{site.baseurl}}/images/pubimages/{{pub.img}}" class="responsive">
	</div>
	
{% else %}

	<div class="fully2">
		●
		{% if pub.pdf %}
			<a href="{{ base }}/files/{{pub.pdf}}">{{pub.title}}</a>
		{% else %} 
			{{pub.title}} 
		{% endif %}
	
		<br>{{pub.author | replace: "H. S. Bhat", "<b>H. S. Bhat</b>"}}<br>
		<span style="color:grey">{{pub.school}}</span>
		{% if pub.doi %}
			<a href="https://doi.org/{{pub.doi}}">doi:{{pub.doi}}</a>
		{% endif %}
		({{pub.year}}) 
	</div>	
{% endif %}

</div>	
{% endfor %}

{% include new-window-fix.html %}

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

[LG]: http://www.geologie.ens.fr
[ENS]: http://www.ens.fr
[topics]: /topics/
