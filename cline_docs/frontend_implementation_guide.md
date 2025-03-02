# Frontend Implementation Guide

## Overview
This guide outlines the plan for implementing the new frontend design for the Walk Your Calories application. It provides detailed instructions for the development team to follow when creating the new pages, implementing the calculator widget, and ensuring a consistent user experience across the site.

## General Guidelines
1. Use semantic HTML5 elements for better accessibility and SEO.
2. Implement responsive design using a mobile-first approach.
3. Follow WCAG 2.1 guidelines for web accessibility.
4. Optimize assets for performance (compress images, minify CSS/JS).
5. Use BEM methodology for CSS class naming to ensure maintainable styles.

## Page Structure
Implement a base template (base.html) that includes:
- Header with navigation menu
- Main content area
- Footer with compact calculator widget
- Meta tags for SEO (unique for each page)

## Navigation Menu
Include the following items in the navigation menu:
- Home
- How It Works
- Benefits
- Calculator (direct link to full calculator page)
- FAQ
- About Us

## Pages to Implement
1. Homepage (index.html)
2. How It Works (how-it-works.html)
3. Benefits (benefits.html)
4. FAQ (faq.html)
5. About Us (about-us.html)
6. Full Calculator Page (calculator.html)

## Calculator Widget
Implement the calculator widget as a reusable component:
1. Create a partial template for the widget (e.g., _calculator_widget.html).
2. Implement the widget functionality using JavaScript.
3. Ensure the widget is responsive and works on all devices.
4. Include the full version on the dedicated calculator page and the compact version in the footer.

## Styling
1. Update the existing static/styles.css file or create a new CSS file if starting from scratch.
2. Implement a color scheme and typography that aligns with the Walk Your Calories brand.
3. Use CSS Grid and/or Flexbox for layout.
4. Implement responsive breakpoints for various screen sizes.

## JavaScript
1. Create a new file (e.g., static/js/main.js) for custom JavaScript.
2. Implement the calculator functionality, including API calls to the backend for calculations.
3. Add form validation for user inputs.
4. Implement any necessary interactive elements (e.g., FAQ accordions, smooth scrolling).

## SEO Optimization
1. Implement unique meta titles and descriptions for each page as specified in the frontend_input.md file.
2. Use heading tags (H1, H2, etc.) appropriately and include relevant keywords.
3. Implement schema.org structured data where appropriate (e.g., FAQ page).

## Performance Considerations
1. Lazy load images that are not immediately visible on page load.
2. Consider implementing critical CSS for above-the-fold content.
3. Minimize HTTP requests by concatenating CSS and JavaScript files.

## Testing
1. Test the frontend on various devices and browsers to ensure compatibility.
2. Validate HTML and CSS using W3C validators.
3. Use Lighthouse or similar tools to audit performance, accessibility, and SEO.

## Accessibility
1. Ensure proper color contrast ratios for text and background colors.
2. Provide alternative text for images.
3. Implement keyboard navigation support.
4. Use ARIA attributes where necessary to improve screen reader compatibility.

## Next Steps
1. Implement the base template and global styles.
2. Create individual page templates, starting with the homepage.
3. Implement the calculator widget and integrate it across pages.
4. Add necessary JavaScript for interactivity and form submissions.
5. Conduct thorough testing and optimization.
6. Update documentation to reflect the new frontend implementation.

By following this guide, the development team should be able to implement a consistent, accessible, and performant frontend for the Walk Your Calories application.