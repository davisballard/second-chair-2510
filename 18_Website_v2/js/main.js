  // Intersection Observer — section reveal
  const revealEls = document.querySelectorAll('.reveal');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });
  revealEls.forEach(el => observer.observe(el));

  // Hero proof panel bars — animate on load (if present)
  const heroBars = document.querySelectorAll('.hep-fill');
  if (heroBars.length) {
    setTimeout(() => {
      heroBars.forEach((bar, i) => {
        setTimeout(() => { bar.style.width = bar.dataset.w; }, i * 280);
      });
    }, 700);
  }

  // Page rails — stop above the scrolling logo ticker
  function positionPageRails() {
    const rails = document.getElementById('page-rails');
    const nav = document.getElementById('nav');
    const ticker = document.querySelector('.hero-ticker-wrap');
    if (!rails || !nav || !ticker) return;

    const navBottom = nav.getBoundingClientRect().bottom + window.scrollY;
    const tickerTop = ticker.getBoundingClientRect().top + window.scrollY;
    rails.style.top = `${Math.round(navBottom)}px`;
    rails.style.height = `${Math.max(0, Math.round(tickerTop - navBottom))}px`;
  }

  positionPageRails();
  window.addEventListener('resize', positionPageRails);

  // Nav — subtle shadow on scroll
  const nav = document.getElementById('nav');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 10) {
      nav.style.boxShadow = '0 1px 0 rgba(73,10,10,0.4)';
    } else {
      nav.style.boxShadow = 'none';
    }
  });

  // ── Mobile hamburger menu ──────────────────────────────────
  const navToggle = document.querySelector('.nav-toggle');
  const mobileMenu = document.getElementById('mobile-menu');

  if (navToggle && mobileMenu) {
    navToggle.addEventListener('click', () => {
      const isOpen = mobileMenu.classList.contains('active');
      mobileMenu.classList.toggle('active');
      navToggle.classList.toggle('active');
      navToggle.setAttribute('aria-expanded', !isOpen);
      mobileMenu.setAttribute('aria-hidden', isOpen);
      document.body.style.overflow = isOpen ? '' : 'hidden';
    });

    // Close menu when a link is tapped
    mobileMenu.querySelectorAll('.mobile-menu-link').forEach(link => {
      link.addEventListener('click', () => {
        mobileMenu.classList.remove('active');
        navToggle.classList.remove('active');
        navToggle.setAttribute('aria-expanded', 'false');
        mobileMenu.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
      });
    });
  }

  // ── Video Lightbox ──────────────────────────────────────────
  // Play button on SC ad cards opens a 9:16 video lightbox.
  // Videos are loaded from data-video-src on the .ad-card--playable.
  // When no video src is set (empty string), clicking shows the
  // lightbox with a placeholder — ready for real video URLs.

  const lightbox = document.getElementById('video-lightbox');
  const lightboxVideo = document.getElementById('lightbox-video');
  const lightboxClose = document.querySelector('.video-lightbox-close');
  const lightboxBackdrop = document.querySelector('.video-lightbox-backdrop');

  function openLightbox(videoSrc) {
    if (!lightbox) return;
    if (videoSrc) {
      lightboxVideo.querySelector('source').src = videoSrc;
      lightboxVideo.load();
      lightboxVideo.play();
    }
    lightbox.classList.add('active');
    lightbox.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    if (!lightbox) return;
    lightbox.classList.remove('active');
    lightbox.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
    if (lightboxVideo) {
      lightboxVideo.pause();
      lightboxVideo.currentTime = 0;
    }
  }

  // Play buttons on SC ad cards
  document.querySelectorAll('.ad-card--playable .ad-play-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const card = btn.closest('.ad-card--playable');
      const src = card ? card.dataset.videoSrc : '';
      openLightbox(src);
    });
  });

  // Close lightbox
  if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
  if (lightboxBackdrop) lightboxBackdrop.addEventListener('click', closeLightbox);

  // Escape key closes lightbox
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && lightbox && lightbox.classList.contains('active')) {
      closeLightbox();
    }
  });

  // ── Apply Modal ──────────────────────────────────────────────
  const applyModal = document.getElementById('apply-modal');
  const applyBackdrop = applyModal ? applyModal.querySelector('.apply-modal-backdrop') : null;
  const applyClose = applyModal ? applyModal.querySelector('.apply-modal-close') : null;

  function openApplyModal(e) {
    if (e) e.preventDefault();
    if (!applyModal) return;
    applyModal.classList.add('is-open');
    applyModal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    // Close mobile menu if open
    if (mobileMenu && mobileMenu.classList.contains('active')) {
      mobileMenu.classList.remove('active');
      navToggle.classList.remove('active');
      navToggle.setAttribute('aria-expanded', 'false');
      mobileMenu.setAttribute('aria-hidden', 'true');
    }
  }

  function closeApplyModal() {
    if (!applyModal) return;
    applyModal.classList.remove('is-open');
    applyModal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }

  document.querySelectorAll('[data-open-modal="apply-modal"]').forEach(btn => {
    btn.addEventListener('click', openApplyModal);
  });
  if (applyBackdrop) applyBackdrop.addEventListener('click', closeApplyModal);
  if (applyClose) applyClose.addEventListener('click', closeApplyModal);
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && applyModal && applyModal.classList.contains('is-open')) {
      closeApplyModal();
    }
  });
