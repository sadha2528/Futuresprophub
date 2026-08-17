import os
import re

def update_logo():
    directory = '/Users/sadha/.gemini/antigravity/scratch/'
    
    # We want to replace the <svg>...</svg> block immediately following <a href="index.html" class="logo-lnk">
    # Because there are variations (maybe) we'll just look for the specific SVG code block.
    
    pattern = re.compile(r'<svg width="36" height="36" viewBox="0 0 36 36" fill="none".*?</svg>', re.DOTALL)
    new_logo = '<img src="main-logo.jpg" alt="Futures Prop Compare" width="36" height="36" style="border-radius: 9px; object-fit: cover;">'
    
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                html = f.read()
            
            new_html, num_subs = pattern.subn(new_logo, html)
            if num_subs > 0:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_html)
                print(f"Updated {filename} ({num_subs} replacements)")

if __name__ == '__main__':
    update_logo()
