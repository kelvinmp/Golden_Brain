document.getElementById('calculate-btn').addEventListener('click', () => {
  const weight = parseFloat(document.getElementById('weight').value);
  const height = parseFloat(document.getElementById('height').value);
  const age = parseInt(document.getElementById('age').value);
  const gender = document.querySelector('input[name="gender"]:checked')?.value;

  const resultElement = document.getElementById('imc-result');
  const statusElement = document.getElementById('imc-status');

  if (!weight || !height || !age || !gender || weight <= 0 || height <= 0 || age <= 0) {
    resultElement.textContent = '--';
    statusElement.textContent = 'Por favor, completa todos los campos.';
    return;
  }

  const imc = (weight / (height * height)).toFixed(1);

  resultElement.textContent = imc;

  let status = '';

  if (imc < 16) {
    status = 'Desnutrición';
    statusElement.style.color = '#9900cc';
  } else if (imc >= 16 && imc < 18.5) {
    status = 'Bajo peso';
    statusElement.style.color = '#ffcc00';
  } else if (imc >= 18.5 && imc < 25) {
    status = 'Peso normal';
    statusElement.style.color = '#00ff00';
  } else if (imc >= 25 && imc < 30) {
    status = 'Sobrepeso';
    statusElement.style.color = '#ff9900';
  } else if (imc >= 30 && imc < 40) {
    status = 'Obesidad';
    statusElement.style.color = '#ff0000';
  } else {
    status = 'Obesidad extrema';
    statusElement.style.color = '#000000';
  }

  statusElement.textContent = `(${gender}, ${age} años): ${status}`;
});
