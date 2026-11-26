    // Simple micro-interactions for modal and filters
    const openBtn = document.getElementById('btn-nueva-cita');
    const modal = document.getElementById('modal-nueva-cita');
    const closeBtn = document.getElementById('modal-close-btn');
    const cancelBtn = document.getElementById('modal-cancel-btn');
    const submitBtn = document.getElementById('modal-submit-btn');
    const urgencyBtn = document.getElementById('quick-urgency-btn');

    function toggleModal(show) {
      if (show) {
        modal.classList.remove('hidden');
        modal.classList.add('flex');
      } else {
        modal.classList.add('hidden');
        modal.classList.remove('flex');
      }
    }

    if (openBtn) openBtn.addEventListener('click', () => toggleModal(true));
    if (closeBtn) closeBtn.addEventListener('click', () => toggleModal(false));
    if (cancelBtn) cancelBtn.addEventListener('click', () => toggleModal(false));
    if (submitBtn) submitBtn.addEventListener('click', () => {
      toggleModal(false);
      // Optional subtle feedback
    });

    if (urgencyBtn) {
      urgencyBtn.addEventListener('click', () => {
        urgencyBtn.classList.toggle('ring-2');
        urgencyBtn.classList.toggle('ring-status-cancelled');
      });
    }
  
