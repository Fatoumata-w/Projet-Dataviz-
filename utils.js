// ─────────────────────────────────────────────
//  CHART DEFAULTS — DARK THEME
// ─────────────────────────────────────────────
Chart.defaults.font.family = "'DM Sans', sans-serif";
Chart.defaults.font.size = 12;
Chart.defaults.color = '#7A7670';
Chart.defaults.borderColor = 'rgba(255,255,255,0.06)';

const RED    = '#E8302A';
const RED2   = 'rgba(232,48,42,0.15)';
const BLUE   = '#3A7EC8';
const GREEN  = '#2A8A5A';
const AMBER  = '#C8862A';
const PURPLE = '#7A5AC8';
const INK    = '#F2EFE9';
const INK3   = '#7A7670';
const BG3    = '#181818';

const GRID_COLOR  = 'rgba(255,255,255,0.05)';
const TICK_COLOR  = '#7A7670';

const TOOLTIP = {
  backgroundColor: 'rgba(10,10,10,0.97)',
  borderColor: 'rgba(255,255,255,0.12)',
  borderWidth: 1,
  titleColor: '#F2EFE9',
  bodyColor: 'rgba(242,239,233,0.65)',
  padding: 10,
  cornerRadius: 2
};

// ─────────────────────────────────────────────
//  CSV PARSER
// ─────────────────────────────────────────────
async function loadCSV(path) {
  const res = await fetch(path);
  const text = await res.text();
  const lines = text.trim().split('\n');
  const headers = lines[0].split(',').map(h => h.trim().replace(/\r/, ''));
  return lines.slice(1).map(line => {
    const vals = line.split(',');
    const obj = {};
    headers.forEach((h, i) => {
      const v = (vals[i] || '').trim().replace(/\r/, '');
      obj[h] = v === '' || v === 'nan' || v === 'NaN' ? null : isNaN(v) ? v : +v;
    });
    return obj;
  });
}

// ─────────────────────────────────────────────
//  SCROLL ANIMATIONS
// ─────────────────────────────────────────────
const scrollObs = new IntersectionObserver(entries => {
  entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
}, { threshold: 0.1 });
document.querySelectorAll('.fade-up').forEach(el => scrollObs.observe(el));

// ─────────────────────────────────────────────
//  COUNTER
// ─────────────────────────────────────────────
function animCounter(el, target, suffix = '', dec = 0) {
  const dur = 1800, t0 = performance.now();
  const fmt = n => dec > 0 ? n.toFixed(dec) : Math.round(n).toLocaleString('fr-FR');
  (function step(now) {
    const t = Math.min((now - t0) / dur, 1);
    el.textContent = fmt(target * (1 - Math.pow(1 - t, 3))) + suffix;
    if (t < 1) requestAnimationFrame(step);
    else el.textContent = fmt(target) + suffix;
  })(t0);
}

// ─────────────────────────────────────────────
//  NAV
// ─────────────────────────────────────────────
function toggleMenu() {
  document.querySelector('.nav-links').classList.toggle('open');
}

// ─────────────────────────────────────────────
//  LOADING PLACEHOLDER
// ─────────────────────────────────────────────
function setLoading(id, msg = 'Chargement...') {
  const box = document.getElementById(id);
  if (!box) return;
  const div = document.createElement('div');
  div.className = 'chart-loading';
  div.textContent = msg;
  div.id = id + '-loader';
  box.appendChild(div);
}
function clearLoading(id) {
  const l = document.getElementById(id + '-loader');
  if (l) l.remove();
}
