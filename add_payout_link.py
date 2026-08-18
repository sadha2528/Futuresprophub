import os
import re

def add_payout_calculator():
    directory = '/Users/sadha/.gemini/antigravity/scratch/'
    
    # We want to add Payout Calculator to the Tools column in the footer.
    # In index.html, it's after Compare All button.
    # In other pages, it's after Compare All link.
    
    # Let's match the Compare All line and append the Payout Calculator line.
    
    new_link_btn = '\n          <a href="payout-calculator.html" class="footer-col-link">Payout Calculator</a>'
    
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                html = f.read()
            
            original_html = html
            
            if 'payout-calculator.html' in html:
                continue # Already added
                
            if filename == 'index.html':
                # Match the Compare All button
                pattern = r"(<button class=\"footer-col-btn\".*?>Compare All</button>)"
                html = re.sub(pattern, r"\1" + new_link_btn, html)
            else:
                # Match the Compare All link
                # In other files, it's <a href="index.html" class="footer-col-link">Compare All</a> or similar
                # Let's use a regex to find the Compare All link in the Tools column (or just any Compare All in footer)
                # To be safe, find footer-col-title">Tools</div> and then inject after Compare All
                
                tools_match = re.search(r'(<div class="footer-col-title">Tools</div>.*?</div>)', html, re.DOTALL)
                if tools_match:
                    tools_block = tools_match.group(1)
                    new_tools_block = re.sub(r'(<a .*?>Compare All</a>)', r'\1' + new_link_btn, tools_block)
                    html = html.replace(tools_block, new_tools_block)
            
            if html != original_html:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(html)
                print(f"Added Payout Calculator link to {filename}")

if __name__ == '__main__':
    add_payout_calculator()
