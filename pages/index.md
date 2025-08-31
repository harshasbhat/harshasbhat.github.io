---
layout: page
title: null
permalink: /
published: true
---

<div class="archive">
<article class="article">

	<div class="smallnewsheading">
	 Welcome to Harsha S. Bhat's website
	</div>


	<div class="newsimage">
	<img src="{{site.baseurl}}/images/harsha2.jpg" height="230px" />
	</div>

	<div class="smallnewstxt">
	I am a senior <a href="http://www.cnrs.fr/index.php/en">CNRS</a> Research Scientist (Directeur de Recherche) working at the <a href="http://www.geologie.ens.fr">Laboratoire de Géologie</a> in 
	<a href="http://www.ens.fr">Ecole Normale Supérieure</a> and a Professor at <a href="https://portail.polytechnique.edu/lms/en">Laboratoire de Mécanique Solides, Ecole Polytechnique</a>.
	<br>
	<a href="http://scholar.google.com/citations?user=ZHskR34AAAAJ&hl=en&oi=ao"><i class="ai ai-google-scholar-square ai-3x"></i></a>
		<a href="https://orcid.org/0000-0003-0361-1854"><i class="ai ai-orcid-square ai-3x"></i></a>
		<a href="{{site.baseurl}}/files/CV/CurriculumVitae.pdf"><i class="ai ai-cv-square ai-3x"></i></a>
		<a href="https://www.linkedin.com/in/harshasbhat"><i class="ai ai-inspire-square ai-3x"></i></a>		
	</div>

	<div id="newsbtn">
		<a href="https://harshasbhat.github.io/about/">READ MORE... </a>
	</div>
	<br>
</article>
</div>


<br>

<div class="archive">

{% for news in site.data.news.news %}
<article class="article">

	{% if news.new == true %}
    	<div class="ribbon-badge">NEW</div>
  	{% endif %}

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
