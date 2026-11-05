<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>nowm.tech | Developer Portfolio & Tech Hub</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        brand: {
                            50: '#f0fdfa',
                            100: '#ccfbf1',
                            400: '#2dd4bf',
                            500: '#14b8a6',
                            600: '#0d9488',
                            900: '#134e4a',
                            cyan: '#06b6d4',
                            accent: '#6366f1'
                        }
                    },
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        mono: ['JetBrains Mono', 'Fira Code', 'monospace']
                    }
                }
            }
        }
    </script>
    <!-- Fonts & Icons -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        body {
            font-family: 'Inter', sans-serif;
        }
        .font-mono {
            font-family: 'Fira Code', monospace;
        }
        /* Glassmorphism effects */
        .glass {
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.3);
        }
        .dark .glass {
            background: rgba(15, 23, 42, 0.75);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        /* Custom Glowing & Grid Effects */
        .bg-grid-pattern {
            background-size: 30px 30px;
            background-image: radial-gradient(circle, rgba(148, 163, 184, 0.15) 1px, transparent 1px);
        }
        .dark .bg-grid-pattern {
            background-image: radial-gradient(circle, rgba(255, 255, 255, 0.07) 1px, transparent 1px);
        }
        .glow-effect {
            box-shadow: 0 0 25px -5px rgba(20, 184, 166, 0.3);
        }
        .dark .glow-effect {
            box-shadow: 0 0 35px -5px rgba(45, 212, 191, 0.25);
        }
        /* Smooth Scroll behavior */
        html {
            scroll-behavior: smooth;
        }
        /* Custom scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: transparent;
        }
        ::-webkit-scrollbar-thumb {
            background: #94a3b8;
            border-radius: 4px;
        }
        .dark ::-webkit-scrollbar-thumb {
            background: #334155;
        }
    </style>
</head>
<body class="bg-slate-50 dark:bg-slate-950 text-slate-800 dark:text-slate-100 min-h-screen selection:bg-brand-500 selection:text-white transition-colors duration-300">

    <!-- Ambient Glow BG -->
    <div class="fixed inset-0 overflow-hidden pointer-events-none z-0">
        <div class="absolute -top-40 -left-40 w-96 h-96 bg-brand-500/15 rounded-full blur-3xl"></div>
        <div class="absolute top-1/3 -right-40 w-96 h-96 bg-brand-accent/15 rounded-full blur-3xl"></div>
        <div class="absolute bottom-10 left-1/4 w-96 h-96 bg-cyan-500/10 rounded-full blur-3xl"></div>
    </div>

    <!-- Navigation Header -->
    <header class="sticky top-0 z-40 w-full glass transition-colors">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <!-- Brand Logo -->
            <a href="#" class="flex items-center gap-2 group">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-brand-600 via-brand-500 to-cyan-400 flex items-center justify-center text-white font-mono font-bold text-lg shadow-md group-hover:scale-105 transition-transform">
                    &gt;_
                </div>
                <div class="flex flex-col">
                    <span class="font-bold font-mono text-lg tracking-tight text-slate-900 dark:text-white group-hover:text-brand-500 dark:group-hover:text-brand-400 transition-colors">
                        nowm<span class="text-brand-500 dark:text-brand-400">.tech</span>
                    </span>
                </div>
            </a>

            <!-- Desktop Nav Links -->
            <nav class="hidden md:flex items-center gap-8 font-medium text-sm text-slate-600 dark:text-slate-300">
                <a href="#about" class="hover:text-brand-500 dark:hover:text-brand-400 transition-colors">About</a>
                <a href="#projects" class="hover:text-brand-500 dark:hover:text-brand-400 transition-colors">Projects</a>
                <a href="#skills" class="hover:text-brand-500 dark:hover:text-brand-400 transition-colors">Tech Stack</a>
                <a href="#playground" class="hover:text-brand-500 dark:hover:text-brand-400 transition-colors">Playground</a>
                <a href="#contact" class="hover:text-brand-500 dark:hover:text-brand-400 transition-colors">Contact</a>
            </nav>

            <!-- Actions & Mobile Toggle -->
            <div class="flex items-center gap-3">
                <!-- Theme Toggle Button -->
                <button id="themeToggle" aria-label="Toggle Theme" class="p-2.5 rounded-xl bg-slate-200/60 dark:bg-slate-800/60 text-slate-700 dark:text-slate-200 hover:bg-slate-300/60 dark:hover:bg-slate-700/60 transition-colors">
                    <i id="themeIcon" class="fas fa-moon text-base"></i>
                </button>

                <!-- CTA Button -->
                <a href="#contact" class="hidden sm:inline-flex items-center gap-2 px-4 py-2 rounded-xl bg-gradient-to-r from-brand-600 to-brand-500 hover:from-brand-500 hover:to-brand-400 text-white font-medium text-sm shadow-sm hover:shadow-md transition-all transform hover:-translate-y-0.5">
                    <span>Get in Touch</span>
                    <i class="fas fa-arrow-right text-xs"></i>
                </a>

                <!-- Mobile Menu Button -->
                <button id="mobileMenuBtn" aria-label="Toggle Mobile Menu" class="md:hidden p-2.5 rounded-xl bg-slate-200/60 dark:bg-slate-800/60 text-slate-700 dark:text-slate-200 hover:bg-slate-300/60 dark:hover:bg-slate-700/60">
                    <i class="fas fa-bars text-lg"></i>
                </button>
            </div>
        </div>

        <!-- Mobile Menu Dropdown -->
        <div id="mobileMenu" class="hidden md:hidden border-t border-slate-200 dark:border-slate-800 px-4 pt-3 pb-6 space-y-3 bg-white/90 dark:bg-slate-900/90 backdrop-blur-md">
            <a href="#about" class="block px-3 py-2 rounded-lg text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 font-medium">About</a>
            <a href="#projects" class="block px-3 py-2 rounded-lg text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 font-medium">Projects</a>
            <a href="#skills" class="block px-3 py-2 rounded-lg text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 font-medium">Tech Stack</a>
            <a href="#playground" class="block px-3 py-2 rounded-lg text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 font-medium">Playground</a>
            <a href="#contact" class="block px-3 py-2 rounded-lg text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 font-medium">Contact</a>
        </div>
    </header>

    <main class="relative z-10">
        <!-- Hero Section -->
        <section id="about" class="relative py-20 lg:py-28 overflow-hidden bg-grid-pattern">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
                    
                    <!-- Left Hero Column -->
                    <div class="lg:col-span-7 space-y-6 text-center lg:text-left">
                        <!-- System Badge -->
                        <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-brand-500/10 dark:bg-brand-400/10 border border-brand-500/20 text-brand-600 dark:text-brand-400 text-xs sm:text-sm font-mono font-medium">
                            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                            <span>System Status: Online & Available for Hire</span>
                        </div>

                        <!-- Main Title -->
                        <h1 class="text-4xl sm:text-5xl lg:text-6xl font-extrabold tracking-tight text-slate-900 dark:text-white leading-tight">
                            Engineering High-Performance <br class="hidden sm:inline">
                            <span class="bg-gradient-to-r from-brand-500 via-brand-cyan to-brand-accent bg-clip-text text-transparent">
                                Software & Digital Solutions
                            </span>
                        </h1>

                        <!-- Dynamic Animated Subtitle -->
                        <p class="text-lg sm:text-xl text-slate-600 dark:text-slate-300 font-mono h-8">
                            &gt; I build <span id="typedText" class="text-brand-500 dark:text-brand-400 font-semibold border-r-2 border-brand-500 pr-1"></span>
                        </p>

                        <!-- Intro Paragraph -->
                        <p class="text-slate-600 dark:text-slate-400 text-base sm:text-lg max-w-2xl mx-auto lg:mx-0 leading-relaxed">
                            Welcome to <strong>nowm.tech</strong>—the digital hub for custom web applications, algorithmic tools, automation scripts, and scalable modern web solutions.
                        </p>

                        <!-- Hero Action Buttons -->
                        <div class="flex flex-wrap items-center justify-center lg:justify-start gap-4 pt-4">
                            <a href="#projects" class="px-6 py-3.5 rounded-xl bg-gradient-to-r from-brand-600 to-brand-500 text-white font-semibold shadow-lg shadow-brand-500/25 hover:shadow-brand-500/40 hover:scale-105 transition-all">
                                Explore Projects <i class="fas fa-layer-group ml-2"></i>
                            </a>
                            <a href="#playground" class="px-6 py-3.5 rounded-xl glass hover:bg-slate-200/50 dark:hover:bg-slate-800/50 text-slate-800 dark:text-slate-200 font-semibold transition-all">
                                Try Code Sandbox <i class="fas fa-code ml-2 text-brand-500"></i>
                            </a>
                        </div>

                        <!-- Quick Tech Badges -->
                        <div class="pt-6 border-t border-slate-200 dark:border-slate-800/80 flex flex-wrap items-center justify-center lg:justify-start gap-3 text-slate-500 dark:text-slate-400 text-xs font-mono">
                            <span class="font-semibold text-slate-700 dark:text-slate-300">CORE TECH:</span>
                            <span class="px-2.5 py-1 rounded-md bg-slate-100 dark:bg-slate-900 border border-slate-200 dark:border-slate-800">TypeScript</span>
                            <span class="px-2.5 py-1 rounded-md bg-slate-100 dark:bg-slate-900 border border-slate-200 dark:border-slate-800">React / Next.js</span>
                            <span class="px-2.5 py-1 rounded-md bg-slate-100 dark:bg-slate-900 border border-slate-200 dark:border-slate-800">Python</span>
                            <span class="px-2.5 py-1 rounded-md bg-slate-100 dark:bg-slate-900 border border-slate-200 dark:border-slate-800">Tailwind CSS</span>
                            <span class="px-2.5 py-1 rounded-md bg-slate-100 dark:bg-slate-900 border border-slate-200 dark:border-slate-800">Node.js</span>
                        </div>
                    </div>

                    <!-- Right Hero Column: Interactive Terminal Preview -->
                    <div class="lg:col-span-5">
                        <div class="rounded-2xl bg-slate-900 border border-slate-800 shadow-2xl overflow-hidden glow-effect">
                            <!-- Terminal Bar -->
                            <div class="px-4 py-3 bg-slate-950 flex items-center justify-between border-b border-slate-800">
                                <div class="flex items-center space-x-2">
                                    <div class="w-3 h-3 rounded-full bg-rose-500"></div>
                                    <div class="w-3 h-3 rounded-full bg-amber-500"></div>
                                    <div class="w-3 h-3 rounded-full bg-emerald-500"></div>
                                </div>
                                <div class="text-xs font-mono text-slate-400">nowm@tech-terminal ~</div>
                                <div class="text-xs text-slate-500"><i class="fas fa-lock"></i></div>
                            </div>
                            <!-- Terminal Body -->
                            <div class="p-5 font-mono text-xs sm:text-sm text-slate-300 space-y-3 min-h-[300px]">
                                <p class="text-slate-500">// Terminal System Initialization v2.4</p>
                                <p><span class="text-brand-400">guest@nowm.tech:~$</span> info --fetch</p>
                                <div class="p-3 rounded bg-slate-950/70 border border-slate-800/80 space-y-1 text-xs">
                                    <p class="text-emerald-400">✓ System Status: 100% Operational</p>
                                    <p><span class="text-slate-400">Domain:</span> nowm.tech</p>
                                    <p><span class="text-slate-400">Specialization:</span> Full-Stack Web & Automation</p>
                                    <p><span class="text-slate-400">Location:</span> Global / Remote</p>
                                    <p><span class="text-slate-400">Uptime:</span> 99.98%</p>
                                </div>
                                <p><span class="text-brand-400">guest@nowm.tech:~$</span> execute-ping</p>
                                <p class="text-amber-400">PING nowm.tech (185.199.108.153) 56(84) bytes of data.</p>
                                <p class="text-emerald-400">64 bytes from github.io: icmp_seq=1 ttl=56 time=12.4 ms</p>
                                <div class="flex items-center text-brand-400 pt-2">
                                    <span>guest@nowm.tech:~$ </span>
                                    <span class="ml-2 inline-block w-2.5 h-4 bg-brand-400 animate-pulse"></span>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </section>

        <!-- Dynamic Live Stats / Metrics Counter Section -->
        <section class="py-10 border-y border-slate-200 dark:border-slate-800/80 bg-white/50 dark:bg-slate-900/40">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
                    <div class="p-4 rounded-xl glass">
                        <div class="text-3xl sm:text-4xl font-extrabold text-brand-600 dark:text-brand-400 font-mono" id="statProjects">0</div>
                        <div class="text-xs sm:text-sm text-slate-600 dark:text-slate-400 mt-1 font-medium">Projects Delivered</div>
                    </div>
                    <div class="p-4 rounded-xl glass">
                        <div class="text-3xl sm:text-4xl font-extrabold text-brand-cyan font-mono" id="statCommits">0</div>
                        <div class="text-xs sm:text-sm text-slate-600 dark:text-slate-400 mt-1 font-medium">Code Commits</div>
                    </div>
                    <div class="p-4 rounded-xl glass">
                        <div class="text-3xl sm:text-4xl font-extrabold text-brand-accent font-mono" id="statAccuracy">0%</div>
                        <div class="text-xs sm:text-sm text-slate-600 dark:text-slate-400 mt-1 font-medium">Test Coverage</div>
                    </div>
                    <div class="p-4 rounded-xl glass">
                        <div class="text-3xl sm:text-4xl font-extrabold text-emerald-500 font-mono" id="statUptime">0.0%</div>
                        <div class="text-xs sm:text-sm text-slate-600 dark:text-slate-400 mt-1 font-medium">Server Uptime</div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Projects Showcase Section -->
        <section id="projects" class="py-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-col md:flex-row md:items-end justify-between mb-10 gap-4">
                <div>
                    <h2 class="text-xs font-mono font-bold tracking-wider text-brand-500 uppercase">Portfolio</h2>
                    <p class="text-3xl font-extrabold text-slate-900 dark:text-white mt-1">Featured Projects & Tools</p>
                </div>

                <!-- Category Filters & Search -->
                <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-3">
                    <!-- Search Input -->
                    <div class="relative">
                        <input type="text" id="projectSearch" placeholder="Search tech or name..." class="w-full sm:w-48 pl-9 pr-3 py-2 text-sm rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 focus:outline-none focus:border-brand-500 text-slate-800 dark:text-slate-200">
                        <i class="fas fa-search absolute left-3 top-2.5 text-slate-400 text-xs"></i>
                    </div>
                    <!-- Tag Buttons -->
                    <div class="flex flex-wrap gap-1.5 p-1 rounded-xl bg-slate-200/70 dark:bg-slate-900 border border-slate-200 dark:border-slate-800" id="filterContainer">
                        <button class="filter-btn active px-3 py-1.5 rounded-lg text-xs font-medium transition-all bg-white dark:bg-slate-800 text-slate-900 dark:text-white shadow-sm" data-category="all">All</button>
                        <button class="filter-btn px-3 py-1.5 rounded-lg text-xs font-medium transition-all text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white" data-category="web">Web Apps</button>
                        <button class="filter-btn px-3 py-1.5 rounded-lg text-xs font-medium transition-all text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white" data-category="tools">Tools</button>
                        <button class="filter-btn px-3 py-1.5 rounded-lg text-xs font-medium transition-all text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white" data-category="bots">Scripts/Bots</button>
                    </div>
                </div>
            </div>

            <!-- Projects Grid -->
            <div id="projectsGrid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <!-- Dynamic Projects Rendered via JS -->
            </div>
        </section>

        <!-- Tech Stack & Interactive Dashboard Section -->
        <section id="skills" class="py-20 bg-slate-100/60 dark:bg-slate-900/50 border-y border-slate-200 dark:border-slate-800/80">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center max-w-2xl mx-auto mb-16">
                    <h2 class="text-xs font-mono font-bold tracking-wider text-brand-500 uppercase">Capabilities</h2>
                    <p class="text-3xl font-extrabold text-slate-900 dark:text-white mt-1">Tech Stack & Dashboard</p>
                    <p class="text-slate-600 dark:text-slate-400 mt-2 text-sm">Interactive overview of core proficiencies, architecture skills, and operational tools.</p>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
                    <!-- Left Column: Skill Bars -->
                    <div class="lg:col-span-7 space-y-6 glass p-6 sm:p-8 rounded-2xl">
                        <h3 class="text-lg font-bold text-slate-900 dark:text-white flex items-center gap-2">
                            <i class="fas fa-code text-brand-500"></i> Core Engineering Skills
                        </h3>

                        <!-- Skill Item -->
                        <div class="space-y-2">
                            <div class="flex justify-between text-sm font-medium">
                                <span class="text-slate-700 dark:text-slate-200">Frontend (React, TypeScript, Tailwind CSS)</span>
                                <span class="text-brand-500 font-mono">95%</span>
                            </div>
                            <div class="h-2.5 w-full bg-slate-200 dark:bg-slate-800 rounded-full overflow-hidden">
                                <div class="h-full bg-gradient-to-r from-brand-600 to-brand-400 rounded-full w-[95%] transition-all duration-1000"></div>
                            </div>
                        </div>

                        <!-- Skill Item -->
                        <div class="space-y-2">
                            <div class="flex justify-between text-sm font-medium">
                                <span class="text-slate-700 dark:text-slate-200">Backend & APIs (Node.js, Express, Python)</span>
                                <span class="text-brand-cyan font-mono">90%</span>
                            </div>
                            <div class="h-2.5 w-full bg-slate-200 dark:bg-slate-800 rounded-full overflow-hidden">
                                <div class="h-full bg-gradient-to-r from-cyan-600 to-brand-cyan rounded-full w-[90%] transition-all duration-1000"></div>
                            </div>
                        </div>

                        <!-- Skill Item -->
                        <div class="space-y-2">
                            <div class="flex justify-between text-sm font-medium">
                                <span class="text-slate-700 dark:text-slate-200">Databases & State (PostgreSQL, Redis, MongoDB)</span>
                                <span class="text-brand-accent font-mono">85%</span>
                            </div>
                            <div class="h-2.5 w-full bg-slate-200 dark:bg-slate-800 rounded-full overflow-hidden">
                                <div class="h-full bg-gradient-to-r from-indigo-600 to-brand-accent rounded-full w-[85%] transition-all duration-1000"></div>
                            </div>
                        </div>

                        <!-- Skill Item -->
                        <div class="space-y-2">
                            <div class="flex justify-between text-sm font-medium">
                                <span class="text-slate-700 dark:text-slate-200">DevOps & Cloud (GitHub Pages, Docker, AWS, CI/CD)</span>
                                <span class="text-emerald-500 font-mono">88%</span>
                            </div>
                            <div class="h-2.5 w-full bg-slate-200 dark:bg-slate-800 rounded-full overflow-hidden">
                                <div class="h-full bg-gradient-to-r from-emerald-600 to-emerald-400 rounded-full w-[88%] transition-all duration-1000"></div>
                            </div>
                        </div>
                    </div>

                    <!-- Right Column: Interactive Tech Badges & Health -->
                    <div class="lg:col-span-5 space-y-6">
                        <!-- Tech Cloud Card -->
                        <div class="glass p-6 sm:p-8 rounded-2xl space-y-4">
                            <h3 class="text-lg font-bold text-slate-900 dark:text-white flex items-center gap-2">
                                <i class="fas fa-microchip text-brand-cyan"></i> Ecosystem Badges
                            </h3>
                            <div class="flex flex-wrap gap-2">
                                <span class="px-3 py-1.5 rounded-lg text-xs font-mono bg-slate-200 dark:bg-slate-800 text-slate-800 dark:text-slate-200 hover:scale-105 transition-transform cursor-default">HTML5/CSS3</span>
                                <span class="px-3 py-1.5 rounded-lg text-xs font-mono bg-slate-200 dark:bg-slate-800 text-slate-800 dark:text-slate-200 hover:scale-105 transition-transform cursor-default">JavaScript ES6+</span>
                                <span class="px-3 py-1.5 rounded-lg text-xs font-mono bg-slate-200 dark:bg-slate-800 text-slate-800 dark:text-slate-200 hover:scale-105 transition-transform cursor-default">TypeScript</span>
                                <span class="px-3 py-1.5 rounded-lg text-xs font-mono bg-slate-200 dark:bg-slate-800 text-slate-800 dark:text-slate-200 hover:scale-105 transition-transform cursor-default">Git / GitHub</span>
                                <span class="px-3 py-1.5 rounded-lg text-xs font-mono bg-slate-200 dark:bg-slate-800 text-slate-800 dark:text-slate-200 hover:scale-105 transition-transform cursor-default">REST APIs</span>
                                <span class="px-3 py-1.5 rounded-lg text-xs font-mono bg-slate-200 dark:bg-slate-800 text-slate-800 dark:text-slate-200 hover:scale-105 transition-transform cursor-default">GraphQL</span>
                                <span class="px-3 py-1.5 rounded-lg text-xs font-mono bg-slate-200 dark:bg-slate-800 text-slate-800 dark:text-slate-200 hover:scale-105 transition-transform cursor-default">Tailwind</span>
                                <span class="px-3 py-1.5 rounded-lg text-xs font-mono bg-slate-200 dark:bg-slate-800 text-slate-800 dark:text-slate-200 hover:scale-105 transition-transform cursor-default">Vite</span>
                                <span class="px-3 py-1.5 rounded-lg text-xs font-mono bg-slate-200 dark:bg-slate-800 text-slate-800 dark:text-slate-200 hover:scale-105 transition-transform cursor-default">Jest / Cypress</span>
                            </div>
                        </div>

                        <!-- System Health Card -->
                        <div class="glass p-6 sm:p-8 rounded-2xl space-y-4">
                            <h3 class="text-lg font-bold text-slate-900 dark:text-white flex items-center justify-between">
                                <span class="flex items-center gap-2"><i class="fas fa-server text-emerald-500"></i> Domain Health</span>
                                <span class="text-xs font-mono text-emerald-500 bg-emerald-500/10 px-2 py-1 rounded">SSL ACTIVE</span>
                            </h3>
                            <div class="space-y-3 text-sm">
                                <div class="flex justify-between py-1 border-b border-slate-200 dark:border-slate-800">
                                    <span class="text-slate-500 dark:text-slate-400">Domain</span>
                                    <span class="font-mono font-semibold">nowm.tech</span>
                                </div>
                                <div class="flex justify-between py-1 border-b border-slate-200 dark:border-slate-800">
                                    <span class="text-slate-500 dark:text-slate-400">DNS Infrastructure</span>
                                    <span class="font-mono font-semibold">GitHub Anycast DNS</span>
                                </div>
                                <div class="flex justify-between py-1">
                                    <span class="text-slate-500 dark:text-slate-400">HTTP/2 & HTTPS</span>
                                    <span class="text-emerald-500 font-mono font-semibold">Enabled</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Live Code Playground Sandbox Section -->
        <section id="playground" class="py-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center max-w-2xl mx-auto mb-12">
                <h2 class="text-xs font-mono font-bold tracking-wider text-brand-500 uppercase">Interactive Playground</h2>
                <p class="text-3xl font-extrabold text-slate-900 dark:text-white mt-1">Live JS Code Sandbox</p>
                <p class="text-slate-600 dark:text-slate-400 mt-2 text-sm">Edit the JavaScript below and click <strong>Run Code</strong> to execute live code directly inside your browser.</p>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 rounded-2xl bg-slate-900 border border-slate-800 p-4 sm:p-6 shadow-2xl">
                <!-- Code Editor Column -->
                <div class="flex flex-col space-y-3">
                    <div class="flex items-center justify-between text-xs font-mono text-slate-400 pb-2 border-b border-slate-800">
                        <span class="flex items-center gap-2"><i class="fab fa-js text-yellow-400"></i> sandbox.js</span>
                        <div class="space-x-2">
                            <button id="resetCodeBtn" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 transition-colors">Reset</button>
                            <button id="runCodeBtn" class="px-3 py-1 rounded bg-brand-500 hover:bg-brand-400 text-white font-bold transition-colors">
                                <i class="fas fa-play text-xs mr-1"></i> Run Code
                            </button>
                        </div>
                    </div>
                    <textarea id="codeEditor" spellcheck="false" class="w-full h-64 sm:h-80 p-4 bg-slate-950 text-slate-200 font-mono text-xs sm:text-sm rounded-xl border border-slate-800 focus:outline-none focus:border-brand-500 resize-none leading-relaxed">// Welcome to the nowm.tech playground!
// Modify the script below and click 'Run Code'

function calculateTechStack(stack) {
  console.log("Analyzing stack for nowm.tech...");
  const status = stack.map(item => `[OK] ${item} loaded.`);
  return status.join('\n');
}

const myStack = ["React", "TypeScript", "TailwindCSS", "Node.js"];
console.log(calculateTechStack(myStack));
console.log("\nSystem initialized successfully!");
</textarea>
                </div>

                <!-- Terminal Output Column -->
                <div class="flex flex-col space-y-3">
                    <div class="flex items-center justify-between text-xs font-mono text-slate-400 pb-2 border-b border-slate-800">
                        <span class="flex items-center gap-2"><i class="fas fa-terminal text-brand-400"></i> Console Output</span>
                        <button id="clearConsoleBtn" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 transition-colors">Clear</button>
                    </div>
                    <div id="consoleOutput" class="w-full h-64 sm:h-80 p-4 bg-slate-950 text-emerald-400 font-mono text-xs sm:text-sm rounded-xl border border-slate-800 overflow-y-auto whitespace-pre-wrap">
// Output will appear here...
                    </div>
                </div>
            </div>
        </section>

        <!-- Contact & Connect Section -->
        <section id="contact" class="py-20 bg-slate-100/60 dark:bg-slate-900/50 border-t border-slate-200 dark:border-slate-800/80">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="grid grid-cols-1 lg:grid-cols-12 gap-12">
                    
                    <!-- Left Info Column -->
                    <div class="lg:col-span-5 space-y-6">
                        <div>
                            <h2 class="text-xs font-mono font-bold tracking-wider text-brand-500 uppercase">Connect</h2>
                            <p class="text-3xl font-extrabold text-slate-900 dark:text-white mt-1">Let's Build Something Great</p>
                        </div>
                        <p class="text-slate-600 dark:text-slate-400 text-sm leading-relaxed">
                            Have a project in mind, need custom development, or want to collaborate under <strong>nowm.tech</strong>? Send a message and let's turn ideas into functional technology.
                        </p>

                        <!-- Contact List -->
                        <div class="space-y-4 pt-4">
                            <div class="flex items-start gap-4">
                                <div class="w-10 h-10 rounded-xl bg-brand-500/10 text-brand-500 flex items-center justify-center shrink-0">
                                    <i class="fas fa-globe text-base"></i>
                                </div>
                                <div>
                                    <p class="text-xs text-slate-500 dark:text-slate-400 uppercase font-mono">Domain Host</p>
                                    <p class="font-semibold text-slate-800 dark:text-slate-200">nowm.tech</p>
                                </div>
                            </div>

                            <div class="flex items-start gap-4">
                                <div class="w-10 h-10 rounded-xl bg-brand-500/10 text-brand-500 flex items-center justify-center shrink-0">
                                    <i class="fas fa-envelope text-base"></i>
                                </div>
                                <div>
                                    <p class="text-xs text-slate-500 dark:text-slate-400 uppercase font-mono">Direct Email</p>
                                    <div class="flex items-center gap-2">
                                        <span class="font-semibold text-slate-800 dark:text-slate-200" id="contactEmail">contact@nowm.tech</span>
                                        <button id="copyEmailBtn" class="text-xs text-brand-500 hover:text-brand-400 p-1" title="Copy Email">
                                            <i class="fas fa-copy"></i>
                                        </button>
                                    </div>
                                </div>
                            </div>

                            <div class="flex items-start gap-4">
                                <div class="w-10 h-10 rounded-xl bg-brand-500/10 text-brand-500 flex items-center justify-center shrink-0">
                                    <i class="fab fa-github text-base"></i>
                                </div>
                                <div>
                                    <p class="text-xs text-slate-500 dark:text-slate-400 uppercase font-mono">Repository</p>
                                    <a href="https://github.com" target="_blank" rel="noopener" class="font-semibold text-slate-800 dark:text-slate-200 hover:text-brand-500 transition-colors">
                                        github.com/nowm-tech
                                    </a>
                                </div>
                            </div>
                        </div>

                        <!-- Social Media Icons -->
                        <div class="pt-4 flex items-center gap-3">
                            <a href="#" aria-label="GitHub" class="w-10 h-10 rounded-xl glass flex items-center justify-center text-slate-700 dark:text-slate-300 hover:text-brand-500 dark:hover:text-brand-400 hover:scale-110 transition-all">
                                <i class="fab fa-github text-lg"></i>
                            </a>
                            <a href="#" aria-label="Twitter" class="w-10 h-10 rounded-xl glass flex items-center justify-center text-slate-700 dark:text-slate-300 hover:text-brand-500 dark:hover:text-brand-400 hover:scale-110 transition-all">
                                <i class="fab fa-x-twitter text-lg"></i>
                            </a>
                            <a href="#" aria-label="LinkedIn" class="w-10 h-10 rounded-xl glass flex items-center justify-center text-slate-700 dark:text-slate-300 hover:text-brand-500 dark:hover:text-brand-400 hover:scale-110 transition-all">
                                <i class="fab fa-linkedin-in text-lg"></i>
                            </a>
                            <a href="#" aria-label="Discord" class="w-10 h-10 rounded-xl glass flex items-center justify-center text-slate-700 dark:text-slate-300 hover:text-brand-500 dark:hover:text-brand-400 hover:scale-110 transition-all">
                                <i class="fab fa-discord text-lg"></i>
                            </a>
                        </div>
                    </div>

                    <!-- Right Form Column -->
                    <div class="lg:col-span-7 glass p-6 sm:p-8 rounded-2xl relative">
                        <form id="contactForm" class="space-y-4">
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                                <div>
                                    <label class="block text-xs font-mono font-medium text-slate-700 dark:text-slate-300 mb-1">YOUR NAME</label>
                                    <input type="text" id="formName" required placeholder="Alex Mercer" class="w-full px-4 py-3 text-sm rounded-xl bg-white dark:bg-slate-950 border border-slate-200 dark:border-slate-800 focus:outline-none focus:border-brand-500 text-slate-800 dark:text-slate-200">
                                </div>
                                <div>
                                    <label class="block text-xs font-mono font-medium text-slate-700 dark:text-slate-300 mb-1">YOUR EMAIL</label>
                                    <input type="email" id="formEmail" required placeholder="alex@example.com" class="w-full px-4 py-3 text-sm rounded-xl bg-white dark:bg-slate-950 border border-slate-200 dark:border-slate-800 focus:outline-none focus:border-brand-500 text-slate-800 dark:text-slate-200">
                                </div>
                            </div>

                            <div>
                                <label class="block text-xs font-mono font-medium text-slate-700 dark:text-slate-300 mb-1">SUBJECT</label>
                                <input type="text" id="formSubject" required placeholder="Project Collaboration / Inquiries" class="w-full px-4 py-3 text-sm rounded-xl bg-white dark:bg-slate-950 border border-slate-200 dark:border-slate-800 focus:outline-none focus:border-brand-500 text-slate-800 dark:text-slate-200">
                            </div>

                            <div>
                                <label class="block text-xs font-mono font-medium text-slate-700 dark:text-slate-300 mb-1">MESSAGE</label>
                                <textarea id="formMessage" required rows="4" placeholder="Tell me about your project goals or custom tech needs..." class="w-full px-4 py-3 text-sm rounded-xl bg-white dark:bg-slate-950 border border-slate-200 dark:border-slate-800 focus:outline-none focus:border-brand-500 text-slate-800 dark:text-slate-200 resize-none"></textarea>
                            </div>

                            <button type="submit" id="submitBtn" class="w-full py-3.5 rounded-xl bg-gradient-to-r from-brand-600 to-brand-500 text-white font-semibold text-sm shadow-md hover:shadow-lg hover:from-brand-500 hover:to-brand-400 transition-all flex items-center justify-center gap-2">
                                <span>Send Message</span>
                                <i class="fas fa-paper-plane text-xs"></i>
                            </button>
                        </form>

                        <!-- Toast Feedback Container -->
                        <div id="formToast" class="hidden absolute inset-0 bg-slate-900/95 backdrop-blur-md rounded-2xl p-6 flex flex-col items-center justify-center text-center space-y-4">
                            <div class="w-16 h-16 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center text-2xl">
                                <i class="fas fa-check"></i>
                            </div>
                            <h3 class="text-xl font-bold text-white">Message Transmitted!</h3>
                            <p class="text-sm text-slate-300 max-w-sm">Thank you for reaching out to <strong>nowm.tech</strong>. Your inquiry has been received successfully.</p>
                            <button id="closeToastBtn" class="px-6 py-2.5 rounded-xl bg-brand-500 text-white font-medium text-xs font-mono">Dismiss</button>
                        </div>
                    </div>

                </div>
            </div>
        </section>
    </main>

    <!-- Project Details Modal -->
    <div id="projectModal" class="fixed inset-0 z-50 hidden bg-slate-950/80 backdrop-blur-sm flex items-center justify-center p-4">
        <div class="glass w-full max-w-2xl rounded-2xl overflow-hidden shadow-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800">
            <div class="p-6 border-b border-slate-200 dark:border-slate-800 flex items-center justify-between">
                <h3 id="modalTitle" class="text-xl font-bold text-slate-900 dark:text-white"></h3>
                <button id="closeModalBtn" class="p-2 text-slate-400 hover:text-slate-600 dark:hover:text-slate-200">
                    <i class="fas fa-times text-lg"></i>
                </button>
            </div>
            <div class="p-6 space-y-4">
                <div id="modalBadges" class="flex flex-wrap gap-2"></div>
                <p id="modalDesc" class="text-slate-600 dark:text-slate-300 text-sm leading-relaxed"></p>
                <div class="p-4 rounded-xl bg-slate-100 dark:bg-slate-950/60 border border-slate-200 dark:border-slate-800 space-y-2">
                    <h4 class="text-xs font-mono font-bold text-slate-500 uppercase">Key Features</h4>
                    <ul id="modalFeatures" class="list-disc list-inside text-xs sm:text-sm text-slate-700 dark:text-slate-300 space-y-1"></ul>
                </div>
            </div>
            <div class="p-6 border-t border-slate-200 dark:border-slate-800 flex justify-end gap-3">
                <button id="modalDismiss" class="px-4 py-2 rounded-xl border border-slate-300 dark:border-slate-700 text-xs font-medium text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800">Close</button>
                <a id="modalLink" href="#" target="_blank" rel="noopener" class="px-4 py-2 rounded-xl bg-brand-500 text-white text-xs font-medium hover:bg-brand-400 flex items-center gap-2">
                    <span>View Repository</span>
                    <i class="fas fa-external-link-alt"></i>
                </a>
            </div>
        </div>
    </div>

    <!-- Footer -->
    <footer class="border-t border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-950 py-8 text-xs text-slate-500 dark:text-slate-400">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-4">
            <div class="flex items-center gap-2 font-mono">
                <span class="w-2 h-2 rounded-full bg-brand-500"></span>
                <span>Hosted via GitHub Pages on <strong class="text-slate-800 dark:text-slate-200">nowm.tech</strong></span>
            </div>
            <p>&copy; <span id="yearSpan"></span> nowm.tech. All rights reserved.</p>
        </div>
    </footer>

    <!-- Interactive Logic Script -->
    <script>
        // Sample Projects Data
        const projectsData = [
            {
                id: 1,
                title: 'TechHub Analytics Dashboard',
                category: 'web',
                shortDesc: 'Real-time performance monitoring dashboard with live data visualizations.',
                fullDesc: 'A high-speed dashboard for tracking web infrastructure telemetry, user events, and API latency metrics.',
                tags: ['React', 'TypeScript', 'Tailwind', 'Recharts'],
                features: ['Live WebSocket metrics streaming', 'Dark/Light mode themes', 'Export reports to CSV/PDF'],
                repo: 'https://github.com'
            },
            {
                id: 2,
                title: 'Crypto & Forex Trading Bot',
                category: 'bots',
                shortDesc: 'Automated algorithmic trading strategy runner powered by Python & REST API.',
                fullDesc: 'An execution bot featuring custom indicator signals, stop-loss protection, and paper-trading backtesting capabilities.',
                tags: ['Python', 'CCXT', 'Asyncio', 'Docker'],
                features: ['RSI & MACD strategy modules', 'Telegram real-time alerts', 'Backtesting engine'],
                repo: 'https://github.com'
            },
            {
                id: 3,
                title: 'Developer CLI Toolkit',
                category: 'tools',
                shortDesc: 'Command-line tool to streamline Git workflows and automated deployments.',
                fullDesc: 'A unified CLI utility designed for fast workspace setups, automated release notes generation, and GitHub Pages sync.',
                tags: ['Node.js', 'Commander.js', 'Bash'],
                features: ['Custom scaffolding templates', 'Automated CNAME setup', 'Git hook integrations'],
                repo: 'https://github.com'
            },
            {
                id: 4,
                title: 'SaaS Landing Engine',
                category: 'web',
                shortDesc: 'Ultra-lightweight, SEO-optimized landing page template for modern tech products.',
                fullDesc: 'A performance-first static web generator crafted with accessibility, responsive layout, and zero bloat.',
                tags: ['HTML5', 'Tailwind CSS', 'JavaScript'],
                features: ['100/100 Lighthouse score', 'Built-in contact modal', 'Customizable design tokens'],
                repo: 'https://github.com'
            },
            {
                id: 5,
                title: 'API Status & Health Monitor',
                category: 'tools',
                shortDesc: 'Lightweight pinger script that checks website uptime and response latency.',
                fullDesc: 'An automated utility that periodically sends HTTP requests to specified domain targets and logs latency statistics.',
                tags: ['Python', 'Flask', 'SQLite'],
                features: ['Automated email/webhook notifications', 'Historical uptime charts', 'Low resource footprint'],
                repo: 'https://github.com'
            },
            {
                id: 6,
                title: 'Discord Automation Bot',
                category: 'bots',
                shortDesc: 'Custom server management and verification bot for tech communities.',
                fullDesc: 'A feature-rich Discord bot designed for role management, modern slash commands, and automated moderation.',
                tags: ['TypeScript', 'Discord.js', 'MongoDB'],
                features: ['OAuth2 member verification', 'Custom command triggers', 'Role assignment dashboard'],
                repo: 'https://github.com'
            }
        ];

        // Theme Toggle Logic
        const themeToggle = document.getElementById('themeToggle');
        const themeIcon = document.getElementById('themeIcon');
        const html = document.documentElement;

        function updateThemeIcon() {
            if (html.classList.contains('dark')) {
                themeIcon.className = 'fas fa-sun text-amber-400';
            } else {
                themeIcon.className = 'fas fa-moon text-slate-700';
            }
        }
        updateThemeIcon();

        themeToggle.addEventListener('click', () => {
            html.classList.toggle('dark');
            updateThemeIcon();
        });

        // Dynamic Typing Effect in Hero
        const typedTextElement = document.getElementById('typedText');
        const phrases = ['Modern Web Applications.', 'Algorithmic Trading Tools.', 'Developer Automation Scripts.', 'Scalable Cloud Systems.'];
        let phraseIndex = 0;
        let charIndex = 0;
        let isDeleting = false;

        function typeLoop() {
            const currentPhrase = phrases[phraseIndex];
            
            if (isDeleting) {
                typedTextElement.textContent = currentPhrase.substring(0, charIndex - 1);
                charIndex--;
            } else {
                typedTextElement.textContent = currentPhrase.substring(0, charIndex + 1);
                charIndex++;
            }

            let speed = isDeleting ? 40 : 80;

            if (!isDeleting && charIndex === currentPhrase.length) {
                speed = 2000; // Pause at top
                isDeleting = true;
            } else if (isDeleting && charIndex === 0) {
                isDeleting = false;
                phraseIndex = (phraseIndex + 1) % phrases.length;
                speed = 400;
            }

            setTimeout(typeLoop, speed);
        }
        typeLoop();

        // Animated Metric Counters
        function animateCounter(id, target, isPercent = false, decimal = false) {
            const element = document.getElementById(id);
            let start = 0;
            const duration = 2000;
            const stepTime = 30;
            const steps = duration / stepTime;
            const increment = target / steps;

            const timer = setInterval(() => {
                start += increment;
                if (start >= target) {
                    start = target;
                    clearInterval(timer);
                }
                if (decimal) {
                    element.textContent = start.toFixed(1) + (isPercent ? '%' : '');
                } else {
                    element.textContent = Math.floor(start) + (isPercent ? '%' : '+');
                }
            }, stepTime);
        }

        // Trigger counters when scrolled into view
        let countersTriggered = false;
        window.addEventListener('scroll', () => {
            if (!countersTriggered && window.scrollY > 100) {
                countersTriggered = true;
                animateCounter('statProjects', 24);
                animateCounter('statCommits', 1450);
                animateCounter('statAccuracy', 99, true);
                animateCounter('statUptime', 99.9, true, true);
            }
        });
        // Initial check
        if (window.scrollY > 100) {
            countersTriggered = true;
            animateCounter('statProjects', 24);
            animateCounter('statCommits', 1450);
            animateCounter('statAccuracy', 99, true);
            animateCounter('statUptime', 99.9, true, true);
        }

        // Render Projects Grid
        const projectsGrid = document.getElementById('projectsGrid');
        const projectSearch = document.getElementById('projectSearch');
        const filterBtns = document.querySelectorAll('.filter-btn');

        let currentCategory = 'all';

        function renderProjects() {
            const query = projectSearch.value.toLowerCase();
            projectsGrid.innerHTML = '';

            const filtered = projectsData.filter(p => {
                const matchesCategory = currentCategory === 'all' || p.category === currentCategory;
                const matchesSearch = p.title.toLowerCase().includes(query) || 
                                      p.shortDesc.toLowerCase().includes(query) ||
                                      p.tags.some(t => t.toLowerCase().includes(query));
                return matchesCategory && matchesSearch;
            });

            if (filtered.length === 0) {
                projectsGrid.innerHTML = `
                    <div class="col-span-full py-12 text-center text-slate-500 font-mono">
                        <i class="fas fa-folder-open text-3xl mb-2 text-slate-400"></i>
                        <p>No projects match your current search criteria.</p>
                    </div>
                `;
                return;
            }

            filtered.forEach(project => {
                const card = document.createElement('div');
                card.className = 'glass rounded-2xl p-6 flex flex-col justify-between hover:border-brand-500/50 transition-all hover:-translate-y-1 group cursor-pointer';
                card.onclick = () => openModal(project);

                card.innerHTML = `
                    <div class="space-y-3">
                        <div class="flex items-center justify-between">
                            <span class="text-xs font-mono px-2.5 py-1 rounded-md bg-brand-500/10 text-brand-500 uppercase font-semibold">
                                ${project.category}
                            </span>
                            <i class="fas fa-arrow-right text-slate-400 group-hover:text-brand-500 group-hover:translate-x-1 transition-all"></i>
                        </div>
                        <h3 class="text-lg font-bold text-slate-900 dark:text-white group-hover:text-brand-500 transition-colors">
                            ${project.title}
                        </h3>
                        <p class="text-xs sm:text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
                            ${project.shortDesc}
                        </p>
                    </div>
                    <div class="pt-4 mt-4 border-t border-slate-200 dark:border-slate-800/80 flex flex-wrap gap-1.5">
                        ${project.tags.map(t => `<span class="text-[11px] font-mono px-2 py-0.5 rounded bg-slate-200/60 dark:bg-slate-800 text-slate-700 dark:text-slate-300">${t}</span>`).join('')}
                    </div>
                `;
                projectsGrid.appendChild(card);
            });
        }

        // Filter Handlers
        filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                filterBtns.forEach(b => {
                    b.classList.remove('active', 'bg-white', 'dark:bg-slate-800', 'text-slate-900', 'dark:text-white', 'shadow-sm');
                    b.classList.add('text-slate-600', 'dark:text-slate-400');
                });
                btn.classList.add('active', 'bg-white', 'dark:bg-slate-800', 'text-slate-900', 'dark:text-white', 'shadow-sm');
                btn.classList.remove('text-slate-600', 'dark:text-slate-400');
                currentCategory = btn.getAttribute('data-category');
                renderProjects();
            });
        });

        projectSearch.addEventListener('input', renderProjects);
        renderProjects();

        // Project Modal Logic
        const modal = document.getElementById('projectModal');
        const modalTitle = document.getElementById('modalTitle');
        const modalDesc = document.getElementById('modalDesc');
        const modalBadges = document.getElementById('modalBadges');
        const modalFeatures = document.getElementById('modalFeatures');
        const modalLink = document.getElementById('modalLink');
        const closeModalBtn = document.getElementById('closeModalBtn');
        const modalDismiss = document.getElementById('modalDismiss');

        function openModal(project) {
            modalTitle.textContent = project.title;
            modalDesc.textContent = project.fullDesc;
            modalLink.href = project.repo;

            modalBadges.innerHTML = project.tags.map(t => 
                `<span class="text-xs font-mono px-2.5 py-1 rounded bg-brand-500/10 text-brand-500 font-semibold">${t}</span>`
            ).join('');

            modalFeatures.innerHTML = project.features.map(f => `<li>${f}</li>`).join('');

            modal.classList.remove('hidden');
        }

        function closeModal() {
            modal.classList.add('hidden');
        }

        closeModalBtn.addEventListener('click', closeModal);
        modalDismiss.addEventListener('click', closeModal);
        modal.addEventListener('click', (e) => {
            if (e.target === modal) closeModal();
        });

        // Sandbox Code Execution Logic
        const codeEditor = document.getElementById('codeEditor');
        const consoleOutput = document.getElementById('consoleOutput');
        const runCodeBtn = document.getElementById('runCodeBtn');
        const resetCodeBtn = document.getElementById('resetCodeBtn');
        const clearConsoleBtn = document.getElementById('clearConsoleBtn');

        const defaultCode = codeEditor.value;

        runCodeBtn.addEventListener('click', () => {
            consoleOutput.textContent = '';
            const logs = [];
            
            // Custom Safe Console Implementation
            const customConsole = {
                log: (...args) => {
                    logs.push(args.map(a => typeof a === 'object' ? JSON.stringify(a, null, 2) : a).join(' '));
                },
                error: (...args) => {
                    logs.push('[ERROR] ' + args.join(' '));
                },
                warn: (...args) => {
                    logs.push('[WARN] ' + args.join(' '));
                }
            };

            try {
                const runFunction = new Function('console', codeEditor.value);
                runFunction(customConsole);
                consoleOutput.textContent = logs.join('\n') || '// Script executed (No output generated).';
            } catch (err) {
                consoleOutput.textContent = `Runtime Error: ${err.message}`;
            }
        });

        resetCodeBtn.addEventListener('click', () => {
            codeEditor.value = defaultCode;
            consoleOutput.textContent = '// Code reset to default.';
        });

        clearConsoleBtn.addEventListener('click', () => {
            consoleOutput.textContent = '';
        });

        // Contact Form Submission Logic
        const contactForm = document.getElementById('contactForm');
        const formToast = document.getElementById('formToast');
        const closeToastBtn = document.getElementById('closeToastBtn');
        const copyEmailBtn = document.getElementById('copyEmailBtn');

        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            formToast.classList.remove('hidden');
            contactForm.reset();
        });

        closeToastBtn.addEventListener('click', () => {
            formToast.classList.add('hidden');
        });

        // Copy Email to Clipboard
        copyEmailBtn.addEventListener('click', () => {
            const emailText = document.getElementById('contactEmail').textContent;
            
            // execCommand fallback for strict browser sandboxes
            const tempInput = document.createElement('input');
            tempInput.value = emailText;
            document.body.appendChild(tempInput);
            tempInput.select();
            document.execCommand('copy');
            document.body.removeChild(tempInput);

            copyEmailBtn.innerHTML = '<i class="fas fa-check text-emerald-500"></i>';
            setTimeout(() => {
                copyEmailBtn.innerHTML = '<i class="fas fa-copy"></i>';
            }, 2000);
        });

        // Mobile Menu Toggle
        const mobileMenuBtn = document.getElementById('mobileMenuBtn');
        const mobileMenu = document.getElementById('mobileMenu');

        mobileMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });

        // Set Copyright Year
        document.getElementById('yearSpan').textContent = new Date().getFullYear();
    </script>
</body>
</html>
