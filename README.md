# 🤖 AESSBOT2025

**AESSBOT2025** es un **robot de sumo autónomo de 10x10 cm** diseñado para competir en una arena circular de mayor tamaño. El proyecto implementa la lógica de movimiento, evasión y ataque para detectar y empujar al oponente fuera del área de combate, emulando las reglas básicas del sumo robótico.

---

## 📌 Descripción

Este robot simulado está diseñado para:

- Detectar el borde de la arena y evitar caídas.
- Localizar a su oponente usando sensores simulados o reales.
- Atacar y empujar estratégicamente al oponente fuera del dohyo.
- Ser autónomo, rápido y estable en decisiones.

Fue desarrollado como parte del evento **HackUPC 2025** y busca servir como base para proyectos de robótica competitiva.

---

## ⚙️ Características principales

- 🧠 Estrategia autónoma de ataque/defensa.
- 📏 Dimensiones del bot: **10x10 cm**, compatible con normas de sumo robótico.
- 🟢 Detección de bordes para no salirse del dohyo.
- 🔴 Detección de oponentes y lógica de aproximación.
- 🔄 Lógica de evasión y recuperación en caso de colisión.
- 🧪 Código modular, preparado para simulación o implementación real.

---

## 🛠️ Requisitos

- Python 3.8 o superior.
---

## 🧠 Estrategia del Bot

- **Zona segura:** Se mueve al centro de la arena si no detecta peligro.
- **Detección de borde:** Retrocede y rota al detectar líneas blancas o ausencia de superficie (simulada con sensores IR).
- **Ataque:** Avanza agresivamente al detectar un oponente.
- **Evasión:** Si falla el empuje, reajusta posición y vuelve a atacar.
