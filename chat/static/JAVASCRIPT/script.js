function adicionarMensagem(texto, classe) {
    const div = document.createElement("div");
    div.classList.add("msg", classe);
    div.innerText = texto;

    document.getElementById("messages").appendChild(div);

    // scroll automático
    document.getElementById("messages").scrollTop =
        document.getElementById("messages").scrollHeight;
}

async function enviar() {
    const input = document.getElementById("pergunta");
    const pergunta = input.value;

    if (!pergunta) return;

    adicionarMensagem(pergunta, "user");
    input.value = "";

    const res = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ pergunta })
    });

    const data = await res.json();

    adicionarMensagem(data.resposta, "bot");
}

// ✅ ENTER para enviar mensagem
document.getElementById("pergunta").addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
        enviar();
    }
});