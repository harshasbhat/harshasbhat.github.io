---
layout: page
permalink: /publications/
title: 
---
<a name="top"></a>

> [● **Publications**](#peer-reviewed-publications)  &nbsp;  [● **Books**](#books)  &nbsp;  [● **PhD Theses**](#theses)
{: style="color:$harvard; font-size: 110%; font-weight: bold; text-align: center;"}

<br>
## Publications
{: style="color:grey; font-size: 110%; font-weight: bold; text-align: center;"}
{% assign year = 1980 %}

{% for pub in site.data.pubs.publications %}
{% if {{pub.year}} == {{year}} %} 
{% else %} 


<!-- 
{{pub.year}}
{: style="color:$harvard; font-size: 120%; font-weight: bold; text-align: center;"}
 -->

{% assign year = {{pub.year}} %}
{% endif %} 
 > {% if pub.pdf %}[**{{pub.title}}**]({{ base }}/files/{{pub.pdf}}){% else %} **{{pub.title}}** {% endif %}
<br>{{pub.author}}<br>
{% if {{pub.type}} == "article" %}<span style="color:#777">***{{pub.journal}}***</span>
{% elsif {{pub.type}} == "inproceeding" or {{pub.type}} == "incollection" %}in <span style="color:#777">***{{pub.booktitle}}***</span>
<br>eds. *{{pub.editor}}*
{% endif %}{% if pub.doi %}<br>[*doi:{{pub.doi}}*](https://doi.org/{{pub.doi}}) {% endif %}{% if pub.arxiv %} <br>[*arXiv:{{pub.arxiv}}[physics.geo-ph]*](https://arxiv.org/pdf/{{pub.arxiv}}.pdf){% endif %}
*({{pub.year}})*
<br>
<a href="#top"><img src="{{site.baseurl}}/images/top.png" class="responsive" width="80px" align="right"></a>

{% endfor %}

<br>
## Books
{: style="color:grey; font-size: 110%; font-weight: bold; text-align: center;"}

{% for pub in site.data.books.publications %}
> {% if pub.pdf %}[**{{pub.title}}**]({{ base }}/files/{{pub.pdf}}){% else %}**{{pub.title}}** {% endif %}
<br>edited by {{pub.editor}}<br>
{{pub.publisher}} {% if pub.doi %} <br>[*doi:{{pub.doi}}*](https://doi.org/{{pub.doi}})  {% endif %}({{pub.year}}) 
<br>
<a href="#top"><img src="{{site.baseurl}}/images/top.png" class="responsive" width="80px" align="right"></a>
{% endfor %}


<br>
## Theses
{: style="color:grey; font-size: 110%; font-weight: bold; text-align: center;"}

{% for pub in site.data.theses.publications %}
> {% if pub.pdf %}[**{{pub.title}}**]({{ base }}/files/{{pub.pdf}}){% else %}**{{pub.title}}** {% endif %}<br>
*{{pub.author}}*<br>
**{{pub.school}}** ({{pub.year}})
<br>
<a href="#top"><img src="{{site.baseurl}}/images/top.png" class="responsive" width="80px" align="right"></a>

{% endfor %}


{% include new-window-fix.html %}


