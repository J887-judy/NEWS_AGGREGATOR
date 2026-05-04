document.addEventListener("DOMContentLoaded", () => {
  const loadMoreBtn = document.getElementById("load-more");
  const newsContainer = document.getElementById("news-container");

  if (loadMoreBtn) {
    loadMoreBtn.addEventListener("click", async () => {
      try {
        // Faz uma chamada AJAX para buscar mais notícias
        const response = await fetch("/home?load_more=true");
        const data = await response.json();

        // Renderiza cada notícia nova como card
        data.forEach(noticia => {
          const card = document.createElement("div");
          card.classList.add("news-card");
          card.innerHTML = `
            <h3>${noticia.title}</h3>
            <p>${noticia.description}</p>
            <p><strong>Resumo:</strong> ${noticia.resumo}</p>
            <a href="${noticia.url}" target="_blank">Ver mais</a>
          `;
          newsContainer.appendChild(card);
        });
      } catch (error) {
        console.error("Erro ao carregar mais notícias:", error);
      }
    });
  }
});
