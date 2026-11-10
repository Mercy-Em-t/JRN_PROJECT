// Kikao360 / PulseWire - Core Story Dataset
const STORIES = [
  {
    id: "story-1",
    pillar: "tech",
    category: "Tech & Hustle",
    badge: "Explainer",
    title: "The M-Pesa API Revolution: How Gen-Z Micro-Merchants Are Rewriting Kenya’s Informal Economy",
    subdeck: "From Nairobi estates to TikTok livestreams, young Kenyan hustlers are skipping brick-and-mortar storefronts entirely for direct mobile checkout.",
    bulletLink: "Read our special investigation into eTIMS tax compliance for freelancers",
    author: "Faith Mwende and Brian Kipchumba",
    date: "Tue 10 Nov 2026 10.30 EAT",
    readTime: "4 min read",
    videoDuration: "1:15",
    videoSrc: "assets/VID_094529.mp4",
    poster: "assets/IMG_093824.jpg",
    tags: ["M-Pesa", "Fintech", "Startups", "Nairobi", "Gen-Z", "Youth Economy"],
    stats: {
      views: "18.4K",
      reactions: "🔥 842  💡 512  ❤️ 1.2K",
      comments: 186
    },
    ogData: {
      siteName: "Kikao360 | Kenya's Multimodal Newsroom",
      headline: "The M-Pesa API Revolution: How Gen-Z Micro-Merchants Are Rewriting Kenya’s Economy",
      description: "Young creators are bypassing commercial banks with automated M-Pesa paybill hooks and TikTok livestreams.",
      channelTime: "10:30 AM"
    },
    leadParagraph: "In a sunlit shared apartment along Thika Road, 22-year-old Brian Mwangi watches his dual-monitor setup chime with real-time M-Pesa confirmation pings. Without a physical storefront or a conventional corporate bank account, his custom sneaker consignment platform clears over KES 180,000 in weekly turnover—entirely powered by automated Daraja API webhooks and WhatsApp customer bots.",
    quote: "We don't need expensive mall leases anymore. Our phone is the cash register, the studio, and the distribution pipeline all in one.",
    quoteAuthor: "Brian Mwangi, Co-founder of SneakerVault Kenya",
    secondaryParagraph: "Kenya's formal banking sector is rapidly adapting to this creator-led economy. Safaricom's latest developer release opens instant micropayments, but looming regulatory questions on eTIMS integration and digital services taxation threaten to alter unit economics for over 7.4 million micro and small entrepreneurs."
  },
  {
    id: "story-2",
    pillar: "investigative",
    category: "Cybercrime & Security",
    badge: "Investigation",
    title: "Who Is Hacking Cold-Chain Infrastructure Across Regional Logistics Hubs?",
    subdeck: "Following European supermarket freezer disruptions, cybersecurity agencies warn logistics networks across Nairobi and Mombasa to patch IoT vulnerabilities.",
    bulletLink: "Supermarket fridges and freezers across 7 nations remotely spiked to 50°C",
    author: "Robert Booth and Miatta Mbriwa",
    date: "Mon 9 Nov 2026 19.07 EAT",
    readTime: "5 min read",
    videoDuration: "1:45",
    videoSrc: "assets/VID_094701.mp4",
    poster: "assets/Screenshot_092825.jpg",
    tags: ["Cybercrime", "IoT Security", "Retail", "Supply Chain", "Critical Infrastructure"],
    stats: {
      views: "24.1K",
      reactions: "🚨 1.1K  ⚡ 430  👀 2.8K",
      comments: 247
    },
    ogData: {
      siteName: "Kikao360 | Security Bureau",
      headline: "Cyber Attackers Target Critical Food Cold-Chain Controllers",
      description: "Automated thermostats cranked up in the middle of the night, spoiling millions in perishables. Is East Africa vulnerable?",
      channelTime: "08:15 AM"
    },
    leadParagraph: "Commercial refrigerators and pharmaceutical chilling warehouses across regional supply corridors have reported automated thermostat tampering. Digital forensics teams identified firmware exploits targeting industrial refrigeration controllers—a chilling parallel to the recent wave of retail attacks across Europe.",
    quote: "When critical cold-chain sensors are manipulated remotely, food security and medicine distribution become weaponized overnight.",
    quoteAuthor: "National Cybersecurity Coordination Bureau",
    secondaryParagraph: "Private supermarket chains in Nairobi are now conducting emergency audits of smart telemetry hubs, replacing legacy Wi-Fi thermostats with air-gapped cellular bridges."
  },
  {
    id: "story-3",
    pillar: "campus",
    category: "Campus & Culture",
    badge: "Special Feature",
    title: "The USIU-Africa Entrepreneurship Sprint: Students Building Media Startups in 2026",
    subdeck: "How modern media management courses at USIU-Africa are turning communication majors into digital product owners and venture founders.",
    bulletLink: "Inside the Week 11 Media Investors' Boardroom Simulation",
    author: "Grace Wanjiku & Media Management Lab",
    date: "Tue 10 Nov 2026 09.00 EAT",
    readTime: "3 min read",
    videoDuration: "1:15",
    videoSrc: "assets/VID_094529.mp4",
    poster: "assets/IMG_094519.jpg",
    tags: ["USIU-Africa", "Media Management", "Dr. Ruth Owino", "Higher Ed", "Innovation"],
    stats: {
      views: "9.8K",
      reactions: "🎓 630  🚀 480  👏 790",
      comments: 94
    },
    ogData: {
      siteName: "Kikao360 | Campus Wire",
      headline: "USIU Media Challenge: Pitching The Next Big Digital Platform",
      description: "Students combine WhatsApp channels, Guardian editorial depth, and 3D spherical interfaces for the Fall 2026 venture showcase.",
      channelTime: "Yesterday"
    },
    leadParagraph: "Inside the School of Communication, Cinematics & Creative Arts at USIU-Africa, lecture halls have transformed into high-stakes venture incubators. Guided by Dr. Ruth Owino, media management students are challenging traditional broadcast models by prototyping agile, mobile-first multimedia publications.",
    quote: "A visually appealing prototype alone will not earn high marks if the business model is weak. Both must work in flawless harmony.",
    quoteAuthor: "JRN 3015A Assignment Directive",
    secondaryParagraph: "With seed funding simulations on the line in Week 11, teams are pitching cross-channel architectures that bridge WhatsApp channels directly into interactive 3D spatial web environments."
  },
  {
    id: "story-4",
    pillar: "lifestyle",
    category: "Agri-Tech & Lifestyle",
    badge: "Lifestyle Longform",
    title: "From Burnt-Out Corporate Desk to Smart Bee Farming in Kiambu's Green Ridges",
    subdeck: "How a former investigative journalist left 60-hour workweeks to establish an automated smart apiary and found peace in regenerative farming.",
    bulletLink: "Explore organic honey export cooperatives and smart IoT hive sensors",
    author: "Jeff Lee and Sharon Chebet",
    date: "Sun 8 Nov 2026 14.20 EAT",
    readTime: "6 min read",
    videoDuration: "1:45",
    videoSrc: "assets/VID_094701.mp4",
    poster: "assets/IMG_094540.jpg",
    tags: ["AgriTech", "Lifestyle", "Smart Farming", "Kiambu", "Mental Health"],
    stats: {
      views: "15.3K",
      reactions: "🍯 950  🌿 1.4K  🐝 610",
      comments: 142
    },
    ogData: {
      siteName: "Kikao360 | Green Horizons",
      headline: "Smart Apiaries: Tech Meets Agriculture in the Kiambu Highlands",
      description: "Solar-powered temperature monitors and acoustic sensors are helping young Kenyan farmers harvest premium honey.",
      channelTime: "Sunday"
    },
    leadParagraph: "High on the mist-draped tea hills of Limuru, the hum of 200,000 honeybees replaces the cacophony of Nairobi morning traffic. Solar-powered acoustic microphones inside cedar Langstroth hives monitor queen health and colony swarming patterns with predictive accuracy.",
    quote: "Working with the land taught me patience that no boardroom ever could. Technology should serve the ecosystem, not exploit it.",
    quoteAuthor: "Sharon Chebet, Founder of Rimpa Apiaries",
    secondaryParagraph: "The venture now supplies pure highland comb honey to gourmet delis across Nairobi while training dozens of smallholder farmers on organic pollination techniques."
  },
  {
    id: "story-5",
    pillar: "opinion",
    category: "Opinion & Voices",
    badge: "Editorial View",
    title: "Comment Is Free, But Integrity Is Non-Negotiable: Journalism in the Age of Generative AI",
    subdeck: "As synthetic media and algorithmic feeds flood our screens, grounded human verification and ethical storytelling are more urgent than ever.",
    bulletLink: "Read our transparency charter and 70% human-verified reporting pledge",
    author: "Editorial Board & Guest Columnists",
    date: "Mon 9 Nov 2026 08.00 EAT",
    readTime: "4 min read",
    videoDuration: "1:15",
    videoSrc: "assets/VID_094529.mp4",
    poster: "assets/IMG_094519.jpg",
    tags: ["Editorial", "Media Ethics", "GenAI", "USIU", "Truth & Trust"],
    stats: {
      views: "12.1K",
      reactions: "✍️ 820  🧠 740  🛡️ 1.1K",
      comments: 115
    },
    ogData: {
      siteName: "Kikao360 | Perspective",
      headline: "Why Independent Verification Remains Our Most Sacred Currency",
      description: "Algorithms can summarize data, but they cannot walk the streets of Nairobi or look a source in the eye.",
      channelTime: "Saturday"
    },
    leadParagraph: "In 1921, legendary Guardian editor C.P. Scott famously wrote that 'Comment is free, but facts are sacred.' More than a century later, in an era dominated by hyper-realistic deepfakes and automated clickbait, that tenet is no longer merely a high-minded aphorism—it is an existential survival mandate for credible journalism.",
    quote: "An algorithm can parse a million documents in a split second, but it cannot smell rain on red soil or uncover systemic corruption through human grit.",
    quoteAuthor: "C.P. Scott Centenary Declaration",
    secondaryParagraph: "At Kikao360, we mandate that at least 70% of every investigative dossier reflects direct on-the-ground human inquiry, corroborated documents, and accountable sourcing."
  }
];

const MOST_VIEWED = [
  { rank: 1, title: "The M-Pesa API Revolution: How Gen-Z Micro-Merchants Are Rewriting Kenya’s Economy", category: "Tech & Hustle" },
  { rank: 2, title: "Who Is Hacking Cold-Chain Infrastructure Across Regional Logistics Hubs?", category: "Investigative" },
  { rank: 3, title: "USIU-Africa Media Challenge: Students Pitching Next-Gen News Platforms", category: "Campus" },
  { rank: 4, title: "From Burnt-Out Corporate Desk to Smart Bee Farming in Kiambu", category: "Lifestyle" },
  { rank: 5, title: "Comment Is Free, But Integrity Is Sacred: Journalism in the AI Age", category: "Opinion" },
  { rank: 6, title: "Nairobi Expressway Night Drifts: Law Enforcement Clamps Down on Illegal Racing", category: "News" },
  { rank: 7, title: "Silicon Savannah Funding Pulse: Top 10 Seed Rounds Closed in Q4 2026", category: "Business" },
  { rank: 8, title: "Sheng Dialects of Nairobi: How Eastlands Vernacular Shapes East African Pop Music", category: "Culture" },
  { rank: 9, title: "Central Bank of Kenya Signals New Micropayment Interoperability Rules", category: "Tech" },
  { rank: 10, title: "Solar Micro-Grids Transform Rural Healthcare Clinics in Turkana", category: "Development" }
];

// Attach to window for global browser scope
if (typeof window !== "undefined") {
  window.STORIES = STORIES;
  window.MOST_VIEWED = MOST_VIEWED;
}

