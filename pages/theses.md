---
layout: page
permalink: /theses/
title: 
---

{% include collecttags.html %}

{% for pub in site.data.theses.publications %}
<div class="pubs">
	<div class="articles">
			<img src="{{site.baseurl}}/images/pubimages/{{pub.img}}" class="responsivepubimg">
	</div>	

	<div class="articles">
		{% if pub.pdf %}
			<a href="https://filedn.eu/lg5rE6ReEB4XtX4pGFBGRh4/CollectedPapers/{{pub.type}}/{{pub.pdf}}" style="font-size:100%"><span>{{pub.title}} ({{pub.year}})</span></a>
		{% else %}
		    <span>{{pub.title}} ({{pub.year}})</span> 
		{% endif %}

		
		<span style="font-size:85%">{{pub.author}}</span>
		<span style="font-size:85%">{{pub.school}}</span>

		<div class="pubbuttons">
					
			
		{% if pub.slides %} 
		<div id="newsbtn">
		<a href="https://filedn.eu/lg5rE6ReEB4XtX4pGFBGRh4/CollectedPapers/{{pub.type}}/{{pub.slides}}" style="font-size:65%">SLIDES</a>
		</div>
		{% endif %}
		
		{% if pub.watch %} 
		<div id="watchbtn">
		<a href="{{pub.watch}}" style="font-size:65%">WATCH IT ONLINE</a>
		</div>
		{% endif %}


			</div>    	


  </div>
    
</div>	

{% endfor %}

