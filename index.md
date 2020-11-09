---
layout: page
title: null
permalink: /
published: true
---


<div class="archive">

{% for news in site.data.news.news %}
{% if forloop.index == 1 %}

<article class="article">
	<a href="{{site.baseurl}}/{{news.readmore}}">
		<img src="{{site.baseurl}}/images/{{news.image}}" width="100%"/>
	</a> 
</article>

<article class="article">
	<div class="newsheading">
		<a href="{{site.baseurl}}/{{news.readmore}}">{{news.hl}}</a>
	</div>

	<div class="mainnewstxt"> 
		{{news.txt}}<br><br>
		<b> {{news.closing}} </b>
	</div>
	

	<div class="buttons"> 
		{% if news.readmore %} 
		<span id="newsbtn">
		<a href="{{site.baseurl}}/{{news.readmore}}">READ MORE ...</a>
		</span>
		{% endif %}
		{% if news.pdf %} 
		<span id="newsbtn">
		<a href="{{site.baseurl}}/files/{{news.pdf}}">PDF</a>
		</span>
		{% endif %}
	</div>
</article>

{% else %}

<article class="article">
	{% if news.image %} 
		<div class="newsimage">
				<img src="{{site.baseurl}}/images/{{news.image}}" height="250px" />
		</div>
	{% endif %}
	
	<div class="smallnewsheading">
	 {{news.hl}}
	</div>

	<div class="smallnewstxt"> 
		{{news.txt}}<br><br>
		<b> {{news.closing}} </b>
	</div>

	<div class="buttons"> 
		{% if news.readmore %} 
		<span id="newsbtn">
		<a href="{{news.readmore}}">READ MORE ...</a>
		</span>
		{% endif %}
		{% if news.pdf %} 
		<span id="newsbtn">
		<a href="{{site.baseurl}}/files/{{news.pdf}}">PDF</a>
		</span>
		{% endif %}
	</div>
</article>

{% endif %}     
{% endfor %} 
</div>


{% include new-window-fix.html %}
