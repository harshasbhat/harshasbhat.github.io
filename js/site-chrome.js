---
# Built by Jekyll. Do not edit the generated file; edit the includes it is made from.
---
{%- capture chrome_header -%}{% include header.html %}{%- endcapture -%}
{%- capture chrome_footer -%}{% include footer.html %}{%- endcapture -%}
{%- capture chrome_scripts -%}{% include scripts.html %}{%- endcapture -%}
/*
 * Site header, footer and light/dark switch for pages hosted outside this site
 * (for example the publications page on pCloud).
 *
 * Made from the same _data/menu.yml, _includes/header.html, footer.html and
 * scripts.html as every page here, so the menu and theme always match.
 *
 * Use, at the end of <body>, after a <main id="content">:
 *   <script src="https://harshasbhat.github.io/js/site-chrome.js" data-current="Publications"></script>
 * data-current is the menu label to underline.
 */
(function () {
  var ORIGIN = "https://harshasbhat.github.io";
  var me = document.currentScript;
  var current = me ? me.getAttribute("data-current") : null;

  function fromHTML(html) {
    var t = document.createElement("template");
    t.innerHTML = html.trim();
    return t.content;
  }
  function absolutize(root) {
    root.querySelectorAll('a[href^="/"]').forEach(function (a) {
      var h = a.getAttribute("href");
      if (h.indexOf("//") !== 0) a.setAttribute("href", ORIGIN + h);
    });
  }

  var header = fromHTML({{ chrome_header | jsonify }});
  absolutize(header);
  header.querySelectorAll(".site-nav a").forEach(function (a) {
    a.removeAttribute("aria-current");
    if (current && a.textContent.trim() === current) a.setAttribute("aria-current", "page");
  });

  var footer = fromHTML({{ chrome_footer | jsonify }});
  absolutize(footer);

  var skip = fromHTML('<a class="skip" href="#content">Skip to content</a>');
  var top = fromHTML('<a class="top-link" href="#content" id="js-top">Back to top ↑</a>');

  document.body.insertBefore(header, document.body.firstChild);
  document.body.insertBefore(skip, document.body.firstChild);
  document.body.appendChild(footer);
  document.body.appendChild(top);

  // Same behaviour as on the site: theme switch, menu scroll on phones, back-to-top.
  {{ chrome_scripts | remove: "<script>" | remove: "</script>" }}
})();
