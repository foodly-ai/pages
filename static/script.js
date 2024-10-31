function addGoogleTag() {
    // Create the async gtag.js script
    const gtagScript = document.createElement('script');
    gtagScript.async = true;
    gtagScript.src = 'https://www.googletagmanager.com/gtag/js?id=G-8DQ89R6QNK';
    document.head.appendChild(gtagScript);

    // Add the gtag configuration script
    gtagScript.onload = () => {
        window.dataLayer = window.dataLayer || [];
        function gtag(){ dataLayer.push(arguments); }
        gtag('js', new Date());
        gtag('config', 'G-8DQ89R6QNK');
    };
}

// Call the function to add the Google Tag script
addGoogleTag();
