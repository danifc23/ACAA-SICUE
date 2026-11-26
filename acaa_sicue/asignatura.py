from dataclasses import dataclass
from .tipo_asignatura import TipoAsignatura


@dataclass(eq=False)
class Asignatura:
    codigo: str
    universidad: str
    nombre: str
    ects: float
    tipo: TipoAsignatura
    curso: int
    semestre: int
    requisitos: tuple[str, ...]
    competencias: tuple[str, ...]
    resultados_aprendizaje: tuple[str, ...]
    temario: tuple[str, ...]

    def __eq__(self, otra):
        if not isinstance(otra, Asignatura):
            return NotImplemented

        return (
            self.codigo == otra.codigo
            and self.universidad == otra.universidad
        )