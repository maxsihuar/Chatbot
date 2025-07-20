document.addEventListener("DOMContentLoaded", () => {
    const toggleBtn = document.getElementById("toggle-dark");

    toggleBtn.addEventListener("click", () => {
        const isDark = document.body.classList.toggle("dark-mode");
        localStorage.setItem("modoOscuro", isDark);
        toggleBtn.innerHTML = isDark ? "☀️ Modo Claro" : "🌙 Modo Oscuro";

        toggleBubbleStyles(isDark);
    });

    // Aplicar modo oscuro al cargar si estaba guardado
    if (localStorage.getItem("modoOscuro") === "true") {
        document.body.classList.add("dark-mode");
        toggleBtn.innerHTML = "☀️ Modo Claro";
        toggleBubbleStyles(true);
    }
});

function toggleBubbleStyles(isDark) {
    // Burbujas del bot
    document.querySelectorAll('.bot-msg .bg-light').forEach(el => {
        el.classList.toggle('bg-light', !isDark);
        el.classList.toggle('bg-secondary', isDark);
        el.classList.toggle('text-white', isDark);
    });

    // Burbujas del usuario
    document.querySelectorAll('.user-msg .bg-secondary').forEach(el => {
        el.classList.toggle('bg-secondary', !isDark);
        el.classList.toggle('bg-dark', isDark);
        el.classList.toggle('text-white', isDark);
    });
}