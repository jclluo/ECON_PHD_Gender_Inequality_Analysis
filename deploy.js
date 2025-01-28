const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

try {
  // Clean up any existing gh-pages related files
  execSync('rm -rf node_modules/.cache/gh-pages');
  
  // Create and switch to a temporary directory
  const tempDir = path.join(process.cwd(), 'temp-deploy');
  if (fs.existsSync(tempDir)) {
    execSync(`rm -rf ${tempDir}`);
  }
  fs.mkdirSync(tempDir);
  
  // Copy build files to temp directory
  execSync(`cp -r build/* ${tempDir}`);
  
  // Initialize git in temp directory
  process.chdir(tempDir);
  execSync('git init');
  execSync('git add .');
  execSync('git config user.name "GitHub Actions Bot"');
  execSync('git config user.email "actions@github.com"');
  execSync('git commit -m "Deploy to GitHub Pages"');
  
  // Push to gh-pages branch - using main or HEAD instead of master
  execSync('git push --force https://github.com/jclluo/Gender_composition_STEM.git HEAD:gh-pages');
  
  // Clean up
  process.chdir('..');
  execSync(`rm -rf ${tempDir}`);
  
  console.log('Deployment successful!');
} catch (error) {
  console.error('Deployment failed:', error);
  process.exit(1);
} 