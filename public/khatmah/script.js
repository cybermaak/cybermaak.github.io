(() => {
  const strings = {
    en: {
      title: 'Khatmah — Quran reading and khatma tracking',
      description: 'Read the Quran and follow your khatmas at your own pace with Khatmah for iPhone.',
      siteNav: 'Site', brand: 'Khatmah', allApps: 'All apps',
      switchLabel: 'Switch to Arabic', switchText: 'العربية', storeAction: 'Download Khatmah on the App Store',
      socialAlt: 'Khatmah app icon and name beside an iPhone Quran reading screen and App Store download badge',
      iconAlt: 'Khatmah app icon', badgeAlt: 'Download on the App Store', availability: 'Free for iPhone',
      heroLead: 'Quran reading and khatma tracking, at your own pace.',
      heroSupport: 'Read from a familiar Mushaf, keep your place, and continue whenever you’re ready.',
      heroMedia: 'Actual Khatmah reading and tracking screens',
      pageAlt: 'Khatmah Page Mode showing the familiar Uthmanic Mushaf layout',
      pageCaption: 'Read from the familiar page',
      trackingAlt: 'Khatmah screen showing an active khatma and saved progress',
      trackingCaption: 'Keep your khatma together', viewFull: 'View full size',
      readTitle: 'Read your way.',
      readBody: 'Page Mode preserves the familiar Mushaf. Focus Scroll gives the line you’re reading a clear place to follow.',
      readDetail: 'Move between reading views without losing your place.',
      focusAlt: 'Khatmah Focus Scroll reading screen', focusCaption: 'Focus Scroll',
      progressCaption: 'Khatmah progress', bookmarksAlt: 'Khatmah bookmarks screen showing saved reading places',
      bookmarksCaption: 'Saved places', khatmaTitle: 'Continue your khatma.',
      khatmaBody: 'Track the khatmas you’re reading and return to a saved place when you come back.',
      khatmaDetail: 'Your reading and progress stay on your iPhone.',
      comfortTitle: 'Comfortable in more places.',
      comfortBody: 'Choose a dark reading theme, or turn your iPhone sideways for a wider Focus view.',
      darkAlt: 'Khatmah’s dark theme showing the Mushaf page', darkCaption: 'Dark theme',
      landscapeAlt: 'Khatmah Landscape Focus in the light theme', landscapeCaption: 'Landscape Focus · Light',
      landscapeDarkAlt: 'Khatmah Landscape Focus in the dark theme', landscapeDarkCaption: 'Landscape Focus · Dark',
      sharingTitle: 'Share Quran verses as an image.',
      sharingBody: 'Prepare a clear image of the verses you’re reading, with the surah name and verse numbers.',
      sharingAlt: 'In-app preview of a rendered ayah image, with Quran text and a 2:255 reference',
      sharingCaption: 'Preview of the image', essentials: 'App essentials',
      offline: 'Read offline', noAccount: 'No account', noAds: 'No ads',
      closingTitle: 'Keep reading with Khatmah.',
      closingBody: 'Familiar reading, a reliable place to return to, and khatma progress at your own pace.',
      byline: 'Khatmah by Mohammed Kamel',
      trademark: 'Apple, the Apple logo, and iPhone are trademarks of Apple Inc., registered in the U.S. and other countries. App Store is a service mark of Apple Inc., registered in the U.S. and other countries.'
    },
    ar: {
      title: 'ختمة — قراءة القرآن ومتابعة الختمات',
      description: 'اقرأ القرآن وتابع ختماتك بالطريقة التي تناسبك مع تطبيق ختمة على iPhone.',
      siteNav: 'تصفح الموقع', brand: 'ختمة', allApps: 'جميع التطبيقات',
      switchLabel: 'التبديل إلى الإنجليزية', switchText: 'English', storeAction: 'تنزيل تطبيق ختمة من \u2068App Store\u2069',
      socialAlt: 'أيقونة ختمة بجانب شاشة قراءة القرآن على iPhone وشارة التنزيل من App Store',
      iconAlt: 'أيقونة تطبيق ختمة', badgeAlt: 'تنزيل من \u2068App Store\u2069', availability: 'متاح مجانًا على \u2068iPhone\u2069',
      heroLead: 'اقرأ القرآن وتابع ختماتك بالطريقة التي تناسبك.',
      heroSupport: 'مصحف مألوف، وموضع محفوظ، وختمة تتابعها حين تشاء.',
      heroMedia: 'صور حقيقية للقراءة ومتابعة الختمات في تطبيق ختمة',
      pageAlt: 'صفحة المصحف في تطبيق ختمة بتخطيط المصحف العثماني المألوف',
      pageCaption: 'صفحة المصحف المألوفة',
      trackingAlt: 'شاشة الختمات في تطبيق ختمة تعرض ختمة نشطة وتقدم القراءة',
      trackingCaption: 'تابع ختمتك', viewFull: 'عرض بالحجم الكامل',
      readTitle: 'اقرأ كما تحب.',
      readBody: 'اختر «صفحة المصحف» بتخطيطها المألوف، أو اقرأ سطرًا بسطر مع «تركيز السطر».',
      readDetail: 'بدّل بين طريقتَي القراءة وموضعك محفوظ.',
      focusAlt: 'شاشة القراءة في تركيز السطر في تطبيق ختمة', focusCaption: 'تركيز السطر',
      progressCaption: 'تقدم الختمة', bookmarksAlt: 'شاشة المواضع المحفوظة في تطبيق ختمة',
      bookmarksCaption: 'مواضعك المحفوظة', khatmaTitle: 'واصل ختمتك.',
      khatmaBody: 'تابع ختماتك، وارجع إلى موضع حفظته كلما عدت إلى القراءة.',
      khatmaDetail: 'موضع قراءتك وتقدّم ختمتك محفوظان على \u2068iPhone\u2069.',
      comfortTitle: 'قراءة مريحة في كل وضع.',
      comfortBody: 'اختر المظهر الداكن، أو أدر \u2068iPhone\u2069 أفقيًا لقراءة أوسع في تركيز السطر.',
      darkAlt: 'صفحة المصحف في تطبيق ختمة بالمظهر الداكن', darkCaption: 'المظهر الداكن',
      landscapeAlt: 'تركيز السطر أفقيًا في تطبيق ختمة بالمظهر الفاتح', landscapeCaption: 'تركيز السطر أفقيًا · فاتح',
      landscapeDarkAlt: 'تركيز السطر أفقيًا في تطبيق ختمة بالمظهر الداكن', landscapeDarkCaption: 'تركيز السطر أفقيًا · داكن',
      sharingTitle: 'شارك آيات القرآن في صورة.',
      sharingBody: 'جهّز صورة واضحة للآيات التي تقرؤها، يظهر فيها اسم السورة وأرقام الآيات.',
      sharingAlt: 'معاينة داخل التطبيق لصورة آية من القرآن مع المرجع ٢:٢٥٥',
      sharingCaption: 'معاينة الصورة', essentials: 'مزايا أساسية',
      offline: 'اقرأ دون اتصال', noAccount: 'دون حساب', noAds: 'دون إعلانات',
      closingTitle: 'واصل القراءة مع ختمة.',
      closingBody: 'مصحف مألوف، ومواضع محفوظة، وتقدم ختماتك بين يديك.',
      byline: 'تطبيق ختمة من محمد كامل',
      trademark: '\u2068Apple\u2069 وشعار \u2068Apple\u2069 و\u2068iPhone\u2069 علامات تجارية لشركة \u2068Apple Inc.\u2069، مسجّلة في الولايات المتحدة وبلدان أخرى. \u2068App Store\u2069 علامة خدمة لشركة \u2068Apple Inc.\u2069، مسجّلة في الولايات المتحدة وبلدان أخرى.'
    }
  };
  const media = {
    en: { badge: 'app-store-badge.svg', page: 'page.png', tracking: 'tracking.png', bookmarks: 'bookmarks.png', focus: 'focus-en.png', dark: 'dark.png', landscape: 'landscape.png', landscapeDark: 'landscape-dark-en.png', sharing: 'sharing-rendered-preview.png' },
    ar: { badge: 'app-store-badge-ar.svg', page: 'page-ar.png', tracking: 'tracking-ar.png', bookmarks: 'bookmarks-ar.png', focus: 'focus-ar.png', dark: 'dark-ar.png', landscape: 'landscape-ar.png', landscapeDark: 'landscape-dark-ar.png', sharing: 'sharing-rendered-preview-ar.png' }
  };
  const switcher = document.querySelector('.language-switch');
  const description = document.querySelector('meta[name="description"]');
  let language = 'ar';

  function setLanguage(next, preservePosition = false) {
    let hashTarget = null;
    if (preservePosition && location.hash) {
      try { hashTarget = document.getElementById(decodeURIComponent(location.hash.slice(1))); }
      catch (_) { /* An invalid fragment must not disable the language switch. */ }
    }
    const anchor = hashTarget || (preservePosition ? [...document.querySelectorAll('main section')].filter(section => section.getBoundingClientRect().top < innerHeight / 2).at(-1) : null);
    const anchorTop = hashTarget ? (parseFloat(getComputedStyle(hashTarget).scrollMarginTop) || 0) : anchor?.getBoundingClientRect().top;
    const t = strings[next];
    document.documentElement.lang = next;
    document.documentElement.dir = next === 'ar' ? 'rtl' : 'ltr';
    document.title = t.title;
    description.content = t.description;
    // Static HTML remains Arabic for crawlers that do not execute JavaScript.
    const socialImage = `https://cybermaak.dev/khatmah/assets/social-card-${next}-v1.png`;
    document.querySelectorAll('meta[property="og:image"], meta[name="twitter:image"]').forEach(meta => { meta.content = socialImage; });
    document.querySelectorAll('meta[property="og:image:alt"], meta[name="twitter:image:alt"]').forEach(meta => { meta.content = t.socialAlt; });
    document.querySelector('meta[property="og:locale"]').content = next === 'ar' ? 'ar_SA' : 'en_US';
    document.querySelector('meta[property="og:locale:alternate"]').content = next === 'ar' ? 'en_US' : 'ar_SA';
    document.querySelectorAll('meta[property="og:title"], meta[name="twitter:title"]').forEach(meta => { meta.content = t.title; });
    document.querySelectorAll('meta[property="og:description"], meta[name="twitter:description"]').forEach(meta => { meta.content = t.description; });
    document.querySelectorAll('[data-l10n]').forEach(element => { element.textContent = t[element.dataset.l10n]; });
    document.querySelectorAll('[data-l10n-alt]').forEach(element => { element.alt = t[element.dataset.l10nAlt]; });
    document.querySelectorAll('[data-l10n-aria]').forEach(element => { element.setAttribute('aria-label', t[element.dataset.l10nAria]); });
    document.querySelectorAll('[data-media]').forEach(element => { element.src = 'assets/' + media[next][element.dataset.media]; });
    document.querySelectorAll('[data-full-media]').forEach(element => { element.href = 'assets/' + media[next][element.dataset.fullMedia]; });
    switcher.textContent = t.switchText;
    switcher.setAttribute('aria-label', t.switchLabel);
    switcher.lang = next === 'ar' ? 'en' : 'ar';
    switcher.dir = next === 'ar' ? 'ltr' : 'rtl';
    language = next;
    if (anchor) {
      const hadFocus = document.activeElement === switcher;
      if (hadFocus) switcher.blur();
      const restore = () => scrollBy(0, anchor.getBoundingClientRect().top - anchorTop);
      restore();
      if (hadFocus) switcher.focus({ preventScroll: true });
    }
  }

  let saved;
  try { saved = localStorage.getItem('khatmah-language'); } catch (_) { /* Private browsing can deny storage. */ }
  const requested = new URLSearchParams(location.search).get('lang');
  const isLanguage = value => value === 'ar' || value === 'en';
  const initial = isLanguage(requested) ? requested : (isLanguage(saved) ? saved : 'ar');
  setLanguage(initial);
  switcher.hidden = false;
  switcher.addEventListener('click', () => {
    const next = language === 'en' ? 'ar' : 'en';
    setLanguage(next, true);
    // Keep an explicitly shared language consistent after switching or reloading.
    const url = new URL(location.href);
    url.searchParams.set('lang', next);
    try { history.replaceState(null, '', url); } catch (_) { /* Local file previews may deny history changes. */ }
    try { localStorage.setItem('khatmah-language', next); } catch (_) { /* The switch still works. */ }
  });
})();
