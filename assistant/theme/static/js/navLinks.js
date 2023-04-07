let links = document.querySelectorAll('.nav a');
        links.forEach(link => {
            const currentLink = document.URL;
            const route = currentLink.split('/')[3];
            const newsLink = document.querySelector('.news');
            const bookLink = document.querySelector('.book');
            const noteLink = document.querySelector('.note');

            if (link.href === currentLink) {
                link.classList.add('bg-gray-900');
            }
            if (route === 'newsapp') {
                newsLink.classList.add('bg-gray-900');
            }
            if (route === 'book_app') {
                bookLink.classList.add('bg-gray-900');
            }
            if (route === 'note_app') {
                noteLink.classList.add('bg-gray-900');
            }
        });