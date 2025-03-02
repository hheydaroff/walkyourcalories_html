# Homepage Updates

## Objective
Modify the homepage to make the title big and bold, with the video background as the font background.

## HTML Changes (templates/index.html)

1. Modify the hero section as follows:

```html
<div class="container">
    <div class="hero-section">
        <div class="video-background">
            <!-- Ensure the video element is already present in the base template -->
        </div>
        <h1 class="hero-title">
            <span class="video-text">Walk Your Calories - Calorie to Steps Calculator</span>
        </h1>
        <p>Discover how many steps it takes to burn off your favorite foods. Our innovative calculator turns calorie counts into achievable walking targets, helping you manage your weight and improve your overall health.</p>
    </div>
    
    <!-- Rest of the content remains unchanged -->
</div>
```

## CSS Changes (static/css/styles.css)

Add the following CSS rules:

```css
.hero-section {
    position: relative;
    overflow: hidden;
}

.video-background {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
}

.hero-title {
    font-size: 3rem;
    font-weight: bold;
    text-align: center;
    padding: 20px 0;
}

.video-text {
    background: transparent;
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
}
```

## JavaScript Changes (static/js/main.js)

If not already present, add the following JavaScript to ensure the video text effect works:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    const videoBackground = document.querySelector('.video-background video');
    const videoText = document.querySelector('.video-text');

    if (videoBackground && videoText) {
        videoText.style.backgroundImage = `url(${videoBackground.src})`;
    }
});
```

## Implementation Notes

1. Ensure the video element is properly set up in the base template (base.html) if not already present.
2. Test the changes on various screen sizes to ensure responsiveness.
3. Verify that the text remains readable over the video background. Adjust text shadow or add a semi-transparent overlay if needed.
4. Check browser compatibility, especially for the background-clip property. Consider adding appropriate prefixes or fallbacks.
5. Optimize the video file to ensure fast page load times.
6. Consider adding alternative text or aria-label to the video element for accessibility.

## Accessibility Considerations

1. Ensure sufficient color contrast between the text and the video background.
2. Provide a way to pause or stop the video background for users who may find it distracting.
3. Ensure that the page is still usable and readable if the video fails to load or is turned off.

By implementing these changes, the homepage title will be big, bold, and use the video background as its font background, enhancing the visual appeal of the page while maintaining functionality and accessibility.