#!/usr/bin/env python3
"""
hands4flow CMS — Site beheer tool
Versie 1.1 — Voor Elsemarie

Een simpele command-line tool om de Jekyll-site te beheren.
Alle tekst kan worden aangepast, opmaak en structuur blijven behouden.
"""

import os
import sys
import re
from datetime import datetime
from pathlib import Path

# Kleuren voor terminal output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def clear_screen():
    """Maak het scherm leeg"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(text):
    """Print een mooie header"""
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*60}")
    print(f"  {text}")
    print(f"{'='*60}{Colors.ENDC}\n")

def print_success(text):
    """Print succesmelding"""
    print(f"{Colors.OKGREEN}✓ {text}{Colors.ENDC}")

def print_error(text):
    """Print foutmelding"""
    print(f"{Colors.FAIL}✗ {text}{Colors.ENDC}")

def print_info(text):
    """Print info"""
    print(f"{Colors.OKCYAN}ℹ {text}{Colors.ENDC}")

def wait_for_enter():
    """Wacht op enter om verder te gaan"""
    input(f"\n{Colors.OKBLUE}Druk op ENTER om verder te gaan...{Colors.ENDC}")

def get_file_content(filepath):
    """Lees bestand inhoud"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print_error(f"Bestand niet gevonden: {filepath}")
        return None
    except Exception as e:
        print_error(f"Fout bij lezen: {e}")
        return None

def save_file_content(filepath, content):
    """Sla bestand inhoud op"""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print_error(f"Fout bij opslaan: {e}")
        return False

def extract_between(content, start, end):
    """Haal tekst tussen twee markers"""
    try:
        start_idx = content.find(start)
        if start_idx == -1:
            return None
        
        start_idx += len(start)
        end_idx = content.find(end, start_idx)
        
        if end_idx == -1:
            return None
        
        return content[start_idx:end_idx].strip()
    except:
        return None

def replace_between(content, start, end, new_text):
    """Vervang tekst tussen twee markers"""
    try:
        start_idx = content.find(start)
        if start_idx == -1:
            return content
        
        start_idx += len(start)
        end_idx = content.find(end, start_idx)
        
        if end_idx == -1:
            return content
        
        return content[:start_idx] + new_text + content[end_idx:]
    except:
        return content

def edit_multiline_text(current_text, field_name):
    """Bewerk meerregelige tekst"""
    print(f"\n{Colors.BOLD}Huidige tekst voor {field_name}:{Colors.ENDC}")
    print(f"{Colors.OKCYAN}{current_text}{Colors.ENDC}\n")
    
    print(f"{Colors.WARNING}Nieuwe tekst (typ EINDE op een nieuwe regel als je klaar bent):{Colors.ENDC}")
    lines = []
    while True:
        try:
            line = input()
            if line.strip().upper() == "EINDE":
                break
            lines.append(line)
        except EOFError:
            break
    
    new_text = "\n".join(lines).strip()
    if not new_text:
        print_info("Geen wijziging — oude tekst behouden.")
        return current_text
    
    return new_text

def edit_single_line(current_text, field_name):
    """Bewerk enkele regel tekst"""
    print(f"\n{Colors.BOLD}Huidige {field_name}:{Colors.ENDC} {Colors.OKCYAN}{current_text}{Colors.ENDC}")
    new_text = input(f"Nieuwe {field_name} (of ENTER om te behouden): ").strip()
    return new_text if new_text else current_text

# ═══════════════════════════════════════════════════════════════
#  HOMEPAGE EDITOR
# ═══════════════════════════════════════════════════════════════

def edit_homepage():
    """Bewerk de homepage"""
    clear_screen()
    print_header("📝 Homepage bewerken")
    
    filepath = "index.md"
    content = get_file_content(filepath)
    if not content:
        wait_for_enter()
        return
    
    print("Welk onderdeel wil je bewerken?\n")
    print("1. Hero titel")
    print("2. Hero beschrijving")
    print("3. Behandelingen introductie")
    print("4. Terug naar hoofdmenu")
    
    choice = input("\nKeuze (1-4): ").strip()
    
    if choice == "1":
        # Hero titel bewerken
        current = extract_between(content, "<h1 class=\"fade-up delay-1\">", "</h1>")
        if current:
            # Strip HTML tags
            clean = re.sub(r'<[^>]+>', ' ', current)
            clean = re.sub(r'\s+', ' ', clean).strip()
            
            new_text = edit_single_line(clean, "hero titel")
            
            # Behoud <em> en <br> structuur
            if "licht" in new_text.lower():
                words = new_text.split()
                formatted = []
                for word in words:
                    if "licht" in word.lower():
                        formatted.append(f"<em>{word}</em>")
                    else:
                        formatted.append(word)
                new_text = " ".join(formatted)
            
            # Voeg <br> toe na tweede woord
            parts = new_text.split()
            if len(parts) > 2:
                new_text = " ".join(parts[:2]) + "<br>" + " ".join(parts[2:])
            
            content = replace_between(content, "<h1 class=\"fade-up delay-1\">", "</h1>", f"\n      {new_text}\n    ")
            
            if save_file_content(filepath, content):
                print_success("Hero titel bijgewerkt!")
        else:
            print_error("Kon hero titel niet vinden in index.md")
    
    elif choice == "2":
        # Hero beschrijving
        current = extract_between(content, '<p class="hero-desc fade-up delay-2">', "</p>")
        if current:
            new_text = edit_multiline_text(current, "hero beschrijving")
            content = replace_between(content, '<p class="hero-desc fade-up delay-2">', "</p>", f"\n      {new_text}\n    ")
            
            if save_file_content(filepath, content):
                print_success("Hero beschrijving bijgewerkt!")
        else:
            print_error("Kon hero beschrijving niet vinden")
    
    elif choice == "3":
        # Behandelingen intro
        current = extract_between(content, '<h2 class="section-title">Behandelingen<br>voor jouw welzijn</h2>', '<div class="treatments-grid">')
        if current:
            # Zoek alleen de <p class="section-sub">
            intro = extract_between(current, '<p class="section-sub">', '</p>')
            if intro:
                new_text = edit_multiline_text(intro, "behandelingen introductie")
                content = replace_between(content, '<p class="section-sub">', '</p>', f"\n      {new_text}\n    ")
                
                if save_file_content(filepath, content):
                    print_success("Behandelingen intro bijgewerkt!")
            else:
                print_error("Kon intro tekst niet vinden")
        else:
            print_error("Kon behandelingen sectie niet vinden")
    
    elif choice == "4":
        return
    
    wait_for_enter()

# ═══════════════════════════════════════════════════════════════
#  PAGINA EDITOR
# ═══════════════════════════════════════════════════════════════

def edit_page():
    """Bewerk een pagina"""
    clear_screen()
    print_header("📄 Pagina bewerken")
    
    pages = {
        "1": ("over-mij.md", "Over mij"),
        "2": ("tarieven.md", "Tarieven"),
        "3": ("contact.md", "Contact"),
        "4": ("behandelingen/voetreflexmassage.md", "Voetreflexmassage"),
        "5": ("behandelingen/reiki.md", "Reiki"),
        "6": ("behandelingen/acces-bars.md", "Acces Bars"),
        "7": ("behandelingen/stoelmassage.md", "Stoelmassage"),
        "8": ("coaching/happy-soul-sessies.md", "Happy Soul Sessies"),
    }
    
    print("Welke pagina wil je bewerken?\n")
    for key, (_, name) in pages.items():
        print(f"{key}. {name}")
    print("9. Terug naar hoofdmenu")
    
    choice = input("\nKeuze (1-9): ").strip()
    
    if choice == "9":
        return
    
    if choice not in pages:
        print_error("Ongeldige keuze")
        wait_for_enter()
        return
    
    filepath, pagename = pages[choice]
    
    # Check of bestand bestaat
    if not Path(filepath).exists():
        print_error(f"Bestand niet gevonden: {filepath}")
        print_info("Controleer of het bestand bestaat in de repository")
        wait_for_enter()
        return
    
    content = get_file_content(filepath)
    if not content:
        wait_for_enter()
        return
    
    # Open in standaard editor
    clear_screen()
    print_header(f"✏️ {pagename} bewerken")
    print_info(f"Bestand: {filepath}")
    print(f"\n{Colors.WARNING}Het bestand wordt geopend in je teksteditor...{Colors.ENDC}\n")
    
    wait_for_enter()
    
    if sys.platform == "darwin":  # macOS
        os.system(f'open -e "{filepath}"')
    elif sys.platform == "win32":  # Windows
        os.system(f'notepad "{filepath}"')
    else:  # Linux
        editor = os.environ.get('EDITOR', 'nano')
        os.system(f'{editor} "{filepath}"')
    
    print_success(f"Bestand geopend. Sla op en sluit de editor als je klaar bent.")
    wait_for_enter()

# ═══════════════════════════════════════════════════════════════
#  BLOG EDITOR
# ═══════════════════════════════════════════════════════════════

def list_blog_posts():
    """Toon lijst van blogposts"""
    posts_dir = Path("_posts")
    if not posts_dir.exists():
        posts_dir.mkdir()
    
    posts = sorted(posts_dir.glob("*.md"), reverse=True)
    return posts

def create_blog_post():
    """Maak nieuwe blogpost"""
    clear_screen()
    print_header("✍️ Nieuwe blogpost maken")
    
    title = input("Titel van de blogpost: ").strip()
    if not title:
        print_error("Titel mag niet leeg zijn")
        wait_for_enter()
        return
    
    # Genereer bestandsnaam
    today = datetime.now().strftime("%Y-%m-%d")
    slug = re.sub(r'[^\w\s-]', '', title.lower())
    slug = re.sub(r'[\s_-]+', '-', slug)
    filename = f"{today}-{slug}.md"
    
    print_info(f"Bestandsnaam wordt: {filename}")
    
    excerpt = input("\nKorte samenvatting (1-2 zinnen): ").strip()
    
    print(f"\n{Colors.WARNING}Schrijf nu de volledige blogpost.")
    print("Gebruik lege regels tussen paragrafen.")
    print(f"Typ EINDE op een nieuwe regel als je klaar bent.{Colors.ENDC}\n")
    
    content_lines = []
    while True:
        try:
            line = input()
            if line.strip().upper() == "EINDE":
                break
            # Maak automatisch <p> tags
            if line.strip():
                content_lines.append(f"    <p>{line.strip()}</p>\n")
            else:
                content_lines.append("\n")
        except EOFError:
            break
    
    content_text = "".join(content_lines).strip()
    
    if not content_text:
        print_error("Blogpost mag niet leeg zijn")
        wait_for_enter()
        return
    
    # Genereer markdown bestand
    post_content = f"""---
layout: default
title: "{title}"
date: {today}
excerpt: "{excerpt}"
---

<section class="page-hero">
  <div class="breadcrumb">
    <a href="{{{{ '/' | absolute_url }}}}">Home</a>
    <span><a href="{{{{ '/blog/' | absolute_url }}}}">Blog</a></span>
    <span>{{{{ page.title }}}}</span>
  </div>
  <span class="section-label">{{{{ page.date | date: "%d %B %Y" }}}}</span>
  <h1 class="section-title">{{{{ page.title }}}}</h1>
</section>

<section style="background:var(--white);">
  <article style="max-width:750px;margin:0 auto;font-size:1.05rem;line-height:1.85;color:var(--text);">
    
{content_text}

    <p style="font-style:italic;color:var(--bruin-lt);margin-top:2rem;">— Elsemarie</p>

  </article>
</section>

<section style="background:var(--creme-mid);padding:3rem 5vw;text-align:center;">
  <a href="{{{{ '/blog/' | absolute_url }}}}" class="btn-secondary" style="margin:0;">← Terug naar alle blogposts</a>
</section>
"""
    
    # Sla op
    posts_dir = Path("_posts")
    posts_dir.mkdir(exist_ok=True)
    
    filepath = posts_dir / filename
    
    if save_file_content(filepath, post_content):
        print_success(f"Blogpost aangemaakt: {filename}")
        print_info("Vergeet niet te committen en pushen naar GitHub!")
    
    wait_for_enter()

def edit_blog_post():
    """Bewerk bestaande blogpost"""
    clear_screen()
    print_header("✏️ Blogpost bewerken")
    
    posts = list_blog_posts()
    
    if not posts:
        print_error("Nog geen blogposts gevonden")
        print_info("Maak eerst een blogpost aan via 'Nieuwe blogpost schrijven'")
        wait_for_enter()
        return
    
    print("Beschikbare blogposts:\n")
    for i, post in enumerate(posts, 1):
        # Toon datum en titel
        date_part = post.stem[:10]
        title_part = post.stem[11:].replace('-', ' ').title()
        print(f"{i}. [{date_part}] {title_part}")
    print("\n0. Terug")
    
    choice = input("\nWelke post wil je bewerken? ").strip()
    
    if choice == "0":
        return
    
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(posts):
            filepath = posts[idx]
            print_info(f"\nOpenen: {filepath.name}")
            
            if sys.platform == "darwin":
                os.system(f'open -e "{filepath}"')
            elif sys.platform == "win32":
                os.system(f'notepad "{filepath}"')
            else:
                editor = os.environ.get('EDITOR', 'nano')
                os.system(f'{editor} "{filepath}"')
            
            print_success("Bestand geopend in editor")
        else:
            print_error("Ongeldige keuze")
    except ValueError:
        print_error("Voer een geldig nummer in")
    
    wait_for_enter()

def manage_blog():
    """Blog beheer menu"""
    while True:
        clear_screen()
        print_header("📝 Blog beheren")
        
        posts = list_blog_posts()
        print(f"Aantal blogposts: {len(posts)}\n")
        
        print("1. Nieuwe blogpost schrijven")
        print("2. Bestaande blogpost bewerken")
        print("3. Lijst van alle posts")
        print("4. Terug naar hoofdmenu")
        
        choice = input("\nKeuze (1-4): ").strip()
        
        if choice == "1":
            create_blog_post()
        elif choice == "2":
            edit_blog_post()
        elif choice == "3":
            clear_screen()
            print_header("📚 Alle blogposts")
            if posts:
                for post in posts:
                    date_part = post.stem[:10]
                    title_part = post.stem[11:].replace('-', ' ').title()
                    print(f"  • [{date_part}] {title_part}")
            else:
                print("Nog geen blogposts")
            wait_for_enter()
        elif choice == "4":
            break

# ═══════════════════════════════════════════════════════════════
#  FAQ EDITOR
# ═══════════════════════════════════════════════════════════════

def edit_faq():
    """Bewerk FAQ pagina"""
    clear_screen()
    print_header("❓ FAQ bewerken")
    
    filepath = "faq/veelgestelde-vragen.md"
    
    if not Path(filepath).exists():
        print_error(f"FAQ bestand niet gevonden: {filepath}")
        wait_for_enter()
        return
    
    print_info(f"Het FAQ bestand wordt geopend in je editor...")
    print_info(f"Bestand: {filepath}\n")
    
    wait_for_enter()
    
    if sys.platform == "darwin":
        os.system(f'open -e "{filepath}"')
    elif sys.platform == "win32":
        os.system(f'notepad "{filepath}"')
    else:
        editor = os.environ.get('EDITOR', 'nano')
        os.system(f'{editor} "{filepath}"')
    
    print_success("FAQ bestand geopend. Bewerk en sla op.")
    wait_for_enter()

# ═══════════════════════════════════════════════════════════════
#  HOOFDMENU
# ═══════════════════════════════════════════════════════════════

def main_menu():
    """Hoofdmenu van de CMS"""
    while True:
        clear_screen()
        print(f"{Colors.HEADER}{Colors.BOLD}")
        print("╔══════════════════════════════════════════════════════════╗")
        print("║                                                          ║")
        print("║             hands4flow — Site Beheer Tool                ║")
        print("║                   Versie 1.1                             ║")
        print("║                                                          ║")
        print("╚══════════════════════════════════════════════════════════╝")
        print(f"{Colors.ENDC}\n")
        
        print(f"{Colors.OKCYAN}Wat wil je doen?{Colors.ENDC}\n")
        print("1. 📝 Homepage bewerken")
        print("2. 📄 Pagina's bewerken (opent in editor)")
        print("3. ✍️  Blog beheren")
        print("4. ❓ FAQ bewerken (opent in editor)")
        print("5. ℹ️  Help & uitleg")
        print("6. 🚪 Afsluiten")
        
        choice = input(f"\n{Colors.BOLD}Keuze (1-6): {Colors.ENDC}").strip()
        
        if choice == "1":
            edit_homepage()
        elif choice == "2":
            edit_page()
        elif choice == "3":
            manage_blog()
        elif choice == "4":
            edit_faq()
        elif choice == "5":
            show_help()
        elif choice == "6":
            clear_screen()
            print(f"\n{Colors.OKGREEN}✓ Vergeet niet je wijzigingen te committen en pushen!{Colors.ENDC}")
            print(f"{Colors.OKBLUE}  git add .{Colors.ENDC}")
            print(f"{Colors.OKBLUE}  git commit -m \"Tekst bijgewerkt\"{Colors.ENDC}")
            print(f"{Colors.OKBLUE}  git push{Colors.ENDC}\n")
            print(f"{Colors.OKGREEN}Tot ziens! 👋{Colors.ENDC}\n")
            sys.exit(0)
        else:
            print_error("Ongeldige keuze, probeer opnieuw")
            wait_for_enter()

def show_help():
    """Toon hulp informatie"""
    clear_screen()
    print_header("ℹ️ Help & Uitleg")
    
    print(f"{Colors.BOLD}Hoe werkt deze tool?{Colors.ENDC}\n")
    print("• Homepage: bewerk titel, beschrijving en intro's direct in de tool")
    print("• Pagina's & FAQ: worden geopend in je teksteditor")
    print("• Blog: schrijf nieuwe posts of bewerk bestaande\n")
    
    print(f"{Colors.BOLD}Na het bewerken:{Colors.ENDC}\n")
    print(f"  {Colors.OKBLUE}git add .{Colors.ENDC}")
    print(f"  {Colors.OKBLUE}git commit -m \"Beschrijving van wijziging\"{Colors.ENDC}")
    print(f"  {Colors.OKBLUE}git push{Colors.ENDC}\n")
    
    print(f"{Colors.BOLD}Tips:{Colors.ENDC}\n")
    print("• Blogposts: typ EINDE op nieuwe regel als je klaar bent")
    print("• Laat veld leeg (ENTER) om oude waarde te behouden")
    print("• Check altijd je wijzigingen op www.hands4flow.site\n")
    
    wait_for_enter()

# ═══════════════════════════════════════════════════════════════
#  START
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Check of we in de juiste map zitten
    if not Path("_config.yml").exists():
        print_error("Fout: _config.yml niet gevonden!")
        print_info("Zorg dat je deze tool uitvoert vanuit de root van je Jekyll site.")
        print_info(f"Huidige map: {os.getcwd()}")
        sys.exit(1)
    
    try:
        main_menu()
    except KeyboardInterrupt:
        clear_screen()
        print(f"\n{Colors.WARNING}Tool afgesloten (Ctrl+C){Colors.ENDC}\n")
        sys.exit(0)
