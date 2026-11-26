  (function() {
    const passwordInput = document.getElementById('password');
    const togglePasswordBtn = document.getElementById('toggle-password');
    const passwordIcon = document.getElementById('password-icon');
    const usernameInput = document.getElementById('username');
    const roleButtons = document.querySelectorAll('.role-btn');
    const loginForm = document.getElementById('login-form');
    const submitBtn = document.getElementById('submit-btn');

    if (togglePasswordBtn && passwordInput && passwordIcon) {
      togglePasswordBtn.addEventListener('click', function() {
        const isPassword = passwordInput.getAttribute('type') === 'password';
        passwordInput.setAttribute('type', isPassword ? 'text' : 'password');
        passwordIcon.textContent = isPassword ? 'visibility_off' : 'visibility';
      });
    }

    roleButtons.forEach(btn => {
      btn.addEventListener('click', function() {
        roleButtons.forEach(b => {
          b.classList.remove('bg-bg-main', 'text-primary', 'shadow-sm');
          b.classList.add('text-secondary');
        });
        this.classList.add('bg-bg-main', 'text-primary', 'shadow-sm');
        this.classList.remove('text-secondary');

        const defaultEmail = this.getAttribute('data-email');
        if (defaultEmail && usernameInput) {
          usernameInput.value = defaultEmail;
          usernameInput.focus();
        }
      });
    });

    window.handleLogin = function() {
      if (!submitBtn) return;
      const originalText = submitBtn.innerHTML;
      submitBtn.disabled = true;
      submitBtn.innerHTML = `
        <span class="inline-block animate-spin material-symbols-outlined text-[18px]">progress_activity</span>
        <span>Autenticando credenciales...</span>
      `;
      setTimeout(() => {
        submitBtn.innerHTML = `
          <span class="material-symbols-outlined text-[18px]">done</span>
          <span>Acceso Autorizado</span>
        `;
        submitBtn.classList.remove('bg-primary');
        submitBtn.classList.add('bg-status-confirmed');
      }, 1000);
    };
  })();
