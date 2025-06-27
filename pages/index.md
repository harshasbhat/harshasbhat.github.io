---
layout: page
title: null
permalink: /
published: true
---
<h2 align="center" style="color:#04168b; font-size:20pt">Welcome to Harsha S. Bhat's website</h2>	


<!-- <div class="articles2"> -->
{% include image.html url="/images/group2025.jpg" width="100%" align="center" %}
I am a senior <a href="http://www.cnrs.fr/index.php/en">CNRS</a> Research Scientist (Directeur de Recherche) working at the <a href="http://www.geologie.ens.fr">Laboratoire de Géologie</a> in 
<a href="http://www.ens.fr">Ecole Normale Supérieure</a> and a Professor at <a href="https://portail.polytechnique.edu/lms/en">Laboratoire de Mécanique Solides, Ecole Polytechnique</a>. I am also a visiting Professor at <a href="https://www.niser.ac.in">National Institute of Science Education and Research</a>, India.
<!-- </div>	 -->


<h2 align="center" style="color:#04168b; font-size:20pt">News and Updates</h2>	

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

		{% if news.insu %}
		<div id="watchbtn">
		<a href="{{news.insu}}">INSU</a>
		</div>
		{% endif %}

		{% if news.readmore %}
		<div id="newsbtn">
		<a href="{{news.readmore}}">READ MORE</a>
		</div>
		{% endif %}

	</div>
</article>

{% endfor %}
</div>
