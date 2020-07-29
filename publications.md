---
layout: page
permalink: /publications/
title: 
---
<a name="top"></a>
<style>
    #link_bar a { display: inline;margin-right: 0.25em; font-weight: bold; border-radius: 0.7em; padding: 3px 6px; float:center; color:#3047c9; background-color:#fff; border: 1px solid #dce0f2;}
    #link_bar a:hover { display: inline;margin-right: 0.25em; font-weight: bold; border-radius: 0.7em; padding: 3px 6px; float:center; color:#3047c9; background-color:#dce0f2; border: 1px solid #dce0f2; text-decoration:none;}
</style>
<div id="link_bar">
    <a href="#peer-reviewed-publications">Articles</a>
    <a href="#books">Books</a>
    <a href="#theses">Theses</a>
</div>
<!-- 
[● **Articles**](#peer-reviewed-publications)  &nbsp;  [● **Books**](#books)  &nbsp;  [● **Theses**](#theses)
 -->
<!-- {: style="color:$harvard; font-size: 110%; font-weight: bold; text-align: center;"} -->

## Articles
{: style="text-decoration: underline; color:black; font-size: 110%; font-weight: bold; text-align: center;"}
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
> <a href="#top"><img src="{{site.baseurl}}/images/top.png" class="responsive" width="75px" align="right"></a>
<br> {% if pub.pdf %}["{{pub.title}}"]({{ base }}/files/{{pub.pdf}}){% else %} {{pub.title}} {% endif %}
({{pub.year}})<br>{{pub.author}}<br>
{% if {{pub.type}} == "article" %}<span style="color:#000">***{{pub.journal}}*** <br></span>
{% elsif {{pub.type}} == "inproceeding" or {{pub.type}} == "incollection" %}in <span style="color:#777">***{{pub.booktitle}}***</span>
<br>eds. *{{pub.editor}}*<br>
{% endif %}{% if pub.doi %}[*doi:{{pub.doi}}*](https://doi.org/{{pub.doi}}) <br> {% endif %}{% if pub.arxiv %} [*arXiv:{{pub.arxiv}}[physics.geo-ph]*](https://arxiv.org/pdf/{{pub.arxiv}}.pdf) <br>{% endif %}


{% endfor %}

<br>
## Books
{: style="text-decoration: underline; color:black; font-size: 110%; font-weight: bold; text-align: center;"}

{% for pub in site.data.books.publications %}
> <a href="#top"><img src="{{site.baseurl}}/images/top.png" class="responsive" width="75px" align="right"></a><br> 
{% if pub.pdf %}[{{pub.title}}]({{ base }}/files/{{pub.pdf}}){% else %}{{pub.title}} {% endif %}
<br>edited by {{pub.editor}}<br>
{{pub.publisher}} {% if pub.doi %} <br>[*doi:{{pub.doi}}*](https://doi.org/{{pub.doi}})  {% endif %}({{pub.year}}) 
<br>



{% endfor %}


<br>
## Theses
{: style="text-decoration: underline; color:black; font-size: 110%; font-weight: bold; text-align: center;"}

{% for pub in site.data.theses.publications %}
> <a href="#top"><img src="{{site.baseurl}}/images/top.png" class="responsive" width="75px" align="right"></a><br> 
{% if pub.pdf %}[{{pub.title}}]({{ base }}/files/{{pub.pdf}}){% else %}{{pub.title}} {% endif %} ({{pub.year}})<br>
*{{pub.author}}*<br>
**{{pub.school}}** 


{% endfor %}


[LG]: http://www.geologie.ens.fr
[ENS]: http://www.ens.fr
