const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const Btn = document.getElementById("takePhoto");
const context =  canvas.getContext("2d")


navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream; // Define o stream como fonte do vídeo
        video.play(); // Inicia a reprodução do vídeo
    })
    .catch(err => {
        console.error("Erro ao acessar a câmera:", err);
    });

Btn.addEventListener("click", () => {
    context.drawImage(video, 0, 0, canvas.width, canvas.height)

})
