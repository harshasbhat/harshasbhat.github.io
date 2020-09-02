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
{% assign auth = pub.author %}

<span id="link_bar3"><a href="#top">[top]</a></span>
>  {% if pub.arxiv %}<div class="section">
		<div id="link_bar3">
		   <a href="https://plu.mx/plum/a/?arxiv={{pub.arxiv}}" data-popup="right" data-size="small" class="plumx-plum-print-popup plum-bigben-theme" data-site="plum" data-hide-when-empty="true"></a>
		</div>
	</div>{% endif %}{% if pub.doi %}<div class="section">
		<div id="link_bar3">
		   <a href="https://plu.mx/plum/a/?doi={{pub.doi}}" data-popup="right" data-size="small" class="plumx-plum-print-popup plum-bigben-theme" data-site="plum" data-hide-when-empty="true"></a>
		</div>
	</div>{% endif %} {% if pub.pdf %}[{{pub.title}}]({{ base }}/files/{{pub.pdf}}){% else %} {{pub.title}} {% endif %}
<br>{{pub.author | replace: "H. S. Bhat", "**H. S. Bhat**"}}<br>
{% if pub.type == "article" %}<span style="color:#0d667f">***{{pub.journal}}*** <br></span>
{% elsif pub.type == "inproceeding" or pub.type == "incollection" %}in <span style="color:#0d667f">***{{pub.booktitle}}*** <br></span>
eds. *{{pub.editor}}*<br>{% endif %}{% if pub.doi %}[doi:{{pub.doi}}](https://doi.org/{{pub.doi}}) ({{pub.year}})<br>{% endif %}{% if pub.arxiv %}[arXiv:{{pub.arxiv}}[physics.geo-ph]](https://arxiv.org/pdf/{{pub.arxiv}}.pdf) ({{pub.year}}) <br>{% endif %}
{% if pub.topics %}{% for topic in uniqetopics %}<span id="link_bar2"><a href="{{ base }}/topics/#{{topic|slugify}}">{{topic | upcase }}</a></span>{% endfor %}{% endif %}
{% assign j = j | minus: 1 %}
{% endfor %}

<br>
## Books
{: style="text-decoration: underline; color:black; font-size: 110%; font-weight: bold; text-align: center;"}

{% for pub in site.data.books.publications %}
<span id="link_bar3"><a href="#top">[top]</a></span><br>

> {% if pub.pdf %}[{{pub.title}}]({{ base }}/files/{{pub.pdf}}){% else %}{{pub.title}} {% endif %}
<br>edited by {{pub.editor | replace: "H. S. Bhat", "**H. S. Bhat**"}}<br>
{{pub.publisher}} {% if pub.doi %} <br>[*doi:{{pub.doi}}*](https://doi.org/{{pub.doi}})  {% endif %}({{pub.year}}) 
{% endfor %}


<br>
## Theses
{: style="text-decoration: underline; color:black; font-size: 110%; font-weight: bold; text-align: center;"}

{% for pub in site.data.theses.publications %}
<span id="link_bar3"><a href="#top">[top]</a></span><br>

> {% if pub.pdf %}[{{pub.title}}]({{ base }}/files/{{pub.pdf}}){% else %}{{pub.title}} {% endif %} ({{pub.year}})<br>
{{pub.author | replace: "H. S. Bhat", "**H. S. Bhat**"}}<br>
**{{pub.school}}** 
{% endfor %}

{% include new-window-fix.html %}

[LG]: http://www.geologie.ens.fr
[ENS]: http://www.ens.fr
[topics]: /topics/
