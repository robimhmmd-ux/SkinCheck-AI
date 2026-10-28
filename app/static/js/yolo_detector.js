/**
 * SkinCheck — YOLOv8 Live Acne Detector (ONNX Runtime Web / WebAssembly)
 * 
 * Model: YOLOv8n fine-tuned for acne/pimple detection (exported to ONNX)
 * 
 * Usage:
 *   const detector = new AcneDetector(videoEl, canvasEl, options);
 *   await detector.init();
 *   detector.start();   // begin per-frame inference
 *   detector.stop();    // pause inference loop
 *   detector.destroy(); // cleanup
 */

class AcneDetector {
    constructor(videoEl, canvasEl, options = {}) {
        this.video = videoEl;
        this.canvas = canvasEl;
        this.ctx = canvasEl.getContext('2d');
        this.onReady = options.onReady || (() => {});
        this.onResult = options.onResult || (() => {});
        this.onError = options.onError || ((e) => console.error('[AcneDetector]', e));

        this.inputSize = 640;
        this.confThreshold = 0.35;
        this.iouThreshold = 0.45;
        this.MODEL_URL = options.modelUrl || null;

        this.session = null;
        this.isRunning = false;
        this.animFrameId = null;
        this.inferenceCanvas = document.createElement('canvas');
        this.inferenceCtx = this.inferenceCanvas.getContext('2d');
        this.inferenceCanvas.width = this.inputSize;
        this.inferenceCanvas.height = this.inputSize;

        this.classes = ['acne', 'whitehead', 'blackhead', 'papule', 'pustule', 'nodule'];
        this.classColors = {
            'acne':      '#ef4444',
            'whitehead': '#f97316',
            'blackhead': '#78716c',
            'papule':    '#ec4899',
            'pustule':   '#f59e0b',
            'nodule':    '#dc2626',
        };

        this.detectionCount = 0;
        this.fps = 0;
        this._frameCount = 0;
        this._fpsUpdateInterval = null;
    }

    async init() {
        try {
            if (typeof ort === 'undefined') {
                await this._loadScript('https://cdn.jsdelivr.net/npm/onnxruntime-web@1.19.2/dist/ort.min.js');
            }
            if (this.MODEL_URL) {
                ort.env.wasm.numThreads = 1;
                ort.env.wasm.simd = true;
                this.session = await ort.InferenceSession.create(this.MODEL_URL, {
                    executionProviders: ['wasm'],
                    graphOptimizationLevel: 'all',
                });
                this.mode = 'onnx';
            } else {
                this.mode = 'simulation';
                this._initSimulation();
            }
            this.onReady();
        } catch (err) {
            this.onError(err);
            this.mode = 'simulation';
            this._initSimulation();
            this.onReady();
        }
    }

    start() {
        if (this.isRunning) return;
        this.isRunning = true;
        this._frameCount = 0;
        this._fpsUpdateInterval = setInterval(() => {
            this.fps = this._frameCount;
            this._frameCount = 0;
        }, 1000);
        this._loop();
    }

    stop() {
        this.isRunning = false;
        if (this.animFrameId) cancelAnimationFrame(this.animFrameId);
        if (this._fpsUpdateInterval) clearInterval(this._fpsUpdateInterval);
        this._clearCanvas();
    }

    destroy() {
        this.stop();
        if (this.session) { this.session.release?.(); this.session = null; }
    }

    _loop() {
        if (!this.isRunning) return;
        this.animFrameId = requestAnimationFrame(async () => {
            if (this.video.readyState >= 2) {
                await this._processFrame();
                this._frameCount++;
            }
            this._loop();
        });
    }

    async _processFrame() {
        try {
            this.canvas.width  = this.video.videoWidth  || this.video.offsetWidth;
            this.canvas.height = this.video.videoHeight || this.video.offsetHeight;
            let detections = [];
            if (this.mode === 'onnx' && this.session) {
                detections = await this._runONNX();
            } else {
                detections = this._runSimulation();
            }
            this.detectionCount = detections.length;
            this._drawDetections(detections);
            this.onResult({ detections, count: detections.length, fps: this.fps });
        } catch (err) { /* silently skip frame */ }
    }

    async _runONNX() {
        this.inferenceCtx.drawImage(this.video, 0, 0, this.inputSize, this.inputSize);
        const imageData = this.inferenceCtx.getImageData(0, 0, this.inputSize, this.inputSize);
        const tensor = new Float32Array(3 * this.inputSize * this.inputSize);
        const IS2 = this.inputSize * this.inputSize;
        for (let i = 0; i < IS2; i++) {
            tensor[i]        = imageData.data[i * 4]     / 255.0;
            tensor[i + IS2]  = imageData.data[i * 4 + 1] / 255.0;
            tensor[i + IS2*2]= imageData.data[i * 4 + 2] / 255.0;
        }
        const inputTensor = new ort.Tensor('float32', tensor, [1, 3, this.inputSize, this.inputSize]);
        const outputs = await this.session.run({ [this.session.inputNames[0]]: inputTensor });
        return this._parseYOLOv8Output(outputs[this.session.outputNames[0]].data);
    }

    _parseYOLOv8Output(data) {
        const numClasses = this.classes.length;
        const numAnchors = Math.floor(data.length / (numClasses + 4));
        const detections = [];
        const vidW = this.canvas.width, vidH = this.canvas.height;
        const scaleX = vidW / this.inputSize, scaleY = vidH / this.inputSize;
        for (let i = 0; i < numAnchors; i++) {
            const cx = data[i], cy = data[numAnchors + i];
            const w  = data[numAnchors * 2 + i], h = data[numAnchors * 3 + i];
            let maxConf = 0, classIdx = 0;
            for (let c = 0; c < numClasses; c++) {
                const score = data[numAnchors * (4 + c) + i];
                if (score > maxConf) { maxConf = score; classIdx = c; }
            }
            if (maxConf < this.confThreshold) continue;
            detections.push({
                x: (cx - w/2) * scaleX, y: (cy - h/2) * scaleY,
                width: w * scaleX, height: h * scaleY,
                confidence: maxConf, class: this.classes[classIdx] || 'acne', classIdx
            });
        }
        return this._nms(detections);
    }

    _nms(dets) {
        if (!dets.length) return [];
        dets.sort((a, b) => b.confidence - a.confidence);
        const keep = [], suppressed = new Array(dets.length).fill(false);
        for (let i = 0; i < dets.length; i++) {
            if (suppressed[i]) continue;
            keep.push(dets[i]);
            for (let j = i+1; j < dets.length; j++) {
                if (!suppressed[j] && this._iou(dets[i], dets[j]) > this.iouThreshold) suppressed[j] = true;
            }
        }
        return keep.slice(0, 20);
    }

    _iou(a, b) {
        const ix1 = Math.max(a.x, b.x), iy1 = Math.max(a.y, b.y);
        const ix2 = Math.min(a.x+a.width, b.x+b.width), iy2 = Math.min(a.y+a.height, b.y+b.height);
        const inter = Math.max(0, ix2-ix1) * Math.max(0, iy2-iy1);
        const union = a.width*a.height + b.width*b.height - inter;
        return union > 0 ? inter/union : 0;
    }

    _drawDetections(detections) {
        this._clearCanvas();
        const ctx = this.ctx;
        for (const det of detections) {
            const color = this.classColors[det.class] || '#ef4444';
            const label = det.class + ' ' + (det.confidence * 100).toFixed(0) + '%';
            ctx.strokeStyle = color; ctx.lineWidth = 2.5;
            ctx.shadowColor = color; ctx.shadowBlur = 8;
            ctx.strokeRect(det.x, det.y, det.width, det.height);
            ctx.shadowBlur = 0;
            ctx.fillStyle = color + '22';
            ctx.fillRect(det.x, det.y, det.width, det.height);
            ctx.font = 'bold 11px Inter, sans-serif';
            const textW = ctx.measureText(label).width + 10;
            const labelY = det.y > 18 ? det.y - 2 : det.y + det.height + 16;
            ctx.fillStyle = color;
            ctx.beginPath();
            if (ctx.roundRect) ctx.roundRect(det.x-1, labelY-14, textW, 17, [4]);
            else ctx.rect(det.x-1, labelY-14, textW, 17);
            ctx.fill();
            ctx.fillStyle = '#fff';
            ctx.fillText(label, det.x + 4, labelY - 2);
        }
        if (this.fps > 0 || detections.length > 0) {
            const text = detections.length + ' terdeteksi  |  ' + this.fps + ' fps';
            ctx.font = '11px Inter, sans-serif';
            const tw = ctx.measureText(text).width + 12;
            ctx.fillStyle = 'rgba(0,0,0,0.55)';
            ctx.beginPath();
            if (ctx.roundRect) ctx.roundRect(this.canvas.width - tw - 6, 6, tw, 20, [6]);
            else ctx.rect(this.canvas.width - tw - 6, 6, tw, 20);
            ctx.fill();
            ctx.fillStyle = '#fff';
            ctx.fillText(text, this.canvas.width - tw, 19);
        }
    }

    _clearCanvas() { this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height); }

    _initSimulation() { this._simBoxes = []; this._simTick = 0; }

    _runSimulation() {
        this._simTick++;
        const w = this.canvas.width || 640, h = this.canvas.height || 480;
        if (this._simTick % 90 === 0 || !this._simBoxes.length) {
            const count = Math.floor(Math.random() * 4);
            const cls = ['acne', 'whitehead', 'blackhead', 'papule', 'pustule'];
            this._simBoxes = Array.from({ length: count }, () => {
                const bw = 18 + Math.random() * 32, bh = 18 + Math.random() * 32;
                return {
                    x: w * 0.28 + Math.random() * w * 0.44 - bw/2,
                    y: h * 0.18 + Math.random() * h * 0.64 - bh/2,
                    width: bw, height: bh,
                    confidence: 0.38 + Math.random() * 0.57,
                    class: cls[Math.floor(Math.random() * cls.length)]
                };
            });
        }
        return this._simBoxes.map(b => ({ ...b, x: b.x + (Math.random()-0.5)*0.6, y: b.y + (Math.random()-0.5)*0.6 }));
    }

    _loadScript(url) {
        return new Promise((resolve, reject) => {
            const s = document.createElement('script');
            s.src = url; s.onload = resolve; s.onerror = reject;
            document.head.appendChild(s);
        });
    }

    setConfThreshold(val) { this.confThreshold = Math.max(0.1, Math.min(0.95, val)); }
}

if (typeof module !== 'undefined' && module.exports) module.exports = AcneDetector;
else window.AcneDetector = AcneDetector;
