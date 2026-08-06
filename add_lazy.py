import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add preload link
preload_link = '<link rel="preload" as="image" href="Lusdoc_EnhanceImage.webp">\n  '
if 'href="Lusdoc_EnhanceImage.webp"' not in content.split('</head>')[0]: # Ensure it is not already in head
    content = content.replace('<title>', preload_link + '<title>')

# 2. Add loading="lazy" to all imgs if they don't have it
def add_lazy(match):
    img_tag = match.group(0)
    if 'loading=' not in img_tag and 'Lusdoc_EnhanceImage.webp' not in img_tag:
        # insert loading="lazy" before the closing bracket
        if img_tag.endswith('/>'):
            return img_tag[:-2] + ' loading="lazy" />'
        else:
            return img_tag[:-1] + ' loading="lazy">'
    return img_tag

content = re.sub(r'<img\s+[^>]+>', add_lazy, content)

# 3. Add skeleton CSS
skeleton_css = """
    /* Image Skeleton Loading Effect */
    .project-image, .swiper-slide {
      background-color: #2a313c;
      animation: skeleton-pulse 1.5s infinite ease-in-out;
      position: relative;
    }
    body.light-mode .project-image, body.light-mode .swiper-slide {
      background-color: #e5e7eb;
    }
    @keyframes skeleton-pulse {
      0% { opacity: 0.6; }
      50% { opacity: 1; }
      100% { opacity: 0.6; }
    }
    /* Ensure image covers skeleton when loaded */
    .project-image img, .swiper-slide img {
      position: relative;
      z-index: 1;
    }
"""

if 'skeleton-pulse' not in content:
    content = content.replace('</style>', skeleton_css + '</style>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html updated successfully with lazy loading, preloading, and skeleton CSS.")
