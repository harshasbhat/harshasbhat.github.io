---
layout: page
permalink: /publications/
title: 
---

Jump to [Publications](#peer-reviewed-publications), [Books](#books), [PhD Theses](#theses)

---
<br>

## Publications
{: style="color:grey; font-size: 120%; font-weight: bold; text-align: left;"}
{% assign year = 1980 %}

{% for pub in site.data.pubs.publications %}
{% if {{pub.year}} == {{year}} %} 
{% else %} 
---
{{pub.year}}
{: style="color:grey; font-size: 120%; font-weight: bold; text-align: center;"}
---
{% assign year = {{pub.year}} %}
{% endif %} 

<span style="color: #c90016; font-size: 70%;">📘︎</span> {% if pub.pdf %}[**{{pub.title}}**]({{ base }}/files/{{pub.pdf}}){% else %} **{{pub.title}}** {% endif %}
 <br>*{{pub.author}}*<br>
{% if {{pub.type}} == "article" %} <span style="text-decoration:underline">***{{pub.journal}}***</span>
{% elsif {{pub.type}} == "inproceeding" or {{pub.type}} == "incollection" %} in ***{{pub.booktitle}}***, eds. *{{pub.editor}}*
{% elsif {{pub.type}} == "phdthesis" %}**{{pub.school}}**, Ph. D Thesis
{% endif %} {% if pub.doi %} doi: *{{pub.doi}}* {% endif %}{% if pub.arxiv %} *arXiv:{{pub.arxiv}}[physics.geo-ph]* {% endif %}({{pub.year}})
<br>
{% endfor %}

---
<br><br>
## Books
{: style="color:grey; font-size: 120%; font-weight: bold; text-align: left;"}
---
{% for pub in site.data.books.publications %}
{% if pub.pdf %}<span style="color: #c90016">︎📘︎</span> [**{{pub.title}}**]({{ base }}/files/{{pub.pdf}}){% else %}**{{pub.title}}** {% endif %}
 <br>edited by {{pub.editor}}<br>
 {{pub.publisher}} {% if pub.doi %} doi: {{pub.doi}} {% endif %}({{pub.year}}) 
{% endfor %}


---
<br><br>
## Theses
{: style="color:grey; font-size: 120%; font-weight: bold; text-align: left;"}
---
{% for pub in site.data.theses.publications %}
{% if pub.pdf %}<span style="color: #c90016">📘︎</span> [**{{pub.title}}**]({{ base }}/files/{{pub.pdf}}){% else %}**{{pub.title}}** {% endif %}<br>
*{{pub.author}}*<br>
 **{{pub.school}}**, Ph. D. thesis ({{pub.year}})
{% endfor %}


{% include new-window-fix.html %}
