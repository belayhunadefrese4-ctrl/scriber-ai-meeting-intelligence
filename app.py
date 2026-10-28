<!DOCTYPE html>
<html lang="en" class="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scriber AI Pro — Amharic & English Speech-to-Text & Executive ቃለ ጉባዔ Generator</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Google Fonts Inter & Noto Sans Ethiopic -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Noto+Sans+Ethiopic:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        burgundy: {
                            50: '#fdf2f4',
                            100: '#fbe6e9',
                            200: '#f7cfd5',
                            500: '#a31534',
                            700: '#800020',
                            800: '#66001a',
                            900: '#4d0013',
                        },
                        navy: {
                            800: '#1e293b',
                            900: '#0f172a',
                            950: '#080d1a',
                        },
                        gold: {
                            400: '#fbbf24',
                            500: '#f59e0b',
                            600: '#d97706',
                        }
                    },
                    fontFamily: {
                        sans: ['Inter', 'Noto Sans Ethiopic', 'sans-serif'],
                    }
                }
            }
        }
    </script>
    <style>
        .glass-card {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(226, 232, 240, 0.8);
        }
        .dark .glass-card {
            background: rgba(15, 23, 42, 0.9);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(30, 41, 59, 0.8);
        }
        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        ::-webkit-scrollbar-track {
            background: transparent;
        }
        ::-webkit-scrollbar-thumb {
            background: #CBD5E1;
            border-radius: 4px;
        }
        .dark ::-webkit-scrollbar-thumb {
            background: #334155;
        }
    </style>
</head>
<body class="bg-slate-50 text-slate-900 dark:bg-navy-950 dark:text-slate-100 font-sans min-h-screen flex flex-col transition-colors duration-200">

    <!-- NAVIGATION HEADER -->
    <header class="sticky top-0 z-40 bg-white/90 dark:bg-navy-900/90 backdrop-blur-md border-b border-slate-200 dark:border-slate-800 px-4 lg:px-8 py-3 transition-colors duration-200">
        <div class="max-w-7xl mx-auto flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-burgundy-700 to-burgundy-500 flex items-center justify-center text-white shadow-md shadow-burgundy-700/20">
                    <i class="fa-solid fa-microphone-lines text-xl"></i>
                </div>
                <div>
                    <div class="flex items-center space-x-2">
                        <span class="font-extrabold text-xl tracking-tight text-navy-900 dark:text-white">Scriber<span class="text-burgundy-700 dark:text-burgundy-500">AI</span> Pro</span>
                        <span class="bg-burgundy-100 dark:bg-burgundy-900/40 text-burgundy-800 dark:text-burgundy-300 text-[10px] font-bold px-2 py-0.5 rounded-full uppercase tracking-wider">Enterprise v3.5</span>
                    </div>
                    <p id="appSubHeader" class="text-xs text-slate-500 dark:text-slate-400 hidden sm:block">Amharic &amp; English Speech-to-Text, Executive ቃለ ጉባዔ Generator &amp; Audio Analytics</p>
                </div>
            </div>

            <div class="flex items-center space-x-3">
                <!-- UI Language Selector Toggle -->
                <div class="relative inline-block">
                    <button id="uiLangBtn" onclick="toggleLangDropdown()" class="flex items-center space-x-1.5 px-3 py-1.5 rounded-xl border border-slate-300 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-800 text-xs font-semibold transition">
                        <span id="uiLangFlag">🇪🇹</span>
                        <span id="uiLangText">አማርኛ</span>
                        <i class="fa-solid fa-chevron-down text-[10px] ml-1"></i>
                    </button>
                    <div id="langDropdown" class="hidden absolute right-0 mt-2 w-44 rounded-xl shadow-xl bg-white dark:bg-navy-900 border border-slate-200 dark:border-slate-800 z-50 overflow-hidden text-xs">
                        <button onclick="setSystemLanguage('am')" class="w-full text-left px-3 py-2 hover:bg-slate-100 dark:hover:bg-navy-800 flex items-center space-x-2 font-medium"><span>🇪🇹</span><span>አማርኛ (Amharic)</span></button>
                        <button onclick="setSystemLanguage('en')" class="w-full text-left px-3 py-2 hover:bg-slate-100 dark:hover:bg-navy-800 flex items-center space-x-2 font-medium"><span>🇬🇧</span><span>English</span></button>
                        <button onclick="setSystemLanguage('om')" class="w-full text-left px-3 py-2 hover:bg-slate-100 dark:hover:bg-navy-800 flex items-center space-x-2 font-medium"><span>🇪🇹</span><span>Afaan Oromoo</span></button>
                        <button onclick="setSystemLanguage('ti')" class="w-full text-left px-3 py-2 hover:bg-slate-100 dark:hover:bg-navy-800 flex items-center space-x-2 font-medium"><span>🇪🇹</span><span>ትግርኛ (Tigrinya)</span></button>
                        <button onclick="setSystemLanguage('fr')" class="w-full text-left px-3 py-2 hover:bg-slate-100 dark:hover:bg-navy-800 flex items-center space-x-2 font-medium"><span>🇫🇷</span><span>Français</span></button>
                        <button onclick="setSystemLanguage('ar')" class="w-full text-left px-3 py-2 hover:bg-slate-100 dark:hover:bg-navy-800 flex items-center space-x-2 font-medium"><span>🇸🇦</span><span>العربية</span></button>
                    </div>
                </div>

                <!-- Dark Mode Toggle -->
                <button onclick="toggleDarkMode()" class="p-2 rounded-xl border border-slate-300 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-600 dark:text-slate-300 transition" title="Toggle Theme">
                    <i class="fa-solid fa-moon dark:hidden"></i>
                    <i class="fa-solid fa-sun hidden dark:block text-amber-400"></i>
                </button>

                <!-- Subscription Upgrade Button -->
                <button onclick="openPaymentModal()" class="flex items-center space-x-2 bg-gradient-to-r from-burgundy-700 to-burgundy-800 hover:from-burgundy-800 hover:to-burgundy-900 text-white text-xs font-semibold px-4 py-2 rounded-xl shadow-md shadow-burgundy-700/20 transition transform active:scale-95">
                    <i class="fa-solid fa-crown text-gold-400"></i>
                    <span id="navUpgradeBtn">Upgrade Plan</span>
                </button>
            </div>
        </div>
    </header>

    <!-- MAIN CONTAINER -->
    <main class="flex-grow max-w-7xl w-full mx-auto px-4 lg:px-8 py-6 space-y-6">

        <!-- SYSTEM METERS & CONFIGURATION BAR -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            
            <!-- Free Trial Counter Card -->
            <div class="glass-card rounded-2xl p-4 flex items-center justify-between shadow-sm">
                <div class="space-y-1">
                    <div class="flex items-center space-x-2 text-xs font-semibold text-slate-500 dark:text-slate-400">
                        <i class="fa-solid fa-clock-rotate-left text-burgundy-700 dark:text-burgundy-500"></i>
                        <span id="labelTrialMeter">Trial Usage Meter</span>
                    </div>
                    <div class="text-lg font-bold">
                        <span id="usedMinutes">2.5</span> / <span id="maxMinutes">10.0</span> <span class="text-xs font-normal text-slate-500">mins used</span>
                    </div>
                    <p id="labelFreeTrialBadge" class="text-[10px] text-emerald-600 dark:text-emerald-400 font-semibold"><i class="fa-solid fa-gift mr-1"></i>First 10 Mins Free</p>
                </div>
                <div class="w-16 h-16 relative flex items-center justify-center">
                    <svg class="w-full h-full transform -rotate-90">
                        <circle cx="32" cy="32" r="26" stroke="currentColor" stroke-width="5" class="text-slate-200 dark:text-slate-800" fill="transparent"/>
                        <circle id="meterCircle" cx="32" cy="32" r="26" stroke="currentColor" stroke-width="5" class="text-burgundy-700 dark:text-burgundy-500 transition-all duration-500" fill="transparent" stroke-dasharray="163" stroke-dashoffset="122"/>
                    </svg>
                    <span id="meterText" class="absolute text-[11px] font-bold">25%</span>
                </div>
            </div>

            <!-- AI Engine & Model Selector -->
            <div class="glass-card rounded-2xl p-4 flex flex-col justify-between shadow-sm">
                <div class="flex items-center justify-between text-xs font-semibold text-slate-500 dark:text-slate-400">
                    <span class="flex items-center space-x-1.5"><i class="fa-solid fa-microchip text-blue-600"></i><span id="labelSpeechEngine">Speech Engine</span></span>
                    <span class="text-emerald-600 dark:text-emerald-400 font-bold">Online</span>
                </div>
                <div class="flex items-center justify-between mt-2 gap-2">
                    <select id="whisperModel" class="w-1/2 bg-slate-100 dark:bg-navy-800 border border-slate-300 dark:border-slate-700 rounded-lg text-xs font-semibold px-2.5 py-1.5 focus:outline-none focus:ring-2 focus:ring-burgundy-700">
                        <option value="base">Whisper Base (Fast)</option>
                        <option value="medium" selected>Whisper Medium (Accurate)</option>
                        <option value="large-v3">Whisper Large-v3 (Pro)</option>
                    </select>
                    <select id="personaSelect" class="w-1/2 bg-slate-100 dark:bg-navy-800 border border-slate-300 dark:border-slate-700 rounded-lg text-xs font-semibold px-2.5 py-1.5 focus:outline-none focus:ring-2 focus:ring-burgundy-700">
                        <option value="boardroom">Boardroom Persona</option>
                        <option value="project">Project Manager</option>
                        <option value="legal">Legal Counsel</option>
                        <option value="financial">Financial Auditor</option>
                    </select>
                </div>
            </div>

            <!-- Target Language & Auto-Diarize Selector -->
            <div class="glass-card rounded-2xl p-4 flex flex-col justify-between shadow-sm">
                <div class="flex items-center justify-between text-xs font-semibold text-slate-500 dark:text-slate-400">
                    <span class="flex items-center space-x-1.5"><i class="fa-solid fa-language text-purple-600"></i><span id="labelAudioLang">Speech Language</span></span>
                    <span class="text-xs font-semibold bg-purple-100 dark:bg-purple-900/40 text-purple-700 dark:text-purple-300 px-2 py-0.5 rounded">Auto-Diarize</span>
                </div>
                <div class="flex items-center space-x-2 mt-2">
                    <select id="meetingLang" onchange="onAudioLanguageChange()" class="w-full bg-slate-100 dark:bg-navy-800 border border-slate-300 dark:border-slate-700 rounded-lg text-xs font-semibold px-3 py-1.5 focus:outline-none focus:ring-2 focus:ring-burgundy-700">
                        <option value="am" selected>🇪🇹 አማርኛ (Amharic)</option>
                        <option value="en">🇬🇧 English</option>
                        <option value="om">🇪🇹 Afaan Oromoo</option>
                        <option value="ti">🇪🇹 ትግርኛ (Tigrinya)</option>
                        <option value="fr">🇫🇷 Français (French)</option>
                        <option value="ar">🇸🇦 العربية (Arabic)</option>
                        <option value="auto">🌐 Auto-Detect Mix</option>
                    </select>
                </div>
            </div>

        </div>

        <!-- MAIN INTERACTIVE WORKSPACE GRID -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">

            <!-- LEFT PANEL: INGESTION HUB & AUDIO CONTROL (4 COLS) -->
            <div class="lg:col-span-4 space-y-6">

                <!-- Audio Upload & Live Recording Card -->
                <div class="glass-card rounded-2xl p-5 shadow-sm space-y-4">
                    <div class="flex items-center justify-between">
                        <h2 class="font-bold text-base flex items-center space-x-2">
                            <i class="fa-solid fa-cloud-arrow-up text-burgundy-700 dark:text-burgundy-500"></i>
                            <span id="titleIngestCard">Ingest Audio / Video</span>
                        </h2>
                        <span class="text-[11px] font-medium text-slate-500">MP3, WAV, M4A, MP4</span>
                    </div>

                    <!-- Dropzone -->
                    <div id="dropzone" onclick="triggerFileInput()" class="border-2 border-dashed border-slate-300 dark:border-slate-700 hover:border-burgundy-700 dark:hover:border-burgundy-500 rounded-xl p-6 flex flex-col items-center justify-center text-center cursor-pointer transition bg-slate-50/50 dark:bg-navy-900/50 group">
                        <input type="file" id="audioFileInput" accept="audio/*,video/*" class="hidden" onchange="handleFileSelect(event)">
                        <div class="w-12 h-12 rounded-full bg-burgundy-50 dark:bg-burgundy-900/30 text-burgundy-700 dark:text-burgundy-400 flex items-center justify-center mb-2 group-hover:scale-110 transition">
                            <i class="fa-solid fa-file-audio text-xl"></i>
                        </div>
                        <p class="text-xs font-semibold text-slate-700 dark:text-slate-300" id="dropzoneText">Drag &amp; Drop file or <span class="text-burgundy-700 dark:text-burgundy-400 underline">Browse</span></p>
                        <p class="text-[10px] text-slate-400 mt-1">Recommended size: &lt; 250MB</p>
                    </div>

                    <!-- Live Mic Record Simulator & Waveform Canvas -->
                    <div class="pt-2 border-t border-slate-200 dark:border-slate-800 space-y-3">
                        <div class="flex items-center justify-between">
                            <div class="flex items-center space-x-2">
                                <button id="micBtn" onclick="toggleMicRecording()" class="w-9 h-9 rounded-full bg-rose-600 hover:bg-rose-700 text-white flex items-center justify-center shadow-md transition">
                                    <i class="fa-solid fa-microphone text-sm"></i>
                                </button>
                                <div>
                                    <p class="text-xs font-semibold" id="labelLiveMic">Live Mic Recorder</p>
                                    <p id="recTimer" class="text-[10px] text-slate-400">00:00 (Click to start)</p>
                                </div>
                            </div>
                            <button onclick="loadSampleAudio()" class="text-xs text-burgundy-700 dark:text-burgundy-400 font-semibold hover:underline" id="btnLoadDemo">
                                Load Ethiopian Boardroom Audio
                            </button>
                        </div>
                        <!-- Live Web Canvas Soundwave Visualizer -->
                        <canvas id="waveformCanvas" class="w-full h-10 bg-slate-100 dark:bg-navy-900 rounded-lg border border-slate-200 dark:border-slate-800"></canvas>
                    </div>

                    <!-- Selected File Info & Controls -->
                    <div id="fileInfoCard" class="hidden bg-slate-100 dark:bg-navy-800/80 rounded-xl p-3.5 space-y-3">
                        <div class="flex items-center justify-between">
                            <div class="flex items-center space-x-2 truncate">
                                <i class="fa-solid fa-music text-burgundy-700 dark:text-burgundy-400 text-sm"></i>
                                <span id="fileName" class="text-xs font-bold truncate">Ethiopian_Bank_Boardroom_Q3.mp3</span>
                            </div>
                            <span id="fileSize" class="text-[10px] bg-slate-200 dark:bg-navy-700 px-2 py-0.5 rounded font-mono">14.2 MB</span>
                        </div>

                        <!-- Player Controls -->
                        <div class="flex items-center justify-between text-xs pt-1">
                            <div class="flex items-center space-x-2">
                                <button id="playPauseBtn" onclick="toggleAudioPlayback()" class="w-7 h-7 rounded-lg bg-burgundy-700 text-white flex items-center justify-center">
                                    <i class="fa-solid fa-play text-xs"></i>
                                </button>
                                <span id="playbackTime" class="font-mono text-[11px] text-slate-500">00:00 / 08:45</span>
                            </div>
                            <select id="playbackSpeed" class="bg-white dark:bg-navy-700 text-[11px] font-mono border border-slate-300 dark:border-slate-600 rounded px-1 py-0.5">
                                <option value="1">1.0x</option>
                                <option value="1.25">1.25x</option>
                                <option value="1.5">1.5x</option>
                                <option value="2">2.0x</option>
                            </select>
                        </div>
                    </div>

                    <!-- Process Audio Button -->
                    <button id="processBtn" onclick="runAiProcessing()" class="w-full bg-gradient-to-r from-burgundy-700 to-burgundy-800 hover:from-burgundy-800 hover:to-burgundy-900 text-white font-bold text-sm py-3 rounded-xl shadow-lg shadow-burgundy-700/25 flex items-center justify-center space-x-2 transition transform active:scale-[0.99]">
                        <i class="fa-solid fa-wand-magic-sparkles"></i>
                        <span id="btnProcessText">Generate Intelligence &amp; ቃለ ጉባዔ</span>
                    </button>
                </div>

                <!-- Processing Status Overlay Box -->
                <div id="processingCard" class="hidden glass-card rounded-2xl p-4 space-y-3 border-l-4 border-l-burgundy-700 animate-pulse">
                    <div class="flex items-center justify-between text-xs font-bold">
                        <span class="flex items-center space-x-2 text-burgundy-700 dark:text-burgundy-400">
                            <i class="fa-solid fa-spinner fa-spin"></i>
                            <span id="procStatusText">Transcribing Audio (Whisper Medium)...</span>
                        </span>
                        <span id="procPercent" class="font-mono">45%</span>
                    </div>
                    <div class="w-full bg-slate-200 dark:bg-navy-800 h-2 rounded-full overflow-hidden">
                        <div id="procProgressBar" class="bg-burgundy-700 h-full w-[45%] transition-all duration-300"></div>
                    </div>
                    <p id="procSubText" class="text-[11px] text-slate-500">Speaker diarization and boardroom summarization engine active...</p>
                </div>

                <!-- Executive Quick Metrics Card -->
                <div class="glass-card rounded-2xl p-5 space-y-3">
                    <h3 class="text-xs font-bold uppercase tracking-wider text-slate-400 flex items-center space-x-1.5">
                        <i class="fa-solid fa-chart-line"></i>
                        <span id="titleAnalyticsOverview">Meeting Analytics Overview</span>
                    </h3>
                    <div class="grid grid-cols-2 gap-3 text-center">
                        <div class="bg-slate-100 dark:bg-navy-800/60 p-2.5 rounded-xl">
                            <p class="text-[10px] text-slate-500" id="lblDuration">Total Duration</p>
                            <p id="statDuration" class="text-base font-extrabold text-navy-900 dark:text-white">08m 45s</p>
                        </div>
                        <div class="bg-slate-100 dark:bg-navy-800/60 p-2.5 rounded-xl">
                            <p class="text-[10px] text-slate-500" id="lblSpeakers">Identified Speakers</p>
                            <p id="statSpeakers" class="text-base font-extrabold text-burgundy-700 dark:text-burgundy-400">3 Speakers</p>
                        </div>
                        <div class="bg-slate-100 dark:bg-navy-800/60 p-2.5 rounded-xl">
                            <p class="text-[10px] text-slate-500" id="lblActions">Action Items</p>
                            <p id="statActions" class="text-base font-extrabold text-amber-600">4 Items</p>
                        </div>
                        <div class="bg-slate-100 dark:bg-navy-800/60 p-2.5 rounded-xl">
                            <p class="text-[10px] text-slate-500" id="lblSentiment">Overall Sentiment</p>
                            <p id="statSentiment" class="text-base font-extrabold text-emerald-600">Positive (88%)</p>
                        </div>
                    </div>
                </div>

            </div>

            <!-- RIGHT PANEL: INTERACTIVE TABS & OUTPUT ENGINE (8 COLS) -->
            <div class="lg:col-span-8 space-y-4">

                <!-- MAIN WORKSPACE TAB HEADERS -->
                <div class="flex items-center justify-between border-b border-slate-200 dark:border-slate-800 pb-2">
                    <div class="flex space-x-2 overflow-x-auto py-1">
                        <button onclick="switchTab('tabMinutes', this)" id="btnTabMinutes" class="tab-btn px-4 py-2 rounded-xl text-xs font-bold flex items-center space-x-2 transition bg-burgundy-700 text-white shadow-md">
                            <i class="fa-solid fa-file-contract"></i>
                            <span id="tabMinutesTitle">Executive ቃለ ጉባዔ (Minutes)</span>
                        </button>
                        <button onclick="switchTab('tabTranscript', this)" id="btnTabTranscript" class="tab-btn px-4 py-2 rounded-xl text-xs font-bold flex items-center space-x-2 transition bg-slate-200 text-slate-700 dark:bg-navy-800 dark:text-slate-300 hover:bg-slate-300">
                            <i class="fa-solid fa-align-left"></i>
                            <span id="tabTranscriptTitle">Interactive Transcript</span>
                        </button>
                        <button onclick="switchTab('tabAnalytics', this)" id="btnTabAnalytics" class="tab-btn px-4 py-2 rounded-xl text-xs font-bold flex items-center space-x-2 transition bg-slate-200 text-slate-700 dark:bg-navy-800 dark:text-slate-300 hover:bg-slate-300">
                            <i class="fa-solid fa-chart-pie"></i>
                            <span id="tabAnalyticsTitle">Analytics &amp; Sentiment</span>
                        </button>
                    </div>

                    <!-- Export Package Dropdown -->
                    <div class="relative inline-block text-left">
                        <button onclick="toggleExportMenu()" class="flex items-center space-x-1.5 bg-slate-200 dark:bg-navy-800 hover:bg-slate-300 dark:hover:bg-navy-700 text-slate-800 dark:text-slate-200 px-3 py-1.5 rounded-xl text-xs font-bold transition">
                            <i class="fa-solid fa-download text-burgundy-700 dark:text-burgundy-400"></i>
                            <span id="btnExportTitle">Export Package</span>
                            <i class="fa-solid fa-chevron-down text-[10px]"></i>
                        </button>
                        <div id="exportMenu" class="hidden absolute right-0 mt-2 w-48 rounded-xl shadow-xl bg-white dark:bg-navy-900 border border-slate-200 dark:border-slate-800 z-50 overflow-hidden">
                            <a href="#" onclick="exportData('docx')" class="block px-4 py-2.5 text-xs text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-navy-800 flex items-center space-x-2">
                                <i class="fa-solid fa-file-word text-blue-600"></i>
                                <span>Word Document (.docx)</span>
                            </a>
                            <a href="#" onclick="exportData('pdf')" class="block px-4 py-2.5 text-xs text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-navy-800 flex items-center space-x-2">
                                <i class="fa-solid fa-file-pdf text-rose-600"></i>
                                <span>Boardroom PDF Report</span>
                            </a>
                            <a href="#" onclick="exportData('txt')" class="block px-4 py-2.5 text-xs text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-navy-800 flex items-center space-x-2">
                                <i class="fa-solid fa-file-lines text-slate-500"></i>
                                <span>Plain Text (.txt)</span>
                            </a>
                            <a href="#" onclick="exportData('md')" class="block px-4 py-2.5 text-xs text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-navy-800 flex items-center space-x-2">
                                <i class="fa-brands fa-markdown text-purple-600"></i>
                                <span>Markdown Format (.md)</span>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- TAB CONTENT 1: EXECUTIVE ቃለ ጉባዔ (MINUTES) -->
                <div id="tabMinutes" class="tab-content space-y-4">
                    <div class="glass-card rounded-2xl p-6 space-y-6">

                        <!-- Document Header Block -->
                        <div class="border-b border-slate-200 dark:border-slate-800 pb-4 flex flex-col md:flex-row md:items-center justify-between gap-4">
                            <div>
                                <h2 id="docTitle" class="text-xl font-extrabold text-navy-900 dark:text-white">የስብሰባ ቃለ ጉባዔ — Executive Boardroom Summary</h2>
                                <p class="text-xs text-slate-500 mt-1">Generated by Scriber AI Pro • Date: <span id="docDate">October 28, 2026</span></p>
                            </div>
                            <div class="flex items-center space-x-2">
                                <span class="text-xs bg-emerald-100 text-emerald-800 dark:bg-emerald-900/40 dark:text-emerald-300 font-bold px-3 py-1 rounded-full flex items-center space-x-1">
                                    <i class="fa-solid fa-certificate"></i>
                                    <span>AI Certified Minutes</span>
                                </span>
                            </div>
                        </div>

                        <!-- 1. Executive Summary -->
                        <div class="space-y-2">
                            <h3 class="text-sm font-bold uppercase tracking-wider text-burgundy-700 dark:text-burgundy-400 flex items-center space-x-2">
                                <i class="fa-solid fa-quote-left"></i>
                                <span id="titleSecSummary">1. Executive Overview</span>
                            </h3>
                            <p id="minutesSummary" class="text-xs md:text-sm leading-relaxed text-slate-700 dark:text-slate-300 bg-slate-50 dark:bg-navy-900/50 p-4 rounded-xl border border-slate-200 dark:border-slate-800">
                                የ 2026 Q3 የፋይናንስ እና ኦፕሬሽን አፈፃፀም ግምገማ ስብሰባ በዋና ዋና የባንክ ቅርንጫፎች የተቀማጭ ገንዘብ፣ በኢትዮጵያ ካፒታል ማርኬት አሰራር እና በዲጂታል የክፍያ ስርአቶች ዙሪያ ተወያይቷል።
                            </p>
                        </div>

                        <!-- 2. Agenda Items Breakdown -->
                        <div class="space-y-3">
                            <h3 class="text-sm font-bold uppercase tracking-wider text-burgundy-700 dark:text-burgundy-400 flex items-center space-x-2">
                                <i class="fa-solid fa-list-check"></i>
                                <span id="titleSecAgenda">2. Agenda Breakdown &amp; Deliberations</span>
                            </h3>
                            <div id="agendaList" class="space-y-2">
                                <div class="bg-slate-50 dark:bg-navy-900/50 p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 text-xs space-y-1">
                                    <div class="flex items-center justify-between">
                                        <span class="font-bold text-navy-900 dark:text-slate-200">አጀንዳ 1: የኢትዮጵያ ካፒታል ማርኬት (ESX) ዝግጅት እና የካፒታል ምደባ</span>
                                        <span class="text-[10px] bg-blue-100 text-blue-800 dark:bg-blue-900/40 dark:text-blue-300 font-semibold px-2 py-0.5 rounded">00:00 - 03:15</span>
                                    </div>
                                    <p class="text-slate-600 dark:text-slate-400">የመንግስት የግምጃ ቤት ሰነዶች እና የቦንድ ግዥዎች በኢትዮጵያ የካፒታል ማርኬት ባለስልጣን (ECMA) መመሪያ መሰረት ስለማደራጀት ዝርዝር ውይይት ተደረገ።</p>
                                </div>
                                <div class="bg-slate-50 dark:bg-navy-900/50 p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 text-xs space-y-1">
                                    <div class="flex items-center justify-between">
                                        <span class="font-bold text-navy-900 dark:text-slate-200">አጀንዳ 2: የቅርንጫፎች የተቀማጭ ገንዘብ (Deposit Mobilization) አፈፃፀም</span>
                                        <span class="text-[10px] bg-blue-100 text-blue-800 dark:bg-blue-900/40 dark:text-blue-300 font-semibold px-2 py-0.5 rounded">03:16 - 06:40</span>
                                    </div>
                                    <p class="text-slate-600 dark:text-slate-400">በቀዳሚ 10 ቅርንጫፎች የነበረው አፈፃፀም ከእቅድ በላይ 14.2% ማሳየቱ የተገለጸ ሲሆን ዝቅተኛ አፈፃፀም ላላቸው 10 ቅርንጫፎች ድጋፍ እንዲደረግ ተወሰነ።</p>
                                </div>
                            </div>
                        </div>

                        <!-- 3. Key Resolutions -->
                        <div class="space-y-3">
                            <h3 class="text-sm font-bold uppercase tracking-wider text-burgundy-700 dark:text-burgundy-400 flex items-center space-x-2">
                                <i class="fa-solid fa-gavel"></i>
                                <span id="titleSecResolutions">3. Key Resolutions &amp; Board Decisions</span>
                            </h3>
                            <ul id="decisionsList" class="space-y-2 text-xs">
                                <li class="flex items-start space-x-2.5 bg-emerald-50 dark:bg-emerald-950/30 p-3 rounded-xl border border-emerald-200 dark:border-emerald-800/50">
                                    <i class="fa-solid fa-circle-check text-emerald-600 mt-0.5"></i>
                                    <div>
                                        <strong class="text-emerald-950 dark:text-emerald-200">የዲጂታል ሲስተም በጀት ፀደቀ:</strong> ለ AI አፕሊኬሽኖች እና ቴሌብር ክፍያዎች ማቀናጃ 45.8 ሚሊዮን ብር በጀት ፀደቀ።
                                    </div>
                                </li>
                                <li class="flex items-start space-x-2.5 bg-emerald-50 dark:bg-emerald-950/30 p-3 rounded-xl border border-emerald-200 dark:border-emerald-800/50">
                                    <i class="fa-solid fa-circle-check text-emerald-600 mt-0.5"></i>
                                    <div>
                                        <strong class="text-emerald-950 dark:text-emerald-200">የሪፖርት ማቅረቢያ ጊዜ ተራዘመ:</strong> የ Q4 የኦዲት ሪፖርት ማጠቃለያ እስከ ህዳር 15 ቀን 2026 እንዲራዘም ተወሰነ።
                                    </div>
                                </li>
                            </ul>
                        </div>

                        <!-- 4. Action Items Matrix -->
                        <div class="space-y-3">
                            <h3 class="text-sm font-bold uppercase tracking-wider text-burgundy-700 dark:text-burgundy-400 flex items-center space-x-2">
                                <i class="fa-solid fa-tasks"></i>
                                <span id="titleSecActions">4. Action Items Matrix &amp; Responsibilities</span>
                            </h3>
                            <div class="overflow-x-auto">
                                <table class="w-full text-left text-xs border-collapse">
                                    <thead>
                                        <tr class="bg-slate-100 dark:bg-navy-800 text-slate-700 dark:text-slate-300 font-bold border-b border-slate-200 dark:border-slate-700">
                                            <th class="p-2.5 w-8">Status</th>
                                            <th class="p-2.5">Task Description</th>
                                            <th class="p-2.5">Assignee</th>
                                            <th class="p-2.5">Priority</th>
                                            <th class="p-2.5">Deadline</th>
                                        </tr>
                                    </thead>
                                    <tbody id="actionMatrix" class="divide-y divide-slate-200 dark:divide-slate-800">
                                        <tr>
                                            <td class="p-2.5"><input type="checkbox" onclick="toggleTask(this)" class="w-4 h-4 accent-burgundy-700 rounded cursor-pointer"></td>
                                            <td class="p-2.5 font-medium task-text">የቴሌብር እና ሲቢኢ ብር API ማቀናጃ ዶክመንት ማዘጋጀት</td>
                                            <td class="p-2.5 text-burgundy-700 dark:text-burgundy-400 font-semibold">አቶ በቀለ (የ IT ዳይሬክተር)</td>
                                            <td class="p-2.5"><span class="bg-rose-100 text-rose-800 dark:bg-rose-900/40 dark:text-rose-300 font-bold px-2 py-0.5 rounded text-[10px]">High</span></td>
                                            <td class="p-2.5 font-mono">Nov 05, 2026</td>
                                        </tr>
                                        <tr>
                                            <td class="p-2.5"><input type="checkbox" onclick="toggleTask(this)" class="w-4 h-4 accent-burgundy-700 rounded cursor-pointer"></td>
                                            <td class="p-2.5 font-medium task-text">የኢትዮጵያ ካፒታል ማርኬት የ ESX ሰነዶች ማዘጋጀት</td>
                                            <td class="p-2.5 text-burgundy-700 dark:text-burgundy-400 font-semibold">ወ/ሮ ቤተልሔም (የህግ አማካሪ)</td>
                                            <td class="p-2.5"><span class="bg-amber-100 text-amber-800 dark:bg-amber-900/40 dark:text-amber-300 font-bold px-2 py-0.5 rounded text-[10px]">Medium</span></td>
                                            <td class="p-2.5 font-mono">Nov 12, 2026</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>

                    </div>
                </div>

                <!-- TAB CONTENT 2: SYNCHRONIZED INTERACTIVE TRANSCRIPT -->
                <div id="tabTranscript" class="tab-content hidden space-y-4">
                    <div class="glass-card rounded-2xl p-6 space-y-4">
                        
                        <!-- Search & Filter Bar -->
                        <div class="flex flex-col sm:flex-row items-center justify-between gap-3 bg-slate-100 dark:bg-navy-800/60 p-3 rounded-xl">
                            <div class="relative w-full sm:w-72">
                                <i class="fa-solid fa-magnifying-glass absolute left-3 top-2.5 text-slate-400 text-xs"></i>
                                <input type="text" id="transcriptSearch" oninput="filterTranscript()" placeholder="Search keywords..." class="w-full bg-white dark:bg-navy-900 border border-slate-300 dark:border-slate-700 rounded-lg pl-9 pr-3 py-1.5 text-xs focus:outline-none focus:ring-2 focus:ring-burgundy-700">
                            </div>
                            <div class="flex items-center space-x-2 w-full sm:w-auto justify-end">
                                <button onclick="toggleTranscriptEditMode()" id="editTranscriptBtn" class="px-3 py-1.5 bg-white dark:bg-navy-900 border border-slate-300 dark:border-slate-700 rounded-lg text-xs font-semibold hover:bg-slate-50 dark:hover:bg-navy-800 flex items-center space-x-1.5">
                                    <i class="fa-solid fa-pen-to-square"></i>
                                    <span>Edit Mode</span>
                                </button>
                            </div>
                        </div>

                        <!-- Diarized Transcript Container -->
                        <div id="transcriptContainer" class="space-y-4 max-h-[500px] overflow-y-auto pr-2">
                            <!-- Segment 1 -->
                            <div class="transcript-row group p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 hover:border-burgundy-700/50 transition space-y-1 bg-slate-50/50 dark:bg-navy-900/30">
                                <div class="flex items-center justify-between">
                                    <div class="flex items-center space-x-2">
                                        <span class="w-2.5 h-2.5 rounded-full bg-blue-600"></span>
                                        <span class="font-bold text-xs text-navy-900 dark:text-slate-100">Speaker 1 (Chairperson)</span>
                                    </div>
                                    <button onclick="seekAudioTo('00:05')" class="font-mono text-[11px] text-slate-400 hover:text-burgundy-700 dark:hover:text-burgundy-400">
                                        <i class="fa-solid fa-play text-[9px] mr-1"></i>00:05
                                    </button>
                                </div>
                                <p class="transcript-text text-xs leading-relaxed text-slate-700 dark:text-slate-300">
                                    እንኳን ደህና መጣችሁ። የዛሬው የስብሰባችን ዋና አጀንዳ በ Q3 የበጀት አፈፃፀም፣ በቅርንጫፎቻችን የተቀማጭ ገንዘብ መጠን እና በካፒታል ማርኬት ዝግጅታችን ዙሪያ ያተኩራል።
                                </p>
                            </div>

                            <!-- Segment 2 -->
                            <div class="transcript-row group p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 hover:border-burgundy-700/50 transition space-y-1 bg-slate-50/50 dark:bg-navy-900/30">
                                <div class="flex items-center justify-between">
                                    <div class="flex items-center space-x-2">
                                        <span class="w-2.5 h-2.5 rounded-full bg-burgundy-600"></span>
                                        <span class="font-bold text-xs text-navy-900 dark:text-slate-100">Speaker 2 (Finance Director)</span>
                                    </div>
                                    <button onclick="seekAudioTo('01:20')" class="font-mono text-[11px] text-slate-400 hover:text-burgundy-700 dark:hover:text-burgundy-400">
                                        <i class="fa-solid fa-play text-[9px] mr-1"></i>01:20
                                    </button>
                                </div>
                                <p class="transcript-text text-xs leading-relaxed text-slate-700 dark:text-slate-300">
                                    እሺ አመሰግናለሁ። በበጀት አፈፃፀማችን ዙሪያ የላቁ ቅርንጫፎች ግባቸውን 114% አክናውኗል። ለቀጣይ ወርም የቴሌብር ክፍያ API የተቀናጀ አሰራር ሙሉ በሙሉ ስራ ላይ ይውላል።
                                </p>
                            </div>
                        </div>

                    </div>
                </div>

                <!-- TAB CONTENT 3: ANALYTICS & SENTIMENT DASHBOARD -->
                <div id="tabAnalytics" class="tab-content hidden space-y-4">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        
                        <!-- Speaker Talk-Time Pie Chart -->
                        <div class="glass-card rounded-2xl p-5 space-y-3">
                            <h3 class="text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400 flex items-center space-x-2">
                                <i class="fa-solid fa-chart-pie text-burgundy-700 dark:text-burgundy-400"></i>
                                <span>Speaker Talk-Time Share</span>
                            </h3>
                            <div class="h-44 flex items-center justify-center">
                                <svg class="w-36 h-36" viewBox="0 0 36 36">
                                    <path d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none" stroke="#E2E8F0" stroke-width="3.8"/>
                                    <path d="M18 2.0845 a 15.9155 15.9155 0 0 1 14.8 21.8" fill="none" stroke="#2563EB" stroke-width="3.8" stroke-dasharray="55, 100"/>
                                    <path d="M18 2.0845 a 15.9155 15.9155 0 0 1 -14.8 21.8" fill="none" stroke="#800020" stroke-width="3.8" stroke-dasharray="30, 100" stroke-dashoffset="-55"/>
                                    <path d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831" fill="none" stroke="#D97706" stroke-width="3.8" stroke-dasharray="15, 100" stroke-dashoffset="-85"/>
                                </svg>
                            </div>
                            <div class="flex justify-center space-x-4 text-[11px] font-semibold">
                                <span class="flex items-center space-x-1"><span class="w-2.5 h-2.5 rounded-full bg-blue-600"></span><span>Speaker 1 (55%)</span></span>
                                <span class="flex items-center space-x-1"><span class="w-2.5 h-2.5 rounded-full bg-burgundy-700"></span><span>Speaker 2 (30%)</span></span>
                                <span class="flex items-center space-x-1"><span class="w-2.5 h-2.5 rounded-full bg-amber-600"></span><span>Speaker 3 (15%)</span></span>
                            </div>
                        </div>

                        <!-- Sentiment & Tone Meter -->
                        <div class="glass-card rounded-2xl p-5 space-y-3">
                            <h3 class="text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400 flex items-center space-x-2">
                                <i class="fa-solid fa-face-smile text-emerald-600"></i>
                                <span>Meeting Tone &amp; Sentiment Score</span>
                            </h3>
                            <div class="space-y-3 pt-2">
                                <div>
                                    <div class="flex justify-between text-xs font-bold mb-1">
                                        <span>Positive / Constructive</span>
                                        <span class="text-emerald-600">88%</span>
                                    </div>
                                    <div class="w-full bg-slate-200 dark:bg-navy-800 h-2 rounded-full overflow-hidden">
                                        <div class="bg-emerald-500 h-full w-[88%]"></div>
                                    </div>
                                </div>
                                <div>
                                    <div class="flex justify-between text-xs font-bold mb-1">
                                        <span>Neutral / Informational</span>
                                        <span class="text-blue-600">10%</span>
                                    </div>
                                    <div class="w-full bg-slate-200 dark:bg-navy-800 h-2 rounded-full overflow-hidden">
                                        <div class="bg-blue-500 h-full w-[10%]"></div>
                                    </div>
                                </div>
                                <div>
                                    <div class="flex justify-between text-xs font-bold mb-1">
                                        <span>Risk / Critical Concerns</span>
                                        <span class="text-rose-600">2%</span>
                                    </div>
                                    <div class="w-full bg-slate-200 dark:bg-navy-800 h-2 rounded-full overflow-hidden">
                                        <div class="bg-rose-500 h-full w-[2%]"></div>
                                    </div>
                                </div>
                            </div>
                        </div>

                    </div>

                    <!-- Topic Clusters & Keywords -->
                    <div class="glass-card rounded-2xl p-5 space-y-3">
                        <h3 class="text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400 flex items-center space-x-2">
                            <i class="fa-solid fa-tags text-purple-600"></i>
                            <span>Key Topic Clusters Detected</span>
                        </h3>
                        <div class="flex flex-wrap gap-2 text-xs">
                            <span class="bg-burgundy-50 dark:bg-burgundy-900/30 text-burgundy-700 dark:text-burgundy-300 border border-burgundy-200 dark:border-burgundy-800 px-3 py-1 rounded-full font-bold"># ኢትዮጵያ ካፒታል ማርኬት (18)</span>
                            <span class="bg-blue-50 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300 border border-blue-200 dark:border-blue-800 px-3 py-1 rounded-full font-bold"># Telebirr API Integration (14)</span>
                            <span class="bg-emerald-50 dark:bg-emerald-900/30 text-emerald-700 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-800 px-3 py-1 rounded-full font-bold"># የተቀማጭ ገንዘብ መጠን (11)</span>
                            <span class="bg-purple-50 dark:bg-purple-900/30 text-purple-700 dark:text-purple-300 border border-purple-200 dark:border-purple-800 px-3 py-1 rounded-full font-bold"># ECMA Compliance (9)</span>
                            <span class="bg-amber-50 dark:bg-amber-900/30 text-amber-700 dark:text-amber-300 border border-amber-200 dark:border-amber-800 px-3 py-1 rounded-full font-bold"># Q4 Audit Timeline (7)</span>
                        </div>
                    </div>
                </div>

            </div>

        </div>

    </main>

    <!-- INTEGRATED PAYMENT & BILLING MODAL -->
    <div id="paymentModal" class="fixed inset-0 bg-navy-950/80 backdrop-blur-md z-50 flex items-center justify-center hidden p-4">
        <div class="glass-card bg-white dark:bg-navy-900 rounded-3xl max-w-lg w-full p-6 space-y-6 shadow-2xl border border-slate-200 dark:border-slate-800">
            <div class="flex items-center justify-between border-b border-slate-200 dark:border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <div class="w-8 h-8 rounded-lg bg-burgundy-700 text-white flex items-center justify-center">
                        <i class="fa-solid fa-credit-card"></i>
                    </div>
                    <div>
                        <h3 class="font-extrabold text-base">Scriber AI Pro Subscription Hub</h3>
                        <p class="text-[10px] text-slate-400">Unlock Unlimited High-Speed Audio &amp; Video Minutes</p>
                    </div>
                </div>
                <button onclick="closePaymentModal()" class="text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 text-lg">
                    <i class="fa-solid fa-xmark"></i>
                </button>
            </div>

            <!-- Pricing Tiers selector -->
            <div class="grid grid-cols-3 gap-3">
                <div onclick="selectPlan('payg')" id="planPayg" class="border-2 border-slate-300 dark:border-slate-700 hover:border-burgundy-700 rounded-2xl p-3 text-center cursor-pointer transition space-y-1">
                    <p class="text-[11px] font-bold text-slate-500">Pay As You Go</p>
                    <p class="text-base font-extrabold text-burgundy-700 dark:text-burgundy-400">ETB 50 <span class="text-[10px] font-normal text-slate-400">/hr</span></p>
                    <p class="text-[9px] text-slate-400">Instant top-up</p>
                </div>
                <div onclick="selectPlan('pro')" id="planPro" class="border-2 border-burgundy-700 bg-burgundy-50/50 dark:bg-burgundy-950/30 rounded-2xl p-3 text-center cursor-pointer transition space-y-1 relative">
                    <span class="absolute -top-2.5 left-1/2 transform -translate-x-1/2 bg-burgundy-700 text-white text-[9px] font-bold px-2 py-0.5 rounded-full">POPULAR</span>
                    <p class="text-[11px] font-bold text-burgundy-700 dark:text-burgundy-400">Monthly Pro</p>
                    <p class="text-base font-extrabold text-burgundy-700 dark:text-burgundy-400">ETB 500 <span class="text-[10px] font-normal text-slate-400">/mo</span></p>
                    <p class="text-[9px] text-slate-400">Unlimited mins</p>
                </div>
                <div onclick="selectPlan('enterprise')" id="planEnterprise" class="border-2 border-slate-300 dark:border-slate-700 hover:border-burgundy-700 rounded-2xl p-3 text-center cursor-pointer transition space-y-1">
                    <p class="text-[11px] font-bold text-slate-500">Enterprise</p>
                    <p class="text-base font-extrabold text-burgundy-700 dark:text-burgundy-400">Custom</p>
                    <p class="text-[9px] text-slate-400">Multi-user bank</p>
                </div>
            </div>

            <!-- Payment Gateway Selector -->
            <div class="space-y-2">
                <label class="text-xs font-bold text-slate-700 dark:text-slate-300">Select Payment Method:</label>
                <div class="grid grid-cols-2 gap-3">
                    <button onclick="selectGateway('telebirr')" id="gwTelebirr" class="flex items-center justify-between p-3 rounded-xl border border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-navy-800 font-bold text-xs hover:border-burgundy-700 transition">
                        <span>📱 Telebirr API</span>
                        <i class="fa-solid fa-circle-check text-burgundy-700 hidden" id="chkTelebirr"></i>
                    </button>
                    <button onclick="selectGateway('cbe')" id="gwCbe" class="flex items-center justify-between p-3 rounded-xl border border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-navy-800 font-bold text-xs hover:border-burgundy-700 transition">
                        <span>🏦 CBE Birr</span>
                        <i class="fa-solid fa-circle-check text-burgundy-700 hidden" id="chkCbe"></i>
                    </button>
                    <button onclick="selectGateway('chapa')" id="gwChapa" class="flex items-center justify-between p-3 rounded-xl border border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-navy-800 font-bold text-xs hover:border-burgundy-700 transition">
                        <span>⚡ Chapa Gateway</span>
                        <i class="fa-solid fa-circle-check text-burgundy-700 hidden" id="chkChapa"></i>
                    </button>
                    <button onclick="selectGateway('card')" id="gwCard" class="flex items-center justify-between p-3 rounded-xl border border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-navy-800 font-bold text-xs hover:border-burgundy-700 transition">
                        <span>💳 Visa / Mastercard</span>
                        <i class="fa-solid fa-circle-check text-burgundy-700 hidden" id="chkCard"></i>
                    </button>
                </div>
            </div>

            <!-- Coupon Code input -->
            <div class="flex space-x-2">
                <input type="text" id="promoCode" placeholder="Enter Coupon Code (ETHIO-AI-2026)" class="flex-grow bg-slate-100 dark:bg-navy-800 border border-slate-300 dark:border-slate-700 rounded-xl px-3 py-2 text-xs uppercase focus:outline-none focus:ring-2 focus:ring-burgundy-700">
                <button onclick="applyPromo()" class="px-4 py-2 bg-slate-800 text-white rounded-xl text-xs font-bold hover:bg-slate-900">Apply</button>
            </div>
            <p id="promoStatusMsg" class="text-[11px] hidden font-semibold"></p>

            <!-- Action button -->
            <button onclick="completePayment()" id="paySubmitBtn" class="w-full bg-gradient-to-r from-burgundy-700 to-burgundy-800 hover:from-burgundy-800 hover:to-burgundy-900 text-white font-bold py-3.5 rounded-xl shadow-lg shadow-burgundy-700/30 transition">
                Proceed with Payment (ETB 500)
            </button>
        </div>
    </div>

    <!-- FOOTER -->
    <footer class="border-t border-slate-200 dark:border-slate-800 py-4 px-6 text-center text-xs text-slate-500">
        <p>© 2026 Scriber AI Pro — Enterprise Multilingual Speech-to-Text &amp; ቃለ ጉባዔ Engine.</p>
    </footer>

    <!-- JAVASCRIPT LOGIC ENGINE -->
    <script>
        // System State Variables
        let isDarkMode = false;
        let currentSystemLang = 'am';
        let isAudioPlaying = false;
        let isRecording = false;
        let recInterval = null;
        let recSeconds = 0;
        let usedMinsVal = 2.5;
        let maxMinsVal = 10.0;
        let selectedGateway = 'telebirr';
        let selectedPlan = 'pro';

        // Web Audio API & Waveform Animation ID
        let animFrameId = null;

        const translations = {
            am: {
                flag: '🇪🇹',
                text: 'አማርኛ',
                subHeader: 'የስብሰባ ድምፅ ቅጂዎችን ወደ ጽሑፍ እና የቃለ ጉባዔ ማጠቃለያ በሰኮንዶች ውስጥ ይቀይሩ',
                upgrade: 'መተግበሪያውን አሻሽል (Upgrade)',
                trialMeter: 'የሙከራ ደቂቃዎች መጠን',
                freeBadge: 'የመጀመሪያዎቹ 10 ደቂቃዎች ነፃ!',
                speechEngine: 'የSpeech Engine ሁኔታ',
                speechLang: 'የስብሰባው ቋንቋ',
                ingestTitle: 'የድምፅ ወይም ቪዲዮ ቅጂ ያስገቡ',
                dropzone: 'ፋይሉን እዚህ ይጎትቱ ወይም <span class="text-burgundy-700 underline">ይምረጡ</span>',
                liveMic: 'በቀጥታ በድምፅ ይቅዱ',
                loadDemo: 'የኢትዮጵያ ቦርድ ስብሰባ ድምፅ ይጫኑ',
                btnProcess: 'ቃለ ጉባዔ እና ጽሑፍ አዘጋጅ (Generate Intelligence)',
                analyticsTitle: 'የስብሰባው አጠቃላይ መረጃ (Analytics)',
                lblDuration: 'ጠቅላላ የድምፅ ርዝመት',
                lblSpeakers: 'የተለዩ ተናጋሪዎች',
                lblActions: 'የተሰጡ ኃላፊነቶች',
                lblSentiment: 'አጠቃላይ የስብሰባ ስሜት',
                tabMinutes: 'Executive ቃለ ጉባዔ (Minutes)',
                tabTranscript: 'ሙሉ የጽሑፍ ግልባጭ (Transcript)',
                tabAnalytics: 'አናሊቲክስ & Sentiment',
                btnExport: 'ቃለ ጉባዔውን አውርድ',
                docTitle: 'የስብሰባ ቃለ ጉባዔ — Executive Boardroom Summary',
                secSummary: '1. የስብሰባው ዋና ማጠቃለያ (Overview)',
                secAgenda: '2. የአጀንዳዎች ዝርዝር እና ውይይት',
                secResolutions: '3. የተላለፉ ውሳኔዎች (Resolutions)',
                secActions: '4. የተሰጡ ኃላፊነቶች (Action Items Matrix)',
                summaryText: 'የ 2026 Q3 የፋይናንስ እና ኦፕሬሽን አፈፃፀም ግምገማ ስብሰባ በዋና ዋና የባንክ ቅርንጫፎች የተቀማጭ ገንዘብ፣ በኢትዮጵያ ካፒታል ማርኬት አሰራር እና በዲጂታል የክፍያ ስርአቶች ዙሪያ ተወያይቷል።'
            },
            en: {
                flag: '🇬🇧',
                text: 'English',
                subHeader: 'Amharic & English Speech-to-Text, Executive ቃለ ጉባዔ Generator & Audio Analytics',
                upgrade: 'Upgrade Plan',
                trialMeter: 'Trial Usage Meter',
                freeBadge: 'First 10 Mins Free',
                speechEngine: 'Speech Engine Status',
                speechLang: 'Speech Language',
                ingestTitle: 'Ingest Audio / Video',
                dropzone: 'Drag & Drop file or <span class="text-burgundy-700 underline">Browse</span>',
                liveMic: 'Live Mic Recorder',
                loadDemo: 'Load Ethiopian Boardroom Audio',
                btnProcess: 'Generate Intelligence & Minutes',
                analyticsTitle: 'Meeting Analytics Overview',
                lblDuration: 'Total Duration',
                lblSpeakers: 'Identified Speakers',
                lblActions: 'Action Items',
                lblSentiment: 'Overall Sentiment',
                tabMinutes: 'Executive ቃለ ጉባዔ (Minutes)',
                tabTranscript: 'Interactive Transcript',
                tabAnalytics: 'Analytics & Sentiment',
                btnExport: 'Export Package',
                docTitle: 'Meeting Minutes — Executive Boardroom Summary',
                secSummary: '1. Executive Overview',
                secAgenda: '2. Agenda Breakdown & Deliberations',
                secResolutions: '3. Key Resolutions & Board Decisions',
                secActions: '4. Action Items Matrix & Responsibilities',
                summaryText: 'The Q3 Financial & Operational Strategy Alignment meeting evaluated branch rollout targets, dematerialized capital market readiness, and digital payment engine integrations.'
            },
            om: {
                flag: '🇪🇹',
                text: 'Afaan Oromoo',
                subHeader: 'Sagalee gara barruutti jijjiiruu fi gabaasa yaa\'ii haala salphaan qophaessu',
                upgrade: 'Sagantaa Fooyyessi',
                trialMeter: 'Safartuu Daqiiqaa',
                freeBadge: 'Daqiiqaan 10 Jalqabaa Bilisa',
                speechEngine: 'Haala Injiinii Sagalee',
                speechLang: 'Afaan Yaa\'ii',
                ingestTitle: 'Sagalee ykn Viidiyoo Galchu',
                dropzone: 'File asitti harkisaa ykn <span class="text-burgundy-700 underline">Filadhaa</span>',
                liveMic: 'Kallattiin Waraabuu',
                loadDemo: 'Fakkeenya Sagalee Yaa\'ii Fe\'i',
                btnProcess: 'Gabaasa Yaa\'ii Qopheessi',
                analyticsTitle: 'Xiinxala Walga\'ii',
                lblDuration: 'Yeroo Guutuu',
                lblSpeakers: 'Dubbartoota Adda Ba\'an',
                lblActions: 'Hojiiwwan Kennaman',
                lblSentiment: 'Miira Walga\'ii',
                tabMinutes: 'Gabaasa Yaa\'ii (Minutes)',
                tabTranscript: 'Barruu Sagalee Complete',
                tabAnalytics: 'Xiinxala & Miira',
                btnExport: 'Gabaasa Buufadhu',
                docTitle: 'Gabaasa Yaa\'ii — Executive Boardroom Summary',
                secSummary: '1. Gabaasa Naannoo (Overview)',
                secAgenda: '2. Tarreessuu Ajendaa',
                secResolutions: '3. Murteewwan Ijoo',
                secActions: '4. Gabatee Hojii Kennamee',
                summaryText: 'Yaa\'iin Q3 toora baankii, faayinaansii fi teeknoolojii kaffaltii dijitaala irratti mari\'atee murtee dabarseera.'
            },
            ti: {
                flag: '🇪🇹',
                text: 'ትግርኛ',
                subHeader: 'መዝገብ ድምצי ናብ ፅሑፍን ማጠቃለያ ቃለ ጉባኤን ብቕልጣፈ ዘይርያ መተግበሪ',
                upgrade: 'ፕላን ምምሕያሽ',
                trialMeter: 'መዐቀኒ ደቒቕ',
                freeBadge: 'ቀዳሞት 10 ደቒቓታት ብነፃ!',
                speechEngine: 'ኩነታት ሞዴል ድምፂ',
                speechLang: 'ቋንቋ ኣኼባ',
                ingestTitle: 'ድምፂ ወይ ቪዲዮ ኣእትው',
                dropzone: 'ፋይል ናብዚ ስሐብ ወይ <span class="text-burgundy-700 underline">ምረፅ</span>',
                liveMic: 'ብቐጥታ ብድምፂ መዝግብ',
                loadDemo: 'ኣብነት ድምፂ ኣኼባ ፅዓን',
                btnProcess: 'ቃለ ጉባኤን ፅሑፍን ኣዳልው',
                analyticsTitle: 'ሓፈሻዊ ሓበሬታ ኣኼባ',
                lblDuration: 'ጠቕላላ ኑዋሕቲ ድምፂ',
                lblSpeakers: 'ዝተለለዩ ተናገርቲ',
                lblActions: 'ዝተወሃቡ ሓላፍነታት',
                lblSentiment: 'ስምዒት ኣኼባ',
                tabMinutes: 'ቃለ ጉባኤ (Minutes)',
                tabTranscript: 'ምሉእ ፅሑፍ (Transcript)',
                tabAnalytics: 'ኣናሊቲክስ & ስምዒት',
                btnExport: 'ቃለ ጉባኤ ኣውርድ',
                docTitle: 'ቃለ ጉባኤ ኣኼባ — Executive Summary',
                secSummary: '1. ሓፈሻዊ ማጠቃለያ ኣኼባ',
                secAgenda: '2. ዝርዝር ኣጀንዳታት',
                secResolutions: '3. ዝተሓለፉ ውሳነታት',
                secActions: '4. ዝተወሃቡ ሓላፍነታት (Action Items)',
                summaryText: 'ኣኼባ 2026 Q3 ኣብ ሓፈሻዊ ሒሳብ ባንክን ክፍሊት ዲጂታልን ብሰፊሑ ተዘቲዩ ውሳነታት ኣሕሊፉ።'
            },
            fr: {
                flag: '🇫🇷',
                text: 'Français',
                subHeader: 'Transcription Vocale & Générateur de Procès-Verbal Exécutif par IA',
                upgrade: 'Mettre à niveau',
                trialMeter: 'Compteur d\'essai',
                freeBadge: '10 premières min gratuites',
                speechEngine: 'Moteur Vocal',
                speechLang: 'Langue de Réunion',
                ingestTitle: 'Importer Audio / Vidéo',
                dropzone: 'Glisser-déposer ou <span class="text-burgundy-700 underline">Parcourir</span>',
                liveMic: 'Enregistrement En Direct',
                loadDemo: 'Charger Audio de Démo',
                btnProcess: 'Générer le Procès-Verbal',
                analyticsTitle: 'Aperçu Analytique',
                lblDuration: 'Durée Totale',
                lblSpeakers: 'Intervenants Détectés',
                lblActions: 'Actions à Mener',
                lblSentiment: 'Sentiment Général',
                tabMinutes: 'Procès-Verbal (Minutes)',
                tabTranscript: 'Transcription Interactive',
                tabAnalytics: 'Analyses & Sentiment',
                btnExport: 'Exporter',
                docTitle: 'Procès-Verbal de Réunion — Résumé Exécutif',
                secSummary: '1. Aperçu Exécutif',
                secAgenda: '2. Ordre du Jour & Délibérations',
                secResolutions: '3. Décisions Clés',
                secActions: '4. Matrice des Actions',
                summaryText: 'La réunion de revue stratégique du T3 a évalué les objectifs de performance et la préparation aux marchés financiers.'
            },
            ar: {
                flag: '🇸🇦',
                text: 'العربية',
                subHeader: 'تحويل الصوت إلى نص وتوليد محضر الاجتماع التنفيذي بالذكاء الاصطناعي',
                upgrade: 'ترقية الاشتراك',
                trialMeter: 'عداد الدقائق التجريبية',
                freeBadge: 'أول 10 دقائق مجانًا',
                speechEngine: 'محرك التحويل الصوتي',
                speechLang: 'لغة الاجتماع',
                ingestTitle: 'تحميل ملف صوتي / فيديو',
                dropzone: 'اسحب الملف هنا أو <span class="text-burgundy-700 underline">استعرض</span>',
                liveMic: 'تسجيل مباشر',
                loadDemo: 'تحميل صوت تجريبي',
                btnProcess: 'توليد محضر الاجتماع',
                analyticsTitle: 'تحليلات الاجتماع',
                lblDuration: 'المدة الإجمالية',
                lblSpeakers: 'المتحدثون المحددون',
                lblActions: 'مهام العمل',
                lblSentiment: 'الانطباع العام',
                tabMinutes: 'محضر الاجتماع (Minutes)',
                tabTranscript: 'النص المكتوب',
                tabAnalytics: 'التحليلات والانطباع',
                btnExport: 'تصدير التقرير',
                docTitle: 'محضر الاجتماع — الملخص التنفيذي',
                secSummary: '1. الملخص التنفيذي',
                secAgenda: '2. جدول الأعمال والمناقشات',
                secResolutions: '3. القرارات الرئيسية',
                secActions: '4. جدول المهام والمسؤوليات',
                summaryText: 'استعرض اجتماع مراجعة الأداء للربع الثالث الأهداف الماليّة واستراتيجية التحول الرقمي والتكامل مع الأسواق المالية.'
            }
        };

        window.onload = function() {
            initCanvasWaveform();
            selectGateway('telebirr');
            updateMeterVisual();
        };

        function toggleDarkMode() {
            isDarkMode = !isDarkMode;
            if (isDarkMode) {
                document.documentElement.classList.add('dark');
                document.documentElement.classList.remove('light');
            } else {
                document.documentElement.classList.remove('dark');
                document.documentElement.classList.add('light');
            }
        }

        function toggleLangDropdown() {
            document.getElementById('langDropdown').classList.toggle('hidden');
        }

        function setSystemLanguage(langKey) {
            currentSystemLang = langKey;
            document.getElementById('langDropdown').classList.add('hidden');
            const t = translations[langKey] || translations['am'];

            document.getElementById('uiLangFlag').innerText = t.flag;
            document.getElementById('uiLangText').innerText = t.text;
            document.getElementById('appSubHeader').innerText = t.subHeader;
            document.getElementById('navUpgradeBtn').innerText = t.upgrade;
            document.getElementById('labelTrialMeter').innerText = t.trialMeter;
            document.getElementById('labelFreeTrialBadge').innerHTML = `<i class="fa-solid fa-gift mr-1"></i>${t.freeBadge}`;
            document.getElementById('labelSpeechEngine').innerText = t.speechEngine;
            document.getElementById('labelAudioLang').innerText = t.speechLang;
            document.getElementById('titleIngestCard').innerText = t.ingestTitle;
            document.getElementById('dropzoneText').innerHTML = t.dropzone;
            document.getElementById('labelLiveMic').innerText = t.liveMic;
            document.getElementById('btnLoadDemo').innerText = t.loadDemo;
            document.getElementById('btnProcessText').innerText = t.btnProcess;
            document.getElementById('titleAnalyticsOverview').innerText = t.analyticsTitle;
            document.getElementById('lblDuration').innerText = t.lblDuration;
            document.getElementById('lblSpeakers').innerText = t.lblSpeakers;
            document.getElementById('lblActions').innerText = t.lblActions;
            document.getElementById('lblSentiment').innerText = t.lblSentiment;
            document.getElementById('tabMinutesTitle').innerText = t.tabMinutes;
            document.getElementById('tabTranscriptTitle').innerText = t.tabTranscript;
            document.getElementById('tabAnalyticsTitle').innerText = t.tabAnalytics;
            document.getElementById('btnExportTitle').innerText = t.btnExport;
            document.getElementById('docTitle').innerText = t.docTitle;
            document.getElementById('titleSecSummary').innerText = t.secSummary;
            document.getElementById('titleSecAgenda').innerText = t.secAgenda;
            document.getElementById('titleSecResolutions').innerText = t.secResolutions;
            document.getElementById('titleSecActions').innerText = t.secActions;
            document.getElementById('minutesSummary').innerText = t.summaryText;

            // Sync meeting language dropdown selector
            document.getElementById('meetingLang').value = langKey;
        }

        function onAudioLanguageChange() {
            const val = document.getElementById('meetingLang').value;
            if (translations[val]) {
                setSystemLanguage(val);
            }
        }

        function updateMeterVisual() {
            const pct = Math.min(100, Math.round((usedMinsVal / maxMinsVal) * 100));
            document.getElementById('usedMinutes').innerText = usedMinsVal.toFixed(1);
            document.getElementById('maxMinutes').innerText = maxMinsVal.toFixed(1);
            document.getElementById('meterText').innerText = `${pct}%`;

            // SVG Circumference = 163
            const dashoffset = 163 - (163 * pct / 100);
            document.getElementById('meterCircle').setAttribute('stroke-dashoffset', dashoffset);
        }

        // Animated Web Canvas Visualizer
        function initCanvasWaveform() {
            const canvas = document.getElementById('waveformCanvas');
            const ctx = canvas.getContext('2d');
            canvas.width = canvas.parentElement.clientWidth;
            canvas.height = 40;

            function drawWave() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                const barWidth = 4;
                const gap = 3;
                const count = Math.floor(canvas.width / (barWidth + gap));

                for (let i = 0; i < count; i++) {
                    const height = isRecording || isAudioPlaying 
                        ? Math.floor(Math.random() * 30) + 5 
                        : 3;
                    
                    ctx.fillStyle = isDarkMode ? '#800020' : '#a31534';
                    ctx.fillRect(i * (barWidth + gap), (canvas.height - height) / 2, barWidth, height);
                }

                animFrameId = requestAnimationFrame(drawWave);
            }

            drawWave();
        }

        function triggerFileInput() {
            document.getElementById('audioFileInput').click();
        }

        function handleFileSelect(event) {
            const file = event.target.files[0];
            if (file) {
                document.getElementById('fileName').innerText = file.name;
                document.getElementById('fileSize').innerText = (file.size / (1024 * 1024)).toFixed(1) + ' MB';
                document.getElementById('fileInfoCard').classList.remove('hidden');
            }
        }

        function loadSampleAudio() {
            document.getElementById('fileName').innerText = 'Ethiopian_Bank_Boardroom_Q3.mp3';
            document.getElementById('fileSize').innerText = '18.4 MB';
            document.getElementById('fileInfoCard').classList.remove('hidden');
        }

        function toggleMicRecording() {
            const btn = document.getElementById('micBtn');
            const timer = document.getElementById('recTimer');

            if (!isRecording) {
                isRecording = true;
                btn.classList.remove('bg-rose-600');
                btn.classList.add('bg-amber-600', 'animate-pulse');
                recSeconds = 0;
                recInterval = setInterval(() => {
                    recSeconds++;
                    const mins = String(Math.floor(recSeconds / 60)).padStart(2, '0');
                    const secs = String(recSeconds % 60).padStart(2, '0');
                    timer.innerText = `${mins}:${secs} (Recording live...)`;
                }, 1000);
            } else {
                isRecording = false;
                clearInterval(recInterval);
                btn.classList.remove('bg-amber-600', 'animate-pulse');
                btn.classList.add('bg-rose-600');
                timer.innerText = `Recorded ${Math.floor(recSeconds / 60)}m ${recSeconds % 60}s`;
                loadSampleAudio();
            }
        }

        function toggleAudioPlayback() {
            const btn = document.getElementById('playPauseBtn');
            isAudioPlaying = !isAudioPlaying;
            if (isAudioPlaying) {
                btn.innerHTML = '<i class="fa-solid fa-pause text-xs"></i>';
            } else {
                btn.innerHTML = '<i class="fa-solid fa-play text-xs"></i>';
            }
        }

        function runAiProcessing() {
            if (usedMinsVal >= maxMinsVal) {
                alert("🔒 Free trial minute limit reached! Please upgrade your plan or apply a coupon code.");
                openPaymentModal();
                return;
            }

            const card = document.getElementById('processingCard');
            const statusText = document.getElementById('procStatusText');
            const percent = document.getElementById('procPercent');
            const bar = document.getElementById('procProgressBar');

            card.classList.remove('hidden');
            let progress = 0;

            const interval = setInterval(() => {
                progress += 25;
                if (progress > 100) progress = 100;
                percent.innerText = `${progress}%`;
                bar.style.width = `${progress}%`;

                if (progress === 50) {
                    statusText.innerText = "Diarizing Speakers & Voice Fingerprints...";
                } else if (progress === 75) {
                    statusText.innerText = "Generating Boardroom Executive ቃለ ጉባዔ...";
                } else if (progress >= 100) {
                    clearInterval(interval);
                    card.classList.add('hidden');

                    // Increment used minutes by 1.5
                    usedMinsVal = Math.min(maxMinsVal, usedMinsVal + 1.5);
                    updateMeterVisual();
                }
            }, 200);
        }

        function switchTab(tabId, btnElement) {
            document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
            document.querySelectorAll('.tab-btn').forEach(btn => {
                btn.classList.remove('bg-burgundy-700', 'text-white', 'shadow-md');
                btn.classList.add('bg-slate-200', 'text-slate-700', 'dark:bg-navy-800', 'dark:text-slate-300');
            });

            document.getElementById(tabId).classList.remove('hidden');
            
            if (btnElement) {
                btnElement.classList.remove('bg-slate-200', 'text-slate-700', 'dark:bg-navy-800', 'dark:text-slate-300');
                btnElement.classList.add('bg-burgundy-700', 'text-white', 'shadow-md');
            }
        }

        function toggleTask(checkbox) {
            const textEl = checkbox.parentElement.nextElementSibling;
            if (checkbox.checked) {
                textEl.classList.add('line-through', 'text-slate-400');
            } else {
                textEl.classList.remove('line-through', 'text-slate-400');
            }
        }

        function filterTranscript() {
            const term = document.getElementById('transcriptSearch').value.toLowerCase();
            const rows = document.querySelectorAll('.transcript-row');

            rows.forEach(row => {
                const text = row.querySelector('.transcript-text').innerText.toLowerCase();
                if (text.includes(term)) {
                    row.classList.remove('hidden');
                } else {
                    row.classList.add('hidden');
                }
            });
        }

        function seekAudioTo(timestamp) {
            document.getElementById('playbackTime').innerText = `${timestamp} / 08:45`;
            if (!isAudioPlaying) {
                toggleAudioPlayback();
            }
        }

        function toggleTranscriptEditMode() {
            const texts = document.querySelectorAll('.transcript-text');
            const btn = document.getElementById('editTranscriptBtn');
            const isEditing = texts[0].isContentEditable;

            texts.forEach(t => t.contentEditable = !isEditing);
            btn.classList.toggle('bg-burgundy-700');
            btn.classList.toggle('text-white');
        }

        function toggleExportMenu() {
            document.getElementById('exportMenu').classList.toggle('hidden');
        }

        function exportData(format) {
            document.getElementById('exportMenu').classList.add('hidden');
            const minutesText = document.getElementById('tabMinutes').innerText;
            
            const blob = new Blob([minutesText], { type: 'text/plain;charset=utf-8' });
            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = `Scriber_AI_Pro_Minutes.${format}`;
            link.click();
        }

        function openPaymentModal() {
            document.getElementById('paymentModal').classList.remove('hidden');
        }

        function closePaymentModal() {
            document.getElementById('paymentModal').classList.add('hidden');
        }

        function selectGateway(gw) {
            selectedGateway = gw;
            ['Telebirr', 'Cbe', 'Chapa', 'Card'].forEach(item => {
                document.getElementById(`chk${item}`).classList.add('hidden');
            });
            const formatted = gw.charAt(0).toUpperCase() + gw.slice(1);
            document.getElementById(`chk${formatted}`).classList.remove('hidden');
        }

        function selectPlan(plan) {
            selectedPlan = plan;
            ['Payg', 'Pro', 'Enterprise'].forEach(p => {
                const el = document.getElementById(`plan${p}`);
                el.classList.remove('border-burgundy-700', 'bg-burgundy-50/50', 'dark:bg-burgundy-950/30');
            });
            const selEl = document.getElementById(`plan${plan.charAt(0).toUpperCase() + plan.slice(1)}`);
            selEl.classList.add('border-burgundy-700', 'bg-burgundy-50/50', 'dark:bg-burgundy-950/30');

            const payBtn = document.getElementById('paySubmitBtn');
            if (plan === 'payg') payBtn.innerText = 'Proceed with Payment (ETB 50)';
            else if (plan === 'pro') payBtn.innerText = 'Proceed with Payment (ETB 500)';
            else payBtn.innerText = 'Contact Enterprise Sales';
        }

        function applyPromo() {
            const val = document.getElementById('promoCode').value.trim();
            const msg = document.getElementById('promoStatusMsg');
            msg.classList.remove('hidden');

            if (val.toUpperCase() === 'ETHIO-AI-2026') {
                msg.className = "text-[11px] font-semibold text-emerald-600";
                msg.innerText = "✅ Promo code ETHIO-AI-2026 applied! 100 Free Minutes Unlocked.";
                usedMinsVal = 0.0;
                maxMinsVal = 100.0;
                updateMeterVisual();
            } else {
                msg.className = "text-[11px] font-semibold text-rose-600";
                msg.innerText = "❌ Invalid coupon code. Try ETHIO-AI-2026";
            }
        }

        function completePayment() {
            usedMinsVal = 0.0;
            maxMinsVal = 500.0;
            updateMeterVisual();
            closePaymentModal();
        }
    </script>
</body>
</html>
