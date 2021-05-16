# ia_blackjack
Correr con Python 3, porque sino sos boleta

# Crear venv
python3 -m venv --system-site-packages .\venv

# Activar venv
.\venv\Scripts\activate

# Instalar pip
pip install --upgrade pip

# Instalar tensorflow
pip install --upgrade tensorflow

# Validar instalacion de tensorflow
python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"

# Desactivar cdo ya termine
deactivate