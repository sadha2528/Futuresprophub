import os
import re

def update_favicon():
    directory = '/Users/sadha/.gemini/antigravity/scratch/'
    
    # We want to replace any <link rel="icon" ...> with the new one.
    # It might be spread across multiple lines or single lines.
    
    # regex to match <link rel="icon" ...> 
    pattern_svg = re.compile(r'<link rel="icon" type="image/svg\+xml"[^>]*>', re.IGNORECASE)
    pattern_png = re.compile(r'<link rel="icon" type="image/png"[^>]*>', re.IGNORECASE)
    
    new_favicon = '<link rel="icon" type="image/jpeg" href="main-logo.jpg">'
    
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                html = f.read()
            
            # Replace svg link with new jpeg link
            html, subs1 = pattern_svg.subn(new_favicon, html)
            # Remove the png link completely to avoid duplicates
            html, subs2 = pattern_png.subn('', html)
            
            if subs1 > 0 or subs2 > 0:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(html)
                print(f"Updated favicon in {filename}")

if __name__ == '__main__':
    update_favicon()
