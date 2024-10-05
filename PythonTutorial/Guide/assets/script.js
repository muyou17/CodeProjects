document.addEventListener('DOMContentLoaded', () => {
    const scrollbarThumb = document.createElement('style');
    document.head.appendChild(scrollbarThumb);
    
    function displayScrollbar(shouldDisplayScrollbar) {
        if (shouldDisplayScrollbar) {
            scrollbarThumb.innerHTML = '::-webkit-scrollbar-thumb { background-color: gray }';
        } else {
            scrollbarThumb.innerHTML = '::-webkit-scrollbar-thumb { background-color: transparent }';
        }
    }

    document.addEventListener('scroll', () => {
        displayScrollbar(true)

        setTimeout(() => {
            displayScrollbar(false);
        }, 800);
    });

    document.addEventListener('mousemove', (e) => {
        const windowWidth = window.innerWidth;
        const threshold = windowWidth / 9.80665;

        if (e.clientX > windowWidth - threshold) {
            displayScrollbar(true);
        } else {
            displayScrollbar(false);
        }
    });
});