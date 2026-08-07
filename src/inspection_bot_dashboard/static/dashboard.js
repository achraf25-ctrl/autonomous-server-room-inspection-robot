const socket = io();

const ROOM_LAYOUT = [
  ["rack_1_1", "rack_1_2", "rack_1_3", "rack_1_4"],
  ["rack_2_1", "rack_2_2", "rack_2_3", "rack_2_4"],
  ["rack_3_1", "rack_3_2", "rack_3_3", "rack_3_4"],
];

const roomGrid = document.getElementById("room-grid");
const alertFeed = document.getElementById("alert-feed");
const healthScoreValue = document.getElementById("health-score-value");
const reportLink = document.getElementById("report-link");

function renderRacks(racksState) {
  roomGrid.innerHTML = "";
  ROOM_LAYOUT.flat().forEach((rackId) => {
    const info = racksState[rackId] || { status: "ok" };
    const cell = document.createElement("div");
    cell.className = `rack-cell ${info.status}`;
    cell.textContent = rackId.replace("rack_", "R");
    cell.title = rackId;
    roomGrid.appendChild(cell);
  });
}

function renderAlert(alert) {
  const li = document.createElement("li");
  li.className = alert.critical ? "critical" : "";
  const time = new Date(alert.timestamp || Date.now()).toLocaleTimeString();
  li.innerHTML = `
    <strong>${alert.rack_id}</strong> — ${alert.anomaly_type}
    ${alert.critical ? "⚠️ CRITIQUE" : ""}
    <div class="meta">confiance ${((alert.confidence || 0) * 100).toFixed(0)}% · ${time}</div>
  `;
  alertFeed.prepend(li);
}

async function refreshAll() {
  const [racksRes, alertsRes, scoreRes] = await Promise.all([
    fetch("/api/racks"),
    fetch("/api/alerts"),
    fetch("/api/health_score"),
  ]);
  renderRacks(await racksRes.json());
  const alerts = await alertsRes.json();
  alertFeed.innerHTML = "";
  alerts.forEach(renderAlert);
  const { health_score } = await scoreRes.json();
  healthScoreValue.textContent = health_score;
}

socket.on("racks_update", renderRacks);
socket.on("new_alert", (alert) => {
  renderAlert(alert);
  fetch("/api/health_score").then((r) => r.json()).then((d) => {
    healthScoreValue.textContent = d.health_score;
  });
});
socket.on("report_ready", (data) => {
  reportLink.innerHTML = `✅ Rapport prêt : <a href="/reports/${data.filename}" target="_blank">${data.filename}</a>`;
});

document.getElementById("btn-generate-report").addEventListener("click", async () => {
  reportLink.textContent = "⏳ Génération du rapport...";
  const res = await fetch("/api/generate_report", { method: "POST" });
  const data = await res.json();
  reportLink.innerHTML = `✅ Rapport prêt : <a href="/reports/${data.filename}" target="_blank">${data.filename}</a>`;
});

document.getElementById("btn-reset-demo").addEventListener("click", async () => {
  await fetch("/api/reset_demo", { method: "POST" });
  refreshAll();
});

refreshAll();
