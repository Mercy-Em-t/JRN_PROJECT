// ============================================================================
// SPHERE.JS — Inside-the-Sphere 3D Spatial Room Controller
// ============================================================================

class SphericalRoom {
  constructor(roomElementId, hudElementId) {
    this.room = document.getElementById(roomElementId);
    this.hudCoords = document.getElementById(hudElementId);
    this.viewport = document.getElementById("sphereViewport");

    this.rotX = -10; // Pitch angle (tilt up/down)
    this.rotY = 0;   // Yaw angle (turn 360 left/right)
    this.zoom = 1.0;
    this.updateRadius();

    this.isDragging = false;
    this.startX = 0;
    this.startY = 0;
    this.dragDist = 0;
    this.targetRotX = -4;
    this.targetRotY = 0;
    this.angleStep = 60;

    this.autoRotate = true;
    this.autoRotateSpeed = 0.18;

    this.init();
  }

  updateRadius() {
    const isMobile = window.innerWidth < 640;
    this.radius = isMobile ? 290 : 480;
  }

  init() {
    this.populateCards();
    this.bindEvents();
    this.animate();

    // Re-adjust sphere radius on screen resize / orientation change
    window.addEventListener("resize", () => {
      const oldRadius = this.radius;
      this.updateRadius();
      if (oldRadius !== this.radius) {
        this.populateCards();
      }
    });
  }

  populateCards() {
    if (!this.room || typeof STORIES === "undefined") return;

    this.room.innerHTML = "";
    const pillars = 6;
    const tiers = [-1, 0, 1]; // Top, Middle, Bottom cards per pillar
    const tierSpacing = window.innerWidth < 640 ? 330 : 390;
    const angleStep = 360 / pillars;
    this.angleStep = angleStep;

    for (let p = 0; p < pillars; p++) {
      const theta = p * angleStep;

      tiers.forEach((tier, tIdx) => {
        const story = STORIES[(p + tIdx * 2) % STORIES.length];
        const yOffset = tier * tierSpacing;

        const card = document.createElement("div");
        card.className = "spatial-card";
        card.setAttribute("data-story-id", story.id);

        // Vertical pillar of cards running up and down around each 60° column
        card.style.transform = `rotateY(${theta}deg) translateY(${yOffset}px) translateZ(${this.radius}px)`;

        card.innerHTML = `
          <div class="spatial-card-media">
            <img src="${story.poster}" alt="${story.title}" loading="lazy">
            <span class="spatial-card-badge">${story.badge}</span>
          </div>
          <div class="spatial-card-body">
            <span class="spatial-card-cat">${story.category}</span>
            <h4 class="spatial-card-title">${story.title}</h4>
            <p class="spatial-card-desc">${story.leadParagraph}</p>
            <div class="spatial-card-cta">
              <span>Read / Watch Story</span>
              <span>❯</span>
            </div>
          </div>
        `;

        // Only open story on clean tap/click (ignore drags)
        card.addEventListener("click", () => {
          if (this.dragDist > 8) return;
          if (window.app) {
            window.app.loadStory(story.id);
            window.app.switchView("guardian");
          }
        });

        this.room.appendChild(card);
      });
    }
  }

  bindEvents() {
    if (!this.viewport) return;

    // Mouse Dragging
    this.viewport.addEventListener("mousedown", (e) => {
      this.isDragging = true;
      this.dragDist = 0;
      this.startX = e.clientX;
      this.startY = e.clientY;
      this.room.classList.add("grabbing");
      this.autoRotate = false;
      this.updateAutoRotateBtn();
    });

    window.addEventListener("mousemove", (e) => {
      if (!this.isDragging) return;
      const deltaX = e.clientX - this.startX;
      const deltaY = e.clientY - this.startY;
      this.dragDist += Math.hypot(deltaX, deltaY);

      this.targetRotY += deltaX * 0.35;
      this.targetRotX -= deltaY * 0.35;

      // Clamp vertical pitch between -55 and 55 degrees
      this.targetRotX = Math.max(-55, Math.min(55, this.targetRotX));

      this.startX = e.clientX;
      this.startY = e.clientY;
    });

    window.addEventListener("mouseup", () => {
      if (this.isDragging) {
        this.isDragging = false;
        this.room.classList.remove("grabbing");
      }
    });

    // Touch Dragging on Mobile
    this.viewport.addEventListener("touchstart", (e) => {
      if (e.touches.length === 1) {
        this.isDragging = true;
        this.dragDist = 0;
        this.startX = e.touches[0].clientX;
        this.startY = e.touches[0].clientY;
        this.autoRotate = false;
        this.updateAutoRotateBtn();
      }
    }, { passive: true });

    this.viewport.addEventListener("touchmove", (e) => {
      if (!this.isDragging || e.touches.length !== 1) return;
      const deltaX = e.touches[0].clientX - this.startX;
      const deltaY = e.touches[0].clientY - this.startY;
      this.dragDist += Math.hypot(deltaX, deltaY);

      this.targetRotY += deltaX * 0.45;
      this.targetRotX -= deltaY * 0.45;
      this.targetRotX = Math.max(-55, Math.min(55, this.targetRotX));

      this.startX = e.touches[0].clientX;
      this.startY = e.touches[0].clientY;
    }, { passive: true });

    this.viewport.addEventListener("touchend", () => {
      this.isDragging = false;
    });

    // Zoom via Mouse Wheel inside the Sphere
    this.viewport.addEventListener("wheel", (e) => {
      e.preventDefault();
      this.zoom -= e.deltaY * 0.001;
      this.zoom = Math.max(0.65, Math.min(1.45, this.zoom));
    }, { passive: false });

    // HUD Button: Reset View
    const resetBtn = document.getElementById("sphereResetBtn");
    if (resetBtn) {
      resetBtn.addEventListener("click", () => {
        this.targetRotX = -10;
        this.targetRotY = 0;
        this.zoom = 1.0;
      });
    }

    // HUD Button: Toggle Auto-Rotate
    const autoBtn = document.getElementById("sphereAutoRotateBtn");
    if (autoBtn) {
      autoBtn.addEventListener("click", () => {
        this.autoRotate = !this.autoRotate;
        this.updateAutoRotateBtn();
      });
    }
  }

  updateAutoRotateBtn() {
    const autoBtn = document.getElementById("sphereAutoRotateBtn");
    if (autoBtn) {
      autoBtn.textContent = `Auto-Orbit: ${this.autoRotate ? 'ON' : 'OFF'}`;
      autoBtn.style.color = this.autoRotate ? '#00a884' : '#ffffff';
    }
  }

  animate() {
    requestAnimationFrame(() => this.animate());

    if (this.autoRotate && !this.isDragging) {
      this.targetRotY += this.autoRotateSpeed;
    }

    // Smooth inertia interpolation
    this.rotX += (this.targetRotX - this.rotX) * 0.12;
    this.rotY += (this.targetRotY - this.rotY) * 0.12;

    if (this.room) {
      // Push carousel back by -radius so front-most card sits cleanly at Z=0
      this.room.style.transform = `translateZ(-${this.radius}px) scale(${this.zoom}) rotateX(${this.rotX}deg) rotateY(${this.rotY}deg)`;
    }

    if (this.hudCoords) {
      this.hudCoords.textContent = `RotX: ${Math.round(this.rotX)}° | RotY: ${Math.round(this.rotY % 360)}° | Zoom: ${this.zoom.toFixed(2)}x`;
    }
  }
}
