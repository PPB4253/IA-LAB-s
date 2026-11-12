# Inteligencia Artificial.
# Grado en Ingeniería Informática - Tecnologías Informáticas
# jugar_tenis.py
# Ejemplo visto en clase (tema 7)



datos_tenis=[['Soleado' , 'Alta'        , 'Alta'    , 'Débil' , 'no'],
      ['Soleado' , 'Alta'        , 'Alta'    , 'Fuerte', 'no'],
      ['Nublado' , 'Alta'        , 'Alta'    , 'Débil' , 'si'],
      ['Lluvia'  , 'Suave'       , 'Alta'    , 'Débil' , 'si'],
      ['Lluvia'  , 'Baja'        , 'Normal'  , 'Débil' , 'si'],
      ['Lluvia'  , 'Baja'        , 'Normal'  , 'Fuerte', 'no'],
      ['Nublado' , 'Baja'        , 'Normal'  , 'Fuerte', 'si'],
      ['Soleado' , 'Suave'       , 'Alta'    , 'Débil' , 'no'],
      ['Soleado' , 'Baja'        , 'Normal'  , 'Débil' , 'si'],
      ['Lluvia'  , 'Suave'       , 'Normal'  , 'Débil' , 'si'],
      ['Soleado' , 'Suave'       , 'Normal'  , 'Fuerte', 'si'],
      ['Nublado' , 'Suave'       , 'Alta'    , 'Fuerte', 'si'],
      ['Nublado' , 'Alta'        , 'Normal'  , 'Débil' , 'si'],
      ['Lluvia'  , 'Suave'       , 'Alta'    , 'Fuerte', 'no']]


X_tenis=[ej[:-1] for ej in datos_tenis]
y_tenis=[ej[-1] for ej in datos_tenis]