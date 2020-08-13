---
layout: page
permalink: /publications/
title: 
---


{% include collecttags.html %}

<div class="container">
	<div class="section">
		<div id="link_bar">
		   <a href="#peer-reviewed-publications">Peer Reviewed Articles</a> 
		</div>
	</div>
	<div class="section">
		<div id="link_bar">
		   <a href="#books">Books</a>
		</div>
	</div>
	<div class="section">
		<div id="link_bar">
		   <a href="#theses">Ph. D. Theses</a>
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

<span id="link_bar3"><a href="#top">[top]</a></span><br>

> ({{ j }})  {% if pub.pdf %}[{{pub.title}}]({{ base }}/files/{{pub.pdf}}){% else %} {{pub.title}} {% endif %}
({{pub.year}})<br>{{pub.author}}<br>
{% if pub.type == "article" %}<span style="color:#000">***{{pub.journal}}*** <br></span>
{% elsif pub.type == "inproceeding" or pub.type == "incollection" %}in <span style="color:#666">***{{pub.booktitle}}***</span>
<br>eds. *{{pub.editor}}*{% endif %}{% if pub.doi %}[*doi:{{pub.doi}}*](https://doi.org/{{pub.doi}}){% endif %}{% if pub.arxiv %} [*arXiv:{{pub.arxiv}}[physics.geo-ph]*](https://arxiv.org/pdf/{{pub.arxiv}}.pdf) {% endif %}
{% if pub.topics %}<br>{% for topic in uniqetopics %}<span id="link_bar2"><a href="{{ base }}/topics/#{{topic|slugify}}">{{topic | upcase }}</a></span>{% endfor %}{% endif %}
{% assign j = j | minus: 1 %}
{% endfor %}

<br>
## Books
{: style="text-decoration: underline; color:black; font-size: 110%; font-weight: bold; text-align: center;"}

{% for pub in site.data.books.publications %}
<span id="link_bar3"><a href="#top">[top]</a></span><br>

> {% if pub.pdf %}[{{pub.title}}]({{ base }}/files/{{pub.pdf}}){% else %}{{pub.title}} {% endif %}
<br>edited by {{pub.editor}}<br>
{{pub.publisher}} {% if pub.doi %} <br>[*doi:{{pub.doi}}*](https://doi.org/{{pub.doi}})  {% endif %}({{pub.year}}) 
{% endfor %}


<br>
## Theses
{: style="text-decoration: underline; color:black; font-size: 110%; font-weight: bold; text-align: center;"}

{% for pub in site.data.theses.publications %}
<span id="link_bar3"><a href="#top">[top]</a></span><br>

> {% if pub.pdf %}[{{pub.title}}]({{ base }}/files/{{pub.pdf}}){% else %}{{pub.title}} {% endif %} ({{pub.year}})<br>
*{{pub.author}}*<br>
**{{pub.school}}** 
{% endfor %}


[LG]: http://www.geologie.ens.fr
[ENS]: http://www.ens.fr
[topics]: /topics/
