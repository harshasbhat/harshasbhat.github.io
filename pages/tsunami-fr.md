---
layout: page
title: Tsunami
permalink: /tsunami-fr/
published: true
---
{% include usemath.html %}

<div class="pagewidth">
<div id="sectionbtnlst">
   <a href="https://harshasbhat.github.io/files/AmlaniBhatSimons2020a.pdf">PDF</a>
   <a href="{{site.baseurl}}/tsunami-en/">English</a>
   <a href="{{site.baseurl}}/tsunami-fr/">Français</a>
</div>

<h2 align="center" style="color:#4181BD; font-size:18pt">Supershear shock front contributions to the tsunami from the 2018 $M_w$ 7.5 Palu earthquake$^*$</h2>	

<button class="accordion">Authors & Affiliations</button>
<div class="panel">
<div class="columntxtauthors">

Faisal Amlani,$^{1}$ Harsha S. Bhat,$^{2,*}$ Wim J. F. Simons,$^{3}$ Alexandre Schubnel,$^{2}$ Christophe Vigny,$^{2}$ Ares J. Rosakis,$^{4}$ Joni Efendi,$^5$ Ahmed Elbanna,$^6$ and Hasanuddin Z. Abidin$^{5,7}$ <br><br>

(1) Department of Aerospace and Mechanical Engineering, University of Southern California, Los Angeles, USA, 
(2) Laboratoire de Géologie, École Normale Supérieure, CNRS-UMR 8538, PSL Research University, Paris, France, 
(3) Faculty of Aerospace Engineering, Delft University of Technology, Delft, Netherlands, 
(4) Graduate Aerospace Laboratories, California Institute of Technology, Pasadena, California, USA, 
(5) BIG (Badan Informasi Geospasial / Geospatial Information Agency of Indonesia), Java, Indonesia, 
(6) Department of Civil and Environmental Engineering, University of Illinois at Urbana Champaign, USA, 
(7) Department of Geodesy and Geomatics Engineering, Institute of Technology Bandung, Indonesia<br> <br>
* Corresponding author: 
{% include image.html url="/images/email.png" width="150px" align="right" %}<br>
Data Availability: <a href="https://doi.org/10.5281/zenodo.4066297"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.4066297.svg" alt="DOI"></a>
</div>
</div>

<button class="accordion">Résumé Scientifque</button>
<div class="panel">
<p><b>On sait que en principe, les tsunamis dangereux sont principalement
générés dans les zones de subduction par de grands séismes qui
produisent un déplacement vertical du plancher océanique. Cependant, un
tremblement de terre d'une magnitude, $M_w$ 7,5 qui s’est produit à
Sulawesi (Indonésie) en 2018 sur une faille de glissement latéral a
provoqué un tsunami qui a dévasté la ville de Palu. Le mécanisme par
lequel ce grand tsunami a pris naissance à la suite d'un tremblement de
terre de type "strike-slip" a été débattu. Nous présentons ici des
données sur les mouvements du sol en champ proche provenant d'une
station GPS qui confirment que la rupture associée au tremblement de
terre de Palu de 2018 s’est propagée à une vitesse supérieure à la
vitesse des ondes de cisaillement dans le milieu hôte. Ce phénomène,
rare, est qualifié de rupture « supershear ». Nous étudions l'effet de
cette rupture particulièrement rapidesur la génération de tsunamis en
couplant le mouvement du sol à une onde de cisaillement non linéaire 
qui tient compte de cet effet supershear et de la bathymétrie de la baie
de Palu (modèle simple 1-D en eau peu profonde).Nous constatons que ces
simulations reproduisent les mouvements du tsunami mesurés par le
marégraphe situé au port de Palu (Pantoloan), avec seulement un réglage
minimal des paramètres. Nous concluons que les fronts de Mach (chocs),
générés par la vitesse de la rupture, ont interagi avec la bathymétrie
et ont contribué au tsunami. Ces observations valident un nouveau
mécanisme de génération de Tsunami destructeur, qui peut donc se
produire non seulement dans les environs d’une zone de subduction mais
également à proximité d’une faille décrochante, pour peu que la rupture
soit excessivement rapide. Cela suggère que la vitesse de rupture des
séismes, et non seulement leur mécanisme, devrait être prise en compte
dans l'évaluation du risque de tsunami.</b></p>
</div>


<button class="accordion">Les Sections</button>
<div class="panel">
	<div id="sectionbtnlst">
	   <a href="#one"> 1. Le Séisme </a>
	   <a href="#two"> 2. Supershear Séismes </a>
	   <a href="#three"> 3. Les Preuves </a>
	   <a href="#four"> 4. Tsunami Classique </a>
	   <a href="#five"> 5. Tsunami Supershear </a>
	</div>
</div>

<h3 align="left" id="one">1. Le Séisme</h3>

{% include image.html url="/images/tsunami/setting.jpg" 
caption="The regional tectonic setting and the faults associated with 
the 2018 Palu earthquake. Image on left from Ulrich et al. (2019)$^1$." width="100%" align="center" %}

Le séisme de magnitude $M_w$ 7,5 de Palu Sulawesi (Indonésie), a
frappé le 28 septembre 2018, causant des dégats  importants et de
nombreuses pertes de vies humaines.  Ce séisme ne se produit pas
sur une subduction mais sur une faille de glissement latéral qui
traverse l’Île de Sulawesi. Ce tremblement de terre a également
généré un tsunami qui a dévasté la ville de Palu. En règle
générale, ce type de séisme (dit en décrochement) ne provoque pas
de grands mouvements verticaux du sol et donc pas de Tsunami,
contrairement à Tohoku, au Japon, lors du tremblement de terre de
2011. La raison  d’un tel tsunami à Palu est donc un peu
mystérieuse.  

<h4 align="center">Cependant, il s'agissait d'un séismes "Supershear"</h4>    

<h3 align="left" id="two">2. Supershear Séismes</h3>

{% include video.html id="hMHSsEobbz0"%}    

<br><br>

Lorsqu'un tremblement de terre commence à ouvrir une faille, le
front de propagation de la rupture (le chariot de la fermeture
éclair) émet constamment des ondes de pression et de cisaillement
dans le milieu. Les ondes P se déplacent à une vitesse d'environ 5
km/s (18000 km/h) et les ondes S à environ 3,5 km/s (12600 km/h).
Dans le cas d’un séisme typique normal, la vitesse du front est
inférieure à celle des ondes S. On les appelle des séismes «
subshear ». Pour les séismes de type « Supershear », en revanche,
le front de la rupture se déplace plus rapidement que les ondes de
cisaillement. Lorsque la barrière de vitesse des ondes S est
franchie, des fronts de choc linéaires se manifestent. Ils sont
exactement semblables au boum sonique que nous entendons lorsqu’un
avion supersonique franchi le mur du son (dépasse la vitesse du
son).


<h3 align="left" id="three">3. Les Preuves</h3>

{% include image.html url="/images/tsunami/GPS.png" 
caption="Ground Velocity recorded by the PALP GPS station." width="100%" align="center" %}

<br><br>

Les séismes de type "Supershear" ont une signature unique de
mouvement du sol. La façon dont le sol se déplace parallèlement et
perpendiculairement à la faille nous renseigne sur la vitesse à
laquelle le front de la rupture sismique s'est déplacé. Le
déplacement de la station GPS PALP située à l’aéroport de Palu à
proximité de la faille, monitoré en continu durant la propagation
de la rupture, révèle la nature « supershear » du séisme du 28
septembre 2018 : un pic de déplacement parallèle à la faille de
l’ordre de 1 m/s prédit pour une rupture supershear et absent dans
le cas d’une rupture standard subshear. <br><br>

C'est  la première fois qu'un tremblement de terre de type Supershear
est détecté à l'aide d'une station GPS.

<h3 align="left"  id="four">4. Génération Classique de Tsunamis</h3>

{% include video.html id="4Xebwzb3dDE?start=12" caption="Classical Tsunami Generation. Courtesy: Caltech Tectonics Observatory"%}


Les tsunamis classiques sont générés par le déplacement vertical
du fond marin autour de la faille. Les tremblements de terre de la
zone de subduction sont des sources typiques de ces tsunamis. Les
tremblements de terre de type "Strike-Slip", en revanche, ne
soulèvent pas autant le fond de l'océan puisqu’il s’agit de
glissement essentiellement horizontaux.

<h4 align="right">Sauf quand il s'agit de tremblements de terre de type "Supershear".</h4>    

<h3 align="left"  id="five">5. Génération de Tsunamis Par Des Séismes de Type "Supershear"</h3>

{% include video.html id="3fJfKwOEzQ4"%}

<br>

Les ruptures de cisaillement produisent des fronts de choc. Ces
fronts de choc transportent l'énergie de la faille sur de grandes
distances et sans grande perte. Dans ce travail, nous montrons que
même si les déplacements sont faibles, le simple fait que les
fronts de choc affectent une grande région suffit à générer un
tsunami. Au final, la forme de la baie de Palu, en « baignoire »,
a encore contribué à amplifier le tsunami ainsi généré.

<br><br>
<hr>
<div class="columntxtauthors">
$^*$ <a href="https://harshasbhat.github.io/files/AmlaniBhatSimons2020a.pdf"> F. Amlani, H. S. Bhat, W. J. F. Simons, A. Schubnel, C. Vigny, A. J. Rosakis, J. Efendi, A. Elbanna & H. Z. Abidin, accepted in principle Nature Geoscience, arXiv:1910.14547v3[physics.geo-ph] (2020)</a> <br><br>
$^1$ <a href="https://doi.org/10.1007/s00024-019-02290-5">Ulrich et al. (2019) Coupled, Physics-Based Modeling Reveals Earthquake Displacements are Critical to the 2018 Palu, Sulawesi Tsunami, Pure Appl. Geophys. </a><br><br>
$^2$ <a href="https://www.nytimes.com/2018/09/28/world/asia/tsunami-palu-indonesia-earthquake.html">NYTimes: Tsunami and Earthquake in Indonesia Kill Nearly 400, Officials Say</a>
</div>
{% include new-window-fix.html %}
</div>



