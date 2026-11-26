  // Contextual Preview Drawer controller
  function openPreviewDrawer(name, exp, treatment, doctor, status, bio, phone, email, lastDate, nextDate) {
    const drawer = document.getElementById('patient-drawer');
    document.getElementById('drawer-name').innerText = name;
    document.getElementById('drawer-exp').innerText = '#' + exp;
    document.getElementById('drawer-treatment').innerText = treatment;
    document.getElementById('drawer-doctor').innerText = doctor;
    document.getElementById('drawer-bio').innerText = bio;
    document.getElementById('drawer-phone').innerText = phone;
    document.getElementById('drawer-email').innerText = email;
    document.getElementById('drawer-next-date').innerText = nextDate;
    
    const badge = document.getElementById('drawer-status-badge');
    badge.innerText = status;
    if (status.toLowerCase().includes('saldo')) {
      badge.className = 'px-2.5 py-0.5 rounded-full text-label-sm font-label-sm bg-status-pending-bg text-status-pending';
    } else if (status.toLowerCase().includes('plan')) {
      badge.className = 'px-2.5 py-0.5 rounded-full text-label-sm font-label-sm bg-status-active-bg text-status-active';
    } else {
      badge.className = 'px-2.5 py-0.5 rounded-full text-label-sm font-label-sm bg-status-confirmed-bg text-status-confirmed';
    }

    drawer.classList.remove('translate-x-full');
  }

  function closePreviewDrawer() {
    const drawer = document.getElementById('patient-drawer');
    drawer.classList.add('translate-x-full');
  }

  // Register Patient Modal Interaction
  const openModalBtn = document.getElementById('open-register-modal-btn');
  const closeModalBtn = document.getElementById('close-register-modal-btn');
  const cancelModalBtn = document.getElementById('cancel-register-modal-btn');
  const modalBackdrop = document.getElementById('patient-modal-backdrop');
  const registerForm = document.getElementById('new-patient-form');

  if(openModalBtn && modalBackdrop) {
    openModalBtn.addEventListener('click', () => {
      modalBackdrop.classList.remove('hidden');
    });
  }

  const hideModal = () => {
    if(modalBackdrop) modalBackdrop.classList.add('hidden');
  };

  if(closeModalBtn) closeModalBtn.addEventListener('click', hideModal);
  if(cancelModalBtn) cancelModalBtn.addEventListener('click', hideModal);

  if(registerForm) {
    registerForm.addEventListener('submit', (e) => {
      e.preventDefault();
      alert('Paciente registrado exitosamente en el consultorio.');
      hideModal();
    });
  }

  // Basic Filter Simulation
  const searchInput = document.getElementById('patient-search-input');
  if(searchInput) {
    searchInput.addEventListener('input', function(e) {
      const val = e.target.value.toLowerCase();
      const rows = document.querySelectorAll('tbody tr');
      rows.forEach(row => {
        const text = row.innerText.toLowerCase();
        row.style.display = text.includes(val) ? '' : 'none';
      });
    });
  }
