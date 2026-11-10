// ============================================================================
// GESTURES.JS — Pinch Gesture & Multi-View Transition Handler
// ============================================================================

class GestureController {
  constructor(app) {
    this.app = app;
    this.initialDistance = null;
    this.isPinching = false;
    this.threshold = 40; // minimum pixel delta to trigger view switch

    this.init();
  }

  init() {
    this.bindTouchGestures();
    this.bindMousePinchSimulator();
  }

  getDistance(touches) {
    const dx = touches[0].clientX - touches[1].clientX;
    const dy = touches[0].clientY - touches[1].clientY;
    return Math.sqrt(dx * dx + dy * dy);
  }

  bindTouchGestures() {
    window.addEventListener("touchstart", (e) => {
      if (e.touches.length === 2) {
        this.initialDistance = this.getDistance(e.touches);
        this.isPinching = true;
      }
    }, { passive: true });

    window.addEventListener("touchmove", (e) => {
      if (!this.isPinching || e.touches.length !== 2) return;

      const currentDistance = this.getDistance(e.touches);
      const delta = currentDistance - this.initialDistance;

      if (Math.abs(delta) > this.threshold) {
        if (delta < -this.threshold) {
          // Pinch In (Zooming Out) -> Switch from Magazine to Pinterest Grid or 3D Sphere
          this.handlePinchIn();
        } else if (delta > this.threshold) {
          // Pinch Out (Spreading Fingers / Zooming In) -> Switch to Magazine or Story
          this.handlePinchOut();
        }
        // Reset to prevent continuous rapid cycling
        this.isPinching = false;
      }
    }, { passive: true });

    window.addEventListener("touchend", () => {
      this.isPinching = false;
      this.initialDistance = null;
    });
  }

  bindMousePinchSimulator() {
    // For desktop testing: Ctrl + Mousewheel simulates pinch in / pinch out
    window.addEventListener("wheel", (e) => {
      if (e.ctrlKey) {
        e.preventDefault();
        if (e.deltaY > 0) {
          // Zoom out (pinch in)
          this.handlePinchIn();
        } else {
          // Zoom in (pinch out)
          this.handlePinchOut();
        }
      }
    }, { passive: false });
  }

  handlePinchIn() {
    const currentMode = this.app.currentMode;
    if (currentMode === "guardian") {
      this.app.switchView("pinterest");
      this.showGestureToast("🤏 Pinched In: Switched to Pinterest Masonry Grid!");
    } else if (currentMode === "pinterest") {
      this.app.switchView("sphere");
      this.showGestureToast("🌐 Pinched In: Entered 3D Spherical Room!");
    }
  }

  handlePinchOut() {
    const currentMode = this.app.currentMode;
    if (currentMode === "sphere") {
      this.app.switchView("pinterest");
      this.showGestureToast("🔍 Pinched Out: Switched to Pinterest Grid!");
    } else if (currentMode === "pinterest") {
      this.app.switchView("guardian");
      this.showGestureToast("📖 Pinched Out: Switched to Magazine Spread!");
    } else if (currentMode === "whatsapp") {
      this.app.switchView("guardian");
      this.showGestureToast("📰 Expanded: Switched to Guardian Magazine!");
    }
  }

  showGestureToast(msg) {
    let toast = document.getElementById("gestureToast");
    if (!toast) {
      toast = document.createElement("div");
      toast.id = "gestureToast";
      toast.style.cssText = `
        position: fixed;
        bottom: 80px;
        left: 50%;
        transform: translateX(-50%);
        background: rgba(0, 168, 132, 0.95);
        color: #0b141a;
        font-weight: 700;
        font-size: 0.85rem;
        padding: 0.6rem 1.2rem;
        border-radius: 30px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.5);
        z-index: 3000;
        transition: opacity 0.3s, transform 0.3s;
        pointer-events: none;
      `;
      document.body.appendChild(toast);
    }
    toast.textContent = msg;
    toast.style.opacity = "1";
    toast.style.transform = "translateX(-50%) translateY(0)";

    clearTimeout(this.toastTimeout);
    this.toastTimeout = setTimeout(() => {
      toast.style.opacity = "0";
      toast.style.transform = "translateX(-50%) translateY(10px)";
    }, 2200);
  }
}
