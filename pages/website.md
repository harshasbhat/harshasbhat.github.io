---
layout: page
permalink: /website/
title: 
---

{% include new-window-fix.html %}

> This website was built using a static website generator called Jekyll and is hosted on Github. 
I forked the website of [Gaurav Chaurasia's][gc] and tinkered with CSS and basic content.
<br><br>
First open an account on Github and set up a website for yourself. Follow the instructions [here.][GHpages]
<br><br>
I use GitHub Desktop app to commit changes, pull requests etc. Feel free to use any method that you like.
<br><br>
Now head on over to the instructions to install [Jekyll][jekyll] on your local machine.
<br><br>
[Download][mysite] my website repository, rename it as *your-github-username*.github.io
<br><br>
Open a terminal, cd to the above directory and run 'jekyll serve'. Et Voila. Modify the files as you wish.
<br><br>
One big feature is the automatic collection and listing of research topics per paper. 
If you look at '_data/pubs.yml' you will see that each publication has a topics item. 
First I collect these topics per paper and display them before each article. All this is accomplished using Liquid in
'_includes/collecttags.html'. I then make an array of unique topics (as multiple articles can share topics) and 
use it to generate the research [topics] page.


[gc]: https://gchauras.github.io
[jekyll]: https://jekyllrb.com/docs/installation/
[GHpages]: https://pages.github.com
[mysite]: https://github.com/harshasbhat/harshasbhat.github.io/archive/master.zip
[topics]: /topics/
