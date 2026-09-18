---
layout: page
permalink: /courses/numerics
title:
---

Links below for syllabus, lecture notes and jupyter note books. There are going to plenty of typos and errors. Please contact me for more info.


<div id="numerics-calendar"></div>

<style>
#numerics-calendar {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  max-width: 900px;
  margin: 1.5em 0;
}

#numerics-calendar .cal-months {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.5em;
}

#numerics-calendar .cal-month h4 {
  margin: 0 0 0.5em;
  font-size: 1em;
  font-weight: 600;
  color: #1a4d8f;
  text-align: center;
}

#numerics-calendar table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.85em;
}

#numerics-calendar th {
  padding: 4px 2px;
  text-align: center;
  color: #888;
  font-weight: 500;
  font-size: 0.8em;
}

#numerics-calendar td {
  padding: 0;
  text-align: center;
  height: 34px;
  vertical-align: middle;
  border-radius: 4px;
}

#numerics-calendar td.session {
  color: #fff;
  font-weight: 600;
  cursor: default;
  position: relative;
}

#numerics-calendar td.session.theory {
  background-color: #1a4d8f;
}

#numerics-calendar td.session.coding {
  background-color: #2e7d32;
}

#numerics-calendar td.session.vacances {
  background-color: #c0783a;
}

#numerics-calendar td.session .session-num {
  position: absolute;
  top: 1px;
  right: 3px;
  font-size: 0.6em;
  font-weight: 400;
  opacity: 0.8;
}

#numerics-calendar td.empty {
  color: transparent;
}

#numerics-calendar .cal-legend {
  margin-top: 1.2em;
  font-size: 0.85em;
  line-height: 1.6;
}

#numerics-calendar .cal-legend .session-row {
  display: flex;
  gap: 0.6em;
  align-items: baseline;
  padding: 2px 0;
}

#numerics-calendar .cal-legend .num {
  display: inline-block;
  min-width: 1.6em;
  height: 1.6em;
  line-height: 1.6em;
  text-align: center;
  border-radius: 4px;
  color: #fff;
  font-weight: 600;
  font-size: 0.8em;
}

#numerics-calendar .cal-legend .num.theory {
  background-color: #1a4d8f;
}

#numerics-calendar .cal-legend .num.coding {
  background-color: #2e7d32;
}

#numerics-calendar .cal-legend .num.vacances {
  background-color: #c0783a;
}

#numerics-calendar .cal-legend .type-tag {
  color: #666;
  font-size: 0.85em;
}

#numerics-calendar .cal-key {
  display: flex;
  gap: 1.2em;
  margin-top: 1em;
  font-size: 0.8em;
  color: #555;
}

#numerics-calendar .cal-key span.swatch {
  display: inline-block;
  width: 0.8em;
  height: 0.8em;
  border-radius: 3px;
  margin-right: 0.3em;
  vertical-align: middle;
}
</style>

<script>
(function () {
  const sessions = [
    { n: "1",  date: "2026-09-11", type: "Theory", topic: "Foundations — root-finding & time integration" },
    { n: "2",  date: "2026-09-18", type: "Coding", topic: "Foundations" },
    { n: "3",  date: "2026-10-09", type: "Theory", topic: "FD — thermal pressurization I" },
    { n: "4",  date: "2026-10-16", type: "Coding", topic: "FD" },
    { n: "5",  date: "2026-10-23", type: "Theory", topic: "FV — thermal pressurization II", vacances: true },
    { n: "6",  date: "2026-10-30", type: "Coding", topic: "FV", vacances: true },
    { n: "7",  date: "2026-11-06", type: "Theory", topic: "BEM — elastic interaction matrix" },
    { n: "8",  date: "2026-11-13", type: "Coding", topic: "BEM" },
    { n: "9",  date: "2026-11-20", type: "Theory", topic: "Coupling — mechanics + TP + dilatancy + adaptive integration" },
    { n: "10", date: "2026-12-04", type: "Coding", topic: "Coupling" },
    { n: "11", date: "2026-12-11", type: "Theory", topic: "Synthesis — multi-patch assembly & benchmarking" },
    { n: "12", date: "2026-12-18", type: "Coding", topic: "Synthesis" }
  ];

  const byDate = {};
  sessions.forEach(s => { byDate[s.date] = s; });

  const months = [
    [2026, 8], [2026, 9], [2026, 10], [2026, 11]
  ]; // month index is 0-based

  const monthNames = ["January","February","March","April","May","June",
    "July","August","September","October","November","December"];

  function pad(n) { return n < 10 ? "0" + n : "" + n; }

  function buildMonth(year, month) {
    const wrap = document.createElement("div");
    wrap.className = "cal-month";

    const h4 = document.createElement("h4");
    h4.textContent = monthNames[month] + " " + year;
    wrap.appendChild(h4);

    const table = document.createElement("table");
    const thead = document.createElement("thead");
    const headRow = document.createElement("tr");
    ["S","M","T","W","T","F","S"].forEach(d => {
      const th = document.createElement("th");
      th.textContent = d;
      headRow.appendChild(th);
    });
    thead.appendChild(headRow);
    table.appendChild(thead);

    const tbody = document.createElement("tbody");
    const firstDay = new Date(year, month, 1).getDay();
    const daysInMonth = new Date(year, month + 1, 0).getDate();

    let day = 1;
    for (let row = 0; row < 6 && day <= daysInMonth; row++) {
      const tr = document.createElement("tr");
      for (let col = 0; col < 7; col++) {
        const td = document.createElement("td");
        if ((row === 0 && col < firstDay) || day > daysInMonth) {
          td.className = "empty";
          td.textContent = "-";
        } else {
          const dateStr = year + "-" + pad(month + 1) + "-" + pad(day);
          const session = byDate[dateStr];
          if (session) {
            const typeClass = session.type.toLowerCase();
            td.className = "session " + (session.vacances ? "vacances" : typeClass);
            td.title = session.topic + " (" + session.type + ")";
            td.textContent = day;

            const badge = document.createElement("span");
            badge.className = "session-num";
            badge.textContent = session.n;
            td.appendChild(badge);
          } else {
            td.textContent = day;
          }
          day++;
        }
        tr.appendChild(td);
      }
      tbody.appendChild(tr);
    }
    table.appendChild(tbody);
    wrap.appendChild(table);
    return wrap;
  }

  const root = document.getElementById("numerics-calendar");
  const monthsWrap = document.createElement("div");
  monthsWrap.className = "cal-months";
  months.forEach(([y, m]) => monthsWrap.appendChild(buildMonth(y, m)));
  root.appendChild(monthsWrap);

  const key = document.createElement("div");
  key.className = "cal-key";
  key.innerHTML =
    '<span><span class="swatch" style="background:#1a4d8f"></span>Theory</span>' +
    '<span><span class="swatch" style="background:#2e7d32"></span>Coding</span>' +
    '<span><span class="swatch" style="background:#c0783a"></span>Vacances de la Toussaint</span>';
  root.appendChild(key);

  const legend = document.createElement("div");
  legend.className = "cal-legend";
  sessions.forEach(s => {
    const row = document.createElement("div");
    row.className = "session-row";
    const typeClass = s.type.toLowerCase();
    const num = document.createElement("span");
    num.className = "num " + (s.vacances ? "vacances" : typeClass);
    num.textContent = s.n;
    const text = document.createElement("span");
    text.innerHTML = s.topic + ' <span class="type-tag">— ' + s.type + '</span>';
    row.appendChild(num);
    row.appendChild(text);
    legend.appendChild(row);
  });
  root.appendChild(legend);
})();
</script>

> [Course Syllabus][syl]

> [Lecture Notes on Numerical Methods][num]

***

**Jupyter Notebooks**

> [Newton-Raphson Jupyter notebook][jup01]



> Last updated on {{ site.time | date: '%B %-d, %Y' }}


[num]: https://filedn.eu/lg5rE6ReEB4XtX4pGFBGRh4/Teaching/ENS/Numerical2026/latex/master.pdf
[jup01]: https://filedn.eu/lg5rE6ReEB4XtX4pGFBGRh4/Teaching/ENS/Numerical2026/jupyter/newton_method.ipynb
[syl]: https://filedn.eu/lg5rE6ReEB4XtX4pGFBGRh4/Teaching/ENS/Numerical2026/Syllabus/numerical.pdf

