// ── Intersection Observer — section reveal (mirrors SC) ─────
const revealEls = document.querySelectorAll(".reveal");
const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.02, rootMargin: "0px 0px 100px 0px" },
);
revealEls.forEach((el) => observer.observe(el));

// ── Nav — subtle shadow on scroll (mirrors SC) ─────────────
const nav = document.getElementById("nav");
if (nav) {
  window.addEventListener("scroll", () => {
    if (window.scrollY > 10) {
      nav.style.boxShadow = "0 1px 0 rgba(13,31,60,0.4)";
    } else {
      nav.style.boxShadow = "none";
    }
  });
}

// ── Mobile hamburger menu ───────────────────────────────────
const navToggle = document.querySelector(".nav-toggle");
const mobileMenu = document.getElementById("mobile-menu");

if (navToggle && mobileMenu) {
  navToggle.addEventListener("click", () => {
    const isOpen = mobileMenu.classList.contains("active");
    mobileMenu.classList.toggle("active");
    navToggle.classList.toggle("active");
    navToggle.setAttribute("aria-expanded", !isOpen);
    mobileMenu.setAttribute("aria-hidden", isOpen);
    document.body.style.overflow = isOpen ? "" : "hidden";
  });

  // Close menu when a link is tapped
  mobileMenu.querySelectorAll(".mobile-menu-link").forEach((link) => {
    link.addEventListener("click", () => {
      mobileMenu.classList.remove("active");
      navToggle.classList.remove("active");
      navToggle.setAttribute("aria-expanded", "false");
      mobileMenu.setAttribute("aria-hidden", "true");
      document.body.style.overflow = "";
    });
  });
}

// ── Notification form submission ────────────────────────────
const notifyForm = document.getElementById("notify-form");

if (notifyForm) {
  notifyForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const followup = notifyForm.querySelector(".form-followup");
    const submitBtn = notifyForm.querySelector('button[type="submit"]');
    const originalText = submitBtn ? submitBtn.textContent : "";

    const email = notifyForm.elements.email.value.trim();
    if (!email) {
      if (followup) {
        followup.textContent = "Please enter your email address.";
        followup.className = "form-followup error";
      }
      return;
    }

    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.textContent = "Sending...";
    }

    try {
      const response = await fetch(notifyForm.action, {
        method: "POST",
        headers: { Accept: "application/json", "Content-Type": "application/json" },
        body: JSON.stringify({
          email: email,
          state: notifyForm.elements.state ? notifyForm.elements.state.value : "",
        }),
      });

      if (response.ok) {
        notifyForm.reset();
        if (followup) {
          followup.textContent = "You're on the list. We'll be in touch.";
          followup.className = "form-followup success";
        }
      } else {
        throw new Error("Submission failed");
      }
    } catch {
      if (followup) {
        followup.textContent = "Something went wrong. Please try again.";
        followup.className = "form-followup error";
      }
    } finally {
      if (submitBtn) {
        submitBtn.disabled = false;
        submitBtn.textContent = originalText;
      }
    }
  });
}
