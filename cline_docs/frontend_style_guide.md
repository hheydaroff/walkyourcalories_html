# Frontend Style Guide for Walk Your Calories

## Color Palette

- Alabaster: #f3f0e8 (RGB: 243, 240, 232)
- Sage: #b9b99d (RGB: 185, 185, 157)
- Ebony: #606c5a (RGB: 96, 108, 90)
- Davy's Gray: #5e5e5e (RGB: 94, 94, 94)
- Platinum: #e6e4e0 (RGB: 230, 228, 224)

Use these colors consistently across the site to maintain a cohesive look and feel.

## Typography

- Headings: Use a clean, modern sans-serif font (e.g., 'Roboto', 'Open Sans')
- Body Text: Use a highly readable sans-serif font (e.g., 'Lato', 'Source Sans Pro')
- Font Sizes:
  - H1: 32px
  - H2: 24px
  - H3: 20px
  - Body: 16px
- Line Height: 1.5 for body text

## Layout

- Use a responsive grid system
- Max-width for content areas: 1200px
- Padding for mobile: 20px
- Padding for desktop: 40px

## Components

### Calculator Widget

- Full Version:
  ```html
  <div id="calculator-widget">
    <!-- Implement full calculator functionality here -->
  </div>
  ```
- Mini Version (for Benefits page):
  ```html
  <div id="mini-calculator">
    <form>
      <input type="number" placeholder="Quick Calorie Check" required>
      <button type="submit">Convert to Steps</button>
    </form>
    <div id="quick-result"></div>
  </div>
  ```
- Footer Version:
  ```html
  <div id="footer-calculator">
    <form>
      <input type="number" placeholder="Quick Calorie Check" required>
      <button type="submit">Get Steps</button>
    </form>
  </div>
  ```

### Navigation Menu

- Include the following items:
  - Home
  - How It Works
  - Benefits
  - Calculator (Direct link to full calculator page)
  - FAQ
  - About Us
- Use a responsive design that collapses into a hamburger menu on mobile devices

### Buttons

- Primary CTA:
  - Background: Ebony (#606c5a)
  - Text: Alabaster (#f3f0e8)
  - Hover: Lighten background by 10%
- Secondary CTA:
  - Background: Sage (#b9b99d)
  - Text: Ebony (#606c5a)
  - Hover: Darken background by 10%

### Forms

- Input fields:
  - Border: 1px solid Davy's Gray (#5e5e5e)
  - Background: Alabaster (#f3f0e8)
  - Text: Davy's Gray (#5e5e5e)
- Labels: Above input fields, Sage (#b9b99d) color

## Responsive Design

- Mobile-first approach
- Breakpoints:
  - Mobile: up to 767px
  - Tablet: 768px to 1023px
  - Desktop: 1024px and above

## SEO Best Practices

- Use unique meta titles and descriptions for each page
- Include relevant keywords in headings and content
- Use semantic HTML5 elements (header, nav, main, section, article, footer)
- Implement schema.org structured data where appropriate

## Content Guidelines

- Keep paragraphs short and scannable
- Use bullet points for lists and key features
- Include clear calls-to-action (CTAs) on each page
- Maintain a consistent, friendly, and informative tone

## Images and Icons

- Use high-quality, relevant images that represent diverse body types and activities
- Optimize images for web to ensure fast loading times
- Use SVG icons where possible for scalability

## Accessibility

- Ensure sufficient color contrast (WCAG 2.1 compliant)
- Use descriptive alt text for images
- Implement proper heading hierarchy (H1, H2, H3, etc.)
- Ensure keyboard navigation for all interactive elements

## Performance

- Minimize HTTP requests
- Use lazy loading for images and non-critical content
- Implement critical CSS for above-the-fold content

By following this style guide, we'll create a consistent, user-friendly, and visually appealing experience across the Walk Your Calories website.