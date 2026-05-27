# Newton-Raphson Calculator

Aplicación gráfica desarrollada en Python utilizando PyQt6 para resolver ecuaciones mediante el método numérico de Newton-Raphson.

El programa permite ingresar funciones matemáticas mediante un teclado matemático interactivo, analizar la función, derivarla automáticamente y calcular aproximaciones de raíces mostrando iteraciones y gráficas.

---

# Características

- Interfaz gráfica moderna con tema oscuro
- Teclado matemático interactivo
- Parser matemático avanzado con SymPy
- Derivación automática
- Método de Newton-Raphson
- Tabla de iteraciones
- Gráfica de la función
- Renderizado matemático con LaTeX
- Arquitectura modular y organizada

---

# Tecnologías utilizadas

- Python 3
- PyQt6
- SymPy
- NumPy
- Matplotlib

---

# Estructura del proyecto

```text
app/
│
├── main.py
│
├── core/
│   ├── parser.py
│   ├── validator.py
│   └── newton_method.py
│
├── ui/
│   ├── main_window.py
│   ├── keyboard_widget.py
│   ├── loading_dialog.py
│   └── result_window.py
│
└── README.md
```

---

# Funcionamiento del programa

## 1. Ingreso de función

El usuario escribe una función matemática usando el teclado matemático integrado.

Ejemplos:

```text
x^2 - 4
sin(x)
sqrt(x)
x^3 - 2x - 5
```

---

## 2. Parser matemático

El sistema convierte automáticamente la entrada del usuario a una expresión matemática válida utilizando SymPy.

También:
- convierte `^` a `**`
- interpreta multiplicación implícita (`2x` → `2*x`)

---

## 3. Validación

Se verifica:
- que la función sea válida
- que pueda derivarse
- que no se simplifique a una constante

---

## 4. Método de Newton-Raphson

El programa aplica iterativamente la fórmula:

\[
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
\]

hasta alcanzar la tolerancia definida.

---

## 5. Resultados

El sistema muestra:

- Función original
- Derivada
- Raíz aproximada
- Tabla de iteraciones
- Gráfica de la función

---

# Instalación

## 1. Clonar repositorio

```bash
git clone https://github.com/TU_USUARIO/newton-raphson.git
```

---

## 2. Entrar al proyecto

```bash
cd newton-raphson/app
```

---

## 3. Crear entorno virtual

Linux/macOS:

```bash
python -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Ejecución

```bash
python main.py
```

---

# Dependencias principales

```text
PyQt6
sympy
numpy
matplotlib
```

---
