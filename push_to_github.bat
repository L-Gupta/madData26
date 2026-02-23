@echo off
echo Starting git push process...
git add .
git commit -m "Deployment configurations and latest changes"
git branch -M main
git remote remove origin 2>nul
git remote add origin https://github.com/L-Gupta/madData26.git
echo Pushing to origin...
git push -u origin main
echo Done!
