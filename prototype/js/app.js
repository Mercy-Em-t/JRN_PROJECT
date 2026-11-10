// ============================================================================
// APP.JS — Master Prototype Controller (Kikao360 Multimodal Experience)
// ============================================================================

class KikaoApp {
  constructor() {
    this.currentMode = "whatsapp";
    this.currentStory = STORIES[0];
    this.audioPlaying = false;
    this.audioSpeed = 1.0;

    this.init();
  }

  init() {
    this.renderWhatsAppFeed();
    this.renderGuardianArticle(this.currentStory);
    this.renderLeaderboard();
    this.renderPinterestGrid();
    this.renderTikTokFeed();
    
    // Initialize 3D Sphere & Gestures
    this.sphereRoom = new SphericalRoom("sphereRoom", "hudCoords");
    this.gestureCtrl = new GestureController(this);

    this.bindDockNavigation();
    this.bindGuardianInteractions();
    this.bindAudioPlayer();
    this.bindModals();
  }

  // ==========================================================================
  // VIEW SWITCHING ENGINE
  // ==========================================================================
  switchView(mode) {
    if (this.currentMode === mode) return;
    this.currentMode = mode;

    // Update body theme class
    document.body.className = `theme-dark mode-${mode}`;

    // Update Dock Buttons
    document.querySelectorAll(".mode-btn").forEach((btn) => {
      btn.classList.toggle("active", btn.getAttribute("data-mode") === mode);
    });

    // Update View Panels
    document.querySelectorAll(".view-panel").forEach((panel) => {
      panel.classList.remove("active");
    });

    const targetPanel = document.getElementById(`view${mode.charAt(0).toUpperCase() + mode.slice(1)}`);
    if (targetPanel) {
      targetPanel.classList.add("active");
      // Scroll to top of panel
      targetPanel.scrollTop = 0;
    }

    // Auto-pause or trigger TikTok videos
    const ttVideos = document.querySelectorAll(".tt-video-slide video");
    if (mode === "tiktok") {
      const firstVid = document.querySelector(".tt-video-slide.active video") || ttVideos[0];
      if (firstVid) firstVid.play().catch(() => {});
    } else {
      ttVideos.forEach(v => v.pause());
    }
  }

  bindDockNavigation() {
    document.querySelectorAll(".mode-btn").forEach((btn) => {
      btn.addEventListener("click", () => {
        const mode = btn.getAttribute("data-mode");
        this.switchView(mode);
      });
    });

    // Gesture Help Button
    const helpBtn = document.getElementById("gestureHelpBtn");
    if (helpBtn) {
      helpBtn.addEventListener("click", () => {
        alert("✨ Multimodal Navigation Gestures:\n\n• Pinch IN (two fingers together): Zooms out from Magazine to Pinterest Grid or 3D Sphere.\n• Pinch OUT (spread fingers): Zooms in to the Editorial Magazine.\n• Inside 3D Sphere: Click & drag to rotate 360°, scroll to zoom, click cards to open.\n• Ctrl + Mouse Wheel (Desktop): Simulates pinch-in and pinch-out!");
      });
    }
  }

  // ==========================================================================
  // 1. WHATSAPP CHANNEL FEED
  // ==========================================================================
  renderWhatsAppFeed() {
    const list = document.getElementById("waFeedList");
    if (!list || typeof STORIES === "undefined") return;

    list.innerHTML = "";
    STORIES.forEach((story) => {
      const card = document.createElement("article");
      card.className = "wa-post-card";
      card.innerHTML = `
        <div class="wa-og-box" data-story-id="${story.id}">
          <div class="wa-og-media">
            <img src="${story.poster}" alt="${story.title}" loading="lazy">
            <div class="wa-video-play-overlay">▶</div>
          </div>
          <div class="wa-og-meta-content">
            <div class="wa-og-domain">${story.ogData.siteName}</div>
            <h3 class="wa-og-headline">${story.ogData.headline}</h3>
            <p class="wa-og-desc">${story.ogData.description}</p>
            <div class="wa-og-cta-row">
              <span class="wa-open-pill">Read &amp; Watch Magazine ❯</span>
              <span class="wa-views-badge">${story.stats.views} views</span>
            </div>
          </div>
        </div>
        <div class="wa-post-footer">
          <div class="wa-reactions-pill">${story.stats.reactions}</div>
          <div class="wa-post-timestamp">${story.ogData.channelTime}</div>
        </div>
      `;

      // Tap OG card to open directly into Guardian Magazine
      card.querySelector(".wa-og-box").addEventListener("click", () => {
        this.loadStory(story.id);
        this.switchView("guardian");
      });

      list.appendChild(card);
    });
  }

  // ==========================================================================
  // 2. THE GUARDIAN-STYLE MAGAZINE
  // ==========================================================================
  loadStory(storyId) {
    const story = STORIES.find(s => s.id === storyId);
    if (story) {
      this.currentStory = story;
      this.renderGuardianArticle(story);
      // Also update persistent bottom player title
      const nprTitle = document.getElementById("nprHeadline");
      if (nprTitle) nprTitle.textContent = `${story.title} (Audio Brief)`;
    }
  }

  renderGuardianArticle(story) {
    const setElem = (id, text) => {
      const el = document.getElementById(id);
      if (el) el.textContent = text;
    };

    setElem("articleEyebrow", story.category);
    setElem("articleBadge", story.badge);
    setElem("articleAuthor", story.author);
    setElem("articleDate", story.date);
    setElem("articleHeadline", story.title);
    setElem("articleSubdeck", story.subdeck);
    setElem("articleBulletLink", story.bulletLink);
    setElem("articleLead", story.leadParagraph);
    setElem("articleQuote", story.quote);
    setElem("articleQuoteAuthor", `— ${story.quoteAuthor}`);
    setElem("articleSecondary", story.secondaryParagraph);
    setElem("articleVideoDuration", story.videoDuration);

    // Update video source & poster
    const video = document.getElementById("gmMainVideo");
    if (video) {
      video.poster = story.poster;
      video.src = story.videoSrc;
      video.load();
    }

    // Update Topic Tags
    const tagsContainer = document.getElementById("articleTopicTags");
    if (tagsContainer) {
      tagsContainer.innerHTML = story.tags
        .map(tag => `<span class="pill-tag">${tag}</span>`)
        .join("");
    }
  }

  bindGuardianInteractions() {
    // Mega-Menu Drawer Toggle
    const menuBtn = document.getElementById("gmMenuToggle");
    const drawer = document.getElementById("gmMegamenu");
    if (menuBtn && drawer) {
      menuBtn.addEventListener("click", () => {
        drawer.classList.toggle("open");
        const isOpen = drawer.classList.contains("open");
        menuBtn.innerHTML = isOpen ? "✕" : "☰";
        menuBtn.style.background = isOpen ? "#c70000" : "#ffe500";
        menuBtn.style.color = isOpen ? "#ffffff" : "#121212";
      });
    }

    // Pillar navigation tabs
    document.querySelectorAll(".gm-pillar-btn").forEach((btn) => {
      btn.addEventListener("click", () => {
        document.querySelectorAll(".gm-pillar-btn").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        const pillar = btn.getAttribute("data-pillar");
        const matchedStory = STORIES.find(s => s.pillar === pillar);
        if (matchedStory) {
          this.loadStory(matchedStory.id);
        }
      });
    });

    // Format switcher inside article (Read / Watch / Listen)
    const btnRead = document.getElementById("tabFormatRead");
    const btnWatch = document.getElementById("tabFormatWatch");
    const btnListen = document.getElementById("tabFormatListen");
    const video = document.getElementById("gmMainVideo");

    if (btnRead && btnWatch && btnListen) {
      btnRead.addEventListener("click", () => {
        [btnRead, btnWatch, btnListen].forEach(b => b.classList.remove("active"));
        btnRead.classList.add("active");
        document.getElementById("articleProse")?.scrollIntoView({ behavior: "smooth" });
      });

      btnWatch.addEventListener("click", () => {
        [btnRead, btnWatch, btnListen].forEach(b => b.classList.remove("active"));
        btnWatch.classList.add("active");
        if (video) {
          video.scrollIntoView({ behavior: "smooth", block: "center" });
          video.play().catch(() => {});
        }
      });

      btnListen.addEventListener("click", () => {
        [btnRead, btnWatch, btnListen].forEach(b => b.classList.remove("active"));
        btnListen.classList.add("active");
        this.toggleAudioPlayer(true);
      });
    }
  }

  // Most-Viewed Leaderboard
  renderLeaderboard() {
    const list = document.getElementById("gmLeaderboardList");
    if (!list || typeof MOST_VIEWED === "undefined") return;

    list.innerHTML = "";
    MOST_VIEWED.slice(0, 5).forEach((item) => {
      const li = document.createElement("li");
      li.className = "gm-leaderboard-item";
      li.innerHTML = `
        <span class="lb-rank">${item.rank}</span>
        <div class="lb-info">
          <span class="lb-cat">${item.category}</span>
          <h4 class="lb-title">${item.title}</h4>
        </div>
      `;
      li.addEventListener("click", () => {
        const found = STORIES.find(s => s.category.includes(item.category) || s.title.includes(item.title));
        if (found) this.loadStory(found.id);
      });
      list.appendChild(li);
    });
  }

  // ==========================================================================
  // 3. PINTEREST MASONRY GRID
  // ==========================================================================
  renderPinterestGrid() {
    const canvas = document.getElementById("pinMasonryCanvas");
    if (!canvas || typeof STORIES === "undefined") return;

    canvas.innerHTML = "";
    STORIES.forEach((story) => {
      const card = document.createElement("div");
      card.className = "pin-card";
      card.setAttribute("data-category", story.pillar);
      card.innerHTML = `
        <div class="pin-media-wrapper">
          <img src="${story.poster}" alt="${story.title}" loading="lazy">
          <span class="pin-badge-float">${story.badge}</span>
          <span class="pin-video-runtime">▶ ${story.videoDuration}</span>
        </div>
        <div class="pin-card-body">
          <div class="pin-card-cat">${story.category}</div>
          <h3 class="pin-card-title">${story.title}</h3>
          <p class="pin-card-desc">${story.leadParagraph}</p>
          <div class="pin-card-footer">
            <span>${story.stats.views} views</span>
            <button class="pin-save-btn">Save</button>
          </div>
        </div>
      `;

      card.addEventListener("click", (e) => {
        if (e.target.classList.contains("pin-save-btn")) {
          e.stopPropagation();
          e.target.textContent = "Saved ✓";
          e.target.style.background = "#2ea043";
          return;
        }
        this.loadStory(story.id);
        this.switchView("guardian");
      });

      canvas.appendChild(card);
    });

    // Filter pills
    document.querySelectorAll(".pin-pill").forEach((pill) => {
      pill.addEventListener("click", () => {
        document.querySelectorAll(".pin-pill").forEach(p => p.classList.remove("active"));
        pill.classList.add("active");
        const filter = pill.getAttribute("data-filter");
        document.querySelectorAll(".pin-card").forEach((card) => {
          if (filter === "all" || card.getAttribute("data-category") === filter) {
            card.style.display = "block";
          } else {
            card.style.display = "none";
          }
        });
      });
    });
  }

  // ==========================================================================
  // 4. TIKTOK / REELS VERTICAL VIDEO FEED
  // ==========================================================================
  renderTikTokFeed() {
    const container = document.getElementById("ttFeedContainer");
    if (!container || typeof STORIES === "undefined") return;

    container.innerHTML = "";
    STORIES.forEach((story, idx) => {
      const slide = document.createElement("div");
      slide.className = `tt-video-slide ${idx === 0 ? "active" : ""}`;
      slide.setAttribute("data-slide-index", idx);
      slide.innerHTML = `
        <video loop playsinline poster="${story.poster}">
          <source src="${story.videoSrc}" type="video/mp4">
        </video>
        
        <!-- Right Action Rail -->
        <div class="tt-action-rail">
          <button class="tt-action-btn like-btn">
            <div class="tt-icon-circle">❤️</div>
            <span class="tt-count">24.5K</span>
          </button>
          <button class="tt-action-btn">
            <div class="tt-icon-circle">💬</div>
            <span class="tt-count">${story.stats.comments}</span>
          </button>
          <button class="tt-action-btn">
            <div class="tt-icon-circle">🔖</div>
            <span class="tt-count">1.4K</span>
          </button>
          <button class="tt-action-btn">
            <div class="tt-icon-circle">↗️</div>
            <span class="tt-count">Share</span>
          </button>
          <div class="tt-sound-disc"></div>
        </div>

        <!-- Bottom Story Meta -->
        <div class="tt-bottom-overlay">
          <div class="tt-creator-row">
            <div class="tt-avatar">K360</div>
            <span class="tt-handle">@kikao360</span>
            <span class="tt-category-pill">${story.category}</span>
          </div>
          <p class="tt-caption">${story.title}</p>
          <div class="tt-sound-track">🎵 Original Sound - Kikao360 Nairobi Field Unit</div>
        </div>
      `;

      // Tap slide to play/pause
      const video = slide.querySelector("video");
      slide.addEventListener("click", (e) => {
        if (e.target.closest(".tt-action-rail")) return;
        if (video.paused) {
          video.play().catch(() => {});
        } else {
          video.pause();
        }
      });

      // Like button interaction
      const likeBtn = slide.querySelector(".like-btn");
      likeBtn.addEventListener("click", () => {
        likeBtn.classList.toggle("liked");
      });

      container.appendChild(slide);
    });

    // Vertical Nav Buttons
    const prevBtn = document.getElementById("ttPrevBtn");
    const nextBtn = document.getElementById("ttNextBtn");
    if (prevBtn && nextBtn) {
      prevBtn.addEventListener("click", () => {
        container.scrollBy({ top: -container.clientHeight, behavior: "smooth" });
      });
      nextBtn.addEventListener("click", () => {
        container.scrollBy({ top: container.clientHeight, behavior: "smooth" });
      });
    }

    // Intersection observer for video playback on scroll
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        const vid = entry.target.querySelector("video");
        if (entry.isIntersecting && this.currentMode === "tiktok") {
          vid?.play().catch(() => {});
          entry.target.classList.add("active");
        } else {
          vid?.pause();
          entry.target.classList.remove("active");
        }
      });
    }, { threshold: 0.6 });

    document.querySelectorAll(".tt-video-slide").forEach(s => observer.observe(s));
  }

  // ==========================================================================
  // 5. PERSISTENT FLOATING NPR AUDIO PLAYER DOCK
  // ==========================================================================
  bindAudioPlayer() {
    const playBtn = document.getElementById("nprPlayBtn");
    const drawerBtn = document.getElementById("nprDrawerBtn");
    const drawerCloseBtn = document.getElementById("nprDrawerCloseBtn");
    const drawer = document.getElementById("nprExpandedDrawer");
    const speedBtn = document.getElementById("nprSpeedBtn");

    if (playBtn) {
      playBtn.addEventListener("click", () => this.toggleAudioPlayer());
    }

    if (drawerBtn && drawer) {
      drawerBtn.addEventListener("click", () => drawer.classList.toggle("open"));
    }

    if (drawerCloseBtn && drawer) {
      drawerCloseBtn.addEventListener("click", () => drawer.classList.remove("open"));
    }

    if (speedBtn) {
      speedBtn.addEventListener("click", () => {
        const speeds = [1.0, 1.25, 1.5, 2.0];
        const nextIdx = (speeds.indexOf(this.audioSpeed) + 1) % speeds.length;
        this.audioSpeed = speeds[nextIdx];
        speedBtn.textContent = `${this.audioSpeed.toFixed(1)}x`;
      });
    }
  }

  toggleAudioPlayer(forcePlay = false) {
    const playBtn = document.getElementById("nprPlayBtn");
    const wave = document.getElementById("nprWaveBars");
    this.audioPlaying = forcePlay ? true : !this.audioPlaying;

    if (playBtn) {
      playBtn.innerHTML = this.audioPlaying ? "❚❚" : "▶";
      playBtn.classList.toggle("playing", this.audioPlaying);
    }
    if (wave) {
      wave.classList.toggle("active", this.audioPlaying);
    }
  }

  // ==========================================================================
  // 6. MODALS (M-PESA & INVESTOR PITCH DECK)
  // ==========================================================================
  bindModals() {
    // M-Pesa Modal
    const openMpesa = document.getElementById("openMpesaModalBtn");
    const triggerPrompt = document.getElementById("triggerMpesaPromptBtn");
    const closeMpesa = document.getElementById("closeMpesaModalBtn");
    const mpesaModal = document.getElementById("mpesaModal");
    const sendPromptBtn = document.getElementById("sendMpesaPromptBtn");
    const statusMsg = document.getElementById("mpesaStatusMsg");

    const openMpesaHandler = () => {
      if (mpesaModal) mpesaModal.classList.add("open");
      if (statusMsg) statusMsg.style.display = "none";
    };

    openMpesa?.addEventListener("click", openMpesaHandler);
    triggerPrompt?.addEventListener("click", openMpesaHandler);
    closeMpesa?.addEventListener("click", () => mpesaModal?.classList.remove("open"));

    // Amount presets
    document.querySelectorAll(".amount-btn").forEach((btn) => {
      btn.addEventListener("click", () => {
        document.querySelectorAll(".amount-btn").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
      });
    });

    // Send M-Pesa STK Push Prompt
    sendPromptBtn?.addEventListener("click", () => {
      const activeAmount = document.querySelector(".amount-btn.active")?.getAttribute("data-amount") || "100";
      const phone = document.getElementById("mpesaPhone")?.value || "715 478 466";

      if (statusMsg) {
        statusMsg.style.display = "block";
        statusMsg.innerHTML = `
          ⏳ <strong>Sending Daraja STK Push...</strong><br>
          Requesting KES ${activeAmount} from +254 ${phone}.
        `;

        setTimeout(() => {
          statusMsg.innerHTML = `
            ✅ <strong>STK Push Prompt Delivered!</strong><br>
            Please check your phone and enter your M-Pesa PIN to complete the transaction. Asante sana for powering Kikao360!
          `;
        }, 1500);
      }
    });

    // Pitch Deck Modal (USIU-Africa Simulation)
    const openPitch = document.getElementById("openPitchDeckBtn");
    const closePitch = document.getElementById("closePitchDeckBtn");
    const pitchModal = document.getElementById("pitchDeckModal");
    const prevSlide = document.getElementById("prevSlideBtn");
    const nextSlide = document.getElementById("nextSlideBtn");

    let currentSlide = 1;
    const maxSlides = 3;

    const showSlide = (idx) => {
      currentSlide = idx;
      document.querySelectorAll(".pitch-slide").forEach((s) => {
        s.classList.toggle("active", s.getAttribute("data-slide") == idx);
      });
      document.querySelectorAll(".slide-dot").forEach((d) => {
        d.classList.toggle("active", d.getAttribute("data-target") == idx);
      });
    };

    openPitch?.addEventListener("click", () => pitchModal?.classList.add("open"));
    closePitch?.addEventListener("click", () => pitchModal?.classList.remove("open"));

    prevSlide?.addEventListener("click", () => {
      if (currentSlide > 1) showSlide(currentSlide - 1);
    });

    nextSlide?.addEventListener("click", () => {
      if (currentSlide < maxSlides) showSlide(currentSlide + 1);
    });

    document.querySelectorAll(".slide-dot").forEach((d) => {
      d.addEventListener("click", () => {
        const target = parseInt(d.getAttribute("data-target"), 10);
        showSlide(target);
      });
    });
  }
}

// Global helpers so buttons always work directly
window.switchView = function(mode) {
  if (!window.app) initKikao();
  window.app?.switchView(mode);
};

window.openMpesaModal = function() {
  const mpesaModal = document.getElementById("mpesaModal");
  if (mpesaModal) mpesaModal.classList.add("open");
};

window.closeMpesaModal = function() {
  const mpesaModal = document.getElementById("mpesaModal");
  if (mpesaModal) mpesaModal.classList.remove("open");
};

window.openPitchDeck = function() {
  const pitchModal = document.getElementById("pitchDeckModal");
  if (pitchModal) pitchModal.classList.add("open");
};

window.closePitchDeck = function() {
  const pitchModal = document.getElementById("pitchDeckModal");
  if (pitchModal) pitchModal.classList.remove("open");
};

// Safe initialization whether DOM is loading or already loaded
function initKikao() {
  if (!window.app) {
    try {
      window.app = new KikaoApp();
      console.log("Kikao360 App initialized successfully!");
    } catch (e) {
      console.error("Error initializing KikaoApp:", e);
    }
  }
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initKikao);
} else {
  initKikao();
}

