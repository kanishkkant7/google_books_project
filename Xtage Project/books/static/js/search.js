gsap.from(".banner-disp-txt-search",
    {
        opacity: 0,
        x: 50,
        duration: 1,
        onComplete: gsap.from(".search-banner", {
    
                opacity: 0,
                duration: 2
            })
    }
    )