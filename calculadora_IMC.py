def calcular_imc(peso, altura):
    """
    Calcula el IMC a partir del peso y la altura.
    """
    imc = round(peso / (altura ** 2), 2)
    return imc

def clasificar_imc(imc):
    """
    Clasifica el IMC según las categorías generales.
    """
    if imc < 16:
        return "Desnutrición severa"
    elif 16 <= imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 39.9:
        return "Obesidad"
    else:
        return "Obesidad mórbida"

def main():
    print("Bienvenido a la calculadora de IMC")
    
    # Solicitar datos al usuario
    try:
        edad = int(input("Por favor, ingresa tu edad: "))
        if edad < 0:
            print("La edad no puede ser negativa. Intenta de nuevo.")
            return
        
        genero = input("Por favor, ingresa tu género (Masculino/Femenino): ").strip().lower()
        if genero not in ["masculino", "femenino"]:
            print("Por favor, ingresa un género válido (Masculino o Femenino).")
            return

        peso = float(input("Por favor, ingresa tu peso en kilogramos (kg): "))
        if peso <= 0:
            print("El peso debe ser un número positivo. Intenta de nuevo.")
            return

        altura = float(input("Por favor, ingresa tu altura en metros (m): "))
        if altura <= 0:
            print("La altura debe ser un número positivo. Intenta de nuevo.")
            return
        
        # Calcular el IMC
        imc = calcular_imc(peso, altura)
        clasificacion = clasificar_imc(imc, genero)
        
        # Mostrar resultados
        print("\n--- Resultados ---")
        print(f"Edad: {edad} años")
        print(f"Género: {genero.capitalize()}")
        print(f"Peso: {peso} kg")
        print(f"Altura: {altura} m")
        print(f"Tu IMC es: {imc}")
        print(f"Clasificación: {clasificacion}")

    except ValueError:
        print("Entrada no válida. Por favor, ingresa los datos correctamente.")

if __name__ == "__main__":
    main()
