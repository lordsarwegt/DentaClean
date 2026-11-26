const searchInput = document.querySelector('#appointment-search');
const appointmentRows = [...document.querySelectorAll('#appointment-list tr')];
const emptyState = document.querySelector('#empty-state');
const toast = document.querySelector('#toast');
const sidebar = document.querySelector('#sidebar');
let toastTimeout;

searchInput.addEventListener('input', () => {
  const query = searchInput.value.trim().toLocaleLowerCase('es');
  let visibleRows = 0;

  appointmentRows.forEach((row) => {
    const matches = row.textContent.toLocaleLowerCase('es').includes(query);
    row.hidden = !matches;
    if (matches) visibleRows += 1;
  });

  emptyState.hidden = visibleRows > 0;
});

document.querySelector('#new-appointment').addEventListener('click', () => {
  window.clearTimeout(toastTimeout);
  toast.textContent = 'El formulario de citas se conectará con la API.';
  toast.classList.add('visible');
  toastTimeout = window.setTimeout(() => toast.classList.remove('visible'), 2800);
});

document.querySelector('#menu-toggle').addEventListener('click', () => {
  sidebar.classList.toggle('open');
});

document.querySelectorAll('.nav-item[data-section]').forEach((item) => {
  item.addEventListener('click', () => {
    document.querySelectorAll('.nav-item[data-section]').forEach((link) => link.classList.remove('active'));
    item.classList.add('active');
    const sectionName = item.dataset.section;
    document.querySelector('.breadcrumbs strong').textContent = sectionName;
    if (window.matchMedia('(max-width: 680px)').matches) sidebar.classList.remove('open');
  });
});