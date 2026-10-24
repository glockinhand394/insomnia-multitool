"""Complete, theme-aware command reference for Insomnia Multitool.

This reference mirrors the top-level dashboard and its visible submenus.
Sensitive or potentially abusive features are identified by name only; this
menu does not provide instructions for credential theft, covert surveillance,
spam, service disruption, or unauthorized account/server actions.
"""

import shutil

from core.display import Theme, Colorate, clr, get_inpt

HELP_PAGES = [
    {
        "title": "NAVIGATION & DASHBOARD",
        "intro": "Every dashboard page and how to move around the app.",
        "sections": [
            ("NAVIGATION", [
                ("A / P", "Previous dashboard page"),
                ("D / N", "Next dashboard page"),
                ("P1 - P6", "Jump directly to dashboard page 1 through 6"),
                ("H / ?", "Open this help menu"),
                ("99", "Exit the app; in submenus, usually return"),
            ]),
            ("DASHBOARD GROUPS", [
                ("Page 1", "Discord Tools: options 1-9 and Discord-related submenus"),
                ("Page 2", "OSINT & Network: options 10-17"),
                ("Page 3", "Security-sensitive tools: options 20-28"),
                ("Page 4", "Roblox Utilities: options 40-47"),
                ("Page 5", "Faker & Simulators: option 50 and QR generator 35"),
                ("Page 6", "General & System: options 13, 30-34, 60-65"),
            ]),
            ("GENERAL TIPS", [
                ("Input", "Enter the number shown beside a dashboard tool"),
                ("Submenus", "Use the submenu's listed number; use 99 to return where supported"),
                ("Help pages", "Use N/D for next, P/A for previous, or a page number; 99 returns"),
            ]),
        ],
    },
    {
        "title": "DISCORD TOOLS (1-9)",
        "intro": "Top-level Discord options and the options inside their submenus.",
        "sections": [
            ("DASHBOARD OPTIONS", [
                ("1", "Webhook Tools submenu: 1 Webhook Spammer, 2 Webhook Deleter"),
                ("2", "Token & Account Tools submenu: 1 Token Bruteforce, 2 Token Info, 3 Token Nuker"),
                ("2 continued", "4 Token Login, 5 Status Rotator, 6 Token Onliner, 7 Selfbot, 8 Report Bot, 9 Server Cloner"),
                ("3", "Nitro Generator - synthetic gift-code generation/checking utility"),
                ("4", "Server Info - retrieve server details from an invite link"),
                ("5", "Bot Invite Generator - create an OAuth invite URL from a bot ID"),
                ("6", "Open the Selfbot menu"),
                ("7", "Open the Server Cloner flow"),
                ("8", "Open the Nuke Bot console"),
                ("9", "Discord Username Checker"),
            ]),
            ("SAFETY & ACCOUNT NOTES", [
                ("Tokens", "Never share account tokens; use only authorized accounts"),
                ("Webhooks", "Only manage webhooks you own or are authorized to administer"),
                ("Server actions", "Do not automate destructive actions or act on servers without permission"),
            ]),
        ],
    },
    {
        "title": "OSINT & NETWORK (10-17)",
        "intro": "Network diagnostics and lookup utilities shown in the dashboard.",
        "sections": [
            ("NETWORK", [
                ("10", "Port Scanner - checks reachable ports on a host"),
                ("11", "WHOIS Lookup - domain/IP registration details"),
                ("12", "DNS Lookup - queries DNS records such as A, MX, and TXT"),
                ("32", "IP Pinger - checks reachability and response latency"),
                ("64", "Proxy Scraper - gathers publicly listed proxy endpoints"),
                ("65", "Proxy Checker - tests proxy connectivity and response"),
            ]),
            ("LOOKUPS", [
                ("14", "Dox Tracker - local lookup/tracking utility; handle personal data lawfully"),
                ("15", "Dox Creator - profile/data organization utility; use consent-based data only"),
                ("16", "Phone Lookup - phone-number lookup utility; results may be approximate"),
                ("17", "Email Lookup - email-related public OSINT lookup"),
            ]),
            ("RESPONSIBLE USE", [
                ("Scope", "Only scan hosts/networks you own or have explicit permission to test"),
                ("Privacy", "Do not use lookup tools to stalk, expose, or harass people"),
                ("Accuracy", "Network and OSINT results can be incomplete or outdated"),
            ]),
        ],
    },
    {
        "title": "SECURITY-SENSITIVE TOOLS (20-28)",
        "intro": "These entries exist in the dashboard. This reference lists names only.",
        "sections": [
            ("DASHBOARD OPTIONS", [
                ("20", "Email Bomber - bulk email feature; not for unsolicited messaging"),
                ("21", "Crypto Clipper - clipboard/payload builder; potentially harmful"),
                ("22", "Vulnerability Scanner / SQL scanner"),
                ("23", "Brute-force / stress-test utility; only authorized lab testing is appropriate"),
                ("24", "Stealer Builder GUI - credential-stealing functionality; not documented here"),
                ("25", "Keylogger Builder - keystroke capture functionality; not documented here"),
                ("26", "IP Grabber - tracking-link functionality; respect consent and privacy"),
                ("27", "RAT Builder - remote-access payload builder; not documented here"),
                ("28", "Wallet Scanner - cryptocurrency wallet-related utility"),
            ]),
            ("SAFETY", [
                ("Authorization", "Only perform security testing with explicit authorization"),
                ("Credentials", "Never collect, expose, or use someone else's passwords, tokens, or cookies"),
                ("Network load", "Do not send unsolicited bulk traffic or disrupt services"),
            ]),
        ],
    },
    {
        "title": "ROBLOX UTILITIES (40-47)",
        "intro": "Roblox-related tools visible in the main dashboard.",
        "sections": [
            ("DASHBOARD OPTIONS", [
                ("40", "User Info - view available public profile information"),
                ("41", "Cookie Info - cookie inspection flow; do not share session cookies"),
                ("42", "Cookie Login - account-cookie login flow; sensitive account access"),
                ("43", "Group Info - inspect available group information"),
                ("44", "Asset Downloader - download supported assets"),
                ("45", "Name History - view available username history"),
                ("46", "Username Checker - check Roblox username availability"),
                ("47", "Cookie Refresher - cookie refresh flow; sensitive account credentials"),
            ]),
            ("ACCOUNT SAFETY", [
                ("Cookies", "A session cookie can grant account access; never paste it into chats"),
                ("Permission", "Use account tools only with accounts you own or are authorized to manage"),
                ("Public data", "Respect platform rules and personal privacy"),
            ]),
        ],
    },
    {
        "title": "FAKER & SIMULATORS (50)",
        "intro": "Option 50 opens a submenu with the following numbered entries.",
        "sections": [
            ("SUBMENU OPTIONS", [
                ("1", "Fake Token Generator"),
                ("2", "Fake Mail Generator"),
                ("3", "Fake Identity Generator"),
                ("4", "Fake Nitro"),
                ("5", "Fake DDoS simulation"),
                ("6", "Fake Credit Cards"),
                ("7", "Fake Wallet Miner"),
                ("8", "Social Botter simulation"),
                ("9", "Fake PayPal OTP simulation"),
                ("10", "Fake Account Generator"),
                ("11", "Fake Fortnite Check"),
                ("12", "Fake Exodus simulation"),
                ("13", "Hacker Terminal simulation"),
                ("14", "Ransomware simulation"),
                ("15", "Fake Bruteforcer simulation"),
                ("16", "QR Code Generator"),
                ("17", "Faker explanation screen"),
                ("99", "Return from the Faker submenu"),
            ]),
            ("RELATED OPTION", [
                ("35", "QR Code Generator also has a direct dashboard shortcut"),
                ("Note", "Simulation labels do not mean a tool is safe to use on real accounts or systems"),
            ]),
        ],
    },
    {
        "title": "GENERAL, FILES & SYSTEM (13, 30-35, 60-65)",
        "intro": "Utilities, app configuration, and Windows helpers.",
        "sections": [
            ("UTILITIES", [
                ("13", "Metadata Scan - inspect file metadata"),
                ("30", "Base64 Codec - enter E to encode or D to decode text"),
                ("31", "System Info - display local machine information"),
                ("33", "Obfuscator - transform Python source code"),
                ("34", "Web Cloner - retrieve website HTML for authorized archival/testing"),
                ("35", "QR Code Generator"),
            ]),
            ("APP & WINDOWS", [
                ("60", "App Info - show application information/configuration"),
                ("61", "App Config - open theme and startup settings"),
                ("62", "Defender Exclusion - modifies antivirus exclusions; use caution"),
                ("63", "Windows Debloater - launches the external WinUtil script"),
                ("64", "Proxy Scraper"),
                ("65", "Proxy Checker"),
            ]),
            ("CONFIG SUBMENU (61)", [
                ("1-13, 16", "Select a theme: Blue, Red, Purple, Green, Yellow, Pink, Cyan, Gray, Rainbow, Modern, Modern Red, Modern Purple, Insomnia, Monochrome"),
                ("14", "Toggle Auto-Update"),
                ("15", "Toggle Discord Popup"),
                ("99", "Return to the main menu"),
            ]),
        ],
    },
    {
        "title": "SETUP & TROUBLESHOOTING",
        "intro": "Install requirements and solve common launch issues.",
        "sections": [
            ("INSTALLATION", [
                ("install.bat", "Run on Windows to install the project's dependencies"),
                ("requirements.txt", "Contains Python package requirements, if provided"),
                ("start.bat", "Use the included launcher when present"),
                ("Python", "Run the app with a Python version compatible with its dependencies"),
            ]),
            ("COMMON ISSUES", [
                ("ImportError", "Install the missing package in the same Python environment"),
                ("Terminal", "Increase terminal width if borders or text are clipped"),
                ("Network", "Check connectivity, DNS settings, and firewall permissions"),
                ("Permissions", "Use elevated privileges only when genuinely required"),
                ("Updates", "Back up core/config.json and other personal configuration first"),
            ]),
            ("KEEP YOUR DATA SAFE", [
                ("Secrets", "Never share passwords, tokens, session cookies, or private keys"),
                ("Scripts", "Review unfamiliar scripts before running them"),
                ("Permission", "Use tools only on accounts, systems, and networks you are allowed to access"),
            ]),
        ],
    },
]


def show_help():
    """Display the complete paginated help menu using the active theme."""
    page_index = 0

    while True:
        clr()
        colors = Theme.get_colors()
        terminal_width = shutil.get_terminal_size(fallback=(100, 30)).columns
        box_width = max(64, min(100, terminal_width - 4))
        inner = box_width - 2
        margin = " " * max(0, (terminal_width - box_width) // 2)
        page = HELP_PAGES[page_index]

        def draw_border(left, fill, right):
            print(margin + Colorate.Horizontal(colors["head"], left + fill * inner + right))

        def draw_line(value=""):
            value = str(value).replace("\t", "    ")
            # Split overly long content into lines so no feature description disappears.
            chunks = [value[i:i + inner] for i in range(0, len(value), inner)] or [""]
            for chunk in chunks:
                padding = " " * max(0, inner - len(chunk))
                print(
                    margin
                    + Colorate.Horizontal(colors["num"], "│")
                    + Colorate.Horizontal(colors["txt"], chunk)
                    + padding
                    + Colorate.Horizontal(colors["num"], "│")
                )

        title = f" INSOMNIA HELP [{page_index + 1}/{len(HELP_PAGES)}] "
        title = title[:max(1, inner - 4)]
        left_pad = max(0, (inner - len(title)) // 2)
        right_pad = max(0, inner - len(title) - left_pad)
        print(margin + Colorate.Horizontal(
            colors["head"], "┌" + "─" * left_pad + title + "─" * right_pad + "┐"
        ))
        draw_line()
        draw_line("  " + page["title"])
        draw_line("  " + page["intro"])
        draw_line()

        for section, entries in page["sections"]:
            draw_border("├", "─", "┤")
            draw_line("  " + section)
            for key, description in entries:
                prefix = f"  [{key}] "
                available = max(1, inner - len(prefix))
                words = description.split()
                wrapped, current = [], ""
                for word in words:
                    candidate = word if not current else current + " " + word
                    if len(candidate) <= available:
                        current = candidate
                    else:
                        if current:
                            wrapped.append(current)
                        # Preserve long unbroken words rather than dropping them.
                        current = word
                if current:
                    wrapped.append(current)
                if not wrapped:
                    wrapped = [""]
                draw_line(prefix + wrapped[0])
                for continuation in wrapped[1:]:
                    draw_line(" " * len(prefix) + continuation)
            draw_line()

        draw_border("├", "─", "┤")
        draw_line(f"  [P/A] Previous  [N/D] Next  [1-{len(HELP_PAGES)}] Jump  [99] Return")
        draw_border("└", "─", "┘")

        choice = get_inpt("insomnia@help:~#").strip().lower()
        if choice in {"99", "b", "back", "q", "quit"}:
            return
        if choice in {"n", "d", "next"}:
            page_index = (page_index + 1) % len(HELP_PAGES)
        elif choice in {"p", "a", "prev", "previous"}:
            page_index = (page_index - 1) % len(HELP_PAGES)
        elif choice.isdigit() and 1 <= int(choice) <= len(HELP_PAGES):
            page_index = int(choice) - 1
