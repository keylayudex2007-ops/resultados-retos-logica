# Protocolo de Control de Acceso

## Validación de Seguridad
**¿Hay fuga de gas?**
* **SÍ:** Acceso Denegado por Seguridad.
* **NO:** Pasar a validación de credenciales.

---

## Evaluación de Credenciales y Equipo
**¿ID válida AND Traje puesto?**
* **SÍ:** Acceso Autorizado.
* **NO:** Evaluar motivo del fallo.

### Análisis de Fallo
**¿ID válida?**
* **SÍ:** Equipo Incompleto (Falta traje).
* **NO:** Acceso Denegado: Sin ID.

---
**Estado Final: Fin del proceso.**