    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    const img = new Image();
    let x = 100;

    img.src = 'https://via.placeholder.com/150'; // URL da imagem
    img.onload = () => ctx.drawImage(img, x, 100); // Desenha a imagem inicialmente

    const updateCanvas = (direction) => {
        x += direction === 'right' ? 10 : -10; // Atualiza posição
    ctx.clearRect(0, 0, canvas.width, canvas.height); // Limpa o canvas
    ctx.drawImage(img, x, 100); // Redesenha a imagem
    };

    document.getElementById('left').addEventListener('click', () => updateCanvas('left'));
    document.getElementById('right').addEventListener('click', () => updateCanvas('right'));

