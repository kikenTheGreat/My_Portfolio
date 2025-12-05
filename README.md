# Lusdoc Portfolio Website

Simple portfolio site for Kent Jocel Lusdoc.

How to view locally

1. Open the `index.html` file in a browser.

```powershell
Start-Process 'c:\Users\kent\Downloads\Lusdoc_Website_Portfolio\index.html'
```

How to push to GitHub (example)

1. Create a repository on GitHub.
2. Add the remote and push:

```powershell
# HTTPS
git remote add origin https://github.com/youruser/your-repo.git
# or SSH
# git remote add origin git@github.com:youruser/your-repo.git

git branch -M main
git push -u origin main
```

Notes
- The site includes a theme toggle (dark/light) that persists your choice.
- CSS lives in `css/styles.css` (and `css/styles.min.css` for production/minified).
- If you want me to push to your remote, share the repo URL and whether to use HTTPS or SSH.
