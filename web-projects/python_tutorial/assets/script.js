document.addEventListener('DOMContentLoaded', () => {
    const scrollbarThumb = document.createElement('style');
    document.head.appendChild(scrollbarThumb);
    
    function displayScrollbar(shouldDisplayScrollbar) {
        if (shouldDisplayScrollbar) {
            scrollbarThumb.innerHTML = '::-webkit-scrollbar-thumb { background-color: gray }';
        }

        setTimeout(() => {
            scrollbarThumb.innerHTML = '::-webkit-scrollbar-thumb { background-color: transparent }';
        }, 800);
    }

    document.addEventListener('scroll', () => {
        displayScrollbar(true)
    });

    document.addEventListener('mousemove', (e) => {
        const windowWidth = window.innerWidth;
        const threshold = windowWidth / 9.80665;

        if (e.clientX > windowWidth - threshold) {
            displayScrollbar(true);
        }
    });
});