"""Builds the aip-sa.com home page in Arabic (public/index.html) and English (public/en/index.html).

    python tools/build_home.py

The copy for both languages is below; edit it here and run the script again, then commit both
pages. The design came from the owner on 2026-11-19 (design/new-design-2026-11-19.html, a packed
design-tool export); this is the same page as plain HTML and CSS (public/assets/css/home.css),
with no script needed to read it. Left out on purpose: a "live status" panel and a server-rack
readout that showed nothing real, results percentages with no source, "99% accuracy", a
scrolling ticker and glow effects. The company is called only "AIP" in both languages.
"""

from __future__ import annotations

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "public"
SITE = "https://aip-sa.com"
WHATSAPP = "https://wa.me/966556330039"
EMAIL = "info@aip-sa.com"
MAP = "https://maps.app.goo.gl/6YbUTbP8iQ181jJt6"

ICON = {
    "arrow": "M5 12h14M13 6l6 6-6 6",
    "out": "M7 17 17 7M8 7h9v9",
    "plus": "M12 5v14M5 12h14",
    "menu": "M4 7h16M4 12h16M4 17h10",
    "whatsapp": "M3 21l1.65-4.8A9 9 0 1 1 7.8 19.35zM9.2 8.2c0 3.6 3 6.6 6.6 6.6l1-1.6-2.1-1-1 .9a4 4 0 0 1-2.4-2.4l.9-1-1-2.1z",
    "mail": "M4 4h16a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2zM22 6l-10 7L2 6",
    "pin": "M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0zM12 13a3 3 0 1 0 0-6 3 3 0 0 0 0 6z",
    "nedaa": "M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z",
    "waqeen": "M2 12C2 6.5 6.5 2 12 2a10 10 0 0 1 8 4M5 19.5C5.5 18 6 15 6 12a6 6 0 0 1 .34-2M17.29 21.02c.12-.6.43-2.3.5-3.02M12 10a2 2 0 0 0-2 2c0 1.02-.1 2.51-.26 4M8.65 22c.21-.66.45-1.32.57-2M14 13.12c0 2.38 0 6.38-1 8.88M9 6.8a6 6 0 0 1 9 5.2c0 .47 0 1.17-.02 2",
    "nawa": "M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8zM14 2v6h6M16 13H8M16 17H8M10 9H8",
    "waseel": "M2 13a2 2 0 0 0 2-2V7a2 2 0 0 1 4 0v13a2 2 0 0 0 4 0V4a2 2 0 0 1 4 0v13a2 2 0 0 0 4 0v-4a2 2 0 0 1 2-2",
    "fath": "M12 8V4H8M4 8h16a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-8a2 2 0 0 1 2-2zM2 14h2M20 14h2M15 13v2M9 13v2",
    "linkedin": "M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6zM2 9h4v12H2zM4 6a2 2 0 1 0 0-4 2 2 0 0 0 0 4z",
    "x": "M4 4l7.2 9.6L4 20h2l6.1-5.2L16 20h4l-7.5-10L19.5 4h-2l-5.7 4.9L8 4z",
    "tiktok": "M9 12a4 4 0 1 0 4 4V4a5 5 0 0 0 5 5",
}

SOCIAL = [
    ("LinkedIn", "https://www.linkedin.com/company/saudiaip/", "linkedin"),
    ("X", "https://x.com/saudi_aip", "x"),
    ("TikTok", "https://www.tiktok.com/@saudi_aip", "tiktok"),
]

PRODUCTS = [  # key, Arabic name, English name, link (None: ask for a demo by email)
    ("nedaa", "نداء", "Nedaa", "https://nedaa.aip-sa.com"),
    ("waqeen", "وقين", "Waqeen", None),
    ("nawa", "نوى", "Nawa", None),
    ("waseel", "وسيل", "Waseel", None),
    ("fath", "فذ", "Fath", None),
]

COPY = {
    "ar": {
        "title": "AIP | من الخادم إلى الذكاء",
        "description": "AIP مجموعة تقنية سعودية تصمّم وتبني وتشغّل مراكز البيانات والسحابة والمنصات المؤسسية والذكاء الاصطناعي.",
        "skip": "تخطَّ إلى المحتوى",
        "menu": "القائمة",
        "nav": [("المنظومة", "#stack"), ("مراكز البيانات", "#dc"), ("المنصات", "#platforms"), ("القطاعات", "#sectors"), ("الشراكة", "#partner")],
        "other_lang": ("English", "/en/", "en"),
        "start": "ابدأ مشروعك",
        "kicker": "AIP · الرياض، المملكة العربية السعودية",
        "h1": ("من الخادم", "إلى الذكاء."),
        "lead": "AIP مجموعة تقنية سعودية تصمّم وتبني وتشغّل كل طبقة تحتاجها منشأتك: مراكز البيانات، والسحابة، والمنصات المؤسسية، والذكاء الاصطناعي. شريك واحد من الأساس إلى القمة.",
        "explore": "استكشف المنظومة",
        "talk": "تحدّث مع فريقنا",
        "figure": "طبقات منظومة AIP الأربع",
        "tiers": ["الذكاء الاصطناعي", "المنصات المؤسسية", "السحابة والاستضافة", "مراكز البيانات"],
        "about_ey": "من نحن",
        "about_h": ("التقنية الحقيقية لا تُرى،", "بل يظهر أثرها."),
        "about_p": "يظهر أثرها في عميل يتلقى الرد خلال ثوانٍ، وفي بيانات محمية، وفي فريق يتفرغ لما يصنع الفرق. هذا ما نبنيه في AIP: بنية تعمل بهدوء، ونتائج واضحة.",
        "values": [
            ("الناس", "التقنية في خدمة الإنسان، لا العكس."),
            ("التقنية", "نبني بأحدث ما توصّل إليه العالم."),
            ("الأفكار", "كل حل يبدأ بالسؤال الصحيح."),
            ("الأثر", "نقيس نجاحنا بنتائج عملائنا."),
        ],
        "stack_ey": "المنظومة",
        "stack_h": "أربع طبقات، وشريك واحد.",
        "stack_p": "بدلًا من التعامل مع أربع جهات، تغطي AIP الطبقات كلها وتربط بينها. افتح أي طبقة لعرض تفاصيلها.",
        "layers": [
            ("الذكاء الاصطناعي", "وكلاء ينجزون المهام، ومنصات تفهم اللغة العربية نصًا وصوتًا وصورة.",
             ["وكلاء الذكاء الاصطناعي", "نماذج لغوية عربية", "تحويل الصوت إلى نص", "التعرّف على الوجه"]),
            ("المنصات والحلول المؤسسية", "برمجيات مخصصة وأنظمة تربط عملياتك، وتتكامل مع أنظمة تخطيط الموارد وإدارة علاقات العملاء والموارد البشرية.",
             ["برمجيات مخصصة", "تكامل الأنظمة", "أتمتة العمليات", "التحول الرقمي"]),
            ("السحابة والاستضافة", "استضافة آمنة داخل المملكة، وسحابة خاصة وهجينة تنمو مع أعمالك.",
             ["سحابة خاصة", "سحابة هجينة", "استضافة سيادية", "النسخ الاحتياطي والتعافي"]),
            ("مراكز البيانات", "نصمّم مراكز البيانات ونبنيها ونشغّلها، من المراكز المصغّرة إلى البنية الجاهزة لأحمال الذكاء الاصطناعي.",
             ["التصميم والبناء", "التشغيل على مدار الساعة", "الطاقة والتبريد", "الجاهزية لوحدات GPU"]),
        ],
        "usual_t": "الطريقة المعتادة",
        "usual": ["مورّد لمراكز البيانات", "مزوّد للسحابة", "شركة برمجيات", "شركة ذكاء اصطناعي"],
        "usual_f": "أربعة عقود، وأربعة فرق دعم، ومسؤولية موزّعة بينها.",
        "ours_t": "مع AIP",
        "ours": ["عقد واحد", "فريق واحد", "مسؤولية واحدة", "منظومة مترابطة من الأساس"],
        "ours_f": "شريك واحد يتحمّل مسؤولية النتيجة كاملة.",
        "dc_ey": "مراكز البيانات",
        "dc_h": ("الأساس الذي", "يقوم عليه كل شيء."),
        "dc_p": "نصمّم ونبني ونشغّل مراكز بيانات حديثة داخل المملكة، جاهزة لأحمال الذكاء الاصطناعي، وتبقى فيها بياناتك تحت سيادتك. من مركز مصغّر داخل منشأتك إلى بنية متكاملة تنمو معك.",
        "dc_facts": [("سيادة", "البيانات داخل المملكة"), ("GPU", "جاهزية لأحمال الذكاء الاصطناعي"), ("24/7", "مراقبة وتشغيل على مدار الساعة"), ("كفاءة", "في استهلاك الطاقة والتبريد")],
        "dc_steps": [
            ("التصميم", "دراسة الأحمال والطاقة والتبريد والمساحة."),
            ("البناء", "الخوادم والشبكات والطاقة الاحتياطية والتبريد."),
            ("التشغيل", "مراقبة لحظية وإدارة الأحمال والاستجابة للحوادث."),
            ("التوسّع", "صيانة وقائية وتحديثات وسعة تنمو مع أعمالك."),
        ],
        "dc_cta": "خطّط لمركز بياناتك معنا",
        "pl_ey": "المنصات",
        "pl_h": "منصات جاهزة للعمل اليوم.",
        "pl_p": "منتجات تعمل من اليوم الأول، وتتكامل فيما بينها ومع أنظمتك.",
        "products": {
            "nedaa": "موظف استقبال ذكي يرد على العملاء ويحجز مواعيدهم باللهجات السعودية وبالإنجليزية.",
            "waqeen": "نظام حضور وانصراف يعتمد على الهوية الحيوية والتعرّف على الوجه.",
            "nawa": "منصة لغوية عربية لتحليل المستندات وتوليد المحتوى.",
            "waseel": "تحويل الصوت إلى نص، مع التلخيص والترجمة.",
            "fath": "منصة لبناء وكلاء ذكاء اصطناعي وتشغيلهم لإنجاز المهام.",
        },
        "visit": "زيارة الموقع",
        "demo": "اطلب عرضًا",
        "se_ey": "القطاعات",
        "se_h": "قطاعات نخدمها.",
        "sectors": ["الرعاية الصحية", "التعليم", "الجهات الحكومية", "التجزئة", "الضيافة والمطاعم", "العقار", "الخدمات المالية", "الصناعة والخدمات اللوجستية"],
        "pa_ey": "الشراكة",
        "pa_h": "اختر نموذج التعاون، ونتولى الباقي.",
        "models": [
            ("مشاريع مخصصة", "حلول مصمّمة وفق احتياجك وأهدافك التشغيلية."),
            ("خدمة مُدارة", "نشغّل ونراقب وندعم، لتتفرغ لأعمالك."),
            ("اشتراك", "منصاتنا باشتراك مرن ينمو معك."),
            ("شراكة استراتيجية", "نبني معك حلولًا مشتركة على المدى الطويل."),
        ],
        "steps": [
            ("نستمع", "نفهم أهدافك وتحدياتك."),
            ("نصمّم", "نقترح الحل والنموذج الأنسب."),
            ("نبني", "ننفّذ ونفعّل وفق خطة واضحة."),
            ("نقيس", "نتابع الأثر ونطوّر باستمرار."),
        ],
        "faq_ey": "أسئلة شائعة",
        "faq_h": "قبل أن تسأل.",
        "faq": [
            ("هل تبنون مراكز بيانات خاصة بالمنشآت؟", "نعم. نصمّم مراكز البيانات ونبنيها ونشغّلها وفق احتياجك، من المراكز المصغّرة داخل منشأتك إلى البنية الجاهزة لأحمال الذكاء الاصطناعي، مع خيار التشغيل والمراقبة المستمرين."),
            ("هل تتكامل حلولكم مع أنظمتنا الحالية؟", "نعم. تعمل حلولنا مع أنظمتك الحالية، مثل الموقع الإلكتروني وواتساب والبريد الإلكتروني وأنظمة تخطيط الموارد وإدارة علاقات العملاء والموارد البشرية، دون الحاجة إلى استبدالها."),
            ("أين تُستضاف بياناتنا؟", "بحسب الحل واحتياجك: في السحابة، أو في استضافة داخل المملكة، أو على خوادمك الخاصة، مع الالتزام بنظام حماية البيانات الشخصية."),
            ("كم تستغرق مدة التنفيذ؟", "تختلف بحسب النطاق. المنصات الجاهزة أسرع في التفعيل، والمشاريع المخصصة تسير وفق خطة واضحة: نستمع، ثم نصمّم، ثم نبني، ثم نقيس."),
            ("هل يمكننا مشاهدة عرض توضيحي قبل اتخاذ القرار؟", "بالتأكيد. نرتّب لك عرضًا توضيحيًا، ونناقش معك حالة استخدام من واقع منشأتك."),
        ],
        "ct_h": ("لنبنِ معًا", "ما هو قادم."),
        "ct_p": "حدّثنا عن فكرتك أو التحدي الذي تواجهه، وسنعود إليك بحل واضح وخطة تنفيذ.",
        "channels": [("واتساب", "+966 55 633 0039", WHATSAPP, "whatsapp", "ltr"), ("البريد الإلكتروني", EMAIL, f"mailto:{EMAIL}", "mail", "ltr"), ("المقر", "برج الستين، الرياض", MAP, "pin", None)],
        "follow": "تابعنا",
        "foot": "مجموعة تقنية سعودية تبني الأساس الرقمي للمنشآت، من مراكز البيانات إلى الذكاء الاصطناعي.",
        "rights": "جميع الحقوق محفوظة.",
        "place": "الرياض، المملكة العربية السعودية",
        "new_tab": "(يفتح في نافذة جديدة)",
    },
    "en": {
        "title": "AIP | From silicon to intelligence",
        "description": "AIP is a Saudi technology group that designs, builds and operates data centers, cloud, enterprise platforms and artificial intelligence.",
        "skip": "Skip to content",
        "menu": "Menu",
        "nav": [("Ecosystem", "#stack"), ("Data centers", "#dc"), ("Platforms", "#platforms"), ("Industries", "#sectors"), ("Partnership", "#partner")],
        "other_lang": ("العربية", "/", "ar"),
        "start": "Start a project",
        "kicker": "AIP · Riyadh, Saudi Arabia",
        "h1": ("From silicon", "to intelligence."),
        "lead": "AIP is a Saudi technology group that designs, builds and operates every layer your organization runs on: data centers, cloud, enterprise platforms and artificial intelligence. One partner, from the ground up.",
        "explore": "Explore the ecosystem",
        "talk": "Talk to our team",
        "figure": "The four layers of AIP's ecosystem",
        "tiers": ["Artificial intelligence", "Enterprise platforms", "Cloud and hosting", "Data centers"],
        "about_ey": "About AIP",
        "about_h": ("Real technology isn't seen.", "Its effect is."),
        "about_p": "You see it in a customer answered within seconds, in data kept secure, and in a team free to focus on what matters. That is what we build at AIP: infrastructure that works quietly, and results that are clear.",
        "values": [
            ("People", "Technology serves people, not the other way around."),
            ("Technology", "We build with the best the world has to offer."),
            ("Ideas", "Every solution starts with the right question."),
            ("Impact", "We measure success by our clients' results."),
        ],
        "stack_ey": "Ecosystem",
        "stack_h": "Four layers. One partner.",
        "stack_p": "Instead of four vendors, AIP covers every layer and connects them. Open any layer for the details.",
        "layers": [
            ("Artificial intelligence", "Agents that get work done, and platforms that understand Arabic in text, speech and images.",
             ["AI agents", "Arabic language models", "Speech to text", "Facial recognition"]),
            ("Enterprise platforms", "Custom software and systems that connect your operations and integrate with ERP, CRM and HR.",
             ["Custom software", "Systems integration", "Process automation", "Digital transformation"]),
            ("Cloud and hosting", "Secure hosting inside the Kingdom, and private and hybrid cloud that grows with you.",
             ["Private cloud", "Hybrid cloud", "Sovereign hosting", "Backup and recovery"]),
            ("Data centers", "We design, build and operate data centers, from edge sites to AI-ready infrastructure.",
             ["Design and build", "24/7 operations", "Power and cooling", "GPU-ready"]),
        ],
        "usual_t": "The usual way",
        "usual": ["A data center vendor", "A cloud provider", "A software house", "An AI company"],
        "usual_f": "Four contracts, four support teams, and accountability split between them.",
        "ours_t": "With AIP",
        "ours": ["One contract", "One team", "One point of accountability", "An ecosystem connected from the ground up"],
        "ours_f": "One partner who owns the outcome.",
        "dc_ey": "Data centers",
        "dc_h": ("The foundation", "everything stands on."),
        "dc_p": "We design, build and operate modern data centers inside the Kingdom, ready for AI workloads, with your data under your sovereignty. From an edge site inside your facility to full infrastructure that scales with you.",
        "dc_facts": [("Sovereign", "Data stays in the Kingdom"), ("GPU", "Ready for AI workloads"), ("24/7", "Monitoring and operations"), ("Efficient", "Power and cooling")],
        "dc_steps": [
            ("Design", "Load, power, cooling and space studies."),
            ("Build", "Servers, networking, backup power and cooling."),
            ("Operate", "Live monitoring, workload management and incident response."),
            ("Scale", "Preventive maintenance, upgrades and growing capacity."),
        ],
        "dc_cta": "Plan your data center with us",
        "pl_ey": "Platforms",
        "pl_h": "Platforms ready today.",
        "pl_p": "Products that work from day one, and connect with each other and with your systems.",
        "products": {
            "nedaa": "An AI receptionist that answers customers and books their appointments in Saudi dialects and English.",
            "waqeen": "Attendance based on biometric identity and facial recognition.",
            "nawa": "An Arabic language platform for document analysis and content generation.",
            "waseel": "Speech to text, with summaries and translation.",
            "fath": "A platform to build and run AI agents that get work done.",
        },
        "visit": "Visit the site",
        "demo": "Request a demo",
        "se_ey": "Industries",
        "se_h": "Industries we serve.",
        "sectors": ["Healthcare", "Education", "Government", "Retail", "Hospitality and food service", "Real estate", "Financial services", "Industry and logistics"],
        "pa_ey": "Partnership",
        "pa_h": "Choose how we work together. We handle the rest.",
        "models": [
            ("Custom projects", "Solutions designed around your needs and operational goals."),
            ("Managed services", "We run, monitor and support, so you can focus on your business."),
            ("Subscription", "Our platforms on flexible plans that grow with you."),
            ("Strategic partnership", "We build long-term solutions together."),
        ],
        "steps": [
            ("Listen", "We understand your goals and challenges."),
            ("Design", "We propose the right solution and model."),
            ("Build", "We deliver and switch on with a clear plan."),
            ("Measure", "We track the impact and keep improving."),
        ],
        "faq_ey": "Questions",
        "faq_h": "Before you ask.",
        "faq": [
            ("Do you build private data centers for organizations?", "Yes. We design, build and operate data centers to your needs, from edge sites inside your facility to AI-ready infrastructure, with optional ongoing operations and monitoring."),
            ("Do your solutions work with our current systems?", "Yes. They work with the systems you already have, such as your website, WhatsApp, email, ERP, CRM and HR, with nothing to replace."),
            ("Where is our data hosted?", "It depends on the solution and your needs: cloud, hosting inside the Kingdom, or your own servers, in line with the Saudi Personal Data Protection Law."),
            ("How long does implementation take?", "It depends on the scope. Ready platforms switch on faster; custom projects follow a clear plan: listen, design, build, measure."),
            ("Can we see a demo before deciding?", "Of course. We arrange a demo and walk through a use case from your own operations."),
        ],
        "ct_h": ("Let's build", "what's next."),
        "ct_p": "Tell us about your idea or challenge, and we will come back with a clear solution and a delivery plan.",
        "channels": [("WhatsApp", "+966 55 633 0039", WHATSAPP, "whatsapp", "ltr"), ("Email", EMAIL, f"mailto:{EMAIL}", "mail", "ltr"), ("Head office", "Al Sitteen Tower, Riyadh", MAP, "pin", None)],
        "follow": "Follow us",
        "foot": "A Saudi technology group building the digital foundation of organizations, from data centers to artificial intelligence.",
        "rights": "All rights reserved.",
        "place": "Riyadh, Saudi Arabia",
        "new_tab": "(opens in a new tab)",
    },
}


def e(text: str) -> str:
    return escape(text, quote=True)


def icon(name: str, stroke: str = "currentColor", width: str = "1.9", cls: str = "") -> str:
    klass = f' class="{cls}"' if cls else ""
    return (
        f'<svg{klass} aria-hidden="true" focusable="false" viewBox="0 0 24 24" fill="none" stroke="{stroke}" '
        f'stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"><path d="{ICON[name]}"/></svg>'
    )


def dir_attr(direction: str | None) -> str:
    return f' dir="{direction}"' if direction else ""


def eyebrow(text: str) -> str:
    return f'<span class="eyebrow">{e(text)}</span>'


def two_lines(lines: tuple[str, str], accent: bool = True) -> str:
    second = f'<span class="accent">{e(lines[1])}</span>' if accent else f"<span>{e(lines[1])}</span>"
    return f"<span>{e(lines[0])}</span>{second}"


def page(lang: str) -> str:
    t = COPY[lang]
    rtl = lang == "ar"
    home = "/" if rtl else "/en/"
    other_label, other_href, other_lang = t["other_lang"]
    nav = "".join(f'<a href="{h}">{e(n)}</a>' for n, h in t["nav"])
    tiers = "".join(
        f'<div class="tier"><span class="num">L0{4 - i}</span><span>{e(name)}</span></div>'
        for i, name in enumerate(t["tiers"])
    )
    values = "".join(
        f'<div><span class="num">0{i + 1}</span><strong>{e(a)}</strong><span>{e(b)}</span></div>'
        for i, (a, b) in enumerate(t["values"])
    )
    layers = "".join(
        f'<details class="layer"{" open" if i == 0 else ""}><summary><span class="num">L0{4 - i}</span>'
        f'<h3>{e(name)}</h3><span class="plus">{icon("plus", width="2")}</span></summary>'
        f'<div class="layer-body"><p>{e(body)}</p><ul class="chips">'
        + "".join(f"<li>{e(c)}</li>" for c in chips)
        + "</ul></div></details>"
        for i, (name, body, chips) in enumerate(t["layers"])
    )
    usual = "".join(f"<li>{e(x)}</li>" for x in t["usual"])
    ours = "".join(f"<li>{e(x)}</li>" for x in t["ours"])
    facts = "".join(f"<div><strong>{e(a)}</strong><span>{e(b)}</span></div>" for a, b in t["dc_facts"])

    def steps(items: list[tuple[str, str]]) -> str:
        return "".join(
            f'<li><span class="num">0{i + 1}</span><strong>{e(a)}</strong><span>{e(b)}</span></li>'
            for i, (a, b) in enumerate(items)
        )

    products = ""
    for i, (key, ar_name, en_name, link) in enumerate(PRODUCTS):
        name, alt = (ar_name, en_name) if rtl else (en_name, ar_name)
        href = link or f"mailto:{EMAIL}?subject={en_name}"
        cta = t["visit"] if link else t["demo"]
        products += (
            f'<a class="product" href="{e(href)}"><div class="product-top"><span class="product-icon">'
            f'{icon(key, stroke="#5FD6A6", width="1.8")}</span><span class="num">0{i + 1}</span></div>'
            f'<div class="product-name"><strong>{e(name)}</strong><span lang="{"en" if rtl else "ar"}">{e(alt)}</span></div>'
            f'<p>{e(t["products"][key])}</p><span class="product-cta">{e(cta)}{icon("out", width="2.2")}</span></a>'
        )
    sectors = "".join(f"<li>{e(x)}</li>" for x in t["sectors"])
    models = "".join(
        f'<div><span class="num">0{i + 1}</span><strong>{e(a)}</strong><span>{e(b)}</span></div>'
        for i, (a, b) in enumerate(t["models"])
    )
    faq = "".join(
        f'<details><summary><span>{e(q)}</span><span class="plus">{icon("plus", width="2")}</span></summary><p>{e(a)}</p></details>'
        for q, a in t["faq"]
    )
    channels = "".join(
        f'<a class="channel" href="{e(url)}"><span class="channel-icon">{icon(ic, stroke="#5FD6A6")}</span>'
        f"<span><small>{e(label)}</small><b{dir_attr(d)}>{e(value)}</b></span></a>"
        for label, value, url, ic, d in t["channels"]
    )
    social = "".join(
        f'<a href="{e(url)}" rel="noopener">{icon(ic, stroke="#5FD6A6")}{e(name)}</a>' for name, url, ic in SOCIAL
    )
    redirect = (
        "<script>if(/[?&]lang=en\\b/.test(location.search))location.replace('/en/'+location.hash)</script>"
        if rtl
        else ""
    )
    font = "Readex+Pro:wght@300;400;500;600" if rtl else "Space+Grotesk:wght@400;500;600&family=Readex+Pro:wght@300;400"
    canonical = f"{SITE}{home}"
    return f"""<!DOCTYPE html>
<html lang="{lang}" dir="{"rtl" if rtl else "ltr"}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t["title"])}</title>
<meta name="description" content="{e(t["description"])}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="ar" href="{SITE}/">
<link rel="alternate" hreflang="en" href="{SITE}/en/">
<link rel="alternate" hreflang="x-default" href="{SITE}/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="AIP">
<meta property="og:title" content="{e(t["title"])}">
<meta property="og:description" content="{e(t["description"])}">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="{"ar_SA" if rtl else "en_US"}">
<meta name="theme-color" content="#07090F">
<link rel="icon" type="image/svg+xml" href="/assets/img/logo-mark.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family={font}&family=JetBrains+Mono:wght@400&display=swap">
<link rel="stylesheet" href="/assets/css/home.css">
{redirect}</head>
<body>
<a class="skip" href="#main">{e(t["skip"])}</a>
<header class="top">
<div class="wrap">
<a class="logo" href="{home}" aria-label="AIP"><img src="/assets/img/aip-wordmark.svg" alt="AIP" width="86" height="24"></a>
<nav class="nav" aria-label="{e(t["menu"])}">{nav}</nav>
<div class="top-actions">
<details class="menu"><summary aria-label="{e(t["menu"])}">{icon("menu", stroke="#F2F4F8", width="2", cls="")}</summary><nav class="menu-panel" aria-label="{e(t["menu"])}">{nav}</nav></details>
<a class="lang" href="{other_href}" lang="{other_lang}" hreflang="{other_lang}">{e(other_label)}</a>
<a class="btn btn-solid" href="mailto:{EMAIL}?subject=AIP%20project">{e(t["start"])}</a>
</div>
</div>
</header>
<main id="main">
<section class="hero">
<div class="wrap">
<div class="hero-text">
{eyebrow(t["kicker"])}
<h1>{two_lines(t["h1"])}</h1>
<p class="lead">{e(t["lead"])}</p>
<div class="actions">
<a class="btn btn-solid" href="#stack">{e(t["explore"])}{icon("arrow", width="2.2", cls="arrow")}</a>
<a class="btn btn-line" href="{WHATSAPP}">{icon("whatsapp", cls="wa")}{e(t["talk"])}</a>
</div>
</div>
<figure class="layers-figure" aria-label="{e(t["figure"])}" style="margin:0">{tiers}</figure>
</div>
</section>

<section class="section light" aria-labelledby="about-h">
<div class="wrap">
<div class="head-title">{eyebrow(t["about_ey"])}<h2 id="about-h" class="h2-xl">{two_lines(t["about_h"])}</h2></div>
<div class="about-body"><p>{e(t["about_p"])}</p><div class="values">{values}</div></div>
</div>
</section>

<section class="section" id="stack" aria-labelledby="stack-h">
<div class="wrap">
<div class="head"><div class="head-title">{eyebrow(t["stack_ey"])}<h2 id="stack-h" class="h2">{e(t["stack_h"])}</h2></div><p>{e(t["stack_p"])}</p></div>
<div class="layers">{layers}</div>
<div class="compare">
<div><h3>{e(t["usual_t"])}</h3><ul>{usual}</ul><p>{e(t["usual_f"])}</p></div>
<div class="ours"><h3>{e(t["ours_t"])}</h3><ul>{ours}</ul><p>{e(t["ours_f"])}</p></div>
</div>
</div>
</section>

<section class="section alt" id="dc" aria-labelledby="dc-h">
<div class="wrap">
<div class="dc-top">
<div class="head-title">{eyebrow(t["dc_ey"])}<h2 id="dc-h" class="h2-xl">{two_lines(t["dc_h"])}</h2><p class="intro">{e(t["dc_p"])}</p>
<div><a class="btn btn-solid" href="mailto:{EMAIL}?subject=AIP%20data%20center">{e(t["dc_cta"])}{icon("arrow", width="2.2", cls="arrow")}</a></div></div>
<div class="facts">{facts}</div>
</div>
<ol class="steps">{steps(t["dc_steps"])}</ol>
</div>
</section>

<section class="section light" id="platforms" aria-labelledby="pl-h">
<div class="wrap">
<div class="head"><div class="head-title">{eyebrow(t["pl_ey"])}<h2 id="pl-h" class="h2">{e(t["pl_h"])}</h2></div><p>{e(t["pl_p"])}</p></div>
<div class="products">{products}</div>
</div>
</section>

<section class="section" id="sectors" aria-labelledby="se-h">
<div class="wrap">
<div class="head-title">{eyebrow(t["se_ey"])}<h2 id="se-h" class="h2">{e(t["se_h"])}</h2></div>
<ul class="sectors">{sectors}</ul>
</div>
</section>

<section class="section light" id="partner" aria-labelledby="pa-h">
<div class="wrap">
<div class="head-title">{eyebrow(t["pa_ey"])}<h2 id="pa-h" class="h2">{e(t["pa_h"])}</h2></div>
<div class="models">{models}</div>
<ol class="steps">{steps(t["steps"])}</ol>
</div>
</section>

<section class="section" id="faq" aria-labelledby="faq-h">
<div class="wrap faq-grid">
<div class="head-title">{eyebrow(t["faq_ey"])}<h2 id="faq-h" class="h2">{e(t["faq_h"])}</h2></div>
<div class="faq">{faq}</div>
</div>
</section>

<section class="section alt contact" id="contact" aria-labelledby="ct-h">
<div class="wrap">
<h2 id="ct-h">{two_lines(t["ct_h"])}</h2>
<p class="intro">{e(t["ct_p"])}</p>
<div class="channels">{channels}</div>
<div class="social"><span>{e(t["follow"])}</span>{social}</div>
</div>
</section>
</main>

<footer class="foot">
<div class="wrap">
<div class="foot-top">
<div class="foot-about"><img src="/assets/img/aip-wordmark.svg" alt="AIP" width="86" height="24"><p>{e(t["foot"])}</p></div>
<nav class="foot-links" aria-label="AIP">{nav}<a class="nedaa" href="https://nedaa.aip-sa.com"><img src="/assets/img/nedaa-mark.svg" alt="" width="14" height="15">{e("نداء" if rtl else "Nedaa")}</a></nav>
</div>
<div class="foot-bottom"><span><bdi dir="ltr">© 2026 AIP</bdi>. {e(t["rights"])}</span><span>{e(t["place"])}</span></div>
</div>
</footer>
<script>document.querySelectorAll('.menu-panel a').forEach(function(a){{a.addEventListener('click',function(){{a.closest('details').removeAttribute('open')}})}})</script>
</body>
</html>
"""


def main() -> None:
    (ROOT / "index.html").write_text(page("ar"), encoding="utf-8", newline="\n")
    (ROOT / "en").mkdir(exist_ok=True)
    (ROOT / "en" / "index.html").write_text(page("en"), encoding="utf-8", newline="\n")
    print("wrote public/index.html and public/en/index.html")


if __name__ == "__main__":
    main()
