import os
import re

def fix_remaining():
    files = ['compare-futures-prop-firms.html', 'best-prop-firms-for-futures.html', 'futures-prop-firm-rules.html']
    directory = '/Users/sadha/.gemini/antigravity/scratch/'
    
    new_link = '<a href="payout-calculator.html">Payout Calculator</a>'
    
    for filename in files:
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
        
        if 'payout-calculator.html' in html:
            continue
            
        pattern = r'(<a href="index\.html">Compare All</a>)'
        html, count = re.subn(pattern, r'\1' + new_link, html)
        
        if count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Added Payout Calculator link to {filename}")

if __name__ == '__main__':
    fix_remaining()
