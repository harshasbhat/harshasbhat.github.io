---
layout: page
permalink: /courses/esm
title:
---

Links below for syllabus and lecture notes. There are going to plenty of typos and errors. Please contact me for more info.

<div id="esm-calendar"></div>

<style>
#esm-calendar {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  max-width: 900px;
  margin: 1.5em 0;
}

#esm-calendar .cal-months {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.5em;
}

#esm-calendar .cal-month h4 {
  margin: 0 0 0.5em;
  font-size: 1em;
  font-weight: 600;
  color: #1a4d8f;
  text-align: center;
}

#esm-calendar table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.85em;
}

#esm-calendar th {
  padding: 4px 2px;
  text-align: center;
  color: #888;
  font-weight: 500;
  font-size: 0.8em;
}

#esm-calendar td {
  padding: 0;
  text-align: center;
  height: 34px;
  vertical-align: middle;
  border-radius: 4px;
}

#esm-calendar td.session {
  background-color: #1a4d8f;
  color: #fff;
  font-weight: 600;
  cursor: default;
  position: relative;
}

#esm-calendar td.session.vacances {
  background-color: #c0783a;
}

#esm-calendar td.session .session-num {
  position: absolute;
  top: 1px;
  right: 3px;
  font-size: 0.6em;
  font-weight: 400;
  opacity: 0.8;
}

#esm-calendar td.empty {
  color: transparent;
}

#esm-calendar .cal-legend {
  margin-top: 1.2em;
  font-size: 0.85em;
  line-height: 1.6;
}

#esm-calendar .cal-legend .session-row {
  display: flex;
  gap: 0.6em;
  align-items: baseline;
  padding: 2px 0;
}

#esm-calendar .cal-legend .num {
  display: inline-block;
  min-width: 1.6em;
  height: 1.6em;
  line-height: 1.6em;
  text-align: center;
  border-radius: 4px;
  background-color: #1a4d8f;
  color: #fff;
  font-weight: 600;
  font-size: 0.8em;
}

#esm-calendar .cal-legend .num.vacances {
  background-color: #c0783a;
}

#esm-calendar .cal-legend .instructor {
  color: #666;
  font-size: 0.85em;
}
</style>

<script>
(function () {
  const sessions = [
    { n: "1",  date: "2026-09-11", topic: "Continuum Mechanics & Math Primer", instructor: "Harsha" },
    { n: "2",  date: "2026-09-18", topic: "Elastodynamics I: The Wave Equation", instructor: "Harsha" },
    { n: "3",  date: "2026-10-09", topic: "Elastodynamics II: Green's Functions & Representation Theorem", instructor: "Harsha" },
    { n: "4",  date: "2026-10-16", topic: "Far-Field Radiation & the Seismic Source", instructor: "Pierre" },
    { n: "5",  date: "2026-10-23", topic: "Kinematic Source Models", instructor: "Pierre", vacances: true },
    { n: "6",  date: "2026-10-30", topic: "Fracture Mechanics Fundamentals", instructor: "Harsha", vacances: true },
    { n: "7",  date: "2026-11-06", topic: "Friction Laws", instructor: "Harsha" },
    { n: "8",  date: "2026-11-13", topic: "Laboratory Friction", instructor: "Carolina" },
    { n: "9",  date: "2026-11-20", topic: "The Dynamic Rupture Problem", instructor: "Harsha" },
    { n: "10", date: "2026-12-04", topic: "Supershear Rupture", instructor: "Harsha" },
    { n: "11", date: "2026-12-11", topic: "Slow-to-Fast Slip Spectrum", instructor: "Harsha" },
    { n: "12", date: "2026-12-18", topic: "Energy Budget & Statistical Seismicity", instructor: "Pierre" },
    { n: "13", date: "2027-01-08", topic: "Laboratory Earthquakes", instructor: "Carolina & Harsha" }
  ];

  const byDate = {};
  sessions.forEach(s => { byDate[s.date] = s; });

  const months = [
    [2026, 8], [2026, 9], [2026, 10], [2026, 11], [2027, 0]
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
            td.className = "session" + (session.vacances ? " vacances" : "");
            td.title = session.topic + " (" + session.instructor + ")";
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

  const root = document.getElementById("esm-calendar");
  const monthsWrap = document.createElement("div");
  monthsWrap.className = "cal-months";
  months.forEach(([y, m]) => monthsWrap.appendChild(buildMonth(y, m)));
  root.appendChild(monthsWrap);

  const legend = document.createElement("div");
  legend.className = "cal-legend";
  sessions.forEach(s => {
    const row = document.createElement("div");
    row.className = "session-row";
    const num = document.createElement("span");
    num.className = "num" + (s.vacances ? " vacances" : "");
    num.textContent = s.n;
    const text = document.createElement("span");
    text.innerHTML = s.topic + ' <span class="instructor">— ' + s.instructor + '</span>';
    row.appendChild(num);
    row.appendChild(text);
    legend.appendChild(row);
  });
  root.appendChild(legend);
})();
</script>

> [Course Syllabus][syl]

> [Lecture Notes on Earthquake Source Mechanics][num]






> Last updated on {{ site.time | date: '%B %-d, %Y' }}


[num]: https://filedn.eu/lg5rE6ReEB4XtX4pGFBGRh4/Teaching/ENS/Earthquake2026/latex/master.pdf
[syl]: https://filedn.eu/lg5rE6ReEB4XtX4pGFBGRh4/Teaching/ENS/Earthquake2026/Syllabus/esm.pdf