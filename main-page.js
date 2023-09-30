// Assume you have an array of post objects.
const articles = [
    { title: "Post 1", content: "This is the content of Post 1" },
    { title: "Post 2", content: "This is the content of Post 2" },
    // Add more articles as needed
];

// Function to dynamically generate HTML for each post
function creatArticleHTML(article) {
    return `
        <div class="swiper-slide">
            <h2>${article.title}</h2>
            <p>${article.content}</p>
        </div>
    `;
}

// Function to display articles in the container
function displayArticles() {
    const articleContainer = document.getElementById("article-container");
    articles.forEach(article => {
        const articleHTML = creatArticleHTML(article);
        articleContainer.innerHTML += articleHTML;
    });
}

// Call the displayarticles function to populate the container with articles
displayArticles();
