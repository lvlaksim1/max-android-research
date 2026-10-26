# Public MAX Bridge JS interface audit\n\nSource: https://st.max.ru/js/max-web-app.js\nSize of examined JS: 26507 characters. Short contextual snippets only.\n\nThis is inspection of the public MAX Bridge library, not a signed mini-app URL.\n\n## \`PrivateWebViewHandler\`: 0 occurrences\n\n## \`WebViewHandler\`: 2 occurrences\n\n\`\`\`text\nsendEvent;
	constructor(e) {
		this.messageCallback = e, this.isIframe() ? (this.sendEvent = this.sendOverIframe, this.initializeIframeTransport()) : typeof window < "u" && window.WebViewHandler ? (this.webviewBridge = window.WebViewHandler, this.sendEvent = this.sendOverWebView) : this.sendEvent = this.sendFallback;
	}
	initializeIframeTransport() {
		window.addEventListener("message", async (e) => {
			if (!(!v.tes\n\`\`\`\n\n\`\`\`text\nlback = e, this.isIframe() ? (this.sendEvent = this.sendOverIframe, this.initializeIframeTransport()) : typeof window < "u" && window.WebViewHandler ? (this.webviewBridge = window.WebViewHandler, this.sendEvent = this.sendOverWebView) : this.sendEvent = this.sendFallback;
	}
	initializeIframeTransport() {
		window.addEventListener("message", async (e) => {
			if (!(!v.test(e.origin) || typeof e.data != "string")) try\n\`\`\`\n\n## \`WebAppVerifyMobileId\`: 0 occurrences\n\n## \`receiveEvent\`: 3 occurrences\n\n\`\`\`text\nt = {}) => {
		let n = this.initDataUnsafe?.query_id;
		return e({
			...t || {},
			queryId: n
		});
	};
	constructor() {
		this.transport = new y(async (e, t) => {
			await this.receiveEvent(e, t);
		}), this.requestController = new b((e, t) => {
			this.transport.sendEvent(e, t);
		}), this.BackButton = new n({
			postBackButtonEvent: (e) => this.postEvent("WebAppSetupBackButton", { isVisible: e }),
			onClick: (e\n\`\`\`\n\n\`\`\`text\ns.requestController.createRequest("WebAppPermissionsOpenSystemSettings", e, { timeout: l }))
		});
	}
	postEvent(e, t = {}, n) {
		this.transport.sendEvent(e, t), n?.();
	}
	async receiveEvent(e, t) {
		i(t) ? this.requestController.handleResponse(e, t) : this.eventHandlers.get(e)?.forEach((n) => {
			try {
				n(t);
			} catch (t) {
				console.error(`Ошибка в обработке события "${e}":`, t);
			}
		});
	}
	async sen\n\`\`\`\n\n\`\`\`text\n(e)?.forEach((n) => {
			try {
				n(t);
			} catch (t) {
				console.error(`Ошибка в обработке события "${e}":`, t);
			}
		});
	}
	async sendEvent(e, t = "{}") {
		try {
			this.receiveEvent(e, JSON.parse(t));
		} catch (e) {
			console.warn(e);
		}
	}
	onEvent(e, t) {
		let n = this.eventHandlers.get(e);
		return n || (n = /* @__PURE__ */ new Set(), this.eventHandlers.set(e, n)), n.add(t), () => {
			this.offEvent\n\`\`\`\n\n## \`receive_event\`: 0 occurrences\n\n## \`postEvent\`: 9 occurrences\n\n\`\`\`text\nбщения: ", e);
			}
		});
	}
	sendOverIframe(e, t) {
		window.parent.postMessage(JSON.stringify({
			type: e,
			...t
		}), "*");
	}
	sendOverWebView(e, t) {
		this.webviewBridge?.postEvent(e, JSON.stringify(t));
	}
	sendFallback(e) {
		console.warn("[WebApp] Событие не отправлено - транспорт недоступен:", e);
	}
}, b = class {
	pendingRequests = /* @__PURE__ */ new Map();
	sendEvent;
	constructor(e) {
		this.sendEve\n\`\`\`\n\n\`\`\`text\nit this.receiveEvent(e, t);
		}), this.requestController = new b((e, t) => {
			this.transport.sendEvent(e, t);
		}), this.BackButton = new n({
			postBackButtonEvent: (e) => this.postEvent("WebAppSetupBackButton", { isVisible: e }),
			onClick: (e) => this.onEvent("WebAppBackButtonPressed", e),
			offClick: (e) => this.offEvent("WebAppBackButtonPressed", e)
		}), this.initDataManager = new r(), this.SecureStorage = \n\`\`\`\n\n\`\`\`text\nngs", e, { timeout: l })),
			openSystemSettings: this.withQueryId((e) => this.requestController.createRequest("WebAppPermissionsOpenSystemSettings", e, { timeout: l }))
		});
	}
	postEvent(e, t = {}, n) {
		this.transport.sendEvent(e, t), n?.();
	}
	async receiveEvent(e, t) {
		i(t) ? this.requestController.handleResponse(e, t) : this.eventHandlers.get(e)?.forEach((n) => {
			try {
				n(t);
			} catch (t) {
				con\n\`\`\`\n\n\`\`\`text\n { maxBrightness: !0 });
	}
	restoreScreenBrightness() {
		return this.requestController.createRequest("WebAppChangeScreenBrightness", { maxBrightness: !1 });
	}
	close() {
		this.postEvent("WebAppClose", {}, () => {
			console.log("Приложение закрыто");
		});
	}
	ready() {
		this.postEvent("WebAppReady", {}, () => {
			console.log("WebApp готово к работе");
		});
	}
	requestContact() {
		return this.requestControlle\n\`\`\`\n\n\`\`\`text\n("WebAppChangeScreenBrightness", { maxBrightness: !1 });
	}
	close() {
		this.postEvent("WebAppClose", {}, () => {
			console.log("Приложение закрыто");
		});
	}
	ready() {
		this.postEvent("WebAppReady", {}, () => {
			console.log("WebApp готово к работе");
		});
	}
	requestContact() {
		return this.requestController.createRequest("WebAppRequestPhone", {}, { timeout: l });
	}
	enableClosingConfirmation() {
		this.po\n\`\`\`\n\n\`\`\`text\np готово к работе");
		});
	}
	requestContact() {
		return this.requestController.createRequest("WebAppRequestPhone", {}, { timeout: l });
	}
	enableClosingConfirmation() {
		this.postEvent("WebAppSetupClosingBehavior", { needConfirmation: !0 });
	}
	disableClosingConfirmation() {
		this.postEvent("WebAppSetupClosingBehavior", { needConfirmation: !1 });
	}
	openLink(e) {
		this.postEvent("WebAppOpenLink", { url: e })\n\`\`\`\n\n\`\`\`text\ntPhone", {}, { timeout: l });
	}
	enableClosingConfirmation() {
		this.postEvent("WebAppSetupClosingBehavior", { needConfirmation: !0 });
	}
	disableClosingConfirmation() {
		this.postEvent("WebAppSetupClosingBehavior", { needConfirmation: !1 });
	}
	openLink(e) {
		this.postEvent("WebAppOpenLink", { url: e });
	}
	openMaxLink(e) {
		this.postEvent("WebAppOpenMaxLink", { url: e });
	}
	getViewportSize() {
		return th\n\`\`\`\n\n\`\`\`text\npClosingBehavior", { needConfirmation: !0 });
	}
	disableClosingConfirmation() {
		this.postEvent("WebAppSetupClosingBehavior", { needConfirmation: !1 });
	}
	openLink(e) {
		this.postEvent("WebAppOpenLink", { url: e });
	}
	openMaxLink(e) {
		this.postEvent("WebAppOpenMaxLink", { url: e });
	}
	getViewportSize() {
		return this.requestController.createRequest("WebAppGetViewportSize");
	}
	downloadFile(e, t) {
		retu\n\`\`\`\n\n## \`onEvent\`: 8 occurrences\n\n\`\`\`text\nKey({ key: e });
	}
	removeItem(e) {
		return this.saveKey({
			key: e,
			value: null
		});
	}
	clear() {
		return this.clearKeys();
	}
}, n = class {
	visible = !1;
	postBackButtonEvent;
	onClick;
	offClick;
	get isVisible() {
		return this.visible;
	}
	constructor({ postBackButtonEvent: e, onClick: t, offClick: n }) {
		this.postBackButtonEvent = e, this.onClick = t, this.offClick = n;
	}
	show() {
		this.visible \n\`\`\`\n\n\`\`\`text\n() {
		return this.clearKeys();
	}
}, n = class {
	visible = !1;
	postBackButtonEvent;
	onClick;
	offClick;
	get isVisible() {
		return this.visible;
	}
	constructor({ postBackButtonEvent: e, onClick: t, offClick: n }) {
		this.postBackButtonEvent = e, this.onClick = t, this.offClick = n;
	}
	show() {
		this.visible = !0, this.postBackButtonEvent(!0);
	}
	hide() {
		this.visible = !1, this.postBackButtonEvent(!1);
	}\n\`\`\`\n\n\`\`\`text\n !1;
	postBackButtonEvent;
	onClick;
	offClick;
	get isVisible() {
		return this.visible;
	}
	constructor({ postBackButtonEvent: e, onClick: t, offClick: n }) {
		this.postBackButtonEvent = e, this.onClick = t, this.offClick = n;
	}
	show() {
		this.visible = !0, this.postBackButtonEvent(!0);
	}
	hide() {
		this.visible = !1, this.postBackButtonEvent(!1);
	}
}, r = class e {
	static WEB_APP_DATA_KEY = "WebAppData";
	\n\`\`\`\n\n\`\`\`text\nctor({ postBackButtonEvent: e, onClick: t, offClick: n }) {
		this.postBackButtonEvent = e, this.onClick = t, this.offClick = n;
	}
	show() {
		this.visible = !0, this.postBackButtonEvent(!0);
	}
	hide() {
		this.visible = !1, this.postBackButtonEvent(!1);
	}
}, r = class e {
	static WEB_APP_DATA_KEY = "WebAppData";
	static WEB_APP_PLATFORM_KEY = "WebAppPlatform";
	static WEB_APP_VERSION_KEY = "WebAppVersion";
	stati\n\`\`\`\n\n\`\`\`text\nis.postBackButtonEvent = e, this.onClick = t, this.offClick = n;
	}
	show() {
		this.visible = !0, this.postBackButtonEvent(!0);
	}
	hide() {
		this.visible = !1, this.postBackButtonEvent(!1);
	}
}, r = class e {
	static WEB_APP_DATA_KEY = "WebAppData";
	static WEB_APP_PLATFORM_KEY = "WebAppPlatform";
	static WEB_APP_VERSION_KEY = "WebAppVersion";
	static WEB_APP_DEVICE_NAME = "WebAppDeviceName";
	static VALID_PLATFO\n\`\`\`\n\n\`\`\`text\nnc (e, t) => {
			await this.receiveEvent(e, t);
		}), this.requestController = new b((e, t) => {
			this.transport.sendEvent(e, t);
		}), this.BackButton = new n({
			postBackButtonEvent: (e) => this.postEvent("WebAppSetupBackButton", { isVisible: e }),
			onClick: (e) => this.onEvent("WebAppBackButtonPressed", e),
			offClick: (e) => this.offEvent("WebAppBackButtonPressed", e)
		}), this.initDataManager = new r(), \n\`\`\`\n\n\`\`\`text\n		this.transport.sendEvent(e, t);
		}), this.BackButton = new n({
			postBackButtonEvent: (e) => this.postEvent("WebAppSetupBackButton", { isVisible: e }),
			onClick: (e) => this.onEvent("WebAppBackButtonPressed", e),
			offClick: (e) => this.offEvent("WebAppBackButtonPressed", e)
		}), this.initDataManager = new r(), this.SecureStorage = new t({
			saveKey: this.withQueryId((e) => this.requestController.createReque\n\`\`\`\n\n\`\`\`text\n`Ошибка в обработке события "${e}":`, t);
			}
		});
	}
	async sendEvent(e, t = "{}") {
		try {
			this.receiveEvent(e, JSON.parse(t));
		} catch (e) {
			console.warn(e);
		}
	}
	onEvent(e, t) {
		let n = this.eventHandlers.get(e);
		return n || (n = /* @__PURE__ */ new Set(), this.eventHandlers.set(e, n)), n.add(t), () => {
			this.offEvent(e, t);
		};
	}
	offEvent(e, t) {
		let n = this.eventHandlers.get(e);
		n &\n\`\`\`\n\n## \`no_cellular\`: 0 occurrences\n\n## \`WebAppRequestPhone\`: 1 occurrences\n\n\`\`\`text\n});
	}
	ready() {
		this.postEvent("WebAppReady", {}, () => {
			console.log("WebApp готово к работе");
		});
	}
	requestContact() {
		return this.requestController.createRequest("WebAppRequestPhone", {}, { timeout: l });
	}
	enableClosingConfirmation() {
		this.postEvent("WebAppSetupClosingBehavior", { needConfirmation: !0 });
	}
	disableClosingConfirmation() {
		this.postEvent("WebAppSetupClosingBehavior", { needCo\n\`\`\`\n\n## \`web_app_request_phone\`: 0 occurrences\n