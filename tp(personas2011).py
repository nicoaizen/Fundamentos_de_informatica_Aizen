import pandas as pd
path = r"C:\Users\nicoa\Documents\Programacion\datos\personas_2011.csv"
personas2011 = pd.read_csv(path, sep = ";")
print(personas2011)
personas = pd.DataFrame(personas2011)
print(personas)
print(personas.info())
"""
personas_joined.to_csv("cities.csv", index=False, header=True)

 0   persona_id                            68552 non-null  int64  
 1   anio                                  68552 non-null  int64  
 2   sexo_id                               68552 non-null  int64  
 3   edad                                  68552 non-null  int64  
 4   maximo_grado_academico_id             68552 non-null  int64  
 5   disciplina_maximo_grado_academico_id  68552 non-null  int64  
 6   disciplina_titulo_grado_id            68552 non-null  int64  
 7   disciplina_experticia_id              68552 non-null  int64  
 8   tipo_personal_id                      68552 non-null  int64  
 9   producciones_ult_anio                 68552 non-null  int64  
 10  producciones_ult_2_anios              68552 non-null  int64  
 11  producciones_ult_3_anios              68552 non-null  int64  
 12  producciones_ult_4_anios              68552 non-null  int64  
 13  institucion_trabajo_id                68552 non-null  int64  
 14  seniority_level                       68552 non-null  object 
 15  categoria_conicet_id                  48640 non-null  float64
 16  categoria_incentivos                  48640 non-null  float64
 17  max_dedicacion_horaria_docente_id     48640 non-null  float64
 18  institucion_cargo_docente_id          48640 non-null  float64
 19  clase_cargo_docente_id                48640 non-null  float64
 20  tipo_condicion_docente_id             48640 non-null  float64
 """
path1 = r"C:\Users\nicoa\Documents\Programacion\datos\ref_categoria_conicet.csv"
categorias = pd.read_csv(path1, sep = ";")
personas_joined = pd.merge(personas, categorias, on = "categoria_conicet_id")

path2 = r"C:\Users\nicoa\Documents\Programacion\datos\ref_clase_cargo.csv"
clase_cargo = pd.read_csv(path2, sep = ";")
clase_cargo.drop(["tipo_cargo_descripcion"], axis=1, inplace=True)
clase_cargo.drop(["grupo_cargo_descripcion"], axis=1, inplace=True)
clase_cargo.drop(["equivalencia_cargo_docente_descripcion"], axis=1, inplace=True)
personas_joined = pd.merge(personas_joined, clase_cargo, on = "clase_cargo_docente_id")

path3 = r"C:\Users\nicoa\Documents\Programacion\datos\ref_sexo.csv"
sexo = pd.read_csv(path3, sep = ";")
personas_joined = pd.merge(personas_joined, sexo, on = "sexo_id")

path4 = r"C:\Users\nicoa\Documents\Programacion\datos\ref_tipo_condicion_docente.csv"
tipo_condicion_docente = pd.read_csv(path4, sep = ";")
personas_joined = pd.merge(personas_joined, tipo_condicion_docente, on = "tipo_condicion_docente_id")

path5 = r"C:\Users\nicoa\Documents\Programacion\datos\ref_disciplina.csv"
disciplina = pd.read_csv(path5, sep = ";")
personas_joined = personas_joined.rename(columns={"disciplina_titulo_grado_id":"disciplina_id"})
personas_joined = pd.merge(personas_joined, disciplina, on = "disciplina_id")

path6 = r"C:\Users\nicoa\Documents\Programacion\datos\ref_grado_academico.csv"
grado_academico = pd.read_csv(path6, sep = ";")
personas_joined = personas_joined.rename(columns={"maximo_grado_academico_id":"grado_academico_id"})
personas_joined = pd.merge(personas_joined, grado_academico, on = "grado_academico_id")

path7 = r"C:\Users\nicoa\Documents\Programacion\datos\ref_tipo_dedicacion_horaria_semanal.csv"
tipo_dedicacion_horaria_semanal = pd.read_csv(path7, sep = ";")
personas_joined = personas_joined.rename(columns={"max_dedicacion_horaria_docente_id":"tipo_dedicacion_horaria_semanal_id"})
personas_joined = pd.merge(personas_joined, tipo_dedicacion_horaria_semanal, on = "tipo_dedicacion_horaria_semanal_id")

path8 = r"C:\Users\nicoa\Documents\Programacion\datos\ref_tipo_personal.csv"
tipo_personal = pd.read_csv(path8, sep = ";")
personas_joined = pd.merge(personas_joined, tipo_personal, on = "tipo_personal_id")

print(personas_joined)
personas_joined.to_csv("personas_joined.csv", index=False, header=True, sep=";")

#print(personas_joined.describe())

path5 = r"C:\Users\nicoa\Documents\Programacion\datos\ref_disciplina.csv"
disciplina = pd.read_csv(path5, sep = ";")
disciplina.drop(["gran_area_codigo"], axis=1, inplace=True)
disciplina.drop(["gran_area_descripcion"], axis=1, inplace=True)
disciplina.drop(["area_codigo"], axis=1, inplace=True)
disciplina.drop(["disciplina_codigo"], axis=1, inplace=True)
disciplina.drop(["disciplina_descripcion"], axis=1, inplace=True)
personas_joined = pd.merge(personas_joined, disciplina, on = "disciplina_maximo_grado_academico_id")

path5 = r"C:\Users\nicoa\Documents\Programacion\datos\ref_disciplina.csv"
disciplina = pd.read_csv(path5, sep = ";")
personas_joined = pd.merge(personas_joined, disciplina, on = "disciplina_maximo_grado_academico_id")

path6 = r"C:\Users\nicoa\Documents\Programacion\datos\ref_grado_academico.csv"
grado_academico = pd.read_csv(path6, sep = ";")
personas_joined = pd.concat(personas_joined, grado_academico, on = "maximo_grado_academico_id")

path7 = r"C:\Users\nicoa\Documents\Programacion\datos\ref_tipo_dedicacion_horaria_semanal.csv"
tipo_dedicacion_horaria_semanal = pd.read_csv(path7, sep = ";")
personas_joined = pd.merge(personas_joined, tipo_dedicacion_horaria_semanal, on = "max_dedicacion_horaria_docente_id")
