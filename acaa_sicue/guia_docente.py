from dataclasses import dataclass


@dataclass(frozen=True)
class GuiaDocente:
    codigo_asignatura: str
    universidad: str
    curso_academico: str
    formato: str
    contenido: bytes