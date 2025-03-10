document.addEventListener('DOMContentLoaded', function() {
  const tocLinks = document.querySelectorAll('.toc-content a');
  const tocTrigger = document.querySelector('.toc-trigger');
  const tocContainer = document.querySelector('.toc-container');
  const tocClose = document.querySelector('.toc-close');

  // Debug to check if elements are found
  console.log('TOC Trigger:', tocTrigger);
  console.log('TOC Container:', tocContainer);
  console.log('TOC Close:', tocClose);

  if (!tocTrigger || !tocContainer || !tocClose) {
      console.error('One or more TOC elements are missing!');
      return;
  }

  // Toggle TOC
  tocTrigger.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      console.log('Button clicked'); // Debug line
      tocContainer.classList.toggle('active');
      console.log('TOC classes after click:', tocContainer.className); // Debug line
  });

  tocClose.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      tocContainer.classList.remove('active');
  });

  // Close TOC when clicking outside
  document.addEventListener('click', function(e) {
      if (!tocContainer.contains(e.target) && !tocTrigger.contains(e.target)) {
          tocContainer.classList.remove('active');
      }
  });
  
  // Smooth scroll to sections
  tocLinks.forEach(link => {
      link.addEventListener('click', (e) => {
          e.preventDefault();
          const targetId = link.getAttribute('href');
          const targetElement = document.querySelector(targetId);
          
          if (targetElement) {
              // Close TOC on mobile
              tocContainer.classList.remove('active');
              
              // Scroll to section with offset for fixed header
              const headerOffset = 80; // Adjust based on your header height
              const elementPosition = targetElement.getBoundingClientRect().top;
              const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
      
              window.scrollTo({
                  top: offsetPosition,
                  behavior: 'smooth'
              });
          }
      });
  });
  
  // Highlight current section in TOC
  const observerOptions = {
      rootMargin: '-80px 0px -80% 0px'
  };
  
  const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
          const id = entry.target.getAttribute('id');
          const tocLink = document.querySelector(`.toc-content a[href="#${id}"]`);
          
          if (tocLink) {
              if (entry.isIntersecting) {
                  tocLink.classList.add('active');
              } else {
                  tocLink.classList.remove('active');
              }
          }
      });
  }, observerOptions);
  
  // Observe all section headers
  document.querySelectorAll('section[id], .card-title[id]').forEach((section) => {
      observer.observe(section);
  });
});