import os

def update_logo_css():
    directory = '/Users/sadha/.gemini/antigravity/scratch/'
    
    old_tag = '<img src="main-logo.jpg" alt="Futures Prop Compare" width="36" height="36" style="border-radius: 9px; object-fit: cover;">'
    
    # We use a container that acts as the 36x36 mask, and scale the image up inside it to crop out the black padding.
    new_tag = (
        '<div style="width:36px; height:36px; border-radius:9px; overflow:hidden; display:flex; align-items:center; justify-content:center; flex-shrink:0;">'
        '<img src="main-logo.jpg" alt="Futures Prop Compare" style="width: 175%; height: 175%; object-fit: cover; object-position: center;">'
        '</div>'
    )
    
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                html = f.read()
            
            if old_tag in html:
                html = html.replace(old_tag, new_tag)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(html)
                print(f"Updated logo CSS in {filename}")

if __name__ == '__main__':
    update_logo_css()
