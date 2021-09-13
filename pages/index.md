---
layout: page
title: null
permalink: /
published: true
---

<div class="archive">

{% for news in site.data.news.news %}
<article class="article">

	<div class="smallnewsheading">
	 {{news.hl}}
	</div>

	{% if news.image %}
		<div class="newsimage">
			{% if news.url %}
			<a href="{{news.url}}">
				<img src="{{site.baseurl}}/images/{{news.image}}" height="230px" />
			</a>
			{% else %}
				<img src="{{site.baseurl}}/images/{{news.image}}" height="230px" />
			{% endif %}
		</div>
	{% endif %}

	<div class="smallnewstxt">
		{{news.txt}}
		<b> {{news.closing}} </b>
	</div>

	<div class="buttons">
		{% if news.readmore %}
		<div id="newsbtn">
		<a href="{{news.readmore}}">READ MORE ...</a>
		</div>
		{% endif %}

		{% if news.pdf %}
		<div id="newsbtn">
		<a href="{{site.baseurl}}/files/{{news.pdf}}">PDF</a>
		</div>
		{% endif %}

		{% if news.watch %}
		<div id="watchbtn">
		<a href="{{news.watch}}">WATCH IT ONLINE</a>
		</div>
		{% endif %}

		{% if news.slides %}
		<div id="newsbtn">
		<a href="{{site.baseurl}}/files/{{news.slides}}">SLIDES</a>
		</div>
		{% endif %}

		{% if news.youtube %}
		<div id="watchbtn">
		<a href="{{news.watch}}">YOUTUBE</a>
		</div>
		{% endif %}

	</div>
</article>

{% endfor %}
</div>
