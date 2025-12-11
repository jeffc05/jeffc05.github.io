#!/usr/bin/env python3
"""Fix Plotly HTML plots by replacing near-black color codes with proper colors."""

import re
import os

# Color palette - using vibrant colors
colors = [
    "#636EFA",  # blue
    "#EF553B",  # red
    "#00CC96",  # green
    "#AB63FA",  # purple
    "#FFA15A",  # orange
    "#19D3F3",  # cyan
    "#FF6692",  # pink
    "#B6E880",  # light green
    "#FF97FF",  # magenta
    "#FECB52",  # yellow
]

def fix_html_file(filepath):
    """Replace near-black color codes with proper colors in HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Find all near-black color codes (#000001, #000002, etc.)
    # and replace with proper colors from our palette
    color_counter = {}
    
    def replace_color(match):
        hex_code = match.group(1)
        try:
            # Extract the number from #000NNN
            num = int(hex_code[5:], 16)
            if num < 1 or num > len(colors):
                return match.group(0)
            
            color_idx = (num - 1) % len(colors)
            return f'"{colors[color_idx]}"'
        except:
            return match.group(0)
    
    # Replace color codes in marker definitions
    content = re.sub(r'"color":"(#000\d{3})"', replace_color, content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Fixed: {filepath}")
        return True
    else:
        print(f"- No changes needed: {filepath}")
        return False

def main():
    """Fix all HTML plot files in the rental_prices directory."""
    plot_dir = "/Users/jchan/Projects/jeffc05.github.io/assets/images/projects/rental_prices"
    html_files = [
        "box_rental_by_category.html",
        "box_rental_by_district.html",
        "box_rental_by_category_and_district.html",
        "scatter_actual_vs_pred_log.html",
        "feature_importances_xgb.html",
    ]
    
    fixed_count = 0
    for filename in html_files:
        filepath = os.path.join(plot_dir, filename)
        if os.path.exists(filepath):
            if fix_html_file(filepath):
                fixed_count += 1
        else:
            print(f"✗ Not found: {filepath}")
    
    print(f"\nFixed {fixed_count} file(s).")

if __name__ == "__main__":
    main()
