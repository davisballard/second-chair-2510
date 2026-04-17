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

  // Hero proof panel bars — animate on load (hero is always above fold)
  const heroBars = document.querySelectorAll('.hep-fill');
  setTimeout(() => {
    heroBars.forEach((bar, i) => {
      setTimeout(() => { bar.style.width = bar.dataset.w; }, i * 280);
    });
  }, 700);

  // Intelligence dashboard bars — animate on scroll into view
  const intelBars = document.querySelectorAll('.intel-bar');
  if (intelBars.length) {
    // Store target widths and set initial width to 0
    intelBars.forEach((bar) => {
      const targetWidth = bar.style.width;
      bar.dataset.targetWidth = targetWidth;
      bar.style.width = '0%';
    });

    // Observe the dashboard container
    const intelDashboard = document.querySelector('.intel-dashboard');
    if (intelDashboard) {
      const barObserver = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              // Animate bars with stagger
              intelBars.forEach((bar, i) => {
                setTimeout(() => {
                  bar.style.width = bar.dataset.targetWidth;
                }, i * 180);
              });
              barObserver.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.3, rootMargin: '0px' }
      );
      barObserver.observe(intelDashboard);
    }
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

  // Animate any bar chart with data-width or data-w when scrolled into view
  function animateBarsOnScroll(containerSelector, fillSelector, dataKey) {
    const containers = document.querySelectorAll(containerSelector);
    containers.forEach(container => {
      const fills = container.querySelectorAll(fillSelector);
      const obs = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            fills.forEach((fill, i) => {
              const target = fill.dataset[dataKey];
              if (target) setTimeout(() => { fill.style.width = target; }, i * 200);
            });
            obs.unobserve(entry.target);
          }
        });
      }, { threshold: 0.35 });
      obs.observe(container);
    });
  }

  animateBarsOnScroll('#cpsc-chart',     '.bar-fill',       'width');
  animateBarsOnScroll('#proof-cpl-chart', '.proof-cpl-fill', 'w');

  // Compliance badges — stamp animation on scroll into view
  const complianceBadges = document.querySelectorAll('.engine-stat-number');
  if (complianceBadges.length) {
    const statsContainers = document.querySelectorAll('.engine-stats');
    
    statsContainers.forEach((container) => {
      const badges = container.querySelectorAll('.engine-stat-number');
      
      const badgeObserver = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              badges.forEach((badge, i) => {
                setTimeout(() => {
                  badge.classList.add('stamped');
                }, i * 100);
              });
              badgeObserver.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.4, rootMargin: '0px' }
      );
      
      badgeObserver.observe(container);
    });
  }

  // Nav — subtle shadow on scroll
  const nav = document.getElementById('nav');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 10) {
      nav.style.boxShadow = '0 1px 0 rgba(73,10,10,0.4)';
    } else {
      nav.style.boxShadow = 'none';
    }
  });