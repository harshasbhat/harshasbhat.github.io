---
layout: page
permalink: /topics/
title: 
---
## Research Topics<br>
{: style="text-decoration: none; color:black; font-size: 120%; font-weight: bold; text-align: center;"}

**This page is being updated...**

Listed below are my publications sorted by various research topics. 
You can browse my full list of publications [here][pubs].
<br><br>

{% include collecttags.html %}

{% assign sorttags = uniqTags | sort_natural %} 

<div class="container">
	{% for tag in sorttags %}
		<div class="section">
			<div id="link_bar">
			   <a href="#{{ tag  | slugify }}"> {{ tag | upcase }} </a>
			</div>
		</div>
	{% endfor %}
</div>

<br>

{% for tag in sorttags %}
## {{ tag | upcase }}
{: style="text-align: center;margin: 0.25em; font-style: italic; font-weight: 450; border-radius: 0.7em; padding: 3px 6px; float:center; color:black; background-color:#fff; text-decoration:italic;"}
<a name="#{{ tag }}"></a>

{% for pub in site.data.pubs.publications %}
{% assign uniqetopics = "" %}
{% assign uniqetopics = pub.topics | split: ', ' | sort_natural | uniq %} 

{% if pub.topics contains tag %}
> {% if pub.pdf %}[{{pub.title}}]({{ base }}/files/{{pub.pdf}}){% else %} {{pub.title}} {% endif %}
({{pub.year}})<br>{{pub.author}}<br>
{% if pub.type == "article" %}<span style="color:#000">***{{pub.journal}}*** <br></span>
{% elsif pub.type == "inproceeding" or pub.type == "incollection" %}in <span style="color:#666">***{{pub.booktitle}}***</span>
<br>eds. *{{pub.editor}}*{% endif %}{% if pub.doi %}[*doi:{{pub.doi}}*](https://doi.org/{{pub.doi}}){% endif %}{% if pub.arxiv %} [*arXiv:{{pub.arxiv}}[physics.geo-ph]*](https://arxiv.org/pdf/{{pub.arxiv}}.pdf){% endif %} 
{% if pub.topics %}<br>{% for topic in uniqetopics %}<span id="link_bar2"><a href="{{ base }}/topics/#{{topic|slugify}}">{{topic | upcase }}</a></span>{% endfor %}{% endif %} <span id="link_bar3"><a href="#top">top</a></span>
{% endif %}
{% endfor %}

<br>
{% endfor %}


[pubs]: /publications/