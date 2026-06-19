const fs = require('fs');
const path = require('path');

const filesToProcess = [
  { source: 'auth.html', target: 'src/pages/auth/Login.vue' },
  { source: 'auth.html', target: 'src/pages/auth/Register.vue' }
];

filesToProcess.forEach(fileInfo => {
  if (fs.existsSync(fileInfo.source)) {
    const htmlContent = fs.readFileSync(fileInfo.source, 'utf8');
    
    // Extract everything between <body...> and </body>
    const bodyMatch = htmlContent.match(/<body[^>]*>([\s\S]*?)<\/body>/i);
    
    if (bodyMatch && bodyMatch[1]) {
      let bodyContent = bodyMatch[1];
      
      // Clean up inline scripts from stitch HTML (like smooth scroll observers)
      bodyContent = bodyContent.replace(/<script>[\s\S]*?<\/script>/gi, '');
      
      // Create Vue component structure
      const vueComponent = `<template>\n  <div>\n    ${bodyContent}\n  </div>\n</template>\n\n<script setup>\n</script>\n\n<style scoped>\n</style>\n`;
      
      // Ensure directory exists
      const targetDir = path.dirname(fileInfo.target);
      if (!fs.existsSync(targetDir)) {
        fs.mkdirSync(targetDir, { recursive: true });
      }
      
      fs.writeFileSync(fileInfo.target, vueComponent, 'utf8');
      console.log(`Successfully generated ${fileInfo.target}`);
    } else {
      console.log(`Could not find body content in ${fileInfo.source}`);
    }
  } else {
    console.log(`Source file ${fileInfo.source} does not exist`);
  }
});
